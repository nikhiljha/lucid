import requests
import yaml
from utils import versions
from utils import output


def build():
    r = requests.get(
        f"https://raw.githubusercontent.com/argoproj/argo-cd/v{versions['argocd']}/manifests/install.yaml")
    if (r.status_code != 200):
        raise Exception('Unable to retrieve the YAML for Tekton.')

    t = r.text
    yaml.load_all(t)  # Make sure the YAML gets parsed.

    # You could also check the hash, like so... but for simplicity we won't do this.
    # if (sha256(t.encode('utf-8')) != "ae1feaf65029e6b025c7220314a49b657785cc063610b7a7e8e37687e8059dbe"):
    #     raise Exception("Hashes didn't match, did I get the right file?")

    return t


output.dump(build())
