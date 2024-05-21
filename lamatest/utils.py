import yaml

def readYaml(yamlfile):
    with open(yamlfile) as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            return exc