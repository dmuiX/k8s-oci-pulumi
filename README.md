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

## setup Pulumi oci

create encrypted ssl keys:

https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm

create a .env with the following content
```bash
export TF_VAR_tenancy_ocid="ocid1.tenancy.oc1..<unique_ID>"
export TF_VAR_user_ocid="ocid1.user.oc1..<unique_ID>"
export TF_VAR_fingerprint="bd:5e:c6:f7:56:c0:4f:88:4f:f8:e1:f7:74:e7:75:ec"
export TF_VAR_region="eu-frankfurt-1"
export TF_VAR_private_key_path="./oci_api_key.pem"
```

Using Pulumi for oci always throws private key errors!!!

## using flake.nix
nix flake init --template github:cachix/devenv

## What does not work
nix-direnv does nothing so far...

devenv without anything seems to work 

flake.nix seem to work as well