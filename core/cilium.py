from utils import helm
from utils import versions
from utils import output


namespace = "cilium"


def build():
    t = helm.Chart(
        repo_name="cilium",
        repo_url="https://helm.cilium.io/",
        chart_name="cilium",
        namespace=namespace,
        version=versions["cilium"],
        values={},
    )

    return t


output.dump(build(), namespace)
