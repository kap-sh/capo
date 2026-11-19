"""Generated from Smithy shape ``com.amazonaws.memorydb#DescribeSnapshotsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.snapshot_list
    import capo_memorydb.types.string


class DescribeSnapshotsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_memorydb.types.string.String"]
    """<p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>"""
    snapshots: NotRequired["capo_memorydb.types.snapshot_list.SnapshotList"]
    """<p>A list of snapshots. Each item in the list contains detailed information about one snapshot.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSnapshotsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "snapshots" in value:
        import capo_memorydb.types.snapshot_list

        out["Snapshots"] = capo_memorydb.types.snapshot_list.serialize_aws_json_1_1(
            value["snapshots"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSnapshotsResponse:
    out: DescribeSnapshotsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Snapshots") is not None:
        import capo_memorydb.types.snapshot_list

        out["snapshots"] = capo_memorydb.types.snapshot_list.deserialize_aws_json_1_1(
            data["Snapshots"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeSnapshotsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "snapshots" in value:
        import capo_memorydb.types.snapshot_list

        out["Snapshots"] = capo_memorydb.types.snapshot_list.serialize_cbor(
            value["snapshots"]
        )
    return out


def deserialize_cbor(data: dict) -> DescribeSnapshotsResponse:
    out: DescribeSnapshotsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Snapshots") is not None:
        import capo_memorydb.types.snapshot_list

        out["snapshots"] = capo_memorydb.types.snapshot_list.deserialize_cbor(
            data["Snapshots"]
        )
    return out
