"""Generated from Smithy shape ``com.amazonaws.kinesis#S3TablesDestinationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis.types.data_freshness_in_seconds
    import capo_kinesis.types.dead_letter_queue_s3_configuration
    import capo_kinesis.types.s3_tables_configuration_list


class S3TablesDestinationConfiguration(TypedDict, closed=True):
    data_freshness_in_seconds: NotRequired[
        "capo_kinesis.types.data_freshness_in_seconds.DataFreshnessInSeconds"
    ]
    """<p>The maximum age, in seconds, of undelivered data before the channel delivers it to the destination. The default value is 300 seconds.</p>"""
    dead_letter_queue_s3_configuration: "capo_kinesis.types.dead_letter_queue_s3_configuration.DeadLetterQueueS3Configuration"
    """<p>The dead-letter queue configuration for records that cannot be delivered. Required for streaming table destinations.</p>"""
    s3_tables_configuration_list: (
        "capo_kinesis.types.s3_tables_configuration_list.S3TablesConfigurationList"
    )
    """<p>The list of streaming table configurations. Currently, one table is supported per channel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3TablesDestinationConfiguration) -> dict:
    out: dict = {}
    if "data_freshness_in_seconds" in value:
        out["DataFreshnessInSeconds"] = value["data_freshness_in_seconds"]
    import capo_kinesis.types.dead_letter_queue_s3_configuration

    out["DeadLetterQueueS3Configuration"] = (
        capo_kinesis.types.dead_letter_queue_s3_configuration.serialize_aws_json_1_1(
            value["dead_letter_queue_s3_configuration"]
        )
    )
    import capo_kinesis.types.s3_tables_configuration_list

    out["S3TablesConfigurationList"] = (
        capo_kinesis.types.s3_tables_configuration_list.serialize_aws_json_1_1(
            value["s3_tables_configuration_list"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3TablesDestinationConfiguration:
    out: S3TablesDestinationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("DataFreshnessInSeconds") is not None:
        out["data_freshness_in_seconds"] = data["DataFreshnessInSeconds"]
    if data.get("DeadLetterQueueS3Configuration") is not None:
        import capo_kinesis.types.dead_letter_queue_s3_configuration

        out["dead_letter_queue_s3_configuration"] = (
            capo_kinesis.types.dead_letter_queue_s3_configuration.deserialize_aws_json_1_1(
                data["DeadLetterQueueS3Configuration"]
            )
        )
    else:
        raise DeserializationError(
            "S3TablesDestinationConfiguration.dead_letter_queue_s3_configuration required"
        )
    if data.get("S3TablesConfigurationList") is not None:
        import capo_kinesis.types.s3_tables_configuration_list

        out["s3_tables_configuration_list"] = (
            capo_kinesis.types.s3_tables_configuration_list.deserialize_aws_json_1_1(
                data["S3TablesConfigurationList"]
            )
        )
    else:
        out["s3_tables_configuration_list"] = []
    return out
