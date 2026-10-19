"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#SnapshotDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_encryption_configuration_description
    import capo_kinesis_analytics_v2.types.application_version_id
    import capo_kinesis_analytics_v2.types.runtime_environment
    import capo_kinesis_analytics_v2.types.snapshot_name
    import capo_kinesis_analytics_v2.types.snapshot_status
    import capo_kinesis_analytics_v2.types.timestamp


class SnapshotDetails(TypedDict, closed=True):
    snapshot_name: "capo_kinesis_analytics_v2.types.snapshot_name.SnapshotName"
    """<p>The identifier for the application snapshot.</p>"""
    snapshot_status: "capo_kinesis_analytics_v2.types.snapshot_status.SnapshotStatus"
    """<p>The status of the application snapshot.</p>"""
    application_version_id: (
        "capo_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    )
    """<p>The current application version ID when the snapshot was created.</p>"""
    snapshot_creation_timestamp: NotRequired[
        "capo_kinesis_analytics_v2.types.timestamp.Timestamp"
    ]
    """<p>The timestamp of the application snapshot.</p>"""
    runtime_environment: NotRequired[
        "capo_kinesis_analytics_v2.types.runtime_environment.RuntimeEnvironment"
    ]
    """<p>The Flink Runtime for the application snapshot.</p>"""
    application_encryption_configuration_description: NotRequired[
        "capo_kinesis_analytics_v2.types.application_encryption_configuration_description.ApplicationEncryptionConfigurationDescription"
    ]
    """<p>Specifies the encryption settings of data at rest for the application snapshot.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotDetails) -> dict:
    out: dict = {}
    out["SnapshotName"] = value["snapshot_name"]
    import capo_kinesis_analytics_v2.types.snapshot_status

    out["SnapshotStatus"] = (
        capo_kinesis_analytics_v2.types.snapshot_status.serialize_aws_json_1_1(
            value["snapshot_status"]
        )
    )
    out["ApplicationVersionId"] = value["application_version_id"]
    if "snapshot_creation_timestamp" in value:
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
    if "application_encryption_configuration_description" in value:
        import capo_kinesis_analytics_v2.types.application_encryption_configuration_description

        out["ApplicationEncryptionConfigurationDescription"] = (
            capo_kinesis_analytics_v2.types.application_encryption_configuration_description.serialize_aws_json_1_1(
                value["application_encryption_configuration_description"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SnapshotDetails:
    out: SnapshotDetails = {}  # type: ignore[typeddict-item]
    if data.get("SnapshotName") is not None:
        out["snapshot_name"] = data["SnapshotName"]
    else:
        out["snapshot_name"] = ""
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
    if data.get("ApplicationVersionId") is not None:
        out["application_version_id"] = data["ApplicationVersionId"]
    else:
        out["application_version_id"] = 0
    if data.get("SnapshotCreationTimestamp") is not None:
        import capo_kinesis_analytics_v2.types.timestamp

        out["snapshot_creation_timestamp"] = (
            capo_kinesis_analytics_v2.types.timestamp.deserialize_aws_json_1_1(
                data["SnapshotCreationTimestamp"]
            )
        )
    if data.get("RuntimeEnvironment") is not None:
        import capo_kinesis_analytics_v2.types.runtime_environment

        out["runtime_environment"] = (
            capo_kinesis_analytics_v2.types.runtime_environment.deserialize_aws_json_1_1(
                data["RuntimeEnvironment"]
            )
        )
    if data.get("ApplicationEncryptionConfigurationDescription") is not None:
        import capo_kinesis_analytics_v2.types.application_encryption_configuration_description

        out["application_encryption_configuration_description"] = (
            capo_kinesis_analytics_v2.types.application_encryption_configuration_description.deserialize_aws_json_1_1(
                data["ApplicationEncryptionConfigurationDescription"]
            )
        )
    return out
