{
  description = "gcp-agentic-architect: toolchain consumed from nix-config labs/agentic-architect";

  inputs = {
    # Prompt 5 lands contrib/nix-config/labs/agentic-architect in nix-config; until then the
    # fallback shell below keeps `nix develop` working. Pin with `nix flake lock` after merging.
    nix-config.url = "github:h0ffmann/nix-config?dir=labs/agentic-architect";
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nix-config, nixpkgs, ... }:
    let
      systems = [ "x86_64-linux" "aarch64-linux" "aarch64-darwin" ];
      forAll = f: nixpkgs.lib.genAttrs systems (system: f system);
    in
    {
      devShells = forAll (system:
        let pkgs = nixpkgs.legacyPackages.${system}; in {
          default = nix-config.devShells.${system}.default or (pkgs.mkShell {
            packages = with pkgs; [ python312 just pandoc jq shellcheck nodejs ];
            shellHook = ''echo "fallback shell — labs/agentic-architect not in nix-config yet (Prompt 5)"'';
          });
        });

      checks = forAll (system:
        let pkgs = nixpkgs.legacyPackages.${system}; in {
          smoke = pkgs.runCommand "smoke" { buildInputs = [ pkgs.python3 ]; } ''
            cd ${self} && python3 scripts/smoke.py --self-test && touch $out
          '';
        });
    };
}
