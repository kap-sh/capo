"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ImportSnapshotResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.snapshot_arn
    import capo_kinesis_analytics_v2.types.snapshot_operation_id
    import capo_kinesis_analytics_v2.types.snapshot_operation_status
    import capo_kinesis_analytics_v2.types.snapshot_status


class ImportSnapshotResponse(TypedDict, closed=True):
    snapshot_arn: "capo_kinesis_analytics_v2.types.snapshot_arn.SnapshotArn"
    """<p>The ARN of the enhanced snapshot.</p>"""
    snapshot_status: "capo_kinesis_analytics_v2.types.snapshot_status.SnapshotStatus"
    """<p>The status of the snapshot. When Managed Service for Apache Flink accepts the request, the status is <code>CREATING</code>.</p>"""
    snapshot_operation_id: (
        "capo_kinesis_analytics_v2.types.snapshot_operation_id.SnapshotOperationId"
    )
    """<p>The ID of the snapshot operation. You can use this value with <code>DescribeSnapshotOperation</code> to track the progress of the import.</p>"""
    snapshot_operation_status: "capo_kinesis_analytics_v2.types.snapshot_operation_status.SnapshotOperationStatus"
    """<p>The status of the snapshot operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportSnapshotResponse) -> dict:
    out: dict = {}
    out["SnapshotArn"] = value["snapshot_arn"]
    import capo_kinesis_analytics_v2.types.snapshot_status

    out["SnapshotStatus"] = (
        capo_kinesis_analytics_v2.types.snapshot_status.serialize_aws_json_1_1(
            value["snapshot_status"]
        )
    )
    out["SnapshotOperationId"] = value["snapshot_operation_id"]
    import capo_kinesis_analytics_v2.types.snapshot_operation_status

    out["SnapshotOperationStatus"] = (
        capo_kinesis_analytics_v2.types.snapshot_operation_status.serialize_aws_json_1_1(
            value["snapshot_operation_status"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportSnapshotResponse:
    out: ImportSnapshotResponse = {}  # type: ignore[typeddict-item]
    if data.get("SnapshotArn") is not None:
        out["snapshot_arn"] = data["SnapshotArn"]
    else:
        out["snapshot_arn"] = ""
    if data.get("SnapshotStatus") is not None:
        import capo_kinesis_analytics_v2.types.snapshot_status

        out["snapshot_status"] = (
            capo_kinesis_analytics_v2.types.snapshot_status.deserialize_aws_json_1_1(
                data["SnapshotStatus"]
            )
        )
    else:
        import typing

        out["snapshot_status"] = typing.cast(
            "capo_kinesis_analytics_v2.types.snapshot_status.SnapshotStatus", ""
        )
    if data.get("SnapshotOperationId") is not None:
        out["snapshot_operation_id"] = data["SnapshotOperationId"]
    else:
        out["snapshot_operation_id"] = ""
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
    return out
