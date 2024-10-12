
import re
import warnings
from pathlib import PurePath
from pathlib import Path
import sys
from inspect import currentframe
import glob, os
import subprocess


gsrs_starter_version           =  os.environ['GSRS_STARTER_VERSION']
gsrs_substance_version     =  os.environ['GSRS_SUBSTANCE_VERSION']
applications_api_version     =  os.environ['APPLICATIONS_API_VERSION']
clinical_trials_api_version    =  os.environ['CLINICAL_TRIALS_API_VERSION']
products_api_version          =  os.environ['PRODUCTS_API_VERSION']
gsrs_clinical_trials_version  =  os.environ['GSRS_CLINICAL_TRIALS_VERSION']


# ====


SHOW_FNLN=True

def get_filename_and_linenumber():
    cf = currentframe()
    return cf.f_code.co_filename + ':' + str(cf.f_back.f_lineno)

# print("This is line 14, python says line", get_linenumber())

def warn(msg):
    if msg:
      if(SHOW_FNLN):
        # need to get line number in where called 
        print(msg.strip()  + " " +  get_filename_and_linenumber(), file=sys.stderr)
      else:
        print(msg, file=sys.stderr)

def inform(msg):
    if msg:
      print(msg, file=sys.stderr)
 

def die(msg, exit_val=1):
    """warn() and sys.exit() with exit_val (default 1)"""
    warn(msg)
    sys.exit(exit_val)

# ====

def slurp_from_path(path): 
  try:   
    with path.open() as file:
      return(file.read())
  except OSError:
    die("Could not open or read file: " + path.absolute().as_posix())

def spew_to_path(path, text):
    try:
      with path.open('w') as file:
        file.write(text)
    except OSError:
      die("Could not open/wite file: " + path.absolute().as_posix())

# ====


# keep up here to avoid scope issues 

parent_artifact_id_argument_message='A parent_artifact_id (argument) is required.'

# yes
path_not_exists_message='The file path provided [{}] does not exist; nothing rewritten.'
find_text_regex_not_match_message='The find_text_regex did not match, which may be intentional. No change made to file [{}]'
parent_tag_not_matched_message='No parent tag matched regex; no change made to file [{}'
parent_artifact_id_argument_not_match_message ='Parent artifictId tag [{}] did not match, which may be intentional. No change made to file [{}].'

def check_string_argument(name, value): 
  if value is None or not isinstance(value, str) or not value.strip():
    die (f'A non-blank {name} of type string is required.')

def check_dict_argument(name, value): 
  if value is None or not isinstance(value, dict):
    die ("bad " + name + " variable")


def set_parent_version(args):
  check_dict_argument('args', args) 
  path_argument = args.get('path_argument')
  version_argument = args.get('version_argument')
  parent_artifact_id = args.get('parent_artifact_id')
  check_string_argument('path_argument', path_argument)
  check_string_argument('version_argument', version_argument) 
  check_string_argument('parent_artifact_id', parent_artifact_id)
  new_version = version_argument
  path = Path(path_argument)
  if not path.is_file(): 
    die(path_not_exists_message.format(path_argument))
  full_string=slurp_from_path(path)
  m1 = re.search(r'<parent>.*</parent>', full_string, re.DOTALL)
  if m1:
    parent_string=m1.group(0)
    qr_parent_artifact_id_tag=re.escape('<artifactId>'+parent_artifact_id+'</artifactId>')
    m2 = re.search(qr_parent_artifact_id_tag, parent_string)
    if m2:
      new_parent_string = parent_string
      new_parent_string = re.sub(r'<version>.*<\/version>', '<version>' + new_version + '</version>', new_parent_string)
      qr_parent_string = re.escape(parent_string)
      full_string =re.sub(qr_parent_string, new_parent_string, full_string)
      spew_to_path(path, full_string);
    else:
       warn(parent_artifact_id_argument_not_match_message.format(parent_artifact_id, path_argument))
  else:
    warn (parent_tag_not_matched_message.format(path_argument))

def find_poms_then_set_parent_versions(args): 
  check_dict_argument('args', args) 
  version_argument = args.get('version_argument')
  parent_artifact_id = args.get('parent_artifact_id')
  check_string_argument('version_argument', version_argument) 
  check_string_argument('parent_artifact_id', parent_artifact_id)
  new_version = version_argument
  for file in glob.glob("**/pom.xml", recursive = True):
    # keep this print
    print(file) 
    args['path_argument']=file
    set_parent_version(args)

def set_main_project_version_by_path_and_regex(args):
  set_version_by_path_and_regex(args);

def set_version_by_path_and_regex(args):
  check_dict_argument('args', args) 
  path_argument = args.get('path_argument')
  version_argument = args.get('version_argument')
  find_text_argument = args.get('find_text_argument')
  check_string_argument('path_argument', path_argument)
  check_string_argument('version_argument', version_argument)
  check_string_argument('find_text_argument', find_text_argument)
  new_version = version_argument
  path = Path(path_argument)
  if not path.is_file(): 
    die(path_not_exists_message.format(path_argument))
  full_string=slurp_from_path(path)

  # qr_re=re.escape(find_text_argument) 
  # p = re.compile(r+"'"+find_text_argument+"'")
  m = re.search(find_text_argument, full_string, re.DOTALL)
  if m:
    sub_string=m.group(0)

    new_sub_string=sub_string
    new_sub_string = re.sub('<version>.*</version>', '<version>'+new_version+'</version>', new_sub_string)
    qr_sub_string=re.escape(sub_string)
    full_string = re.sub(qr_sub_string, new_sub_string, full_string) 
    spew_to_path(path, full_string) 
  else: 
    warn(find_text_regex_not_match_message.format(path_argument))

def set_property_by_path_and_tag(args): 
  check_dict_argument('args', args) 
  path_argument = args.get('path_argument')
  version_argument = args.get('version_argument')
  tag_argument = args.get('tag_argument')
  check_string_argument('path_argument', path_argument)
  check_string_argument('version_argument', version_argument) 
  check_string_argument('tag_argument', tag_argument)
  new_version = version_argument
  path = Path(path_argument)
  if not path.is_file(): 
    die(path_not_exists_message.format(path_argument))
  full_string=slurp_from_path(path)
  new_version=version_argument

  m1 = re.search(r'<properties>.*</properties>', full_string, re.DOTALL)
  if m1:
    sub_string=m1.group(0)
    sub_string_re_qr = re.escape(sub_string)
    new_sub_string=sub_string
    new_sub_string_re_qr ='<{}>[^<]*</{}>'.format(re.escape(tag_argument), re.escape(tag_argument))
    new_sub_string_replacement = f'<{tag_argument}>{new_version}</{tag_argument}>'
    new_sub_string = re.sub(new_sub_string_re_qr, new_sub_string_replacement, new_sub_string)
    full_string = re.sub(sub_string_re_qr, new_sub_string, full_string)
    spew_to_path(path, full_string)
  else:
      warn(find_text_regex_not_match_message.format(path_argument))





# ======== Maven versions 

def mvn_set_property_by_tag(args): 
  check_dict_argument('args', args) 
  version_argument = args.get('version_argument')
  tag_argument = args.get('tag_argument')
  check_string_argument('version_argument', version_argument) 
  check_string_argument('tag_argument', tag_argument)
  new_version = version_argument
  result = subprocess.run(["mvn", "versions:set-property", "-Dproperty=" + tag_argument, "-DnewVersion=" + new_version, "-DgenerateBackupPoms=false"], capture_output=True, text=True)
  print(result.stdout)

def mvn_set_project_versions(args):
  check_dict_argument('args', args) 
  version_argument = args.get('version_argument')
  parent_artifact_id = args.get('parent_artifact_id')
  check_string_argument('version_argument', version_argument) 
  new_version = version_argument
  result = subprocess.run(["mvn", "versions:set", "-DnewVersion=" + new_version, "-DallowSnaphots", "-DgenerateBackupPoms=false"], capture_output=True, text=True)

  print(result.stdout)

# ========



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




def mvn_bump_substances_module(): 
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
  os.chdir("gsrs-fda-substance-extension")
  mvn_set_property_by_tag({
    'version_argument':  applications_api_version,
    'tag_argument':  'gsrs.applications.api.version'
  })
  mvn_set_property_by_tag({
    'version_argument':  clinical_trials_api_version,
    'tag_argument':  'gsrs.clinical-trials.api.version'
  })
  mvn_set_property_by_tag({
    'version_argument':  products_api_version,
    'tag_argument':  'gsrs.products.api.version'
  })
  os.chdir(project_root_cwd)

def mvn_bump_substances_microservice():
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

def mvn_bump_starter_module():
  project_root_cwd = os.getcwd()
  gsrs_starter_version_tag='gsrs.version'
  mvn_set_project_versions({
    'version_argument':  gsrs_starter_version,
  })
  mvn_set_property_by_tag({
    'version_argument':  gsrs_starter_version,
    'tag_argument':  gsrs_starter_version_tag
  })
  os.chdir("gsrs-discovery")
  mvn_set_project_versions({
    'version_argument':  gsrs_starter_version,
  })
  os.chdir(project_root_cwd)






def test(): 
  set_version_by_path_and_regex({
  'path_argument':  './gsrs-fda-substance-extension/pom.xml',
  'version_argument':  applications_api_version,
  'find_text_argument': '''<dependency>\s+
<groupId>gov.nih.ncats</groupId>\s+
<artifactId>applications-api</artifactId>\s+
<version>.*</version>'''
  })


