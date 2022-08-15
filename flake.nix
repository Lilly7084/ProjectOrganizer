{
  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let pkgs = import nixpkgs {inherit system;}; in
      rec {
        packages = flake-utils.lib.flattenTree {
          shell = pkgs.mkShell {
            buildInputs = with pkgs; [
              python310
              python310Packages.pip
              python310Packages.flake8
              python310Packages.pygame
            ];
            shellHook = ''
              alias pip="PIP_PREFIX='$(pwd)/_build/pip_packages' \pip"
              export PYTHONPATH="$(pwd)/_build/pip_packages/lib/python3.10/site-packages:$PYTHONPATH"
              unset SOURCE_DATE_EPOCH
            '';
          };
        };
        defaultPackage = packages.shell;
      }
    );
}
