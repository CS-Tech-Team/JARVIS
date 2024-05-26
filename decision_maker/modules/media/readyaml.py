import yaml
import ollama

def get_medias(yamlfile):
    with open(yamlfile) as stream:
        try:
            return yaml.safe_load(stream)["medias"]
        except yaml.YAMLError as exc:
            return exc
        
        
print(get_medias("media_options.yaml"))


