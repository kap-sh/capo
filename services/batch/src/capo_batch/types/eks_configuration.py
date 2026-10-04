"""Generated from Smithy shape ``com.amazonaws.batch#EksConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.eks_access_entry
    import capo_batch.types.string


class EksConfiguration(TypedDict, closed=True):
    eks_cluster_arn: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Amazon EKS cluster. An example is <code>arn:<i>aws</i>:eks:<i>us-east-1</i>:<i>123456789012</i>:cluster/<i>ClusterForBatch</i> </code>. </p>"""
    kubernetes_namespace: NotRequired["capo_batch.types.string.String"]
    """<p>The namespace of the Amazon EKS cluster. Batch manages pods in this namespace. The value can't left empty or null. It must be fewer than 64 characters long, can't be set to <code>default</code>, can't start with "<code>kube-</code>," and must match this regular expression: <code>^[a-z0-9]([-a-z0-9]*[a-z0-9])?$</code>. For more information, see <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/">Namespaces</a> in the Kubernetes documentation.</p>"""
    access_entry: NotRequired["capo_batch.types.eks_access_entry.EksAccessEntry"]
    """<p>The Batch-managed Amazon EKS access entry for the compute environment. Set <code>desiredState</code> to declare whether Batch manages an access entry on the cluster. In a <code>DescribeComputeEnvironments</code> response, <code>desiredState</code> is the value that Batch recorded for the compute environment and <code>status</code> is the observed state of the access entry on the cluster. To change the access entry on an existing compute environment, use <a href="https://docs.aws.amazon.com/batch/latest/APIReference/API_EksConfigurationUpdate.html#Batch-Type-EksConfigurationUpdate-accessEntry"> <code>EksConfigurationUpdate.accessEntry</code> </a>.</p> <p>Whether the entry is provisioned on the cluster depends on the cluster's <code>authenticationMode</code> and the <code>desiredState</code> recorded for each Batch compute environment targeting the cluster. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/eks-access-entries.html">Amazon EKS access entry authentication</a> in the <i>Batch User Guide</i>.</p> <p>If you don't specify this field, Batch doesn't record a <code>desiredState</code> for the compute environment and <code>DescribeComputeEnvironments</code> doesn't return one. For the purpose of provisioning the access entry, Batch behaves as it does for <code>INHERIT_FROM_CLUSTER</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksConfiguration) -> dict:
    out: dict = {}
    if "eks_cluster_arn" in value:
        out["eksClusterArn"] = value["eks_cluster_arn"]
    if "kubernetes_namespace" in value:
        out["kubernetesNamespace"] = value["kubernetes_namespace"]
    if "access_entry" in value:
        import capo_batch.types.eks_access_entry

        out["accessEntry"] = capo_batch.types.eks_access_entry.serialize_json(
            value["access_entry"]
        )
    return out


def deserialize_json(data: dict) -> EksConfiguration:
    out: EksConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("eksClusterArn") is not None:
        out["eks_cluster_arn"] = data["eksClusterArn"]
    if data.get("kubernetesNamespace") is not None:
        out["kubernetes_namespace"] = data["kubernetesNamespace"]
    if data.get("accessEntry") is not None:
        import capo_batch.types.eks_access_entry

        out["access_entry"] = capo_batch.types.eks_access_entry.deserialize_json(
            data["accessEntry"]
        )
    return out
