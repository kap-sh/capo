"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionExecutionDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.action_execution_id
    import capo_codepipeline.types.action_execution_input
    import capo_codepipeline.types.action_execution_output
    import capo_codepipeline.types.action_execution_status
    import capo_codepipeline.types.action_name
    import capo_codepipeline.types.last_updated_by
    import capo_codepipeline.types.pipeline_execution_id
    import capo_codepipeline.types.pipeline_version
    import capo_codepipeline.types.stage_name
    import capo_codepipeline.types.timestamp


class ActionExecutionDetail(TypedDict, closed=True):
    pipeline_execution_id: NotRequired[
        "capo_codepipeline.types.pipeline_execution_id.PipelineExecutionId"
    ]
    """<p>The pipeline execution ID for the action execution.</p>"""
    action_execution_id: NotRequired[
        "capo_codepipeline.types.action_execution_id.ActionExecutionId"
    ]
    """<p>The action execution ID.</p>"""
    pipeline_version: NotRequired[
        "capo_codepipeline.types.pipeline_version.PipelineVersion"
    ]
    """<p>The version of the pipeline where the action was run.</p>"""
    stage_name: NotRequired["capo_codepipeline.types.stage_name.StageName"]
    """<p>The name of the stage that contains the action.</p>"""
    action_name: NotRequired["capo_codepipeline.types.action_name.ActionName"]
    """<p>The name of the action.</p>"""
    start_time: NotRequired["capo_codepipeline.types.timestamp.Timestamp"]
    """<p>The start time of the action execution.</p>"""
    last_update_time: NotRequired["capo_codepipeline.types.timestamp.Timestamp"]
    """<p>The last update time of the action execution.</p>"""
    updated_by: NotRequired["capo_codepipeline.types.last_updated_by.LastUpdatedBy"]
    """<p>The ARN of the user who changed the pipeline execution details.</p>"""
    status: NotRequired[
        "capo_codepipeline.types.action_execution_status.ActionExecutionStatus"
    ]
    """<p> The status of the action execution. Status categories are <code>InProgress</code>, <code>Succeeded</code>, and <code>Failed</code>.</p>"""
    input: NotRequired[
        "capo_codepipeline.types.action_execution_input.ActionExecutionInput"
    ]
    """<p>Input details for the action execution, such as role ARN, Region, and input artifacts.</p>"""
    output: NotRequired[
        "capo_codepipeline.types.action_execution_output.ActionExecutionOutput"
    ]
    """<p>Output details for the action execution, such as the action execution result.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionExecutionDetail) -> dict:
    out: dict = {}
    if "pipeline_execution_id" in value:
        out["pipelineExecutionId"] = value["pipeline_execution_id"]
    if "action_execution_id" in value:
        out["actionExecutionId"] = value["action_execution_id"]
    if "pipeline_version" in value:
        out["pipelineVersion"] = value["pipeline_version"]
    if "stage_name" in value:
        out["stageName"] = value["stage_name"]
    if "action_name" in value:
        out["actionName"] = value["action_name"]
    if "start_time" in value:
        import capo_codepipeline.types.timestamp

        out["startTime"] = capo_codepipeline.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "last_update_time" in value:
        import capo_codepipeline.types.timestamp

        out["lastUpdateTime"] = (
            capo_codepipeline.types.timestamp.serialize_aws_json_1_1(
                value["last_update_time"]
            )
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    if "status" in value:
        import capo_codepipeline.types.action_execution_status

        out["status"] = (
            capo_codepipeline.types.action_execution_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "input" in value:
        import capo_codepipeline.types.action_execution_input

        out["input"] = (
            capo_codepipeline.types.action_execution_input.serialize_aws_json_1_1(
                value["input"]
            )
        )
    if "output" in value:
        import capo_codepipeline.types.action_execution_output

        out["output"] = (
            capo_codepipeline.types.action_execution_output.serialize_aws_json_1_1(
                value["output"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionExecutionDetail:
    out: ActionExecutionDetail = {}  # type: ignore[typeddict-item]
    if data.get("pipelineExecutionId") is not None:
        out["pipeline_execution_id"] = data["pipelineExecutionId"]
    if data.get("actionExecutionId") is not None:
        out["action_execution_id"] = data["actionExecutionId"]
    if data.get("pipelineVersion") is not None:
        out["pipeline_version"] = data["pipelineVersion"]
    if data.get("stageName") is not None:
        out["stage_name"] = data["stageName"]
    if data.get("actionName") is not None:
        out["action_name"] = data["actionName"]
    if data.get("startTime") is not None:
        import capo_codepipeline.types.timestamp

        out["start_time"] = capo_codepipeline.types.timestamp.deserialize_aws_json_1_1(
            data["startTime"]
        )
    if data.get("lastUpdateTime") is not None:
        import capo_codepipeline.types.timestamp

        out["last_update_time"] = (
            capo_codepipeline.types.timestamp.deserialize_aws_json_1_1(
                data["lastUpdateTime"]
            )
        )
    if data.get("updatedBy") is not None:
        out["updated_by"] = data["updatedBy"]
    if data.get("status") is not None:
        import capo_codepipeline.types.action_execution_status

        out["status"] = (
            capo_codepipeline.types.action_execution_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("input") is not None:
        import capo_codepipeline.types.action_execution_input

        out["input"] = (
            capo_codepipeline.types.action_execution_input.deserialize_aws_json_1_1(
                data["input"]
            )
        )
    if data.get("output") is not None:
        import capo_codepipeline.types.action_execution_output

        out["output"] = (
            capo_codepipeline.types.action_execution_output.deserialize_aws_json_1_1(
                data["output"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ActionExecutionDetail) -> dict:
    out: dict = {}
    if "pipeline_execution_id" in value:
        out["pipelineExecutionId"] = value["pipeline_execution_id"]
    if "action_execution_id" in value:
        out["actionExecutionId"] = value["action_execution_id"]
    if "pipeline_version" in value:
        out["pipelineVersion"] = value["pipeline_version"]
    if "stage_name" in value:
        out["stageName"] = value["stage_name"]
    if "action_name" in value:
        out["actionName"] = value["action_name"]
    if "start_time" in value:
        import capo_codepipeline.types.timestamp

        out["startTime"] = capo_codepipeline.types.timestamp.serialize_cbor(
            value["start_time"]
        )
    if "last_update_time" in value:
        import capo_codepipeline.types.timestamp

        out["lastUpdateTime"] = capo_codepipeline.types.timestamp.serialize_cbor(
            value["last_update_time"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    if "status" in value:
        import capo_codepipeline.types.action_execution_status

        out["status"] = capo_codepipeline.types.action_execution_status.serialize_cbor(
            value["status"]
        )
    if "input" in value:
        import capo_codepipeline.types.action_execution_input

        out["input"] = capo_codepipeline.types.action_execution_input.serialize_cbor(
            value["input"]
        )
    if "output" in value:
        import capo_codepipeline.types.action_execution_output

        out["output"] = capo_codepipeline.types.action_execution_output.serialize_cbor(
            value["output"]
        )
    return out


def deserialize_cbor(data: dict) -> ActionExecutionDetail:
    out: ActionExecutionDetail = {}  # type: ignore[typeddict-item]
    if data.get("pipelineExecutionId") is not None:
        out["pipeline_execution_id"] = data["pipelineExecutionId"]
    if data.get("actionExecutionId") is not None:
        out["action_execution_id"] = data["actionExecutionId"]
    if data.get("pipelineVersion") is not None:
        out["pipeline_version"] = data["pipelineVersion"]
    if data.get("stageName") is not None:
        out["stage_name"] = data["stageName"]
    if data.get("actionName") is not None:
        out["action_name"] = data["actionName"]
    if data.get("startTime") is not None:
        import capo_codepipeline.types.timestamp

        out["start_time"] = capo_codepipeline.types.timestamp.deserialize_cbor(
            data["startTime"]
        )
    if data.get("lastUpdateTime") is not None:
        import capo_codepipeline.types.timestamp

        out["last_update_time"] = capo_codepipeline.types.timestamp.deserialize_cbor(
            data["lastUpdateTime"]
        )
    if data.get("updatedBy") is not None:
        out["updated_by"] = data["updatedBy"]
    if data.get("status") is not None:
        import capo_codepipeline.types.action_execution_status

        out["status"] = (
            capo_codepipeline.types.action_execution_status.deserialize_cbor(
                data["status"]
            )
        )
    if data.get("input") is not None:
        import capo_codepipeline.types.action_execution_input

        out["input"] = capo_codepipeline.types.action_execution_input.deserialize_cbor(
            data["input"]
        )
    if data.get("output") is not None:
        import capo_codepipeline.types.action_execution_output

        out["output"] = (
            capo_codepipeline.types.action_execution_output.deserialize_cbor(
                data["output"]
            )
        )
    return out
