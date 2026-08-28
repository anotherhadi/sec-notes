{
  description = "";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    git-hooks = {
      url = "github:cachix/git-hooks.nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = {
    self,
    nixpkgs,
    git-hooks,
  }: let
    supportedSystems = ["x86_64-linux" "aarch64-linux"];

    forAllSystems = f:
      nixpkgs.lib.genAttrs supportedSystems
      (system: f system (import nixpkgs {inherit system;}));
  in {
    devShells = forAllSystems (system: pkgs: let
      hooks = git-hooks.lib.${system}.run {
        src = ./.;
        hooks = {
          gen-readme = {
            enable = true;
            name = "gen-readme";
            entry = "python3 .github/scripts/gen-readme.py";
            language = "system";
            files = "\\.md$";
            excludes = ["^\\.github/" "^README\\.md$"];
            pass_filenames = false;
            before = ["doctoc"];
          };

          doctoc = {
            enable = true;
            name = "doctoc";
            entry = "python3 .github/scripts/doctoc-all.py";
            language = "system";
            files = "\\.md$";
            excludes = ["^\\.github/"];
            pass_filenames = false;
          };
        };
      };
    in {
      default = pkgs.mkShell {
        packages = with pkgs; [doctoc] ++ hooks.enabledPackages;

        shellHook = hooks.shellHook;
      };
    });
  };
}
