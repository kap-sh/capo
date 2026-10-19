"""Generated from Smithy shape ``com.amazonaws.memorydb#ListAllowedMultiRegionClusterUpdatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.string


class ListAllowedMultiRegionClusterUpdatesRequest(TypedDict, closed=True):
    multi_region_cluster_name: "capo_memorydb.types.string.String"
    """<p>The name of the multi-Region cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAllowedMultiRegionClusterUpdatesRequest) -> dict:
    out: dict = {}
    out["MultiRegionClusterName"] = value["multi_region_cluster_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAllowedMultiRegionClusterUpdatesRequest:
    out: ListAllowedMultiRegionClusterUpdatesRequest = {}  # type: ignore[typeddict-item]
    if data.get("MultiRegionClusterName") is not None:
        out["multi_region_cluster_name"] = data["MultiRegionClusterName"]
    else:
        out["multi_region_cluster_name"] = ""
    return out
