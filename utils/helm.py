import shutil
from subprocess import run, call, PIPE


def Chart(repo_name: str, repo_url: str, chart_name: str, namespace: str, values: dict):
    if shutil.which("helm") is None:
        print("You must install Helm to use this script.")

    # TODO: Validate all function arguments.
    r = run(
        ["helm", "repo", "add", repo_name, repo_url], check=True, stdout=PIPE
    ).stdout

    # TODO: Make sure the helm repo was added successfully.
    # TODO: Support helm chart values (write a tempfile, delete it when done).
    r = run(
        ["helm", "template", "-n", namespace, f"{repo_name}/{chart_name}"],
        check=True,
        stdout=PIPE,
    ).stdout
    run(["helm", "repo", "remove", repo_name], check=True, stdout=PIPE).stdout

    return r
