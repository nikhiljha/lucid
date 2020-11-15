from utils import versions
from utils import hosted


namespace = "argocd"


def build():
    t = hosted.YAML(
        url=f"https://raw.githubusercontent.com/argoproj/argo-cd/v{versions['argocd']}/manifests/install.yaml",
        namespace=namespace,
    )

    return t
