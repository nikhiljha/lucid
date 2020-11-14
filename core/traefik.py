import socket
from utils import helm
from utils import versions
from utils import output


namespace = "traefik"
node_ip = socket.gethostbyname(socket.gethostname())
exposed_ips = [node_ip]


def transformation(obj):
    # The default Traefik chart's Service is a LoadBalancer in the default namespace
    # We set it to a NodePort, listening on all IPs, in the traefik namespace
    if obj and obj["kind"] == "Service":
        obj["spec"]["type"] = "NodePort"
        obj["metadata"]["namespace"] = namespace
        obj["spec"]["externalIPs"] = exposed_ips
    return obj


def build():
    t = helm.Chart(
        repo_name="traefik",
        repo_url="https://helm.traefik.io/traefik",
        chart_name="traefik",
        namespace=namespace,
        version=versions["traefik"],
        values={
            # Debugging
            # "logs": {"general": {"level": "DEBUG"}},
            # These are the ports that Traefik has open
            "ports": {
                # This one is used for readiness/liveness probes, and is not exposed
                "traefik": {
                    "port": 9000,
                    "expose": True,
                    "exposedPort": 9000,
                    "protocol": "TCP",
                },
                # This one is exposed on port 80, and is used for HTTP
                # It redirects traffic it receives to HTTPS
                "web": {
                    "port": 8000,
                    "expose": True,
                    "exposedPort": 80,
                    "protocol": "TCP",
                    "redirectTo": "websecure",
                },
                # This one is exposed on port 443, and is used for HTTPS
                "websecure": {
                    "port": 8443,
                    "expose": True,
                    "exposedPort": 443,
                    "protocol": "TCP",
                    "tls": {
                        "enabled": True,
                    },
                },
            },
        },
    )

    t = [transformation(x) for x in t]

    return t


output.dump(build(), namespace)
