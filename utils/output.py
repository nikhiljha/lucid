from typing import Type
import yaml
from subprocess import run, call, PIPE
from zlib import crc32


def dump(data: str, namespace: str):
    # takes an array of dicts, dumps it into a directory
    run(["mkdir", "-p", f"build/{namespace}"])
    for obj in data:
        # TODO: Make sure it's a valid kubernetes object.
        # TODO: Inject namespace.
        try:
            descriptor = obj["metadata"]["name"]
        except (TypeError, KeyError):
            descriptor = crc32(yaml.dump(obj).encode("utf8"))
        if obj != None:
            with open(f"build/{namespace}/{obj['kind']}-{descriptor}.yml", "w") as f:
                f.write(yaml.dump(obj))
