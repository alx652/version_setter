# keep up here to avoid scope issues 

parent_artifact_id_argument_message='A parent_artifact_id (argument) is required.'

# yes
path_not_exists_message='The file path provided [{}] does not exist; nothing rewritten.'
find_text_regex_not_match_message='The find_text_regex did not match, which may be intentional. No change made to file [{}]'
parent_tag_not_matched_message='No parent tag matched regex; no change made to file [{}'
parent_artifact_id_argument_not_match_message ='Parent artifictId tag [{}] did not match, which may be intentional. No change made to file [{}].'


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


