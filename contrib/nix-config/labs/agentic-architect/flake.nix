{
  # Drop this directory into h0ffmann/nix-config as labs/agentic-architect (Prompt 5).
  # Consumed by gcp-agentic-architect via: inputs.nix-config.url = "github:h0ffmann/nix-config?dir=labs/agentic-architect";
  # Match labs/pratico's conventions (formatter, checks, CI matrix entry) when merging.
  description = "Toolchain for the Professional Agentic Architect exam lab";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }:
    let
      systems = [ "x86_64-linux" "aarch64-linux" "aarch64-darwin" ];
      forAll = f: nixpkgs.lib.genAttrs systems (system: f nixpkgs.legacyPackages.${system});
    in
    {
      devShells = forAll (pkgs: {
        default = pkgs.mkShell {
          packages = with pkgs; [
            python312
            uv                    # `uv pip install google-adk litellm` inside .venv for the --gcp / ADK-real paths
            just
            pandoc
            jq
            shellcheck
            nodejs_22             # MCP reference servers
            google-cloud-sdk      # gcloud, read-only recon; deploys are gated by the repo hooks
            ollama                # open weights for the model-selection lesson
            nixpkgs-fmt
            statix
            deadnix
          ];
          shellHook = ''
            export UV_PROJECT_ENVIRONMENT="$PWD/.venv"
            echo "agentic-architect lab shell — $(python3 --version), $(just --version)"
            echo "ADK: uv venv && uv pip install google-adk (optional; cases run on stdlib)"
          '';
        };
      });

      checks = forAll (pkgs: {
        fmt = pkgs.runCommand "fmt" { buildInputs = [ pkgs.nixpkgs-fmt ]; } ''
          nixpkgs-fmt --check ${./flake.nix} && touch $out
        '';
      });

      formatter = forAll (pkgs: pkgs.nixpkgs-fmt);
    };
}
