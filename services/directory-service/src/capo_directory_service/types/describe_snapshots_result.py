"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeSnapshotsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.next_token
    import capo_directory_service.types.snapshots


class DescribeSnapshotsResult(TypedDict, closed=True):
    snapshots: NotRequired["capo_directory_service.types.snapshots.Snapshots"]
    """<p>The list of <a>Snapshot</a> objects that were retrieved.</p> <p>It is possible that this list contains less than the number of items specified in the <i>Limit</i> member of the request. This occurs if there are less than the requested number of items left to retrieve, or if the limitations of the operation have been exceeded.</p>"""
    next_token: NotRequired["capo_directory_service.types.next_token.NextToken"]
    """<p>If not null, more results are available. Pass this value in the <i>NextToken</i> member of a subsequent call to <a>DescribeSnapshots</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSnapshotsResult) -> dict:
    out: dict = {}
    if "snapshots" in value:
        import capo_directory_service.types.snapshots

        out["Snapshots"] = (
            capo_directory_service.types.snapshots.serialize_aws_json_1_1(
                value["snapshots"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSnapshotsResult:
    out: DescribeSnapshotsResult = {}  # type: ignore[typeddict-item]
    if data.get("Snapshots") is not None:
        import capo_directory_service.types.snapshots

        out["snapshots"] = (
            capo_directory_service.types.snapshots.deserialize_aws_json_1_1(
                data["Snapshots"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeSnapshotsResult) -> dict:
    out: dict = {}
    if "snapshots" in value:
        import capo_directory_service.types.snapshots

        out["Snapshots"] = capo_directory_service.types.snapshots.serialize_cbor(
            value["snapshots"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeSnapshotsResult:
    out: DescribeSnapshotsResult = {}  # type: ignore[typeddict-item]
    if data.get("Snapshots") is not None:
        import capo_directory_service.types.snapshots

        out["snapshots"] = capo_directory_service.types.snapshots.deserialize_cbor(
            data["Snapshots"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
