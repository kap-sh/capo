"""Generated from Smithy shape ``com.amazonaws.fsx#DescribeSnapshotsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.next_token
    import capo_fsx.types.snapshots


class DescribeSnapshotsResponse(TypedDict, closed=True):
    snapshots: NotRequired["capo_fsx.types.snapshots.Snapshots"]
    """<p>An array of snapshots.</p>"""
    next_token: NotRequired["capo_fsx.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSnapshotsResponse) -> dict:
    out: dict = {}
    if "snapshots" in value:
        import capo_fsx.types.snapshots

        out["Snapshots"] = capo_fsx.types.snapshots.serialize_aws_json_1_1(
            value["snapshots"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSnapshotsResponse:
    out: DescribeSnapshotsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Snapshots") is not None:
        import capo_fsx.types.snapshots

        out["snapshots"] = capo_fsx.types.snapshots.deserialize_aws_json_1_1(
            data["Snapshots"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: DescribeSnapshotsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "snapshots" in value:
        import capo_fsx.types.snapshots

        out["snapshots"] = capo_fsx.types.snapshots.redact_sensitive(value["snapshots"])
    return out
