"""Generated from Smithy shape ``com.amazonaws.batch#EksConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.string


class EksConfiguration(TypedDict, closed=True):
    eks_cluster_arn: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Amazon EKS cluster. An example is <code>arn:<i>aws</i>:eks:<i>us-east-1</i>:<i>123456789012</i>:cluster/<i>ClusterForBatch</i> </code>. </p>"""
    kubernetes_namespace: NotRequired["capo_batch.types.string.String"]
    """<p>The namespace of the Amazon EKS cluster. Batch manages pods in this namespace. The value can't left empty or null. It must be fewer than 64 characters long, can't be set to <code>default</code>, can't start with "<code>kube-</code>," and must match this regular expression: <code>^[a-z0-9]([-a-z0-9]*[a-z0-9])?$</code>. For more information, see <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/">Namespaces</a> in the Kubernetes documentation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksConfiguration) -> dict:
    out: dict = {}
    if "eks_cluster_arn" in value:
        out["eksClusterArn"] = value["eks_cluster_arn"]
    if "kubernetes_namespace" in value:
        out["kubernetesNamespace"] = value["kubernetes_namespace"]
    return out


def deserialize_json(data: dict) -> EksConfiguration:
    out: EksConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("eksClusterArn") is not None:
        out["eks_cluster_arn"] = data["eksClusterArn"]
    if data.get("kubernetesNamespace") is not None:
        out["kubernetes_namespace"] = data["kubernetesNamespace"]
    return out
