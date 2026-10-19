"""Generated from Smithy shape ``com.amazonaws.memorydb#ListAllowedNodeTypeUpdatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.string


class ListAllowedNodeTypeUpdatesRequest(TypedDict, closed=True):
    cluster_name: "capo_memorydb.types.string.String"
    """<p>The name of the cluster you want to scale. MemoryDB uses the cluster name to identify the current node type being used by this cluster, and from that to create a list of node types you can scale up to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAllowedNodeTypeUpdatesRequest) -> dict:
    out: dict = {}
    out["ClusterName"] = value["cluster_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAllowedNodeTypeUpdatesRequest:
    out: ListAllowedNodeTypeUpdatesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClusterName") is not None:
        out["cluster_name"] = data["ClusterName"]
    else:
        out["cluster_name"] = ""
    return out
