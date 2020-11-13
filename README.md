# lucid

A (mostly) sane way to sync arbitrarily defined infrastructure (Python or YAML) to Kubernetes.

## Bootstrapping

Assuming you're starting from no existing infrastructure, here are the general steps.

1. deploy a Kubernetes cluster (exercise left to the reader)
2. create an `input` git repository (this one), and an `output` git repository
3. define your infrastructure in `core/` and `apps/`
4. define the deployment pipelines in `infra/`
5. build the entire repository and manually apply it
   - if you have circular dependencies you're on your own
