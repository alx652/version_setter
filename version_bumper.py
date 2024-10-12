import sys
import os
import version_bumper_lib as vbl
import argparse

"""

# version_bumper.py   
# version 0.0002

# Script to help make version changes to pom.xml files in the GSRS project

# Step 1 -- Open terminal 

# Step 2 -- Set environment variables such as:  

export DEFAULT_VERSION=3.1.2-SNAPSHOT
export GSRS_STARTER_VERSION=$DEFAULT_VERSION
export GSRS_SUBSTANCE_VERSION=$DEFAULT_VERSION
export APPLICATIONS_API_VERSION=$DEFAULT_VERSION
export CLINICAL_TRIALS_API_VERSION=$DEFAULT_VERSION
export PRODUCTS_API_VERSION=$DEFAULT_VERSION
export GSRS_CLINICAL_TRIALS_VERSION=$DEFAULT_VERSION

# Step 3 -- cd path/to/microservice/or/module/root/folder 
# Step 4 -- Execute 

> version_bumper.py <bump_sub_routine> 


# Step 5 - verify 

> grep -r --include='pom.xml' '<gsrs\..*\.version>' . | sort


VERSION_STRING = ...
> grep -rl $VERSION_STRING  | grep pom.xml | grep -v target  

> git diff 

"""






def dispatch():
  parser = argparse.ArgumentParser("version_bumper")
  parser.add_argument("action", help="Action to take.", type=str)
  arguments = parser.parse_args()
  action=arguments.action
  actions = {
    'bump_starter_module':  True,
    'bump_substances_module': True,
    'bump_substances_microservice': True,
    'bump_clinical_trials_module': True,
    'bump_clinical_trials_microservice': True,
    'mvn_bump_starter_module': True,
    'mvn_bump_substances_module': True,
    'mvn_bump_substances_microservice': True,
    'mvn_bump_clinical_trials_module': True,
    'mvn_bump_clinical_trials_microservice': True,

    'test': True,
  }

  if actions.get(action): 
    # call(vbl, action)
    getattr(vbl, action)()

  else:
    out = ''
    for x in actions.keys().sort():
       value = str(actions[action])
       out = out + f'{action}: {value}'+"\n"
    vbl.inform(f'There is available action called "{bump}' + "\n" + out) 


dispatch()

