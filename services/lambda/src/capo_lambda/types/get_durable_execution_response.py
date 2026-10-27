"""Generated from Smithy shape ``com.amazonaws.lambda#GetDurableExecutionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.durable_config
    import capo_lambda.types.durable_execution_arn
    import capo_lambda.types.durable_execution_name
    import capo_lambda.types.error_object
    import capo_lambda.types.execution_data_included
    import capo_lambda.types.execution_status
    import capo_lambda.types.execution_timestamp
    import capo_lambda.types.input_payload
    import capo_lambda.types.name_spaced_function_arn
    import capo_lambda.types.output_payload
    import capo_lambda.types.trace_header
    import capo_lambda.types.version_with_latest_published


class GetDurableExecutionResponse(TypedDict, closed=True):
    durable_execution_arn: "capo_lambda.types.durable_execution_arn.DurableExecutionArn"
    """<p>The Amazon Resource Name (ARN) of the durable execution.</p>"""
    durable_execution_name: (
        "capo_lambda.types.durable_execution_name.DurableExecutionName"
    )
    """<p>The name of the durable execution. This is either the name you provided when invoking the function, or a system-generated unique identifier if no name was provided.</p>"""
    function_arn: "capo_lambda.types.name_spaced_function_arn.NameSpacedFunctionArn"
    """<p>The Amazon Resource Name (ARN) of the Lambda function that was invoked to start this durable execution.</p>"""
    input_payload: NotRequired["capo_lambda.types.input_payload.InputPayload"]
    """<p>The JSON input payload that you provided when you started the durable execution. Asynchronous invocations support up to 1 MB, and synchronous invocations support up to 6 MB.</p>"""
    result: NotRequired["capo_lambda.types.output_payload.OutputPayload"]
    """<p>The JSON result returned by the durable execution if it completed successfully. This field is only present when the execution status is <code>SUCCEEDED</code>. Asynchronous invocations support up to 1 MB, and synchronous invocations support up to 6 MB.</p>"""
    error: NotRequired["capo_lambda.types.error_object.ErrorObject"]
    """<p>Error information if the durable execution failed. This field is only present when the execution status is <code>FAILED</code>, <code>TIMED_OUT</code>, or <code>STOPPED</code>. The combined size of all error fields is limited to 1 MB.</p>"""
    start_timestamp: "capo_lambda.types.execution_timestamp.ExecutionTimestamp"
    """<p>The date and time when the durable execution started, in Unix timestamp format.</p>"""
    status: "capo_lambda.types.execution_status.ExecutionStatus"
    """<p>The current status of the durable execution. Valid values are <code>RUNNING</code>, <code>SUCCEEDED</code>, <code>FAILED</code>, <code>TIMED_OUT</code>, and <code>STOPPED</code>.</p>"""
    end_timestamp: NotRequired[
        "capo_lambda.types.execution_timestamp.ExecutionTimestamp"
    ]
    """<p>The date and time when the durable execution ended, in Unix timestamp format. This field is only present if the execution has completed (status is <code>SUCCEEDED</code>, <code>FAILED</code>, <code>TIMED_OUT</code>, or <code>STOPPED</code>).</p>"""
    version: NotRequired[
        "capo_lambda.types.version_with_latest_published.VersionWithLatestPublished"
    ]
    """<p>The version of the Lambda function that was invoked for this durable execution. This ensures that all replays during the execution use the same function version.</p>"""
    trace_header: NotRequired["capo_lambda.types.trace_header.TraceHeader"]
    """<p>The trace headers associated with the durable execution.</p>"""
    execution_data_included: NotRequired[
        "capo_lambda.types.execution_data_included.ExecutionDataIncluded"
    ]
    """<p>Indicates whether execution data is included in this response. Returns <code>false</code> when <code>IncludeExecutionData</code> is set to <code>false</code> in the request.</p>"""
    durable_config: NotRequired["capo_lambda.types.durable_config.DurableConfig"]
    """<p>Configuration settings for the durable execution, including execution timeout, retention period for execution history, and an optional ARN of the Key Management Service (KMS) customer managed key that is used to encrypt your durable execution's payload data, including input, output, and error payloads.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDurableExecutionResponse) -> dict:
    out: dict = {}
    out["DurableExecutionArn"] = value["durable_execution_arn"]
    out["DurableExecutionName"] = value["durable_execution_name"]
    out["FunctionArn"] = value["function_arn"]
    if "input_payload" in value:
        out["InputPayload"] = value["input_payload"]
    if "result" in value:
        out["Result"] = value["result"]
    if "error" in value:
        import capo_lambda.types.error_object

        out["Error"] = capo_lambda.types.error_object.serialize_json(value["error"])
    import capo_lambda.types.execution_timestamp

    out["StartTimestamp"] = capo_lambda.types.execution_timestamp.serialize_json(
        value["start_timestamp"]
    )
    import capo_lambda.types.execution_status

    out["Status"] = capo_lambda.types.execution_status.serialize_json(value["status"])
    if "end_timestamp" in value:
        import capo_lambda.types.execution_timestamp

        out["EndTimestamp"] = capo_lambda.types.execution_timestamp.serialize_json(
            value["end_timestamp"]
        )
    if "version" in value:
        out["Version"] = value["version"]
    if "trace_header" in value:
        import capo_lambda.types.trace_header

        out["TraceHeader"] = capo_lambda.types.trace_header.serialize_json(
            value["trace_header"]
        )
    if "execution_data_included" in value:
        out["ExecutionDataIncluded"] = value["execution_data_included"]
    if "durable_config" in value:
        import capo_lambda.types.durable_config

        out["DurableConfig"] = capo_lambda.types.durable_config.serialize_json(
            value["durable_config"]
        )
    return out


def deserialize_json(data: dict) -> GetDurableExecutionResponse:
    out: GetDurableExecutionResponse = {}  # type: ignore[typeddict-item]
    if data.get("DurableExecutionArn") is not None:
        out["durable_execution_arn"] = data["DurableExecutionArn"]
    else:
        out["durable_execution_arn"] = ""
    if data.get("DurableExecutionName") is not None:
        out["durable_execution_name"] = data["DurableExecutionName"]
    else:
        out["durable_execution_name"] = ""
    if data.get("FunctionArn") is not None:
        out["function_arn"] = data["FunctionArn"]
    else:
        out["function_arn"] = ""
    if data.get("InputPayload") is not None:
        out["input_payload"] = data["InputPayload"]
    if data.get("Result") is not None:
        out["result"] = data["Result"]
    if data.get("Error") is not None:
        import capo_lambda.types.error_object

        out["error"] = capo_lambda.types.error_object.deserialize_json(data["Error"])
    if data.get("StartTimestamp") is not None:
        import capo_lambda.types.execution_timestamp

        out["start_timestamp"] = capo_lambda.types.execution_timestamp.deserialize_json(
            data["StartTimestamp"]
        )
    else:
        import datetime

        out["start_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("Status") is not None:
        import capo_lambda.types.execution_status

        out["status"] = capo_lambda.types.execution_status.deserialize_json(
            data["Status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_lambda.types.execution_status.ExecutionStatus", ""
        )
    if data.get("EndTimestamp") is not None:
        import capo_lambda.types.execution_timestamp

        out["end_timestamp"] = capo_lambda.types.execution_timestamp.deserialize_json(
            data["EndTimestamp"]
        )
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    if data.get("TraceHeader") is not None:
        import capo_lambda.types.trace_header

        out["trace_header"] = capo_lambda.types.trace_header.deserialize_json(
            data["TraceHeader"]
        )
    if data.get("ExecutionDataIncluded") is not None:
        out["execution_data_included"] = data["ExecutionDataIncluded"]
    if data.get("DurableConfig") is not None:
        import capo_lambda.types.durable_config

        out["durable_config"] = capo_lambda.types.durable_config.deserialize_json(
            data["DurableConfig"]
        )
    return out


def redact_sensitive(value: GetDurableExecutionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "input_payload" in value:
        out["input_payload"] = "*** Sensitive Data Redacted ***"
    if "result" in value:
        out["result"] = "*** Sensitive Data Redacted ***"
    if "error" in value:
        import capo_lambda.types.error_object

        out["error"] = capo_lambda.types.error_object.redact_sensitive(value["error"])
    return out
