from utils import versions
from utils import hosted


namespace = "tekton"


def build():
    t = hosted.YAML(
        url=f"https://storage.googleapis.com/tekton-releases/pipeline/previous/v{versions['tekton_pipelines']}/release.yaml",
        namespace=namespace,
    )

    t.extend(
        hosted.YAML(
            url=f"https://storage.googleapis.com/tekton-releases/triggers/previous/v{versions['tekton_triggers']}/release.yaml",
            namespace=namespace,
        )
    )

    t.extend(
        hosted.YAML(
            url=f"https://storage.googleapis.com/tekton-releases/dashboard/previous/v{versions['tekton_dashboard']}/tekton-dashboard-release.yaml",
            namespace=namespace,
        )
    )

    return t
