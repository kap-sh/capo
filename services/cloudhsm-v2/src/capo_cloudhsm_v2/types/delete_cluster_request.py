"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#DeleteClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.cluster_id


class DeleteClusterRequest(TypedDict, closed=True):
    cluster_id: "capo_cloudhsm_v2.types.cluster_id.ClusterId"
    """<p>The identifier (ID) of the cluster that you are deleting. To find the cluster ID, use <a>DescribeClusters</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteClusterRequest) -> dict:
    out: dict = {}
    out["ClusterId"] = value["cluster_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteClusterRequest:
    out: DeleteClusterRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClusterId") is not None:
        out["cluster_id"] = data["ClusterId"]
    else:
        out["cluster_id"] = ""
    return out
