"""Generated from Smithy shape ``com.amazonaws.kinesis#UpdateChannelInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.channel_arn
    import capo_kinesis.types.channel_logging_update_input
    import capo_kinesis.types.s3_destination_update_input
    import capo_kinesis.types.s3_tables_destination_update_input


class UpdateChannelInput(TypedDict, closed=True):
    channel_arn: "capo_kinesis.types.channel_arn.ChannelARN"
    """<p>The Amazon Resource Name (ARN) of the channel to update.</p>"""
    s3_destination_configuration: NotRequired[
        "capo_kinesis.types.s3_destination_update_input.S3DestinationUpdateInput"
    ]
    """<p>The updated configuration for a general purpose Amazon S3 destination. Specify this parameter when the channel delivers to a general purpose Amazon S3 bucket. Only <code>DataFreshnessInSeconds</code> can be updated.</p>"""
    s3_tables_destination_configuration: NotRequired[
        "capo_kinesis.types.s3_tables_destination_update_input.S3TablesDestinationUpdateInput"
    ]
    """<p>The updated configuration for a streaming table destination. Specify this parameter when the channel delivers to streaming tables on Apache Iceberg in Amazon S3 Tables. Only <code>DataFreshnessInSeconds</code> can be updated.</p>"""
    logging_configuration: NotRequired[
        "capo_kinesis.types.channel_logging_update_input.ChannelLoggingUpdateInput"
    ]
    """<p>The updated Amazon CloudWatch Logs configuration for the channel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateChannelInput) -> dict:
    out: dict = {}
    out["ChannelARN"] = value["channel_arn"]
    if "s3_destination_configuration" in value:
        import capo_kinesis.types.s3_destination_update_input

        out["S3DestinationConfiguration"] = (
            capo_kinesis.types.s3_destination_update_input.serialize_aws_json_1_1(
                value["s3_destination_configuration"]
            )
        )
    if "s3_tables_destination_configuration" in value:
        import capo_kinesis.types.s3_tables_destination_update_input

        out["S3TablesDestinationConfiguration"] = (
            capo_kinesis.types.s3_tables_destination_update_input.serialize_aws_json_1_1(
                value["s3_tables_destination_configuration"]
            )
        )
    if "logging_configuration" in value:
        import capo_kinesis.types.channel_logging_update_input

        out["LoggingConfiguration"] = (
            capo_kinesis.types.channel_logging_update_input.serialize_aws_json_1_1(
                value["logging_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateChannelInput:
    out: UpdateChannelInput = {}  # type: ignore[typeddict-item]
    if data.get("ChannelARN") is not None:
        out["channel_arn"] = data["ChannelARN"]
    else:
        out["channel_arn"] = ""
    if data.get("S3DestinationConfiguration") is not None:
        import capo_kinesis.types.s3_destination_update_input

        out["s3_destination_configuration"] = (
            capo_kinesis.types.s3_destination_update_input.deserialize_aws_json_1_1(
                data["S3DestinationConfiguration"]
            )
        )
    if data.get("S3TablesDestinationConfiguration") is not None:
        import capo_kinesis.types.s3_tables_destination_update_input

        out["s3_tables_destination_configuration"] = (
            capo_kinesis.types.s3_tables_destination_update_input.deserialize_aws_json_1_1(
                data["S3TablesDestinationConfiguration"]
            )
        )
    if data.get("LoggingConfiguration") is not None:
        import capo_kinesis.types.channel_logging_update_input

        out["logging_configuration"] = (
            capo_kinesis.types.channel_logging_update_input.deserialize_aws_json_1_1(
                data["LoggingConfiguration"]
            )
        )
    return out
