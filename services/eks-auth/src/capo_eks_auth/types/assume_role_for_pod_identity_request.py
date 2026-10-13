"""Generated from Smithy shape ``com.amazonaws.eksauth#AssumeRoleForPodIdentityRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_eks_auth.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eks_auth.types.cluster_name
    import capo_eks_auth.types.jwt_token


class AssumeRoleForPodIdentityRequest(TypedDict, closed=True):
    cluster_name: "capo_eks_auth.types.cluster_name.ClusterName"
    """<p>The name of the cluster for the request.</p>"""
    token: "capo_eks_auth.types.jwt_token.JwtToken"
    """<p>The token of the Kubernetes service account for the pod.</p>"""
    eks_node_name: NotRequired["str"]
    """<p>The Kubernetes node name of the worker node where the pod is running.</p>"""
    instance_id: NotRequired["str"]
    """<p>The Amazon EC2 instance ID of the worker node where the pod is running.</p>"""
    zone: NotRequired["str"]
    """<p>The Availability Zone ID of the worker node where the pod is running.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssumeRoleForPodIdentityRequest) -> dict:
    out: dict = {}
    out["token"] = value["token"]
    if "eks_node_name" in value:
        out["eksNodeName"] = value["eks_node_name"]
    if "instance_id" in value:
        out["instanceId"] = value["instance_id"]
    if "zone" in value:
        out["zone"] = value["zone"]
    return out


def deserialize_json(data: dict) -> AssumeRoleForPodIdentityRequest:
    out: AssumeRoleForPodIdentityRequest = {}  # type: ignore[typeddict-item]
    if data.get("token") is not None:
        out["token"] = data["token"]
    else:
        raise DeserializationError("AssumeRoleForPodIdentityRequest.token required")
    if data.get("eksNodeName") is not None:
        out["eks_node_name"] = data["eksNodeName"]
    if data.get("instanceId") is not None:
        out["instance_id"] = data["instanceId"]
    if data.get("zone") is not None:
        out["zone"] = data["zone"]
    return out


def redact_sensitive(value: AssumeRoleForPodIdentityRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "token" in value:
        out["token"] = "*** Sensitive Data Redacted ***"
    return out
