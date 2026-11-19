"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#SnapshotOperationInfoDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_operation_description
    import capo_kinesis_analytics_v2.types.encryption_configuration_description
    import capo_kinesis_analytics_v2.types.snapshot_arn
    import capo_kinesis_analytics_v2.types.snapshot_operation
    import capo_kinesis_analytics_v2.types.snapshot_operation_failure_details
    import capo_kinesis_analytics_v2.types.snapshot_operation_id
    import capo_kinesis_analytics_v2.types.snapshot_operation_location_description
    import capo_kinesis_analytics_v2.types.snapshot_operation_status
    import capo_kinesis_analytics_v2.types.timestamp


class SnapshotOperationInfoDetails(TypedDict, closed=True):
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
    snapshot_arn: "capo_kinesis_analytics_v2.types.snapshot_arn.SnapshotArn"
    """<p>The ARN of the enhanced snapshot.</p>"""
    source_encryption_configuration_description: NotRequired[
        "capo_kinesis_analytics_v2.types.encryption_configuration_description.EncryptionConfigurationDescription"
    ]
    """<p>Describes the encryption configuration of the source data. This field is present only for <code>ImportSnapshot</code> operation.</p>"""
    destination_encryption_configuration_description: NotRequired[
        "capo_kinesis_analytics_v2.types.encryption_configuration_description.EncryptionConfigurationDescription"
    ]
    """<p>Describes the encryption configuration of the destination data. This field is present only for <code>ImportSnapshot</code> and <code>ExportSnapshot</code> operations.</p>"""
    snapshot_source_location_description: NotRequired[
        "capo_kinesis_analytics_v2.types.snapshot_operation_location_description.SnapshotOperationLocationDescription"
    ]
    """<p>Describes the location that the snapshot data was read from. This field is present only for <code>ImportSnapshot</code> operations.</p>"""
    snapshot_destination_location_description: NotRequired[
        "capo_kinesis_analytics_v2.types.snapshot_operation_location_description.SnapshotOperationLocationDescription"
    ]
    """<p>Describes the location that the snapshot data was written to. This field is present only for <code>ExportSnapshot</code> operations, after the operation completes.</p>"""
    application_operation_description: NotRequired[
        "capo_kinesis_analytics_v2.types.application_operation_description.ApplicationOperationDescription"
    ]
    """<p>Describes the application operation that initiated the snapshot operation. This field is present only for <code>SystemCreateSnapshot</code> operations.</p>"""
    start_time: NotRequired["capo_kinesis_analytics_v2.types.timestamp.Timestamp"]
    """<p>The timestamp that indicates when the operation was created.</p>"""
    end_time: NotRequired["capo_kinesis_analytics_v2.types.timestamp.Timestamp"]
    """<p>The timestamp that indicates when the operation finished. This field is present only after the operation completes.</p>"""
    snapshot_operation_failure_details: NotRequired[
        "capo_kinesis_analytics_v2.types.snapshot_operation_failure_details.SnapshotOperationFailureDetails"
    ]
    """<p>Provides a description of the operation failure. This field is present only if <code>SnapshotOperationStatus</code> is <code>FAILED</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotOperationInfoDetails) -> dict:
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
    out["SnapshotArn"] = value["snapshot_arn"]
    if "source_encryption_configuration_description" in value:
        import capo_kinesis_analytics_v2.types.encryption_configuration_description

        out["SourceEncryptionConfigurationDescription"] = (
            capo_kinesis_analytics_v2.types.encryption_configuration_description.serialize_aws_json_1_1(
                value["source_encryption_configuration_description"]
            )
        )
    if "destination_encryption_configuration_description" in value:
        import capo_kinesis_analytics_v2.types.encryption_configuration_description

        out["DestinationEncryptionConfigurationDescription"] = (
            capo_kinesis_analytics_v2.types.encryption_configuration_description.serialize_aws_json_1_1(
                value["destination_encryption_configuration_description"]
            )
        )
    if "snapshot_source_location_description" in value:
        import capo_kinesis_analytics_v2.types.snapshot_operation_location_description

        out["SnapshotSourceLocationDescription"] = (
            capo_kinesis_analytics_v2.types.snapshot_operation_location_description.serialize_aws_json_1_1(
                value["snapshot_source_location_description"]
            )
        )
    if "snapshot_destination_location_description" in value:
        import capo_kinesis_analytics_v2.types.snapshot_operation_location_description

        out["SnapshotDestinationLocationDescription"] = (
            capo_kinesis_analytics_v2.types.snapshot_operation_location_description.serialize_aws_json_1_1(
                value["snapshot_destination_location_description"]
            )
        )
    if "application_operation_description" in value:
        import capo_kinesis_analytics_v2.types.application_operation_description

        out["ApplicationOperationDescription"] = (
            capo_kinesis_analytics_v2.types.application_operation_description.serialize_aws_json_1_1(
                value["application_operation_description"]
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
    if "snapshot_operation_failure_details" in value:
        import capo_kinesis_analytics_v2.types.snapshot_operation_failure_details

        out["SnapshotOperationFailureDetails"] = (
            capo_kinesis_analytics_v2.types.snapshot_operation_failure_details.serialize_aws_json_1_1(
                value["snapshot_operation_failure_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SnapshotOperationInfoDetails:
    out: SnapshotOperationInfoDetails = {}  # type: ignore[typeddict-item]
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
    if data.get("SnapshotArn") is not None:
        out["snapshot_arn"] = data["SnapshotArn"]
    else:
        out["snapshot_arn"] = ""
    if data.get("SourceEncryptionConfigurationDescription") is not None:
        import capo_kinesis_analytics_v2.types.encryption_configuration_description

        out["source_encryption_configuration_description"] = (
            capo_kinesis_analytics_v2.types.encryption_configuration_description.deserialize_aws_json_1_1(
                data["SourceEncryptionConfigurationDescription"]
            )
        )
    if data.get("DestinationEncryptionConfigurationDescription") is not None:
        import capo_kinesis_analytics_v2.types.encryption_configuration_description

        out["destination_encryption_configuration_description"] = (
            capo_kinesis_analytics_v2.types.encryption_configuration_description.deserialize_aws_json_1_1(
                data["DestinationEncryptionConfigurationDescription"]
            )
        )
    if data.get("SnapshotSourceLocationDescription") is not None:
        import capo_kinesis_analytics_v2.types.snapshot_operation_location_description

        out["snapshot_source_location_description"] = (
            capo_kinesis_analytics_v2.types.snapshot_operation_location_description.deserialize_aws_json_1_1(
                data["SnapshotSourceLocationDescription"]
            )
        )
    if data.get("SnapshotDestinationLocationDescription") is not None:
        import capo_kinesis_analytics_v2.types.snapshot_operation_location_description

        out["snapshot_destination_location_description"] = (
            capo_kinesis_analytics_v2.types.snapshot_operation_location_description.deserialize_aws_json_1_1(
                data["SnapshotDestinationLocationDescription"]
            )
        )
    if data.get("ApplicationOperationDescription") is not None:
        import capo_kinesis_analytics_v2.types.application_operation_description

        out["application_operation_description"] = (
            capo_kinesis_analytics_v2.types.application_operation_description.deserialize_aws_json_1_1(
                data["ApplicationOperationDescription"]
            )
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
    if data.get("SnapshotOperationFailureDetails") is not None:
        import capo_kinesis_analytics_v2.types.snapshot_operation_failure_details

        out["snapshot_operation_failure_details"] = (
            capo_kinesis_analytics_v2.types.snapshot_operation_failure_details.deserialize_aws_json_1_1(
                data["SnapshotOperationFailureDetails"]
            )
        )
    return out
