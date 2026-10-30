"""Generated from Smithy shape ``com.amazonaws.continuum#KubernetesClusterExternalId``."""

from typing import TypeAlias

"""Optional external ID supplied when Continuum assumes the Kubernetes cluster role. This is STS trust-policy context, not a substitute for iam:PassRole."""
KubernetesClusterExternalId: TypeAlias = str
