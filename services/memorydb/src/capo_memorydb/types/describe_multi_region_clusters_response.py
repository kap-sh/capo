"""Generated from Smithy shape ``com.amazonaws.memorydb#DescribeMultiRegionClustersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.multi_region_cluster_list
    import capo_memorydb.types.string


class DescribeMultiRegionClustersResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_memorydb.types.string.String"]
    """<p>A token to use to retrieve the next page of results.</p>"""
    multi_region_clusters: NotRequired[
        "capo_memorydb.types.multi_region_cluster_list.MultiRegionClusterList"
    ]
    """<p>A list of multi-Region clusters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMultiRegionClustersResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "multi_region_clusters" in value:
        import capo_memorydb.types.multi_region_cluster_list

        out["MultiRegionClusters"] = (
            capo_memorydb.types.multi_region_cluster_list.serialize_aws_json_1_1(
                value["multi_region_clusters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMultiRegionClustersResponse:
    out: DescribeMultiRegionClustersResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MultiRegionClusters") is not None:
        import capo_memorydb.types.multi_region_cluster_list

        out["multi_region_clusters"] = (
            capo_memorydb.types.multi_region_cluster_list.deserialize_aws_json_1_1(
                data["MultiRegionClusters"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeMultiRegionClustersResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "multi_region_clusters" in value:
        import capo_memorydb.types.multi_region_cluster_list

        out["MultiRegionClusters"] = (
            capo_memorydb.types.multi_region_cluster_list.serialize_cbor(
                value["multi_region_clusters"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeMultiRegionClustersResponse:
    out: DescribeMultiRegionClustersResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MultiRegionClusters") is not None:
        import capo_memorydb.types.multi_region_cluster_list

        out["multi_region_clusters"] = (
            capo_memorydb.types.multi_region_cluster_list.deserialize_cbor(
                data["MultiRegionClusters"]
            )
        )
    return out
