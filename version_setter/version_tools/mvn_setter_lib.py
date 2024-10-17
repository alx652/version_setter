import version_tools.utils as utils 
import subprocess

def set_property_by_tag(args): 
  utils.check_dict_argument('args', args) 
  version_argument = args.get('version_argument')
  tag_argument = args.get('tag_argument')
  utils.check_string_argument('version_argument', version_argument) 
  utils.check_string_argument('tag_argument', tag_argument)
  new_version = version_argument
  result = subprocess.run(["mvn", "versions:set-property", "-Dproperty=" + tag_argument, "-DnewVersion=" + new_version, "-DgenerateBackupPoms=false"], capture_output=True, text=True)
  print(result.stdout)

def set_project_versions(args):
  utils.check_dict_argument('args', args) 
  version_argument = args.get('version_argument')
  parent_artifact_id = args.get('parent_artifact_id')
  utils.check_string_argument('version_argument', version_argument) 
  new_version = version_argument
  result = subprocess.run(["mvn", "versions:set", "-DnewVersion=" + new_version, "-DallowSnaphots", "-DgenerateBackupPoms=false"], capture_output=True, text=True)
  print(result.stdout)

