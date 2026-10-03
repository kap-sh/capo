"""Generated from Smithy shape ``com.amazonaws.sfn#DescribeExecutionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sfn.types.arn
    import capo_sfn.types.cloud_watch_events_execution_data_details
    import capo_sfn.types.execution_redrive_status
    import capo_sfn.types.execution_status
    import capo_sfn.types.long_arn
    import capo_sfn.types.name
    import capo_sfn.types.redrive_count
    import capo_sfn.types.sensitive_cause
    import capo_sfn.types.sensitive_data
    import capo_sfn.types.sensitive_error
    import capo_sfn.types.timestamp
    import capo_sfn.types.trace_header


class DescribeExecutionOutput(TypedDict, closed=True):
    execution_arn: "capo_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that identifies the execution.</p>"""
    state_machine_arn: "capo_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the executed stated machine.</p>"""
    name: NotRequired["capo_sfn.types.name.Name"]
    r"""<p>The name of the execution.</p> <p>A name must <i>not</i> contain:</p> <ul> <li> <p>white space</p> </li> <li> <p>brackets <code>< > { } [ ]</code> </p> </li> <li> <p>wildcard characters <code>? *</code> </p> </li> <li> <p>special characters <code>" # % \ ^ | ~ ` $ & , ; : /</code> </p> </li> <li> <p>control characters (<code>U+0000-001F</code>, <code>U+007F-009F</code>, <code>U+FFFE-FFFF</code>)</p> </li> <li> <p>surrogates (<code>U+D800-DFFF</code>)</p> </li> <li> <p>invalid characters (<code> U+10FFFF</code>)</p> </li> </ul> <p>To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _.</p>"""
    status: "capo_sfn.types.execution_status.ExecutionStatus"
    """<p>The current status of the execution.</p>"""
    start_date: "capo_sfn.types.timestamp.Timestamp"
    """<p>The date the execution is started.</p>"""
    stop_date: NotRequired["capo_sfn.types.timestamp.Timestamp"]
    """<p>If the execution ended, the date the execution stopped.</p>"""
    input: NotRequired["capo_sfn.types.sensitive_data.SensitiveData"]
    """<p>The string that contains the JSON input data of the execution. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.</p>"""
    input_details: NotRequired[
        "capo_sfn.types.cloud_watch_events_execution_data_details.CloudWatchEventsExecutionDataDetails"
    ]
    output: NotRequired["capo_sfn.types.sensitive_data.SensitiveData"]
    """<p>The JSON output data of the execution. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.</p> <note> <p>This field is set only if the execution succeeds. If the execution fails, this field is null.</p> </note>"""
    output_details: NotRequired[
        "capo_sfn.types.cloud_watch_events_execution_data_details.CloudWatchEventsExecutionDataDetails"
    ]
    trace_header: NotRequired["capo_sfn.types.trace_header.TraceHeader"]
    """<p>The X-Ray trace header that was passed to the execution.</p> <note> <p> For X-Ray traces, all Amazon Web Services services use the <code>X-Amzn-Trace-Id</code> header from the HTTP request. Using the header is the preferred mechanism to identify a trace. <code>StartExecution</code> and <code>StartSyncExecution</code> API operations can also use <code>traceHeader</code> from the body of the request payload. If <b>both</b> sources are provided, Step Functions will use the <b>header value</b> (preferred) over the value in the request body. </p> </note>"""
    map_run_arn: NotRequired["capo_sfn.types.long_arn.LongArn"]
    """<p>The Amazon Resource Name (ARN) that identifies a Map Run, which dispatched this execution.</p>"""
    error: NotRequired["capo_sfn.types.sensitive_error.SensitiveError"]
    """<p>The error string if the state machine execution failed.</p>"""
    cause: NotRequired["capo_sfn.types.sensitive_cause.SensitiveCause"]
    """<p>The cause string if the state machine execution failed.</p>"""
    state_machine_version_arn: NotRequired["capo_sfn.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the state machine version associated with the execution. The version ARN is a combination of state machine ARN and the version number separated by a colon (:). For example, <code>stateMachineARN:1</code>.</p> <p>If you start an execution from a <code>StartExecution</code> request without specifying a state machine version or alias ARN, Step Functions returns a null value.</p>"""
    state_machine_alias_arn: NotRequired["capo_sfn.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the state machine alias associated with the execution. The alias ARN is a combination of state machine ARN and the alias name separated by a colon (:). For example, <code>stateMachineARN:PROD</code>.</p> <p>If you start an execution from a <code>StartExecution</code> request with a state machine version ARN, this field will be null.</p>"""
    redrive_count: NotRequired["capo_sfn.types.redrive_count.RedriveCount"]
    """<p>The number of times you've redriven an execution. If you have not yet redriven an execution, the <code>redriveCount</code> is 0. This count is only updated if you successfully redrive an execution.</p>"""
    redrive_date: NotRequired["capo_sfn.types.timestamp.Timestamp"]
    """<p>The date the execution was last redriven. If you have not yet redriven an execution, the <code>redriveDate</code> is null.</p> <p>The <code>redriveDate</code> is unavailable if you redrive a Map Run that starts child workflow executions of type <code>EXPRESS</code>.</p>"""
    redrive_status: NotRequired[
        "capo_sfn.types.execution_redrive_status.ExecutionRedriveStatus"
    ]
    """<p>Indicates whether or not an execution can be redriven at a given point in time.</p> <ul> <li> <p>For executions of type <code>STANDARD</code>, <code>redriveStatus</code> is <code>NOT_REDRIVABLE</code> if calling the <a>RedriveExecution</a> API action would return the <code>ExecutionNotRedrivable</code> error.</p> </li> <li> <p>For a Distributed Map that includes child workflows of type <code>STANDARD</code>, <code>redriveStatus</code> indicates whether or not the Map Run can redrive child workflow executions.</p> </li> <li> <p>For a Distributed Map that includes child workflows of type <code>EXPRESS</code>, <code>redriveStatus</code> indicates whether or not the Map Run can redrive child workflow executions.</p> <p>You can redrive failed or timed out <code>EXPRESS</code> workflows <i>only if</i> they're a part of a Map Run. When you <a href="https://docs.aws.amazon.com/step-functions/latest/dg/redrive-map-run.html">redrive</a> the Map Run, these workflows are restarted using the <a>StartExecution</a> API action.</p> </li> </ul>"""
    redrive_status_reason: NotRequired["capo_sfn.types.sensitive_data.SensitiveData"]
    """<p>When <code>redriveStatus</code> is <code>NOT_REDRIVABLE</code>, <code>redriveStatusReason</code> specifies the reason why an execution cannot be redriven.</p> <ul> <li> <p>For executions of type <code>STANDARD</code>, or for a Distributed Map that includes child workflows of type <code>STANDARD</code>, <code>redriveStatusReason</code> can include one of the following reasons:</p> <ul> <li> <p> <code>State machine is in DELETING status</code>.</p> </li> <li> <p> <code>Execution is RUNNING and cannot be redriven</code>.</p> </li> <li> <p> <code>Execution is SUCCEEDED and cannot be redriven</code>.</p> </li> <li> <p> <code>Execution was started before the launch of RedriveExecution</code>.</p> </li> <li> <p> <code>Execution history event limit exceeded</code>.</p> </li> <li> <p> <code>Execution has exceeded the max execution time</code>.</p> </li> <li> <p> <code>Execution redrivable period exceeded</code>.</p> </li> </ul> </li> <li> <p>For a Distributed Map that includes child workflows of type <code>EXPRESS</code>, <code>redriveStatusReason</code> is only returned if the child workflows are not redrivable. This happens when the child workflow executions have completed successfully.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeExecutionOutput) -> dict:
    out: dict = {}
    out["executionArn"] = value["execution_arn"]
    out["stateMachineArn"] = value["state_machine_arn"]
    if "name" in value:
        out["name"] = value["name"]
    import capo_sfn.types.execution_status

    out["status"] = capo_sfn.types.execution_status.serialize_aws_json_1_0(
        value["status"]
    )
    import capo_sfn.types.timestamp

    out["startDate"] = capo_sfn.types.timestamp.serialize_aws_json_1_0(
        value["start_date"]
    )
    if "stop_date" in value:
        import capo_sfn.types.timestamp

        out["stopDate"] = capo_sfn.types.timestamp.serialize_aws_json_1_0(
            value["stop_date"]
        )
    if "input" in value:
        out["input"] = value["input"]
    if "input_details" in value:
        import capo_sfn.types.cloud_watch_events_execution_data_details

        out["inputDetails"] = (
            capo_sfn.types.cloud_watch_events_execution_data_details.serialize_aws_json_1_0(
                value["input_details"]
            )
        )
    if "output" in value:
        out["output"] = value["output"]
    if "output_details" in value:
        import capo_sfn.types.cloud_watch_events_execution_data_details

        out["outputDetails"] = (
            capo_sfn.types.cloud_watch_events_execution_data_details.serialize_aws_json_1_0(
                value["output_details"]
            )
        )
    if "trace_header" in value:
        out["traceHeader"] = value["trace_header"]
    if "map_run_arn" in value:
        out["mapRunArn"] = value["map_run_arn"]
    if "error" in value:
        out["error"] = value["error"]
    if "cause" in value:
        out["cause"] = value["cause"]
    if "state_machine_version_arn" in value:
        out["stateMachineVersionArn"] = value["state_machine_version_arn"]
    if "state_machine_alias_arn" in value:
        out["stateMachineAliasArn"] = value["state_machine_alias_arn"]
    if "redrive_count" in value:
        out["redriveCount"] = value["redrive_count"]
    if "redrive_date" in value:
        import capo_sfn.types.timestamp

        out["redriveDate"] = capo_sfn.types.timestamp.serialize_aws_json_1_0(
            value["redrive_date"]
        )
    if "redrive_status" in value:
        import capo_sfn.types.execution_redrive_status

        out["redriveStatus"] = (
            capo_sfn.types.execution_redrive_status.serialize_aws_json_1_0(
                value["redrive_status"]
            )
        )
    if "redrive_status_reason" in value:
        out["redriveStatusReason"] = value["redrive_status_reason"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeExecutionOutput:
    out: DescribeExecutionOutput = {}  # type: ignore[typeddict-item]
    if data.get("executionArn") is not None:
        out["execution_arn"] = data["executionArn"]
    else:
        raise DeserializationError("DescribeExecutionOutput.execution_arn required")
    if data.get("stateMachineArn") is not None:
        out["state_machine_arn"] = data["stateMachineArn"]
    else:
        raise DeserializationError("DescribeExecutionOutput.state_machine_arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("status") is not None:
        import capo_sfn.types.execution_status

        out["status"] = capo_sfn.types.execution_status.deserialize_aws_json_1_0(
            data["status"]
        )
    else:
        raise DeserializationError("DescribeExecutionOutput.status required")
    if data.get("startDate") is not None:
        import capo_sfn.types.timestamp

        out["start_date"] = capo_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["startDate"]
        )
    else:
        raise DeserializationError("DescribeExecutionOutput.start_date required")
    if data.get("stopDate") is not None:
        import capo_sfn.types.timestamp

        out["stop_date"] = capo_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["stopDate"]
        )
    if data.get("input") is not None:
        out["input"] = data["input"]
    if data.get("inputDetails") is not None:
        import capo_sfn.types.cloud_watch_events_execution_data_details

        out["input_details"] = (
            capo_sfn.types.cloud_watch_events_execution_data_details.deserialize_aws_json_1_0(
                data["inputDetails"]
            )
        )
    if data.get("output") is not None:
        out["output"] = data["output"]
    if data.get("outputDetails") is not None:
        import capo_sfn.types.cloud_watch_events_execution_data_details

        out["output_details"] = (
            capo_sfn.types.cloud_watch_events_execution_data_details.deserialize_aws_json_1_0(
                data["outputDetails"]
            )
        )
    if data.get("traceHeader") is not None:
        out["trace_header"] = data["traceHeader"]
    if data.get("mapRunArn") is not None:
        out["map_run_arn"] = data["mapRunArn"]
    if data.get("error") is not None:
        out["error"] = data["error"]
    if data.get("cause") is not None:
        out["cause"] = data["cause"]
    if data.get("stateMachineVersionArn") is not None:
        out["state_machine_version_arn"] = data["stateMachineVersionArn"]
    if data.get("stateMachineAliasArn") is not None:
        out["state_machine_alias_arn"] = data["stateMachineAliasArn"]
    if data.get("redriveCount") is not None:
        out["redrive_count"] = data["redriveCount"]
    if data.get("redriveDate") is not None:
        import capo_sfn.types.timestamp

        out["redrive_date"] = capo_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["redriveDate"]
        )
    if data.get("redriveStatus") is not None:
        import capo_sfn.types.execution_redrive_status

        out["redrive_status"] = (
            capo_sfn.types.execution_redrive_status.deserialize_aws_json_1_0(
                data["redriveStatus"]
            )
        )
    if data.get("redriveStatusReason") is not None:
        out["redrive_status_reason"] = data["redriveStatusReason"]
    return out
