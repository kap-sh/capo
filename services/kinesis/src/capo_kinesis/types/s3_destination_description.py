"""Generated from Smithy shape ``com.amazonaws.kinesis#S3DestinationDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis.types.data_freshness_in_seconds
    import capo_kinesis.types.dead_letter_queue_s3_configuration
    import capo_kinesis.types.s3_storage_configuration


class S3DestinationDescription(TypedDict, closed=True):
    data_freshness_in_seconds: (
        "capo_kinesis.types.data_freshness_in_seconds.DataFreshnessInSeconds"
    )
    """<p>The maximum age, in seconds, of undelivered data.</p>"""
    dead_letter_queue_s3_configuration: "capo_kinesis.types.dead_letter_queue_s3_configuration.DeadLetterQueueS3Configuration"
    """<p>The dead-letter queue configuration for records that cannot be delivered.</p>"""
    storage_configuration: (
        "capo_kinesis.types.s3_storage_configuration.S3StorageConfiguration"
    )
    """<p>The Amazon S3 storage configuration for the channel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3DestinationDescription) -> dict:
    out: dict = {}
    out["DataFreshnessInSeconds"] = value["data_freshness_in_seconds"]
    import capo_kinesis.types.dead_letter_queue_s3_configuration

    out["DeadLetterQueueS3Configuration"] = (
        capo_kinesis.types.dead_letter_queue_s3_configuration.serialize_aws_json_1_1(
            value["dead_letter_queue_s3_configuration"]
        )
    )
    import capo_kinesis.types.s3_storage_configuration

    out["StorageConfiguration"] = (
        capo_kinesis.types.s3_storage_configuration.serialize_aws_json_1_1(
            value["storage_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3DestinationDescription:
    out: S3DestinationDescription = {}  # type: ignore[typeddict-item]
    if data.get("DataFreshnessInSeconds") is not None:
        out["data_freshness_in_seconds"] = data["DataFreshnessInSeconds"]
    else:
        out["data_freshness_in_seconds"] = 0
    if data.get("DeadLetterQueueS3Configuration") is not None:
        import capo_kinesis.types.dead_letter_queue_s3_configuration

        out["dead_letter_queue_s3_configuration"] = (
            capo_kinesis.types.dead_letter_queue_s3_configuration.deserialize_aws_json_1_1(
                data["DeadLetterQueueS3Configuration"]
            )
        )
    else:
        raise DeserializationError(
            "S3DestinationDescription.dead_letter_queue_s3_configuration required"
        )
    if data.get("StorageConfiguration") is not None:
        import capo_kinesis.types.s3_storage_configuration

        out["storage_configuration"] = (
            capo_kinesis.types.s3_storage_configuration.deserialize_aws_json_1_1(
                data["StorageConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "S3DestinationDescription.storage_configuration required"
        )
    return out
