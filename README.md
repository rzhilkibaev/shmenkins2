# shmenkins2
# Requirements
python 3.6, pipenv, npm

# How to build
`$ make init` this will install tools/dependencies locally (into `node_modules` and virtualenv).

`$ make deploy` to deploy to AWS.

# Notes
Everything is an artifact group (ag): jar(s), test report, running service, VPN...
Every artifact has a dependency. There are multiple types of dependencies: source code, ag, approval...

When an ag changes it makes all it's downstream dependencies outdated.

Each ag has one (?) build script that defines how the ag is built.
It lists all dependencies and artifacts (imports and exports).