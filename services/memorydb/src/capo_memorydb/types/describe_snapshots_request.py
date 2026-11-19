"""Generated from Smithy shape ``com.amazonaws.memorydb#DescribeSnapshotsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.boolean_optional
    import capo_memorydb.types.integer_optional
    import capo_memorydb.types.string


class DescribeSnapshotsRequest(TypedDict, closed=True):
    cluster_name: NotRequired["capo_memorydb.types.string.String"]
    """<p>A user-supplied cluster identifier. If this parameter is specified, only snapshots associated with that specific cluster are described.</p>"""
    snapshot_name: NotRequired["capo_memorydb.types.string.String"]
    """<p>A user-supplied name of the snapshot. If this parameter is specified, only this named snapshot is described.</p>"""
    source: NotRequired["capo_memorydb.types.string.String"]
    """<p>If set to system, the output shows snapshots that were automatically created by MemoryDB. If set to user the output shows snapshots that were manually created. If omitted, the output shows both automatically and manually created snapshots.</p>"""
    next_token: NotRequired["capo_memorydb.types.string.String"]
    """<p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>"""
    max_results: NotRequired["capo_memorydb.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>"""
    show_detail: NotRequired["capo_memorydb.types.boolean_optional.BooleanOptional"]
    """<p>A Boolean value which if true, the shard configuration is included in the snapshot description.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSnapshotsRequest) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["ClusterName"] = value["cluster_name"]
    if "snapshot_name" in value:
        out["SnapshotName"] = value["snapshot_name"]
    if "source" in value:
        out["Source"] = value["source"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "show_detail" in value:
        out["ShowDetail"] = value["show_detail"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSnapshotsRequest:
    out: DescribeSnapshotsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClusterName") is not None:
        out["cluster_name"] = data["ClusterName"]
    if data.get("SnapshotName") is not None:
        out["snapshot_name"] = data["SnapshotName"]
    if data.get("Source") is not None:
        out["source"] = data["Source"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("ShowDetail") is not None:
        out["show_detail"] = data["ShowDetail"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeSnapshotsRequest) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["ClusterName"] = value["cluster_name"]
    if "snapshot_name" in value:
        out["SnapshotName"] = value["snapshot_name"]
    if "source" in value:
        out["Source"] = value["source"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "show_detail" in value:
        out["ShowDetail"] = value["show_detail"]
    return out


def deserialize_cbor(data: dict) -> DescribeSnapshotsRequest:
    out: DescribeSnapshotsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClusterName") is not None:
        out["cluster_name"] = data["ClusterName"]
    if data.get("SnapshotName") is not None:
        out["snapshot_name"] = data["SnapshotName"]
    if data.get("Source") is not None:
        out["source"] = data["Source"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("ShowDetail") is not None:
        out["show_detail"] = data["ShowDetail"]
    return out
