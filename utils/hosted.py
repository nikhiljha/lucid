import requests
import yaml


def YAML(url: str, namespace: str):
    r = requests.get(url)

    if r.status_code != 200:
        raise Exception(f"Unable to retrieve the YAML for {namespace}.")

    t = r.text
    # Make sure we got YAML and not an error message or something.
    yaml.safe_load_all(t)

    # TODO: Inject the given namespace into the YAML.

    # Maybe in the future we can check hashes, but it doesn't seem like it would increase security much.
    # if (sha256(t.encode('utf-8')) != hash):
    #     raise Exception("Hashes didn't match, did I get the right file?")

    return t
