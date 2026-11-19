"""Generated from Smithy shape ``com.amazonaws.memorydb#DescribeMultiRegionClustersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.boolean_optional
    import capo_memorydb.types.integer_optional
    import capo_memorydb.types.string


class DescribeMultiRegionClustersRequest(TypedDict, closed=True):
    multi_region_cluster_name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of a specific multi-Region cluster to describe.</p>"""
    max_results: NotRequired["capo_memorydb.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["capo_memorydb.types.string.String"]
    """<p>A token to specify where to start paginating.</p>"""
    show_cluster_details: NotRequired[
        "capo_memorydb.types.boolean_optional.BooleanOptional"
    ]
    """<p>Details about the multi-Region cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMultiRegionClustersRequest) -> dict:
    out: dict = {}
    if "multi_region_cluster_name" in value:
        out["MultiRegionClusterName"] = value["multi_region_cluster_name"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "show_cluster_details" in value:
        out["ShowClusterDetails"] = value["show_cluster_details"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMultiRegionClustersRequest:
    out: DescribeMultiRegionClustersRequest = {}  # type: ignore[typeddict-item]
    if data.get("MultiRegionClusterName") is not None:
        out["multi_region_cluster_name"] = data["MultiRegionClusterName"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ShowClusterDetails") is not None:
        out["show_cluster_details"] = data["ShowClusterDetails"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeMultiRegionClustersRequest) -> dict:
    out: dict = {}
    if "multi_region_cluster_name" in value:
        out["MultiRegionClusterName"] = value["multi_region_cluster_name"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "show_cluster_details" in value:
        out["ShowClusterDetails"] = value["show_cluster_details"]
    return out


def deserialize_cbor(data: dict) -> DescribeMultiRegionClustersRequest:
    out: DescribeMultiRegionClustersRequest = {}  # type: ignore[typeddict-item]
    if data.get("MultiRegionClusterName") is not None:
        out["multi_region_cluster_name"] = data["MultiRegionClusterName"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ShowClusterDetails") is not None:
        out["show_cluster_details"] = data["ShowClusterDetails"]
    return out
