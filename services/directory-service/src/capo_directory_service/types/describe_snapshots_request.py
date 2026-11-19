"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeSnapshotsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.limit
    import capo_directory_service.types.next_token
    import capo_directory_service.types.snapshot_ids


class DescribeSnapshotsRequest(TypedDict, closed=True):
    directory_id: NotRequired["capo_directory_service.types.directory_id.DirectoryId"]
    """<p>The identifier of the directory for which to retrieve snapshot information.</p>"""
    snapshot_ids: NotRequired["capo_directory_service.types.snapshot_ids.SnapshotIds"]
    """<p>A list of identifiers of the snapshots to obtain the information for. If this member is null or empty, all snapshots are returned using the <i>Limit</i> and <i>NextToken</i> members.</p>"""
    next_token: NotRequired["capo_directory_service.types.next_token.NextToken"]
    """<p>The <i>DescribeSnapshotsResult.NextToken</i> value from a previous call to <a>DescribeSnapshots</a>. Pass null if this is the first call.</p>"""
    limit: NotRequired["capo_directory_service.types.limit.Limit"]
    """<p>The maximum number of objects to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSnapshotsRequest) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "snapshot_ids" in value:
        import capo_directory_service.types.snapshot_ids

        out["SnapshotIds"] = (
            capo_directory_service.types.snapshot_ids.serialize_aws_json_1_1(
                value["snapshot_ids"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSnapshotsRequest:
    out: DescribeSnapshotsRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("SnapshotIds") is not None:
        import capo_directory_service.types.snapshot_ids

        out["snapshot_ids"] = (
            capo_directory_service.types.snapshot_ids.deserialize_aws_json_1_1(
                data["SnapshotIds"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeSnapshotsRequest) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "snapshot_ids" in value:
        import capo_directory_service.types.snapshot_ids

        out["SnapshotIds"] = capo_directory_service.types.snapshot_ids.serialize_cbor(
            value["snapshot_ids"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_cbor(data: dict) -> DescribeSnapshotsRequest:
    out: DescribeSnapshotsRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("SnapshotIds") is not None:
        import capo_directory_service.types.snapshot_ids

        out["snapshot_ids"] = (
            capo_directory_service.types.snapshot_ids.deserialize_cbor(
                data["SnapshotIds"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    return out
