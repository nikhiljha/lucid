# Why use Python packages when you can use weird hacks instead?
import sys
import pkgutil
from utils import output

sys.path.append(".")

# Load the applications, dump them to a file.
for importer, mod_name, _ in pkgutil.iter_modules(["core", "infra"]):
    mod = importer.find_module(mod_name).load_module(mod_name)
    # TODO: Create the ArgoCD deployment object, add it to the argocd namespace.
    output.dump(mod.build(), mod.namespace)
