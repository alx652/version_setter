import re_setter_lib
import settings

def bump_clinical_trials_module():

  gsrs_starter_version_tag='gsrs.version'

  set_property_by_path_and_tag({
    'path_argument':  './pom.xml',
    'version_argument':  gsrs_starter_version,
    'tag_argument':  gsrs_starter_version_tag
  })

  set_property_by_path_and_tag({
    'path_argument':  './pom.xml',
    'version_argument':  gsrs_substance_version,
    'tag_argument':  'gsrs.substance.version'
  })

  set_property_by_path_and_tag({
    'path_argument':  './pom.xml',
    'version_argument':  gsrs_clinical_trials_version,
    'tag_argument':  'gsrs.clinical-trials.version'
  })

  set_main_project_version_by_path_and_regex({
    'path_argument':  './pom.xml',
    'version_argument':  gsrs_clinical_trials_version,
    'find_text_argument': '<version>.*</version><!--main_module_version-->'
  })

  find_poms_then_set_parent_versions({ 
    'version_argument':  gsrs_clinical_trials_version,
    'parent_artifact_id': 'gsrs-module-clinical-trials'
  })


def bump_clinical_trials_microservice():

  gsrs_starter_version_tag='gsrs.starter.version'

  set_property_by_path_and_tag({
    'path_argument':  './pom.xml',
    'version_argument':  gsrs_starter_version,
    'tag_argument':  gsrs_starter_version_tag
  })

  set_property_by_path_and_tag({
    'path_argument':  './pom.xml',
    'version_argument':  gsrs_substance_version,
    'tag_argument':  'gsrs.substance.version'
  })

  set_property_by_path_and_tag({
    'path_argument':  './pom.xml',
    'version_argument':  gsrs_clinical_trials_version,
    'tag_argument':  'gsrs.clinical-trials.version'
  })

  set_main_project_version_by_path_and_regex({
  'path_argument':  './pom.xml',
  'version_argument':  gsrs_clinical_trials_version,
  'find_text_argument': '<version>.*</version><!--main_microservice_version-->'
  })

def bump_substances_microservice():

  gsrs_starter_version_tag='gsrs.starter.version'

  set_property_by_path_and_tag({
    'path_argument':  './pom.xml',
    'version_argument':  gsrs_starter_version,
    'tag_argument':  gsrs_starter_version_tag
    })

  set_property_by_path_and_tag({
    'path_argument':  './pom.xml',
    'version_argument':  gsrs_substance_version,
    'tag_argument':  'gsrs.substance.version'
  })

  set_main_project_version_by_path_and_regex({
    'path_argument':  './pom.xml',
    'version_argument':  gsrs_substance_version,
    'find_text_argument': '<version>.*</version><!--main_microservice_version-->'
  })

def bump_substances_module(): 

  gsrs_starter_version_tag='gsrs.version'

  set_property_by_path_and_tag({
        'path_argument':  './pom.xml',
        'version_argument':  gsrs_starter_version,
        'tag_argument':  gsrs_starter_version_tag
  })

  set_property_by_path_and_tag({
    'path_argument':  './pom.xml',
    'version_argument':  gsrs_substance_version,
    'tag_argument':  'gsrs.substance.version'
  })

  set_main_project_version_by_path_and_regex({
    'path_argument':  './pom.xml',
    'version_argument':  gsrs_substance_version,
    'find_text_argument': '<version>.*</version><!--root_project_version-->'
  })

  find_poms_then_set_parent_versions({ 
    'version_argument':  gsrs_substance_version,
    'parent_artifact_id': 'gsrs-module-substances'
  })

  set_version_by_path_and_regex({
  'path_argument':  './gsrs-fda-substance-extension/pom.xml',
  'version_argument':  applications_api_version,
  'find_text_argument': '''<dependency>\s*
\s*<groupId>gov.nih.ncats</groupId>\s*
\s*<artifactId>applications-api</artifactId>\s*
\s*<version>.*</version>'''
  })

  set_version_by_path_and_regex({
    'path_argument':  './gsrs-fda-substance-extension/pom.xml',
    'version_argument':  clinical_trials_api_version,
    'find_text_argument': '''<dependency>\s*
\s*<groupId>gov.nih.ncats</groupId>\s*
\s*<artifactId>clinical-trials-api</artifactId>\s*
\s*<version>.*</version>'''
  })

  set_version_by_path_and_regex({
    'path_argument':  './gsrs-fda-substance-extension/pom.xml',
    'version_argument':  products_api_version,
    'find_text_argument': '''<dependency>\s*
\s*<groupId>gov.nih.ncats</groupId>\s*
\s*<artifactId>products-api</artifactId>\s*
\s*<version>.*</version>'''
    })
 
def bump_starter_module():

  gsrs_starter_version_tag='gsrs.version'

  set_property_by_path_and_tag({
    'path_argument':  './pom.xml',
    'version_argument':  gsrs_starter_version,
    'tag_argument':  gsrs_starter_version_tag
  })

  set_main_project_version_by_path_and_regex({
    'path_argument':  './pom.xml',
    'version_argument':  gsrs_starter_version,
    'find_text_argument': '<version>.*</version><!--root_project_version-->'
  })

  find_poms_then_set_parent_versions({
    'version_argument':  gsrs_starter_version,
    'parent_artifact_id': 'gsrs-spring-boot'
  })

  set_version_by_path_and_regex({
    'path_argument':  './gsrs-discovery/pom.xml',
    'version_argument':  gsrs_starter_version,
    'find_text_argument': '''<groupId>gov.nih.ncats</groupId>\s*
<artifactId>gsrs-discovery</artifactId>\s*
<version>.*</version>\s*
<name>gsrs-discovery</name>'''
  })


def mvn_bump_clinical_trials_module(): 
  project_root_cwd = os.getcwd()
  gsrs_starter_version_tag='gsrs.version'
  mvn_set_project_versions({
    'version_argument':  gsrs_starter_version,
  })
  mvn_set_property_by_tag({
    'version_argument':  gsrs_starter_version,
    'tag_argument':  gsrs_starter_version_tag
  })
  mvn_set_property_by_tag({
    'version_argument':  gsrs_substance_version,
    'tag_argument':  'gsrs.substance.version'
  })

  mvn_set_property_by_tag({
    'version_argument':  gsrs_clinical_trials_version,
    'tag_argument':  'gsrs.clinical-trials.version'
  })

def mvn_bump_clinical_trials_microservice():

  gsrs_starter_version_tag='gsrs.starter.version'
  project_root_cwd = os.getcwd()

  mvn_set_project_versions({
    'version_argument':  gsrs_starter_version,
  })
  mvn_set_property_by_tag({
    'version_argument':  gsrs_starter_version,
    'tag_argument':  gsrs_starter_version_tag
  })
  mvn_set_property_by_tag({
    'version_argument':  gsrs_substance_version,
    'tag_argument':  'gsrs.substance.version'
  })

  mvn_set_property_by_tag({
    'version_argument':  gsrs_clinical_trials_version,
    'tag_argument':  'gsrs.clinical-trials.version'
  })


