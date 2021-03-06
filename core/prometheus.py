from utils import helm
from utils import versions


namespace = "prometheus"


def build():
    t = helm.Chart(
        repo_name="prometheus-community",
        repo_url="https://prometheus-community.github.io/helm-charts",
        chart_name="kube-prometheus-stack",
        namespace=namespace,
        version=versions["prometheus"],
        values={
            "alertmanager": {
                "enabled": True,
                "ingress": {
                    "enabled": True,
                    "hosts": ["alertmanager.ocf.berkeley.edu"],
                },
            },
            "server": {
                "ingress": {
                    "enabled": True,
                    "hosts": ["prometheus.ocf.berkeley.edu"],
                }
            },
            # Conflicts w/ nodeExporter installed from Puppet.
            "nodeExporter": {
                "enabled": False,
            },
        },
    )

    return t
