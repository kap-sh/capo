"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#SnapshotOperationInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.snapshot_operation
    import capo_kinesis_analytics_v2.types.snapshot_operation_id
    import capo_kinesis_analytics_v2.types.snapshot_operation_status
    import capo_kinesis_analytics_v2.types.timestamp


class SnapshotOperationInfo(TypedDict, closed=True):
    snapshot_operation_id: (
        "capo_kinesis_analytics_v2.types.snapshot_operation_id.SnapshotOperationId"
    )
    """<p>The ID of the snapshot operation.</p>"""
    snapshot_operation: (
        "capo_kinesis_analytics_v2.types.snapshot_operation.SnapshotOperation"
    )
    """<p>The type of operation that was performed on the snapshot.</p>"""
    snapshot_operation_status: "capo_kinesis_analytics_v2.types.snapshot_operation_status.SnapshotOperationStatus"
    """<p>The status of the snapshot operation.</p>"""
    start_time: NotRequired["capo_kinesis_analytics_v2.types.timestamp.Timestamp"]
    """<p>The timestamp that indicates when the operation was created.</p>"""
    end_time: NotRequired["capo_kinesis_analytics_v2.types.timestamp.Timestamp"]
    """<p>The timestamp that indicates when the operation finished. This field is present only after the operation completes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotOperationInfo) -> dict:
    out: dict = {}
    out["SnapshotOperationId"] = value["snapshot_operation_id"]
    import capo_kinesis_analytics_v2.types.snapshot_operation

    out["SnapshotOperation"] = (
        capo_kinesis_analytics_v2.types.snapshot_operation.serialize_aws_json_1_1(
            value["snapshot_operation"]
        )
    )
    import capo_kinesis_analytics_v2.types.snapshot_operation_status

    out["SnapshotOperationStatus"] = (
        capo_kinesis_analytics_v2.types.snapshot_operation_status.serialize_aws_json_1_1(
            value["snapshot_operation_status"]
        )
    )
    if "start_time" in value:
        import capo_kinesis_analytics_v2.types.timestamp

        out["StartTime"] = (
            capo_kinesis_analytics_v2.types.timestamp.serialize_aws_json_1_1(
                value["start_time"]
            )
        )
    if "end_time" in value:
        import capo_kinesis_analytics_v2.types.timestamp

        out["EndTime"] = (
            capo_kinesis_analytics_v2.types.timestamp.serialize_aws_json_1_1(
                value["end_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SnapshotOperationInfo:
    out: SnapshotOperationInfo = {}  # type: ignore[typeddict-item]
    if data.get("SnapshotOperationId") is not None:
        out["snapshot_operation_id"] = data["SnapshotOperationId"]
    else:
        out["snapshot_operation_id"] = ""
    if data.get("SnapshotOperation") is not None:
        import capo_kinesis_analytics_v2.types.snapshot_operation

        out["snapshot_operation"] = (
            capo_kinesis_analytics_v2.types.snapshot_operation.deserialize_aws_json_1_1(
                data["SnapshotOperation"]
            )
        )
    else:
        import typing

        out["snapshot_operation"] = typing.cast(
            "capo_kinesis_analytics_v2.types.snapshot_operation.SnapshotOperation", ""
        )
    if data.get("SnapshotOperationStatus") is not None:
        import capo_kinesis_analytics_v2.types.snapshot_operation_status

        out["snapshot_operation_status"] = (
            capo_kinesis_analytics_v2.types.snapshot_operation_status.deserialize_aws_json_1_1(
                data["SnapshotOperationStatus"]
            )
        )
    else:
        import typing

        out["snapshot_operation_status"] = typing.cast(
            "capo_kinesis_analytics_v2.types.snapshot_operation_status.SnapshotOperationStatus",
            "",
        )
    if data.get("StartTime") is not None:
        import capo_kinesis_analytics_v2.types.timestamp

        out["start_time"] = (
            capo_kinesis_analytics_v2.types.timestamp.deserialize_aws_json_1_1(
                data["StartTime"]
            )
        )
    if data.get("EndTime") is not None:
        import capo_kinesis_analytics_v2.types.timestamp

        out["end_time"] = (
            capo_kinesis_analytics_v2.types.timestamp.deserialize_aws_json_1_1(
                data["EndTime"]
            )
        )
    return out
