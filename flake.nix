{
  description = "Inkscape Cloud Architect";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};

      pythonWithInkex = pkgs.python3.withPackages (ps: with ps; [
        inkex
      ]);
    in {

      devShells.${system}.default = pkgs.mkShell {
        buildInputs = [
          pythonWithInkex
        ];

        shellHook = ''
          echo "Inkscape Cloud Architect development environment"
          echo "Python with inkex module is available"
        '';
      };
    };
}
