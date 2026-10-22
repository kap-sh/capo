"""Generated from Smithy shape ``com.amazonaws.ecs#AssociateGatewayWithClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string


class AssociateGatewayWithClusterRequest(TypedDict, closed=True):
    gateway: "capo_ecs.types.string.String"
    """<p>The name or Amazon Resource Name (ARN) of the gateway to associate.</p>"""
    cluster: "capo_ecs.types.string.String"
    """<p>The name or Amazon Resource Name (ARN) of the cluster to associate the gateway with.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateGatewayWithClusterRequest) -> dict:
    out: dict = {}
    out["gateway"] = value["gateway"]
    out["cluster"] = value["cluster"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateGatewayWithClusterRequest:
    out: AssociateGatewayWithClusterRequest = {}  # type: ignore[typeddict-item]
    if data.get("gateway") is not None:
        out["gateway"] = data["gateway"]
    else:
        out["gateway"] = ""
    if data.get("cluster") is not None:
        out["cluster"] = data["cluster"]
    else:
        out["cluster"] = ""
    return out
