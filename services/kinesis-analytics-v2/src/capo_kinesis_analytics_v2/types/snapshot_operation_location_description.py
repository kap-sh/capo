"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#SnapshotOperationLocationDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.snapshot_operation_s3_prefix_location
    import capo_kinesis_analytics_v2.types.storage_location_type


class SnapshotOperationLocationDescription(TypedDict, closed=True):
    location_type: (
        "capo_kinesis_analytics_v2.types.storage_location_type.StorageLocationType"
    )
    """<p>The type of the location. The only supported value is <code>S3</code>.</p>"""
    s3_prefix_location: "capo_kinesis_analytics_v2.types.snapshot_operation_s3_prefix_location.SnapshotOperationS3PrefixLocation"
    """<p>Describes the Amazon S3 bucket and key prefix of the location.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotOperationLocationDescription) -> dict:
    out: dict = {}
    import capo_kinesis_analytics_v2.types.storage_location_type

    out["LocationType"] = (
        capo_kinesis_analytics_v2.types.storage_location_type.serialize_aws_json_1_1(
            value["location_type"]
        )
    )
    import capo_kinesis_analytics_v2.types.snapshot_operation_s3_prefix_location

    out["S3PrefixLocation"] = (
        capo_kinesis_analytics_v2.types.snapshot_operation_s3_prefix_location.serialize_aws_json_1_1(
            value["s3_prefix_location"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SnapshotOperationLocationDescription:
    out: SnapshotOperationLocationDescription = {}  # type: ignore[typeddict-item]
    if data.get("LocationType") is not None:
        import capo_kinesis_analytics_v2.types.storage_location_type

        out["location_type"] = (
            capo_kinesis_analytics_v2.types.storage_location_type.deserialize_aws_json_1_1(
                data["LocationType"]
            )
        )
    else:
        import typing

        out["location_type"] = typing.cast(
            "capo_kinesis_analytics_v2.types.storage_location_type.StorageLocationType",
            "",
        )
    if data.get("S3PrefixLocation") is not None:
        import capo_kinesis_analytics_v2.types.snapshot_operation_s3_prefix_location

        out["s3_prefix_location"] = (
            capo_kinesis_analytics_v2.types.snapshot_operation_s3_prefix_location.deserialize_aws_json_1_1(
                data["S3PrefixLocation"]
            )
        )
    else:
        raise DeserializationError(
            "SnapshotOperationLocationDescription.s3_prefix_location required"
        )
    return out
