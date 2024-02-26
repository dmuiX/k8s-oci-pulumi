{ pkgs, ... }:

{
  # https://devenv.sh/basics/
  env.GREET = "devenv";

  # https://devenv.sh/packages/

  # https://devenv.sh/scripts/
  scripts.hello.exec = "echo hello from $GREET";

  enterShell = ''
    hello
    git --version
  '';

  packages = with pkgs; [
    kubectl
    kubectx
    kubernetes-helm
    oci-cli
    pulumi
    python311Packages.oci
    python311Packages.pulumi
    pulumiPackages.pulumi-language-python
  ];

  dotenv.enable = true;

  #languages.nix.enable = true;
  
  languages.python = {
    enable = true;
    venv = {
      enable = true;
      requirements = "
        pulumi
        pulumi-oci
        pip
        grpcio==1.59.3
        pylance
        pylint
        setuptools
        ";
    };
    version = "3.11";
    #poetry = {
    #  activate.enable = true;
    #  install = {
    ##    allExtras = true;
    #    enable = true;
    #  };
    #};
  };
  
  # https://devenv.sh/pre-commit-hooks/
  # pre-commit.hooks.shellcheck.enable = true;

  # https://devenv.sh/processes/
  # processes.ping.exec = "ping example.com";

  # See full reference at https://devenv.sh/reference/options/
}
