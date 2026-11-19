"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#DescribeSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.snapshot_v2_name


class DescribeSnapshotRequest(TypedDict, closed=True):
    snapshot_name: "capo_kinesis_analytics_v2.types.snapshot_v2_name.SnapshotV2Name"
    """<p>The name of the enhanced snapshot. You can retrieve this value using <code>ListSnapshots</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSnapshotRequest) -> dict:
    out: dict = {}
    out["SnapshotName"] = value["snapshot_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSnapshotRequest:
    out: DescribeSnapshotRequest = {}  # type: ignore[typeddict-item]
    if data.get("SnapshotName") is not None:
        out["snapshot_name"] = data["SnapshotName"]
    else:
        out["snapshot_name"] = ""
    return out
