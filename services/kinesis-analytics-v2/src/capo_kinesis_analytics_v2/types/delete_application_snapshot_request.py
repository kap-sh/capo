"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#DeleteApplicationSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_name
    import capo_kinesis_analytics_v2.types.snapshot_name
    import capo_kinesis_analytics_v2.types.timestamp


class DeleteApplicationSnapshotRequest(TypedDict, closed=True):
    application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName"
    """<p>The name of an existing application.</p>"""
    snapshot_name: "capo_kinesis_analytics_v2.types.snapshot_name.SnapshotName"
    """<p>The identifier for the snapshot delete.</p>"""
    snapshot_creation_timestamp: "capo_kinesis_analytics_v2.types.timestamp.Timestamp"
    """<p>The creation timestamp of the application snapshot to delete. You can retrieve this value using or .</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteApplicationSnapshotRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    out["SnapshotName"] = value["snapshot_name"]
    import capo_kinesis_analytics_v2.types.timestamp

    out["SnapshotCreationTimestamp"] = (
        capo_kinesis_analytics_v2.types.timestamp.serialize_aws_json_1_1(
            value["snapshot_creation_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteApplicationSnapshotRequest:
    out: DeleteApplicationSnapshotRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationName") is not None:
        out["application_name"] = data["ApplicationName"]
    else:
        out["application_name"] = ""
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
