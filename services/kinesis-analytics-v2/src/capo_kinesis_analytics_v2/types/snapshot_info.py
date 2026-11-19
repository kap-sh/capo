"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#SnapshotInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_name
    import capo_kinesis_analytics_v2.types.snapshot_arn
    import capo_kinesis_analytics_v2.types.snapshot_format
    import capo_kinesis_analytics_v2.types.snapshot_initiator
    import capo_kinesis_analytics_v2.types.snapshot_initiator_operation
    import capo_kinesis_analytics_v2.types.snapshot_status
    import capo_kinesis_analytics_v2.types.snapshot_v2_name
    import capo_kinesis_analytics_v2.types.timestamp


class SnapshotInfo(TypedDict, closed=True):
    snapshot_name: "capo_kinesis_analytics_v2.types.snapshot_v2_name.SnapshotV2Name"
    """<p>The name of the enhanced snapshot.</p>"""
    snapshot_arn: "capo_kinesis_analytics_v2.types.snapshot_arn.SnapshotArn"
    """<p>The ARN of the enhanced snapshot.</p>"""
    snapshot_status: "capo_kinesis_analytics_v2.types.snapshot_status.SnapshotStatus"
    """<p>The status of the enhanced snapshot.</p>"""
    snapshot_creation_timestamp: "capo_kinesis_analytics_v2.types.timestamp.Timestamp"
    """<p>The timestamp that indicates when the snapshot was created.</p>"""
    snapshot_initiator: (
        "capo_kinesis_analytics_v2.types.snapshot_initiator.SnapshotInitiator"
    )
    """<p>Indicates who initiated the snapshot. <code>USER</code> indicates a snapshot that you created or imported. <code>SYSTEM</code> indicates a snapshot that Managed Service for Apache Flink created.</p>"""
    snapshot_initiator_operation: "capo_kinesis_analytics_v2.types.snapshot_initiator_operation.SnapshotInitiatorOperation"
    """<p>The operation that created the snapshot.</p>"""
    source_application_name: NotRequired[
        "capo_kinesis_analytics_v2.types.application_name.ApplicationName"
    ]
    snapshot_format: "capo_kinesis_analytics_v2.types.snapshot_format.SnapshotFormat"
    """<p>The format of the snapshot.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotInfo) -> dict:
    out: dict = {}
    out["SnapshotName"] = value["snapshot_name"]
    out["SnapshotArn"] = value["snapshot_arn"]
    import capo_kinesis_analytics_v2.types.snapshot_status

    out["SnapshotStatus"] = (
        capo_kinesis_analytics_v2.types.snapshot_status.serialize_aws_json_1_1(
            value["snapshot_status"]
        )
    )
    import capo_kinesis_analytics_v2.types.timestamp

    out["SnapshotCreationTimestamp"] = (
        capo_kinesis_analytics_v2.types.timestamp.serialize_aws_json_1_1(
            value["snapshot_creation_timestamp"]
        )
    )
    import capo_kinesis_analytics_v2.types.snapshot_initiator

    out["SnapshotInitiator"] = (
        capo_kinesis_analytics_v2.types.snapshot_initiator.serialize_aws_json_1_1(
            value["snapshot_initiator"]
        )
    )
    import capo_kinesis_analytics_v2.types.snapshot_initiator_operation

    out["SnapshotInitiatorOperation"] = (
        capo_kinesis_analytics_v2.types.snapshot_initiator_operation.serialize_aws_json_1_1(
            value["snapshot_initiator_operation"]
        )
    )
    if "source_application_name" in value:
        out["SourceApplicationName"] = value["source_application_name"]
    import capo_kinesis_analytics_v2.types.snapshot_format

    out["SnapshotFormat"] = (
        capo_kinesis_analytics_v2.types.snapshot_format.serialize_aws_json_1_1(
            value["snapshot_format"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SnapshotInfo:
    out: SnapshotInfo = {}  # type: ignore[typeddict-item]
    if data.get("SnapshotName") is not None:
        out["snapshot_name"] = data["SnapshotName"]
    else:
        out["snapshot_name"] = ""
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
    if data.get("SnapshotInitiator") is not None:
        import capo_kinesis_analytics_v2.types.snapshot_initiator

        out["snapshot_initiator"] = (
            capo_kinesis_analytics_v2.types.snapshot_initiator.deserialize_aws_json_1_1(
                data["SnapshotInitiator"]
            )
        )
    else:
        import typing

        out["snapshot_initiator"] = typing.cast(
            "capo_kinesis_analytics_v2.types.snapshot_initiator.SnapshotInitiator", ""
        )
    if data.get("SnapshotInitiatorOperation") is not None:
        import capo_kinesis_analytics_v2.types.snapshot_initiator_operation

        out["snapshot_initiator_operation"] = (
            capo_kinesis_analytics_v2.types.snapshot_initiator_operation.deserialize_aws_json_1_1(
                data["SnapshotInitiatorOperation"]
            )
        )
    else:
        import typing

        out["snapshot_initiator_operation"] = typing.cast(
            "capo_kinesis_analytics_v2.types.snapshot_initiator_operation.SnapshotInitiatorOperation",
            "",
        )
    if data.get("SourceApplicationName") is not None:
        out["source_application_name"] = data["SourceApplicationName"]
    if data.get("SnapshotFormat") is not None:
        import capo_kinesis_analytics_v2.types.snapshot_format

        out["snapshot_format"] = (
            capo_kinesis_analytics_v2.types.snapshot_format.deserialize_aws_json_1_1(
                data["SnapshotFormat"]
            )
        )
    else:
        import typing

        out["snapshot_format"] = typing.cast(
            "capo_kinesis_analytics_v2.types.snapshot_format.SnapshotFormat", ""
        )
    return out
