{
  inputs.utils = { url = "github:gytis-ivaskevicius/flake-utils-plus/1.3.0"; };

  outputs = inputs@{ self, nixpkgs, utils }:
    utils.lib.mkFlake {
      inherit self inputs;

      outputsBuilder = channels:
        with channels.nixpkgs; {
          devShell = mkShell { packages = [ python39 ]; };
        };
    };
}
