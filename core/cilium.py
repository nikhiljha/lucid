from utils import helm
from utils import versions


namespace = "cilium"


def build():
    t = helm.Chart(
        repo_name="cilium",
        repo_url="https://helm.cilium.io/",
        chart_name="cilium",
        namespace=namespace,
        version=versions["cilium"],
        values={
            "hubble": {
                "metrics": {
                    "enabled": ["dns", "drop", "tcp", "flow", "icmp", "http"],
                    # Requires Prometheus Operator
                    "serviceMonitor": {
                        "enabled": True,
                    },
                },
                "relay": {
                    "enabled": True,
                },
                "ui": {
                    "enabled": True,
                    "ingress": {
                        "enabled": True,
                        "hosts": ["hubble.ocf.berkeley.edu"],
                    },
                },
            },
            "prometheus": {
                "enabled": True,
                # Requires Prometheus Operator
                "serviceMonitor": {
                    "enabled": True,
                },
            },
            "operator": {
                "prometheus": {
                    "enabled": True,
                    # Requires Prometheus Operator
                    "serviceMonitor": {
                        "enabled": True,
                    },
                },
            },
        },
        apis="monitoring.coreos.com/v1",
    )

    return t
