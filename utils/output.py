from typing import Type
import yaml
from subprocess import run, call, PIPE
from zlib import crc32


def dump(data: str, namespace: str):
    # takes a YAML file, dumps it into a directory
    # as defined by cli variables
    for obj in yaml.load_all(data, Loader=yaml.SafeLoader):
        # TODO: Make sure it's a valid kubernetes object.
        # TODO: Inject namespace.
        run(["mkdir", "-p", f"build/{namespace}"])
        try:
            descriptor = obj["metadata"]["name"]
        except TypeError:
            descriptor = crc32(yaml.dump(obj).encode("utf8"))
        if obj != None:
            with open(f"build/{namespace}/{obj['kind']}-{descriptor}.yml", "w") as f:
                f.write(yaml.dump(obj))
