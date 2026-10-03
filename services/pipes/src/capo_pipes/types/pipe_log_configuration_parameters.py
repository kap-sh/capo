"""Generated from Smithy shape ``com.amazonaws.pipes#PipeLogConfigurationParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pipes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pipes.types.cloudwatch_logs_log_destination_parameters
    import capo_pipes.types.firehose_log_destination_parameters
    import capo_pipes.types.include_execution_data
    import capo_pipes.types.log_level
    import capo_pipes.types.s3_log_destination_parameters


class PipeLogConfigurationParameters(TypedDict, closed=True):
    s3_log_destination: NotRequired[
        "capo_pipes.types.s3_log_destination_parameters.S3LogDestinationParameters"
    ]
    """<p>The Amazon S3 logging configuration settings for the pipe.</p>"""
    firehose_log_destination: NotRequired[
        "capo_pipes.types.firehose_log_destination_parameters.FirehoseLogDestinationParameters"
    ]
    """<p>The Amazon Data Firehose logging configuration settings for the pipe.</p>"""
    cloudwatch_logs_log_destination: NotRequired[
        "capo_pipes.types.cloudwatch_logs_log_destination_parameters.CloudwatchLogsLogDestinationParameters"
    ]
    """<p>The Amazon CloudWatch Logs logging configuration settings for the pipe.</p>"""
    level: "capo_pipes.types.log_level.LogLevel"
    """<p>The level of logging detail to include. This applies to all log destinations for the pipe.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-logs.html#eb-pipes-logs-level">Specifying EventBridge Pipes log level</a> in the <i>Amazon EventBridge User Guide</i>.</p>"""
    include_execution_data: NotRequired[
        "capo_pipes.types.include_execution_data.IncludeExecutionData"
    ]
    """<p>Specify <code>ALL</code> to include the execution data (specifically, the <code>payload</code>, <code>awsRequest</code>, and <code>awsResponse</code> fields) in the log messages for this pipe.</p> <p>This applies to all log destinations for the pipe.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-logs.html#eb-pipes-logs-execution-data">Including execution data in logs</a> in the <i>Amazon EventBridge User Guide</i>.</p> <p>By default, execution data is not included.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipeLogConfigurationParameters) -> dict:
    out: dict = {}
    if "s3_log_destination" in value:
        import capo_pipes.types.s3_log_destination_parameters

        out["S3LogDestination"] = (
            capo_pipes.types.s3_log_destination_parameters.serialize_json(
                value["s3_log_destination"]
            )
        )
    if "firehose_log_destination" in value:
        import capo_pipes.types.firehose_log_destination_parameters

        out["FirehoseLogDestination"] = (
            capo_pipes.types.firehose_log_destination_parameters.serialize_json(
                value["firehose_log_destination"]
            )
        )
    if "cloudwatch_logs_log_destination" in value:
        import capo_pipes.types.cloudwatch_logs_log_destination_parameters

        out["CloudwatchLogsLogDestination"] = (
            capo_pipes.types.cloudwatch_logs_log_destination_parameters.serialize_json(
                value["cloudwatch_logs_log_destination"]
            )
        )
    out["Level"] = value["level"]
    if "include_execution_data" in value:
        import capo_pipes.types.include_execution_data

        out["IncludeExecutionData"] = (
            capo_pipes.types.include_execution_data.serialize_json(
                value["include_execution_data"]
            )
        )
    return out


def deserialize_json(data: dict) -> PipeLogConfigurationParameters:
    out: PipeLogConfigurationParameters = {}  # type: ignore[typeddict-item]
    if data.get("S3LogDestination") is not None:
        import capo_pipes.types.s3_log_destination_parameters

        out["s3_log_destination"] = (
            capo_pipes.types.s3_log_destination_parameters.deserialize_json(
                data["S3LogDestination"]
            )
        )
    if data.get("FirehoseLogDestination") is not None:
        import capo_pipes.types.firehose_log_destination_parameters

        out["firehose_log_destination"] = (
            capo_pipes.types.firehose_log_destination_parameters.deserialize_json(
                data["FirehoseLogDestination"]
            )
        )
    if data.get("CloudwatchLogsLogDestination") is not None:
        import capo_pipes.types.cloudwatch_logs_log_destination_parameters

        out["cloudwatch_logs_log_destination"] = (
            capo_pipes.types.cloudwatch_logs_log_destination_parameters.deserialize_json(
                data["CloudwatchLogsLogDestination"]
            )
        )
    if data.get("Level") is not None:
        out["level"] = data["Level"]
    else:
        raise DeserializationError("PipeLogConfigurationParameters.level required")
    if data.get("IncludeExecutionData") is not None:
        import capo_pipes.types.include_execution_data

        out["include_execution_data"] = (
            capo_pipes.types.include_execution_data.deserialize_json(
                data["IncludeExecutionData"]
            )
        )
    return out
