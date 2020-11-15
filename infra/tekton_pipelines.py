from utils import versions
from utils import output
from utils import hosted


namespace = "tekton-pipelines"


def build():
    t = hosted.YAML(
        url=f"https://storage.googleapis.com/tekton-releases/pipeline/previous/v{versions['tekton']}/release.yaml",
        namespace=namespace,
    )

    return t
