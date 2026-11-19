"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#DeleteSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.snapshot_v2_name
    import capo_kinesis_analytics_v2.types.timestamp


class DeleteSnapshotRequest(TypedDict, closed=True):
    snapshot_name: "capo_kinesis_analytics_v2.types.snapshot_v2_name.SnapshotV2Name"
    """<p>The name of the enhanced snapshot to delete.</p>"""
    snapshot_creation_timestamp: "capo_kinesis_analytics_v2.types.timestamp.Timestamp"
    """<p>The creation timestamp of the enhanced snapshot to delete. Use the <code>DescribeSnapshot</code> operation to get this value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSnapshotRequest) -> dict:
    out: dict = {}
    out["SnapshotName"] = value["snapshot_name"]
    import capo_kinesis_analytics_v2.types.timestamp

    out["SnapshotCreationTimestamp"] = (
        capo_kinesis_analytics_v2.types.timestamp.serialize_aws_json_1_1(
            value["snapshot_creation_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSnapshotRequest:
    out: DeleteSnapshotRequest = {}  # type: ignore[typeddict-item]
    if data.get("SnapshotName") is not None:
        out["snapshot_name"] = data["SnapshotName"]
    else:
        out["snapshot_name"] = ""
    if data.get("SnapshotCreationTimestamp") is not None:
        import capo_kinesis_analytics_v2.types.timestamp

        out["snapshot_creation_timestamp"] = (
            capo_kinesis_analytics_v2.types.timestamp.deserialize_aws_json_1_1(
                data["SnapshotCreationTimestamp"]
            )
        )
    else:
        import datetime

        out["snapshot_creation_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
