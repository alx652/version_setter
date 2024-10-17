import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../version_setter')
import version_tools.settings as settings
import version_tools.utils as utils 
# the re version, is deprecated, but keeping in codebase for now as it might handy
# for other purposes.
# import version_tools.re_setter as re_vs 
import version_tools.mvn_setter as mvn_vs
import argparse

"""

# version_setter.py   
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

export GSRS_ADVERSE_EVENTS_VERSION=$DEFAULT_VERSION
export GSRS_APPLICATIONS_VERSION=$DEFAULT_VERSION
export GSRS_CLINICAL_TRIALS_VERSION=$DEFAULT_VERSION
export GSRS_DEPLOYMENT_EXTRAS_VERSION=$DEFAULT_VERSION
export GSRS_DISCOVERY_VERSION=$DEFAULT_VERSION
export GSRS_FRONTEND_VERSION=$DEFAULT_VERSION
export GSRS_GATEWAY_VERSION=$DEFAULT_VERSION
export GSRS_IMPURITIES_VERSION=$DEFAULT_VERSION
export GSRS_INVITRO_PHARMACOLOGY_VERSION=$DEFAULT_VERSION
export GSRS_PRODUCTS_VERSION=$DEFAULT_VERSION
export GSRS_SSG4M_VERSION=$DEFAULT_VERSION




# Step 3 -- cd path/to/microservice/or/module/root/folder 
# Step 4 -- Execute 

> version_setter.py <bump_sub_routine> 


# Step 5 - verify 

> grep -r --include='pom.xml' '<gsrs\..*\.version>' . | sort


VERSION_STRING = ...
> grep -rl $VERSION_STRING  | grep pom.xml | grep -v target  

VERSION_STRING = ...
> grep -RH  --include='pom.xml'  $VERSION_STRING 



> git diff 

"""



settings.Settings.setTargetVersion('gsrs_starter_version', os.environ['GSRS_STARTER_VERSION'])
settings.Settings.setTargetVersion('gsrs_substance_version', os.environ['GSRS_SUBSTANCE_VERSION'])
settings.Settings.setTargetVersion('applications_api_version', os.environ['APPLICATIONS_API_VERSION'])
settings.Settings.setTargetVersion('clinical_trials_api_version', os.environ['CLINICAL_TRIALS_API_VERSION'])
settings.Settings.setTargetVersion('products_api_version', os.environ['PRODUCTS_API_VERSION'])

settings.Settings.setTargetVersion('gsrs_adverse_events_version', os.environ['GSRS_ADVERSE_EVENTS_VERSION'])
settings.Settings.setTargetVersion('gsrs_applications_version', os.environ['GSRS_APPLICATIONS_VERSION'])
settings.Settings.setTargetVersion('gsrs_clinical_trials_version', os.environ['GSRS_CLINICAL_TRIALS_VERSION'])
settings.Settings.setTargetVersion('gsrs_deployment_extras_version', os.environ['GSRS_DEPLOYMENT_EXTRAS_VERSION'])
settings.Settings.setTargetVersion('gsrs_discovery_version', os.environ['GSRS_DISCOVERY_VERSION'])
settings.Settings.setTargetVersion('gsrs_frontend_version', os.environ['GSRS_FRONTEND_VERSION'])
settings.Settings.setTargetVersion('gsrs_gateway_version', os.environ['GSRS_GATEWAY_VERSION'])
settings.Settings.setTargetVersion('gsrs_impurities_version', os.environ['GSRS_IMPURITIES_VERSION'])
settings.Settings.setTargetVersion('gsrs_invitro_pharmacology_version', os.environ['GSRS_INVITRO_PHARMACOLOGY_VERSION'])
settings.Settings.setTargetVersion('gsrs_products_version', os.environ['GSRS_PRODUCTS_VERSION'])
settings.Settings.setTargetVersion('gsrs_ssg4m_version', os.environ['GSRS_SSG4M_VERSION'])



def dispatch():
  parser = argparse.ArgumentParser("version_setter")
  parser.add_argument("action", help="Action to take.", type=str)
  arguments = parser.parse_args()
  action=arguments.action
  actions = {
    'mvn_bump_adverse_events_microservice': True,
    'mvn_bump_adverse_events_module': True,
    'mvn_bump_applications_microservice': True,
    'mvn_bump_applications_module': True,
    'mvn_bump_clinical_trials_microservice': True,
    'mvn_bump_clinical_trials_module': True,
    'mvn_bump_discovery_microservice': True,
    'mvn_bump_deployment_extras_microservices_folder': True,
    'mvn_bump_frontend_microservice': True,
    'mvn_bump_gateway_microservice': True,
    'mvn_bump_impurities_microservice': True,
    'mvn_bump_impurities_module': True,
    'mvn_bump_invitro_pharmacology_microservice': True,
    'mvn_bump_invitro_pharmacology_module': True,
    'mvn_bump_products_microservice': True,
    'mvn_bump_products_module': True,
    'mvn_bump_ssg4m_microservice': True,
    'mvn_bump_ssg4m_module': True,
    'mvn_bump_starter_module': True,
    'mvn_bump_substances_module': True,
    'mvn_bump_substances_microservice': True,
    'test': True,
  }
  if actions.get(action) and actions.get(action) is not None: 
    getattr(mvn_vs, action)()
  else:
    out = ''
    actionKeys = list(actions.keys())
    actionKeys.sort()
    for x in actionKeys:
       value = str(actions[x])
       out = out + f'{x}: {value}'+"\n"
    utils.inform(f'There is no available action called "{action}. The following are defined and runnable if True:' + "\n" + out) 


dispatch()


