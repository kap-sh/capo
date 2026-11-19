"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#DescribeSnapshotOperationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.snapshot_operation_id
    import capo_kinesis_analytics_v2.types.snapshot_v2_name


class DescribeSnapshotOperationRequest(TypedDict, closed=True):
    snapshot_name: "capo_kinesis_analytics_v2.types.snapshot_v2_name.SnapshotV2Name"
    """<p>The name of the enhanced snapshot.</p>"""
    snapshot_operation_id: (
        "capo_kinesis_analytics_v2.types.snapshot_operation_id.SnapshotOperationId"
    )
    """<p>The ID of the snapshot operation. You can retrieve this value using <code>ListSnapshotOperations</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSnapshotOperationRequest) -> dict:
    out: dict = {}
    out["SnapshotName"] = value["snapshot_name"]
    out["SnapshotOperationId"] = value["snapshot_operation_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSnapshotOperationRequest:
    out: DescribeSnapshotOperationRequest = {}  # type: ignore[typeddict-item]
    if data.get("SnapshotName") is not None:
        out["snapshot_name"] = data["SnapshotName"]
    else:
        out["snapshot_name"] = ""
    if data.get("SnapshotOperationId") is not None:
        out["snapshot_operation_id"] = data["SnapshotOperationId"]
    else:
        out["snapshot_operation_id"] = ""
    return out
