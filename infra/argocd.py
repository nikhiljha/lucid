from utils import versions
from utils import helm


namespace = "argocd"


def build():
    metrics = {
        "enabled": True,
        "serviceMonitor": {
            "enabled": True,
        },
    }

    # This chart is the non-HA version.
    t = helm.Chart(
        repo_name="argo",
        repo_url="https://argoproj.github.io/argo-helm",
        chart_name="argo-cd",
        namespace=namespace,
        version=versions["argocd"],
        values={
            # Enable monitoring for all components.
            # Requires Prometheus Operator
            "controller": {"metrics": metrics},
            "dex": {"metrics": metrics},
            "server": {"metrics": metrics},
            "repoServer": {"metrics": metrics},
        },
    )

    return t
