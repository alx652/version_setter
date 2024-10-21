# version_setter

This tool comes in handy when changing the version of a GSRS module or microservice. 

See (bin/set_version.py)[bin/set_version.py] for instructions on how to run, but here's the short version:

```
export DEFAULT_VERSION=3.1.2-SNAPSHOT
export GSRS_STARTER_VERSION=$DEFAULT_VERSION
export GSRS_SUBSTANCE_VERSION=$DEFAULT_VERSION
export APPLICATIONS_API_VERSION=$DEFAULT_VERSION
export CLINICAL_TRIALS_API_VERSION=$DEFAULT_VERSION
export PRODUCTS_API_VERSION=$DEFAULT_VERSION

cd path/to/gsrs-spring-starter 
python3 path/to/bin/set_version.py mvn_bump_starter_module

cd path/to/gsrs-spring-module-substances 
python3 path/to/bin/set_version.py mvn_bump_substances_module

cd path/to/deployment/substances 
python3 path/to/bin/set_version.py mvn_bump_substances_microservice

```

