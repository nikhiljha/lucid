import os
import shutil
import tempfile
import yaml
from subprocess import run, call, PIPE


def Chart(
    repo_name: str,
    repo_url: str,
    chart_name: str,
    namespace: str,
    version: str,
    values: dict,
):
    if shutil.which("helm") is None:
        print("You must install Helm to use this script.")

    # TODO: Validate all function arguments.
    r = run(
        ["helm", "repo", "add", repo_name, repo_url], check=True, stdout=PIPE
    ).stdout

    # TODO: Make sure the helm repo was added successfully.
    values_file, values_file_name = tempfile.mkstemp(suffix=".yml")
    with open(values_file_name, "w") as f:
        f.write(yaml.dump(values))

    r = run(
        [
            "helm",
            "template",
            "-n",
            namespace,
            "--version",
            version,
            "--values",
            values_file_name,
            f"{repo_name}/{chart_name}",
        ],
        check=True,
        stdout=PIPE,
    ).stdout

    os.close(values_file)
    run(["helm", "repo", "remove", repo_name], check=True, stdout=PIPE).stdout

    return r
