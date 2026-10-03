"""Generated from Smithy shape ``com.amazonaws.resiliencehub#EksSourceClusterNamespace``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.eks_namespace


class EksSourceClusterNamespace(TypedDict, closed=True):
    eks_cluster_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Amazon Elastic Kubernetes Service cluster. The format for this ARN is: arn:<code>aws</code>:eks:<code>region</code>:<code>account-id</code>:cluster/<code>cluster-name</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    namespace: "capo_resiliencehub.types.eks_namespace.EksNamespace"
    """<p>Name of the namespace that is located on your Amazon Elastic Kubernetes Service cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksSourceClusterNamespace) -> dict:
    out: dict = {}
    out["eksClusterArn"] = value["eks_cluster_arn"]
    out["namespace"] = value["namespace"]
    return out


def deserialize_json(data: dict) -> EksSourceClusterNamespace:
    out: EksSourceClusterNamespace = {}  # type: ignore[typeddict-item]
    if data.get("eksClusterArn") is not None:
        out["eks_cluster_arn"] = data["eksClusterArn"]
    else:
        raise DeserializationError("EksSourceClusterNamespace.eks_cluster_arn required")
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    else:
        raise DeserializationError("EksSourceClusterNamespace.namespace required")
    return out
