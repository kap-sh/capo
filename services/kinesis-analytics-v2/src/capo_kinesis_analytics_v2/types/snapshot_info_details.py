"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#SnapshotInfoDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.runtime_environment
    import capo_kinesis_analytics_v2.types.snapshot_arn
    import capo_kinesis_analytics_v2.types.snapshot_encryption_configuration
    import capo_kinesis_analytics_v2.types.snapshot_format
    import capo_kinesis_analytics_v2.types.snapshot_initiator
    import capo_kinesis_analytics_v2.types.snapshot_initiator_operation
    import capo_kinesis_analytics_v2.types.snapshot_size_in_bytes
    import capo_kinesis_analytics_v2.types.snapshot_source_description
    import capo_kinesis_analytics_v2.types.snapshot_status
    import capo_kinesis_analytics_v2.types.snapshot_v2_description
    import capo_kinesis_analytics_v2.types.snapshot_v2_name
    import capo_kinesis_analytics_v2.types.timestamp


class SnapshotInfoDetails(TypedDict, closed=True):
    snapshot_name: "capo_kinesis_analytics_v2.types.snapshot_v2_name.SnapshotV2Name"
    """<p>The name of the enhanced snapshot.</p>"""
    snapshot_arn: "capo_kinesis_analytics_v2.types.snapshot_arn.SnapshotArn"
    """<p>The ARN of the enhanced snapshot.</p>"""
    snapshot_description: NotRequired[
        "capo_kinesis_analytics_v2.types.snapshot_v2_description.SnapshotV2Description"
    ]
    """<p>The summary description of the snapshot.</p>"""
    snapshot_status: "capo_kinesis_analytics_v2.types.snapshot_status.SnapshotStatus"
    """<p>The status of the enhanced snapshot.</p>"""
    snapshot_creation_timestamp: "capo_kinesis_analytics_v2.types.timestamp.Timestamp"
    """<p>The timestamp that indicates when the snapshot was created.</p>"""
    runtime_environment: NotRequired[
        "capo_kinesis_analytics_v2.types.runtime_environment.RuntimeEnvironment"
    ]
    """<p>The Flink runtime of the application that the snapshot was created from. This field is not present for imported snapshots.</p>"""
    snapshot_size_in_bytes: (
        "capo_kinesis_analytics_v2.types.snapshot_size_in_bytes.SnapshotSizeInBytes"
    )
    """<p>The size of the snapshot, in bytes. The value is <code>0</code> until the snapshot status is <code>READY</code>.</p>"""
    snapshot_encryption_configuration_description: NotRequired[
        "capo_kinesis_analytics_v2.types.snapshot_encryption_configuration.SnapshotEncryptionConfiguration"
    ]
    """<p>Describes the encryption settings of data at rest for the snapshot.</p>"""
    snapshot_initiator: (
        "capo_kinesis_analytics_v2.types.snapshot_initiator.SnapshotInitiator"
    )
    """<p>Indicates who initiated the snapshot. <code>USER</code> indicates a snapshot that you created or imported. <code>SYSTEM</code> indicates a snapshot that Managed Service for Apache Flink created.</p>"""
    snapshot_initiator_operation: "capo_kinesis_analytics_v2.types.snapshot_initiator_operation.SnapshotInitiatorOperation"
    """<p>The operation that created the snapshot.</p>"""
    snapshot_source_description: "capo_kinesis_analytics_v2.types.snapshot_source_description.SnapshotSourceDescription"
    """<p>Describes the source of the snapshot.</p>"""
    snapshot_format: "capo_kinesis_analytics_v2.types.snapshot_format.SnapshotFormat"
    """<p>The format of the snapshot.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotInfoDetails) -> dict:
    out: dict = {}
    out["SnapshotName"] = value["snapshot_name"]
    out["SnapshotArn"] = value["snapshot_arn"]
    if "snapshot_description" in value:
        out["SnapshotDescription"] = value["snapshot_description"]
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
    if "runtime_environment" in value:
        import capo_kinesis_analytics_v2.types.runtime_environment

        out["RuntimeEnvironment"] = (
            capo_kinesis_analytics_v2.types.runtime_environment.serialize_aws_json_1_1(
                value["runtime_environment"]
            )
        )
    out["SnapshotSizeInBytes"] = value.get("snapshot_size_in_bytes", 0)
    if "snapshot_encryption_configuration_description" in value:
        import capo_kinesis_analytics_v2.types.snapshot_encryption_configuration

        out["SnapshotEncryptionConfigurationDescription"] = (
            capo_kinesis_analytics_v2.types.snapshot_encryption_configuration.serialize_aws_json_1_1(
                value["snapshot_encryption_configuration_description"]
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
    import capo_kinesis_analytics_v2.types.snapshot_source_description

    out["SnapshotSourceDescription"] = (
        capo_kinesis_analytics_v2.types.snapshot_source_description.serialize_aws_json_1_1(
            value["snapshot_source_description"]
        )
    )
    import capo_kinesis_analytics_v2.types.snapshot_format

    out["SnapshotFormat"] = (
        capo_kinesis_analytics_v2.types.snapshot_format.serialize_aws_json_1_1(
            value["snapshot_format"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SnapshotInfoDetails:
    out: SnapshotInfoDetails = {}  # type: ignore[typeddict-item]
    if data.get("SnapshotName") is not None:
        out["snapshot_name"] = data["SnapshotName"]
    else:
        out["snapshot_name"] = ""
    if data.get("SnapshotArn") is not None:
        out["snapshot_arn"] = data["SnapshotArn"]
    else:
        out["snapshot_arn"] = ""
    if data.get("SnapshotDescription") is not None:
        out["snapshot_description"] = data["SnapshotDescription"]
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
    if data.get("RuntimeEnvironment") is not None:
        import capo_kinesis_analytics_v2.types.runtime_environment

        out["runtime_environment"] = (
            capo_kinesis_analytics_v2.types.runtime_environment.deserialize_aws_json_1_1(
                data["RuntimeEnvironment"]
            )
        )
    if data.get("SnapshotSizeInBytes") is not None:
        out["snapshot_size_in_bytes"] = data["SnapshotSizeInBytes"]
    else:
        out["snapshot_size_in_bytes"] = 0
    if data.get("SnapshotEncryptionConfigurationDescription") is not None:
        import capo_kinesis_analytics_v2.types.snapshot_encryption_configuration

        out["snapshot_encryption_configuration_description"] = (
            capo_kinesis_analytics_v2.types.snapshot_encryption_configuration.deserialize_aws_json_1_1(
                data["SnapshotEncryptionConfigurationDescription"]
            )
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
    if data.get("SnapshotSourceDescription") is not None:
        import capo_kinesis_analytics_v2.types.snapshot_source_description

        out["snapshot_source_description"] = (
            capo_kinesis_analytics_v2.types.snapshot_source_description.deserialize_aws_json_1_1(
                data["SnapshotSourceDescription"]
            )
        )
    else:
        raise DeserializationError(
            "SnapshotInfoDetails.snapshot_source_description required"
        )
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
