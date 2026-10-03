"""Generated from Smithy shape ``com.amazonaws.sfn#StartSyncExecutionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sfn.types.arn
    import capo_sfn.types.included_data
    import capo_sfn.types.name
    import capo_sfn.types.sensitive_data
    import capo_sfn.types.trace_header


class StartSyncExecutionInput(TypedDict, closed=True):
    state_machine_arn: "capo_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the state machine to execute.</p>"""
    name: NotRequired["capo_sfn.types.name.Name"]
    """<p>The name of the execution.</p>"""
    input: NotRequired["capo_sfn.types.sensitive_data.SensitiveData"]
    r"""<p>The string that contains the JSON input data for the execution, for example:</p> <p> <code>"{\"first_name\" : \"Alejandro\"}"</code> </p> <note> <p>If you don't include any JSON input data, you still must include the two braces, for example: <code>"{}"</code> </p> </note> <p>Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.</p>"""
    trace_header: NotRequired["capo_sfn.types.trace_header.TraceHeader"]
    """<p>Passes the X-Ray trace header. The trace header can also be passed in the request payload.</p> <note> <p> For X-Ray traces, all Amazon Web Services services use the <code>X-Amzn-Trace-Id</code> header from the HTTP request. Using the header is the preferred mechanism to identify a trace. <code>StartExecution</code> and <code>StartSyncExecution</code> API operations can also use <code>traceHeader</code> from the body of the request payload. If <b>both</b> sources are provided, Step Functions will use the <b>header value</b> (preferred) over the value in the request body. </p> </note>"""
    included_data: NotRequired["capo_sfn.types.included_data.IncludedData"]
    """<p>If your state machine definition is encrypted with a KMS key, callers must have <code>kms:Decrypt</code> permission to decrypt the definition. Alternatively, you can call the API with <code>includedData = METADATA_ONLY</code> to get a successful response without the encrypted definition.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartSyncExecutionInput) -> dict:
    out: dict = {}
    out["stateMachineArn"] = value["state_machine_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "input" in value:
        out["input"] = value["input"]
    if "trace_header" in value:
        out["traceHeader"] = value["trace_header"]
    if "included_data" in value:
        import capo_sfn.types.included_data

        out["includedData"] = capo_sfn.types.included_data.serialize_aws_json_1_0(
            value["included_data"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StartSyncExecutionInput:
    out: StartSyncExecutionInput = {}  # type: ignore[typeddict-item]
    if data.get("stateMachineArn") is not None:
        out["state_machine_arn"] = data["stateMachineArn"]
    else:
        raise DeserializationError("StartSyncExecutionInput.state_machine_arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("input") is not None:
        out["input"] = data["input"]
    if data.get("traceHeader") is not None:
        out["trace_header"] = data["traceHeader"]
    if data.get("includedData") is not None:
        import capo_sfn.types.included_data

        out["included_data"] = capo_sfn.types.included_data.deserialize_aws_json_1_0(
            data["includedData"]
        )
    return out
