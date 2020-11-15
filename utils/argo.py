def Application(namespace: str, repoURL: str):
    return {
        "apiVersion": "argoproj.io/v1alpha1",
        "kind": "Application",
        "metadata": {"name": namespace},
        "spec": {
            "destination": {
                "namespace": namespace,
                "server": "https://kubernetes.default.svc",
            },
            "project": "default",
            "source": {
                "path": f"{namespace}/",
                "repoURL": repoURL,
                "targetRevision": "HEAD",
            },
        },
    }
