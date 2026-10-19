"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#InputUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.id
    import capo_kinesis_analytics_v2.types.in_app_stream_name
    import capo_kinesis_analytics_v2.types.input_parallelism_update
    import capo_kinesis_analytics_v2.types.input_processing_configuration_update
    import capo_kinesis_analytics_v2.types.input_schema_update
    import capo_kinesis_analytics_v2.types.kinesis_firehose_input_update
    import capo_kinesis_analytics_v2.types.kinesis_streams_input_update


class InputUpdate(TypedDict, closed=True):
    input_id: "capo_kinesis_analytics_v2.types.id.Id"
    """<p>The input ID of the application input to be updated.</p>"""
    name_prefix_update: NotRequired[
        "capo_kinesis_analytics_v2.types.in_app_stream_name.InAppStreamName"
    ]
    """<p>The name prefix for in-application streams that Kinesis Data Analytics creates for the specific streaming source.</p>"""
    input_processing_configuration_update: NotRequired[
        "capo_kinesis_analytics_v2.types.input_processing_configuration_update.InputProcessingConfigurationUpdate"
    ]
    """<p>Describes updates to an <a>InputProcessingConfiguration</a>.</p>"""
    kinesis_streams_input_update: NotRequired[
        "capo_kinesis_analytics_v2.types.kinesis_streams_input_update.KinesisStreamsInputUpdate"
    ]
    """<p>If a Kinesis data stream is the streaming source to be updated, provides an updated stream Amazon Resource Name (ARN).</p>"""
    kinesis_firehose_input_update: NotRequired[
        "capo_kinesis_analytics_v2.types.kinesis_firehose_input_update.KinesisFirehoseInputUpdate"
    ]
    """<p>If a Kinesis Data Firehose delivery stream is the streaming source to be updated, provides an updated stream ARN.</p>"""
    input_schema_update: NotRequired[
        "capo_kinesis_analytics_v2.types.input_schema_update.InputSchemaUpdate"
    ]
    """<p>Describes the data format on the streaming source, and how record elements on the streaming source map to columns of the in-application stream that is created.</p>"""
    input_parallelism_update: NotRequired[
        "capo_kinesis_analytics_v2.types.input_parallelism_update.InputParallelismUpdate"
    ]
    """<p>Describes the parallelism updates (the number of in-application streams Kinesis Data Analytics creates for the specific streaming source).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputUpdate) -> dict:
    out: dict = {}
    out["InputId"] = value["input_id"]
    if "name_prefix_update" in value:
        out["NamePrefixUpdate"] = value["name_prefix_update"]
    if "input_processing_configuration_update" in value:
        import capo_kinesis_analytics_v2.types.input_processing_configuration_update

        out["InputProcessingConfigurationUpdate"] = (
            capo_kinesis_analytics_v2.types.input_processing_configuration_update.serialize_aws_json_1_1(
                value["input_processing_configuration_update"]
            )
        )
    if "kinesis_streams_input_update" in value:
        import capo_kinesis_analytics_v2.types.kinesis_streams_input_update

        out["KinesisStreamsInputUpdate"] = (
            capo_kinesis_analytics_v2.types.kinesis_streams_input_update.serialize_aws_json_1_1(
                value["kinesis_streams_input_update"]
            )
        )
    if "kinesis_firehose_input_update" in value:
        import capo_kinesis_analytics_v2.types.kinesis_firehose_input_update

        out["KinesisFirehoseInputUpdate"] = (
            capo_kinesis_analytics_v2.types.kinesis_firehose_input_update.serialize_aws_json_1_1(
                value["kinesis_firehose_input_update"]
            )
        )
    if "input_schema_update" in value:
        import capo_kinesis_analytics_v2.types.input_schema_update

        out["InputSchemaUpdate"] = (
            capo_kinesis_analytics_v2.types.input_schema_update.serialize_aws_json_1_1(
                value["input_schema_update"]
            )
        )
    if "input_parallelism_update" in value:
        import capo_kinesis_analytics_v2.types.input_parallelism_update

        out["InputParallelismUpdate"] = (
            capo_kinesis_analytics_v2.types.input_parallelism_update.serialize_aws_json_1_1(
                value["input_parallelism_update"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InputUpdate:
    out: InputUpdate = {}  # type: ignore[typeddict-item]
    if data.get("InputId") is not None:
        out["input_id"] = data["InputId"]
    else:
        out["input_id"] = ""
    if data.get("NamePrefixUpdate") is not None:
        out["name_prefix_update"] = data["NamePrefixUpdate"]
    if data.get("InputProcessingConfigurationUpdate") is not None:
        import capo_kinesis_analytics_v2.types.input_processing_configuration_update

        out["input_processing_configuration_update"] = (
            capo_kinesis_analytics_v2.types.input_processing_configuration_update.deserialize_aws_json_1_1(
                data["InputProcessingConfigurationUpdate"]
            )
        )
    if data.get("KinesisStreamsInputUpdate") is not None:
        import capo_kinesis_analytics_v2.types.kinesis_streams_input_update

        out["kinesis_streams_input_update"] = (
            capo_kinesis_analytics_v2.types.kinesis_streams_input_update.deserialize_aws_json_1_1(
                data["KinesisStreamsInputUpdate"]
            )
        )
    if data.get("KinesisFirehoseInputUpdate") is not None:
        import capo_kinesis_analytics_v2.types.kinesis_firehose_input_update

        out["kinesis_firehose_input_update"] = (
            capo_kinesis_analytics_v2.types.kinesis_firehose_input_update.deserialize_aws_json_1_1(
                data["KinesisFirehoseInputUpdate"]
            )
        )
    if data.get("InputSchemaUpdate") is not None:
        import capo_kinesis_analytics_v2.types.input_schema_update

        out["input_schema_update"] = (
            capo_kinesis_analytics_v2.types.input_schema_update.deserialize_aws_json_1_1(
                data["InputSchemaUpdate"]
            )
        )
    if data.get("InputParallelismUpdate") is not None:
        import capo_kinesis_analytics_v2.types.input_parallelism_update

        out["input_parallelism_update"] = (
            capo_kinesis_analytics_v2.types.input_parallelism_update.deserialize_aws_json_1_1(
                data["InputParallelismUpdate"]
            )
        )
    return out
