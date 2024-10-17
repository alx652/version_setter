
class Settings: 

  # Used as a static dictionary 
  targetVersions = {}

  def setTargetVersion(key, value):
    Settings.targetVersions[key]=value

  def getTargetVersion(key):
    if key and key in Settings.targetVersions:
      return Settings.targetVersions[key]
    return None

