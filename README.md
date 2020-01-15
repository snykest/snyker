# Snyker

A Lambda application used for demonstration purposes.

## Security testing

Snyker has both runtime and development dependencies, and both are checked by Snyk for known security issues. Snyk is integrated via GitHub, and automatically detects any `requirements` files. Chalice also uses `requirements.txt` for managing dependencies. However, Snyker uses Poetry to manage it dependencies. To bridge this gap we have a GitHub Action which will generate the `requirements` files whenever the Poetry dependencies are changed. You can also do this manually
using the included `Makefile`.

![Requirements](https://github.com/garethr/snyker/workflows/Requirements/badge.svg)

To see the current set of vulnerabilies in this project, see:

* [requirements.txt](https://snyk.io/test/github/garethr/snyker?targetFile=requirements.txt)
* [requirements-dev.txt](https://snyk.io/test/github/garethr/snyker?targetFile=requirements-dev.txt)


## Configuring Chalice for production

[Chalice](https://github.com/aws/chalice) is a nice microframework for building Python applications on Lambda, but like many such frameworks it needs you to do much of the configuration. This sample application includes a basic confuguration mechanism using AWS Systems Manager Parameter Store, as well as configuring structured logging.

![CI](https://github.com/garethr/snyker/workflows/CI/badge.svg)
