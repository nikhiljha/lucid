# Why use Python packages when you can use weird hacks instead?
import sys
import pkgutil
from utils import argo
from utils import output

sys.path.append(".")

# Load the applications, dump them to a file.
argo_apps = []
for importer, mod_name, _ in pkgutil.iter_modules(["core", "infra"]):
    mod = importer.find_module(mod_name).load_module(mod_name)

    print(f"Building {mod.namespace} configuration...")

    # Generate ArgoCD Application object...
    argo_apps.append(
        argo.Application(mod.namespace, "git@github.com:nikhiljha/example.git")
    )

    # TODO: Kickoff CI builds with Tekton tasks.
    output.dump(mod.build(), mod.namespace)

output.dump(argo_apps, "argocd")
