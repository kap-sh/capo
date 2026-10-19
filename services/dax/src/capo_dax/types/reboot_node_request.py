"""Generated from Smithy shape ``com.amazonaws.dax#RebootNodeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dax.types.string


class RebootNodeRequest(TypedDict, closed=True):
    cluster_name: "capo_dax.types.string.String"
    """<p>The name of the DAX cluster containing the node to be rebooted.</p>"""
    node_id: "capo_dax.types.string.String"
    """<p>The system-assigned ID of the node to be rebooted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RebootNodeRequest) -> dict:
    out: dict = {}
    out["ClusterName"] = value["cluster_name"]
    out["NodeId"] = value["node_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RebootNodeRequest:
    out: RebootNodeRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClusterName") is not None:
        out["cluster_name"] = data["ClusterName"]
    else:
        out["cluster_name"] = ""
    if data.get("NodeId") is not None:
        out["node_id"] = data["NodeId"]
    else:
        out["node_id"] = ""
    return out
