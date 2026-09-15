{
  description = "gcp-agentic-architect — exam lab toolchain: python, uv, gcloud, ollama, node, plus nix-config's lint, agentic and publisher labs";

  inputs = {
    # h0ffmann/nix-config labs, one nixpkgs closure: publisher pins it (TeX Live is the heavy part),
    # lint and agentic follow. Bump one with `nix flake update lint`, all with `just lock`.
    publisher.url = "github:h0ffmann/nix-config?dir=labs/publisher";
    nixpkgs.follows = "publisher/nixpkgs";
    lint = {
      url = "github:h0ffmann/nix-config?dir=labs/lint";
      inputs.nixpkgs.follows = "nixpkgs";
    };
    agentic = {
      url = "github:h0ffmann/nix-config?dir=labs/agentic";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { self, nixpkgs, publisher, lint, agentic }:
    let
      inherit (nixpkgs) lib;
      systems = [ "x86_64-linux" "aarch64-linux" "aarch64-darwin" ];
      forAll = f: lib.genAttrs systems (system: f system nixpkgs.legacyPackages.${system});

      # The lab's own tools. Lint, the agent sandbox and the PDF toolchain come from the labs.
      projectTools = pkgs: with pkgs; [
        python3 # scripts/ and cases/ are stdlib-only
        uv # `uv pip install google-adk` in .venv for the ADK-real paths
        just
        jq
        git
        nodejs # MCP reference servers
        google-cloud-sdk # read-only recon; creates and deploys are gated by .claude/
        ollama # open weights for the model-selection lesson; `ollama serve` is the host's
        nixpkgs-fmt
        statix
        deadnix
      ];

      # Only what scripts/build_pdf.sh reads, so unrelated edits don't rebuild the book.
      bookSrc = lib.cleanSourceWith {
        src = ./.;
        filter = path: _type:
          let p = toString path; r = toString ./.;
          in lib.any (d: p == "${r}/${d}" || lib.hasPrefix "${r}/${d}/" p) [ "course" "publications" "scripts" ];
      };
    in
    {
      devShells = forAll (system: pkgs: {
        default = pkgs.mkShell ({
          name = "agentic-architect";
          packages = projectTools pkgs ++ lint.lib.${system}.tools ++ agentic.lib.${system}.tools;
          shellHook = ''
            export UV_PROJECT_ENVIRONMENT="$PWD/.venv"
            echo "agentic-architect: $(python3 --version) | $(just --version) | gcloud $(gcloud version 2>/dev/null | head -1 | awk '{print $NF}')"
            curl -s -m 1 http://127.0.0.1:11434/api/tags >/dev/null 2>&1 \
              || echo "ollama not running — cases run on stdlib without it; 'ollama serve' for the model paths"
            echo "Run 'just' to see available commands."
          '';
        } // agentic.lib.${system}.env);

        # pandoc + TeX Live for `just book`; separate so the default shell stays small.
        pubs = publisher.devShells.${system}.default;

        # `just quality` without ai-jail (a Rust build) — what ci.yml enters.
        lint = pkgs.mkShell {
          name = "agentic-architect-lint";
          packages = [ pkgs.python3 pkgs.just pkgs.nixpkgs-fmt pkgs.statix pkgs.deadnix ] ++ lint.lib.${system}.tools;
        };
      });

      packages = forAll (system: _pkgs: rec {
        book = publisher.lib.${system}.mkPdf {
          name = "agentic-architect-book";
          src = bookSrc;
          command = "bash scripts/build_pdf.sh";
        };
        default = book;
      });

      checks = forAll (_system: pkgs: {
        # Stdlib only, no network: layout, question banks, every script's --self-test, every case.
        smoke = pkgs.runCommand "agentic-architect-smoke" { nativeBuildInputs = [ pkgs.python3 pkgs.bash ]; } ''
          cp -r ${self} src && chmod -R u+w src && cd src
          python3 scripts/smoke.py
          bash .claude/hooks/guard-gcloud.sh --self-test
          for d in cases/*/; do bash "$d/run.sh" >/dev/null; done
          touch $out
        '';
      });

      formatter = forAll (_system: pkgs: pkgs.nixpkgs-fmt);
    };
}
