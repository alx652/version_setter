import os
import version_tools.mvn_setter_lib as msl
import version_tools.settings as settings

def mvn_bump_standard_project(projectVersion, propertyKeyValues):
  msl.set_project_versions({
    'version_argument': projectVersion
  })

  for key in propertyKeyValues.keys():
    msl.set_property_by_tag({
      'version_argument': propertyKeyValues[key],
      'tag_argument': key
    })

def mvn_bump_adverse_events_module(): 
  gsrs_starter_version_tag='gsrs.version'
  projectVersion = settings.Settings.getTargetVersion('gsrs_adverse_events_version')
  propertyKeyValues = {
    gsrs_starter_version_tag: settings.Settings.getTargetVersion('gsrs_starter_version'),
    'gsrs.substance.version': settings.Settings.getTargetVersion('gsrs_substance_version'),
    'gsrs.adverse-events.version': settings.Settings.getTargetVersion('gsrs_adverse_events_version')
  }
  mvn_bump_standard_project(projectVersion, propertyKeyValues)

def mvn_bump_adverse_events_microservice():
  gsrs_starter_version_tag='gsrs.starter.version'
  projectVersion = settings.Settings.getTargetVersion('gsrs_adverse_events_version')
  propertyKeyValues = {
    gsrs_starter_version_tag: settings.Settings.getTargetVersion('gsrs_starter_version'),
    'gsrs.substance.version': settings.Settings.getTargetVersion('gsrs_substance_version'),
    'gsrs.adverse-events.version': settings.Settings.getTargetVersion('gsrs_adverse_events_version')
  }
  mvn_bump_standard_project(projectVersion, propertyKeyValues)

def mvn_bump_applications_module(): 
  gsrs_starter_version_tag='gsrs.version'
  projectVersion = settings.Settings.getTargetVersion('gsrs_applications_version')
  propertyKeyValues = {
    gsrs_starter_version_tag: settings.Settings.getTargetVersion('gsrs_starter_version'),
    'gsrs.substance.version': settings.Settings.getTargetVersion('gsrs_substance_version'),
    'gsrs.application.version': settings.Settings.getTargetVersion('gsrs_applications_version')
  }
  mvn_bump_standard_project(projectVersion, propertyKeyValues)

def mvn_bump_applications_microservice():
  gsrs_starter_version_tag='gsrs.starter.version'
  projectVersion = settings.Settings.getTargetVersion('gsrs_applications_version')
  propertyKeyValues = {
    gsrs_starter_version_tag: settings.Settings.getTargetVersion('gsrs_starter_version'),
    'gsrs.substance.version': settings.Settings.getTargetVersion('gsrs_substance_version'),
    'gsrs.application.version': settings.Settings.getTargetVersion('gsrs_applications_version')
  }
  mvn_bump_standard_project(projectVersion, propertyKeyValues)

def mvn_bump_clinical_trials_module(): 
  gsrs_starter_version_tag='gsrs.version'
  projectVersion = settings.Settings.getTargetVersion('gsrs_clinical_trials_version')
  propertyKeyValues = {
    gsrs_starter_version_tag: settings.Settings.getTargetVersion('gsrs_starter_version'),
    'gsrs.substance.version': settings.Settings.getTargetVersion('gsrs_substance_version'),
    'gsrs.clinical-trials.version': settings.Settings.getTargetVersion('gsrs_clinical_trials_version')
  }
  mvn_bump_standard_project(projectVersion, propertyKeyValues)

def mvn_bump_clinical_trials_microservice():
  gsrs_starter_version_tag='gsrs.starter.version'
  projectVersion = settings.Settings.getTargetVersion('gsrs_clinical_trials_version')
  propertyKeyValues = {
    gsrs_starter_version_tag: settings.Settings.getTargetVersion('gsrs_starter_version'),
    'gsrs.substance.version': settings.Settings.getTargetVersion('gsrs_substance_version'),
    'gsrs.clinical-trials.version': settings.Settings.getTargetVersion('gsrs_clinical_trials_version')
  }
  mvn_bump_standard_project(projectVersion, propertyKeyValues)

def mvn_bump_deployment_extras_microservices_folder():
  gsrs_starter_version_tag='gsrs.starter.version'
  projectVersion = settings.Settings.getTargetVersion('gsrs_deployment_extras_version')
  propertyKeyValues = {
    gsrs_starter_version_tag: settings.Settings.getTargetVersion('gsrs_starter_version')
  }
  mvn_bump_standard_project(projectVersion, propertyKeyValues)

def mvn_bump_discovery_microservice():
  msl.set_project_versions({
    'version_argument': settings.Settings.getTargetVersion('gsrs_discovery_version'),
  })

def mvn_bump_frontend_microservice():
  msl.set_project_versions({
    'version_argument': settings.Settings.getTargetVersion('gsrs_frontend_version'),
  })

def mvn_bump_gateway_microservice(): 
  gsrs_starter_version_tag='gsrs.starter.version'
  projectVersion = settings.Settings.getTargetVersion('gsrs_impurities_version')
  propertyKeyValues = {
    gsrs_starter_version_tag: settings.Settings.getTargetVersion('gsrs_starter_version')
  }
  mvn_bump_standard_project(projectVersion, propertyKeyValues)


def mvn_bump_impurities_module(): 
  gsrs_starter_version_tag='gsrs.version'
  projectVersion = settings.Settings.getTargetVersion('gsrs_impurities_version')
  propertyKeyValues = {
    gsrs_starter_version_tag: settings.Settings.getTargetVersion('gsrs_starter_version'),
    'gsrs.substance.version': settings.Settings.getTargetVersion('gsrs_substance_version'),
    'gsrs.impurities.version': settings.Settings.getTargetVersion('gsrs_impurities_version')
  }
  mvn_bump_standard_project(projectVersion, propertyKeyValues)

def mvn_bump_impurities_microservice():
  gsrs_starter_version_tag='gsrs.starter.version'
  projectVersion = settings.Settings.getTargetVersion('gsrs_impurities_version')
  propertyKeyValues = {
    gsrs_starter_version_tag: settings.Settings.getTargetVersion('gsrs_starter_version'),
    'gsrs.substance.version': settings.Settings.getTargetVersion('gsrs_substance_version'),
    'gsrs.impurities.version': settings.Settings.getTargetVersion('gsrs_impurities_version')
  }
  mvn_bump_standard_project(projectVersion, propertyKeyValues)

def mvn_bump_invitro_pharmacology_module(): 
  gsrs_starter_version_tag='gsrs.version'
  projectVersion = settings.Settings.getTargetVersion('gsrs_invitro_pharmacology_version')
  propertyKeyValues = {
    gsrs_starter_version_tag: settings.Settings.getTargetVersion('gsrs_starter_version'),
    'gsrs.substance.version': settings.Settings.getTargetVersion('gsrs_substance_version'),
    'gsrs.invitro-pharmacology.version': settings.Settings.getTargetVersion('gsrs_invitro_pharmacology_version')
  }
  mvn_bump_standard_project(projectVersion, propertyKeyValues)

def mvn_bump_invitro_pharmacology_microservice():
  gsrs_starter_version_tag='gsrs.starter.version'
  projectVersion = settings.Settings.getTargetVersion('gsrs_invitro_pharmacology_version')
  propertyKeyValues = {
    gsrs_starter_version_tag: settings.Settings.getTargetVersion('gsrs_starter_version'),
    'gsrs.substance.version': settings.Settings.getTargetVersion('gsrs_substance_version'),
    'gsrs.invitro-pharmacology.version': settings.Settings.getTargetVersion('gsrs_invitro_pharmacology_version')
  }
  mvn_bump_standard_project(projectVersion, propertyKeyValues)

def mvn_bump_products_module(): 
  gsrs_starter_version_tag='gsrs.version'
  projectVersion = settings.Settings.getTargetVersion('gsrs_invitro_pharmacology_version')
  propertyKeyValues = {
    gsrs_starter_version_tag: settings.Settings.getTargetVersion('gsrs_starter_version'),
    'gsrs.substance.version': settings.Settings.getTargetVersion('gsrs_substance_version'),
    'gsrs.product.version': settings.Settings.getTargetVersion('gsrs_ssg4m_version')
  }
  mvn_bump_standard_project(projectVersion, propertyKeyValues)

def mvn_bump_products_microservice():
  gsrs_starter_version_tag='gsrs.starter.version'
  projectVersion = settings.Settings.getTargetVersion('gsrs_products_version')
  propertyKeyValues = {
    gsrs_starter_version_tag: settings.Settings.getTargetVersion('gsrs_starter_version'),
    'gsrs.substance.version': settings.Settings.getTargetVersion('gsrs_substance_version'),
    'gsrs.product.version': settings.Settings.getTargetVersion('gsrs_products_version')
  }
  mvn_bump_standard_project(projectVersion, propertyKeyValues)

def mvn_bump_ssg4m_module(): 
  gsrs_starter_version_tag='gsrs.version'
  projectVersion = settings.Settings.getTargetVersion('gsrs_invitro_pharmacology_version')
  propertyKeyValues = {
    gsrs_starter_version_tag: settings.Settings.getTargetVersion('gsrs_starter_version'),
    'gsrs.substance.version': settings.Settings.getTargetVersion('gsrs_substance_version'),
    'gsrs.ssg4.version': settings.Settings.getTargetVersion('gsrs_ssg4m_version')
  }
  mvn_bump_standard_project(projectVersion, propertyKeyValues)

def mvn_bump_ssg4m_microservice():
  gsrs_starter_version_tag='gsrs.starter.version'
  projectVersion = settings.Settings.getTargetVersion('gsrs_ssg4m_version')
  propertyKeyValues = {
    gsrs_starter_version_tag: settings.Settings.getTargetVersion('gsrs_starter_version'),
    'gsrs.substance.version': settings.Settings.getTargetVersion('gsrs_substance_version'),
    'gsrs.ssg4.version': settings.Settings.getTargetVersion('gsrs_ssg4m_version')
  }
  mvn_bump_standard_project(projectVersion, propertyKeyValues)


def mvn_bump_substances_module(): 
  project_root_cwd = os.getcwd()
  gsrs_starter_version_tag='gsrs.version'
  projectVersion = settings.Settings.getTargetVersion('gsrs_starter_version')
  propertyKeyValues = {
    gsrs_starter_version_tag: settings.Settings.getTargetVersion('gsrs_starter_version'),
    'gsrs.substance.version': settings.Settings.getTargetVersion('gsrs_substance_version')
  }
  mvn_bump_standard_project(projectVersion, propertyKeyValues)
  # os.chdir("gsrs-fda-substance-extension")
  msl.set_property_by_tag({
    'version_argument': settings.Settings.getTargetVersion('applications_api_version'),
    'tag_argument': 'gsrs.applications-api.version'
  })
  msl.set_property_by_tag({
    'version_argument': settings.Settings.getTargetVersion('clinical_trials_api_version'),
    'tag_argument': 'gsrs.clinical-trials-api.version'
  })
  msl.set_property_by_tag({
    'version_argument': settings.Settings.getTargetVersion('products_api_version'),
    'tag_argument': 'gsrs.products-api.version'
  })
  # os.chdir(project_root_cwd)

def mvn_bump_substances_microservice():
  gsrs_starter_version_tag='gsrs.starter.version'
  projectVersion = settings.Settings.getTargetVersion('gsrs_substance_version')
  propertyKeyValues = {
    gsrs_starter_version_tag: settings.Settings.getTargetVersion('gsrs_starter_version'),
    'gsrs.substance.version': settings.Settings.getTargetVersion('gsrs_substance_version')
  }
  mvn_bump_standard_project(projectVersion, propertyKeyValues)

def mvn_bump_starter_module():
  project_root_cwd = os.getcwd()
  gsrs_starter_version_tag='gsrs.version'
  projectVersion = settings.Settings.getTargetVersion('gsrs_starter_version')
  propertyKeyValues = {
    gsrs_starter_version_tag: settings.Settings.getTargetVersion('gsrs_starter_version')
  }
  mvn_bump_standard_project(projectVersion, propertyKeyValues)
  os.chdir("gsrs-discovery")
  msl.set_project_versions({
    'version_argument': settings.Settings.getTargetVersion('gsrs_starter_version'),
  })
  os.chdir(project_root_cwd)

