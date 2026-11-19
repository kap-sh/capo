"""Generated from Smithy shape ``com.amazonaws.memorydb#DescribeClustersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.boolean_optional
    import capo_memorydb.types.integer_optional
    import capo_memorydb.types.string


class DescribeClustersRequest(TypedDict, closed=True):
    cluster_name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of the cluster.</p>"""
    max_results: NotRequired["capo_memorydb.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>"""
    next_token: NotRequired["capo_memorydb.types.string.String"]
    """<p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>"""
    show_shard_details: NotRequired[
        "capo_memorydb.types.boolean_optional.BooleanOptional"
    ]
    """<p>An optional flag that can be included in the request to retrieve information about the individual shard(s).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeClustersRequest) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["ClusterName"] = value["cluster_name"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "show_shard_details" in value:
        out["ShowShardDetails"] = value["show_shard_details"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeClustersRequest:
    out: DescribeClustersRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClusterName") is not None:
        out["cluster_name"] = data["ClusterName"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ShowShardDetails") is not None:
        out["show_shard_details"] = data["ShowShardDetails"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeClustersRequest) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["ClusterName"] = value["cluster_name"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "show_shard_details" in value:
        out["ShowShardDetails"] = value["show_shard_details"]
    return out


def deserialize_cbor(data: dict) -> DescribeClustersRequest:
    out: DescribeClustersRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClusterName") is not None:
        out["cluster_name"] = data["ClusterName"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ShowShardDetails") is not None:
        out["show_shard_details"] = data["ShowShardDetails"]
    return out
