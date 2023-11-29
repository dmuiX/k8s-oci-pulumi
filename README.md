# deploy k8s cluster on oracle cloud via pulumi and a devenv nix shell
## Using devenv to initialize the python developenment env
I setup my nix profile with this tutorial: https://sandstorm.de/de/blog/post/my-first-steps-with-nix-on-mac-osx-as-homebrew-replacement.html

Add the direnv hook to your shell:
https://devenv.sh/automatic-shell-activation/

then configure and initialize devenv:
```bash
cachix use devenv
cachix use nixpkgs-python
nix profile upgrade 0
devenv init

aftes that add this to devenv.nix:
  packages = with pkgs; [
    kubernetes-helm
    kubectl
    kubectx
    oci-cli
  ];

  languages.nix.enable = true;

  languages.python = {
    enable = true;
    venv = {
      enable = true;
      requirements = " # install python packages via requirements.txt
        pulumi
        pulumi_oci
        pip";
    };
  };

add this do devenv.yaml:
  nixpkgs-python:
    url: github:cachix/nixpkgs-python
```
