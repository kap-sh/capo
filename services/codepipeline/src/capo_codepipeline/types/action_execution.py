"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionExecution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.action_execution_id
    import capo_codepipeline.types.action_execution_status
    import capo_codepipeline.types.action_execution_token
    import capo_codepipeline.types.error_details
    import capo_codepipeline.types.execution_id
    import capo_codepipeline.types.execution_summary
    import capo_codepipeline.types.last_updated_by
    import capo_codepipeline.types.log_stream_arn
    import capo_codepipeline.types.percentage
    import capo_codepipeline.types.timestamp
    import capo_codepipeline.types.url


class ActionExecution(TypedDict, closed=True):
    action_execution_id: NotRequired[
        "capo_codepipeline.types.action_execution_id.ActionExecutionId"
    ]
    """<p>ID of the workflow action execution in the current stage. Use the <a>GetPipelineState</a> action to retrieve the current action execution details of the current stage.</p> <note> <p>For older executions, this field might be empty. The action execution ID is available for executions run on or after March 2020.</p> </note>"""
    status: NotRequired[
        "capo_codepipeline.types.action_execution_status.ActionExecutionStatus"
    ]
    """<p>The status of the action, or for a completed action, the last status of the action.</p>"""
    summary: NotRequired["capo_codepipeline.types.execution_summary.ExecutionSummary"]
    """<p>A summary of the run of the action.</p>"""
    last_status_change: NotRequired["capo_codepipeline.types.timestamp.Timestamp"]
    """<p>The last status change of the action.</p>"""
    token: NotRequired[
        "capo_codepipeline.types.action_execution_token.ActionExecutionToken"
    ]
    """<p>The system-generated token used to identify a unique approval request. The token for each open approval request can be obtained using the <code>GetPipelineState</code> command. It is used to validate that the approval request corresponding to this token is still valid.</p>"""
    last_updated_by: NotRequired[
        "capo_codepipeline.types.last_updated_by.LastUpdatedBy"
    ]
    """<p>The ARN of the user who last changed the pipeline.</p>"""
    external_execution_id: NotRequired[
        "capo_codepipeline.types.execution_id.ExecutionId"
    ]
    """<p>The external ID of the run of the action.</p>"""
    external_execution_url: NotRequired["capo_codepipeline.types.url.Url"]
    """<p>The URL of a resource external to Amazon Web Services that is used when running the action (for example, an external repository URL).</p>"""
    percent_complete: NotRequired["capo_codepipeline.types.percentage.Percentage"]
    """<p>A percentage of completeness of the action as it runs.</p>"""
    error_details: NotRequired["capo_codepipeline.types.error_details.ErrorDetails"]
    """<p>The details of an error returned by a URL external to Amazon Web Services.</p>"""
    log_stream_arn: NotRequired["capo_codepipeline.types.log_stream_arn.LogStreamARN"]
    """<p>The Amazon Resource Name (ARN) of the log stream for the action compute.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionExecution) -> dict:
    out: dict = {}
    if "action_execution_id" in value:
        out["actionExecutionId"] = value["action_execution_id"]
    if "status" in value:
        import capo_codepipeline.types.action_execution_status

        out["status"] = (
            capo_codepipeline.types.action_execution_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "summary" in value:
        out["summary"] = value["summary"]
    if "last_status_change" in value:
        import capo_codepipeline.types.timestamp

        out["lastStatusChange"] = (
            capo_codepipeline.types.timestamp.serialize_aws_json_1_1(
                value["last_status_change"]
            )
        )
    if "token" in value:
        out["token"] = value["token"]
    if "last_updated_by" in value:
        out["lastUpdatedBy"] = value["last_updated_by"]
    if "external_execution_id" in value:
        out["externalExecutionId"] = value["external_execution_id"]
    if "external_execution_url" in value:
        out["externalExecutionUrl"] = value["external_execution_url"]
    if "percent_complete" in value:
        out["percentComplete"] = value["percent_complete"]
    if "error_details" in value:
        import capo_codepipeline.types.error_details

        out["errorDetails"] = (
            capo_codepipeline.types.error_details.serialize_aws_json_1_1(
                value["error_details"]
            )
        )
    if "log_stream_arn" in value:
        out["logStreamARN"] = value["log_stream_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionExecution:
    out: ActionExecution = {}  # type: ignore[typeddict-item]
    if data.get("actionExecutionId") is not None:
        out["action_execution_id"] = data["actionExecutionId"]
    if data.get("status") is not None:
        import capo_codepipeline.types.action_execution_status

        out["status"] = (
            capo_codepipeline.types.action_execution_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("summary") is not None:
        out["summary"] = data["summary"]
    if data.get("lastStatusChange") is not None:
        import capo_codepipeline.types.timestamp

        out["last_status_change"] = (
            capo_codepipeline.types.timestamp.deserialize_aws_json_1_1(
                data["lastStatusChange"]
            )
        )
    if data.get("token") is not None:
        out["token"] = data["token"]
    if data.get("lastUpdatedBy") is not None:
        out["last_updated_by"] = data["lastUpdatedBy"]
    if data.get("externalExecutionId") is not None:
        out["external_execution_id"] = data["externalExecutionId"]
    if data.get("externalExecutionUrl") is not None:
        out["external_execution_url"] = data["externalExecutionUrl"]
    if data.get("percentComplete") is not None:
        out["percent_complete"] = data["percentComplete"]
    if data.get("errorDetails") is not None:
        import capo_codepipeline.types.error_details

        out["error_details"] = (
            capo_codepipeline.types.error_details.deserialize_aws_json_1_1(
                data["errorDetails"]
            )
        )
    if data.get("logStreamARN") is not None:
        out["log_stream_arn"] = data["logStreamARN"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ActionExecution) -> dict:
    out: dict = {}
    if "action_execution_id" in value:
        out["actionExecutionId"] = value["action_execution_id"]
    if "status" in value:
        import capo_codepipeline.types.action_execution_status

        out["status"] = capo_codepipeline.types.action_execution_status.serialize_cbor(
            value["status"]
        )
    if "summary" in value:
        out["summary"] = value["summary"]
    if "last_status_change" in value:
        import capo_codepipeline.types.timestamp

        out["lastStatusChange"] = capo_codepipeline.types.timestamp.serialize_cbor(
            value["last_status_change"]
        )
    if "token" in value:
        out["token"] = value["token"]
    if "last_updated_by" in value:
        out["lastUpdatedBy"] = value["last_updated_by"]
    if "external_execution_id" in value:
        out["externalExecutionId"] = value["external_execution_id"]
    if "external_execution_url" in value:
        out["externalExecutionUrl"] = value["external_execution_url"]
    if "percent_complete" in value:
        out["percentComplete"] = value["percent_complete"]
    if "error_details" in value:
        import capo_codepipeline.types.error_details

        out["errorDetails"] = capo_codepipeline.types.error_details.serialize_cbor(
            value["error_details"]
        )
    if "log_stream_arn" in value:
        out["logStreamARN"] = value["log_stream_arn"]
    return out


def deserialize_cbor(data: dict) -> ActionExecution:
    out: ActionExecution = {}  # type: ignore[typeddict-item]
    if data.get("actionExecutionId") is not None:
        out["action_execution_id"] = data["actionExecutionId"]
    if data.get("status") is not None:
        import capo_codepipeline.types.action_execution_status

        out["status"] = (
            capo_codepipeline.types.action_execution_status.deserialize_cbor(
                data["status"]
            )
        )
    if data.get("summary") is not None:
        out["summary"] = data["summary"]
    if data.get("lastStatusChange") is not None:
        import capo_codepipeline.types.timestamp

        out["last_status_change"] = capo_codepipeline.types.timestamp.deserialize_cbor(
            data["lastStatusChange"]
        )
    if data.get("token") is not None:
        out["token"] = data["token"]
    if data.get("lastUpdatedBy") is not None:
        out["last_updated_by"] = data["lastUpdatedBy"]
    if data.get("externalExecutionId") is not None:
        out["external_execution_id"] = data["externalExecutionId"]
    if data.get("externalExecutionUrl") is not None:
        out["external_execution_url"] = data["externalExecutionUrl"]
    if data.get("percentComplete") is not None:
        out["percent_complete"] = data["percentComplete"]
    if data.get("errorDetails") is not None:
        import capo_codepipeline.types.error_details

        out["error_details"] = capo_codepipeline.types.error_details.deserialize_cbor(
            data["errorDetails"]
        )
    if data.get("logStreamARN") is not None:
        out["log_stream_arn"] = data["logStreamARN"]
    return out
