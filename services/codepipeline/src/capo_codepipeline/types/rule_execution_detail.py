"""Generated from Smithy shape ``com.amazonaws.codepipeline#RuleExecutionDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.last_updated_by
    import capo_codepipeline.types.pipeline_execution_id
    import capo_codepipeline.types.pipeline_version
    import capo_codepipeline.types.rule_execution_id
    import capo_codepipeline.types.rule_execution_input
    import capo_codepipeline.types.rule_execution_output
    import capo_codepipeline.types.rule_execution_status
    import capo_codepipeline.types.rule_name
    import capo_codepipeline.types.stage_name
    import capo_codepipeline.types.timestamp


class RuleExecutionDetail(TypedDict, closed=True):
    pipeline_execution_id: NotRequired[
        "capo_codepipeline.types.pipeline_execution_id.PipelineExecutionId"
    ]
    """<p>The ID of the pipeline execution in the stage where the rule was run. Use the <a>GetPipelineState</a> action to retrieve the current pipelineExecutionId of the stage.</p>"""
    rule_execution_id: NotRequired[
        "capo_codepipeline.types.rule_execution_id.RuleExecutionId"
    ]
    """<p>The ID of the run for the rule.</p>"""
    pipeline_version: NotRequired[
        "capo_codepipeline.types.pipeline_version.PipelineVersion"
    ]
    """<p>The version number of the pipeline with the stage where the rule was run.</p>"""
    stage_name: NotRequired["capo_codepipeline.types.stage_name.StageName"]
    """<p>The name of the stage where the rule was run.</p>"""
    rule_name: NotRequired["capo_codepipeline.types.rule_name.RuleName"]
    """<p>The name of the rule that was run in the stage.</p>"""
    start_time: NotRequired["capo_codepipeline.types.timestamp.Timestamp"]
    """<p>The start time of the rule execution.</p>"""
    last_update_time: NotRequired["capo_codepipeline.types.timestamp.Timestamp"]
    """<p>The date and time of the last change to the rule execution, in timestamp format.</p>"""
    updated_by: NotRequired["capo_codepipeline.types.last_updated_by.LastUpdatedBy"]
    """<p>The ARN of the user who changed the rule execution details.</p>"""
    status: NotRequired[
        "capo_codepipeline.types.rule_execution_status.RuleExecutionStatus"
    ]
    """<p>The status of the rule execution. Status categories are <code>InProgress</code>, <code>Succeeded</code>, and <code>Failed</code>. </p>"""
    input: NotRequired[
        "capo_codepipeline.types.rule_execution_input.RuleExecutionInput"
    ]
    """<p>Input details for the rule execution, such as role ARN, Region, and input artifacts.</p>"""
    output: NotRequired[
        "capo_codepipeline.types.rule_execution_output.RuleExecutionOutput"
    ]
    """<p>Output details for the rule execution, such as the rule execution result.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleExecutionDetail) -> dict:
    out: dict = {}
    if "pipeline_execution_id" in value:
        out["pipelineExecutionId"] = value["pipeline_execution_id"]
    if "rule_execution_id" in value:
        out["ruleExecutionId"] = value["rule_execution_id"]
    if "pipeline_version" in value:
        out["pipelineVersion"] = value["pipeline_version"]
    if "stage_name" in value:
        out["stageName"] = value["stage_name"]
    if "rule_name" in value:
        out["ruleName"] = value["rule_name"]
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
        import capo_codepipeline.types.rule_execution_status

        out["status"] = (
            capo_codepipeline.types.rule_execution_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "input" in value:
        import capo_codepipeline.types.rule_execution_input

        out["input"] = (
            capo_codepipeline.types.rule_execution_input.serialize_aws_json_1_1(
                value["input"]
            )
        )
    if "output" in value:
        import capo_codepipeline.types.rule_execution_output

        out["output"] = (
            capo_codepipeline.types.rule_execution_output.serialize_aws_json_1_1(
                value["output"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RuleExecutionDetail:
    out: RuleExecutionDetail = {}  # type: ignore[typeddict-item]
    if data.get("pipelineExecutionId") is not None:
        out["pipeline_execution_id"] = data["pipelineExecutionId"]
    if data.get("ruleExecutionId") is not None:
        out["rule_execution_id"] = data["ruleExecutionId"]
    if data.get("pipelineVersion") is not None:
        out["pipeline_version"] = data["pipelineVersion"]
    if data.get("stageName") is not None:
        out["stage_name"] = data["stageName"]
    if data.get("ruleName") is not None:
        out["rule_name"] = data["ruleName"]
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
        import capo_codepipeline.types.rule_execution_status

        out["status"] = (
            capo_codepipeline.types.rule_execution_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("input") is not None:
        import capo_codepipeline.types.rule_execution_input

        out["input"] = (
            capo_codepipeline.types.rule_execution_input.deserialize_aws_json_1_1(
                data["input"]
            )
        )
    if data.get("output") is not None:
        import capo_codepipeline.types.rule_execution_output

        out["output"] = (
            capo_codepipeline.types.rule_execution_output.deserialize_aws_json_1_1(
                data["output"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleExecutionDetail) -> dict:
    out: dict = {}
    if "pipeline_execution_id" in value:
        out["pipelineExecutionId"] = value["pipeline_execution_id"]
    if "rule_execution_id" in value:
        out["ruleExecutionId"] = value["rule_execution_id"]
    if "pipeline_version" in value:
        out["pipelineVersion"] = value["pipeline_version"]
    if "stage_name" in value:
        out["stageName"] = value["stage_name"]
    if "rule_name" in value:
        out["ruleName"] = value["rule_name"]
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
        import capo_codepipeline.types.rule_execution_status

        out["status"] = capo_codepipeline.types.rule_execution_status.serialize_cbor(
            value["status"]
        )
    if "input" in value:
        import capo_codepipeline.types.rule_execution_input

        out["input"] = capo_codepipeline.types.rule_execution_input.serialize_cbor(
            value["input"]
        )
    if "output" in value:
        import capo_codepipeline.types.rule_execution_output

        out["output"] = capo_codepipeline.types.rule_execution_output.serialize_cbor(
            value["output"]
        )
    return out


def deserialize_cbor(data: dict) -> RuleExecutionDetail:
    out: RuleExecutionDetail = {}  # type: ignore[typeddict-item]
    if data.get("pipelineExecutionId") is not None:
        out["pipeline_execution_id"] = data["pipelineExecutionId"]
    if data.get("ruleExecutionId") is not None:
        out["rule_execution_id"] = data["ruleExecutionId"]
    if data.get("pipelineVersion") is not None:
        out["pipeline_version"] = data["pipelineVersion"]
    if data.get("stageName") is not None:
        out["stage_name"] = data["stageName"]
    if data.get("ruleName") is not None:
        out["rule_name"] = data["ruleName"]
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
        import capo_codepipeline.types.rule_execution_status

        out["status"] = capo_codepipeline.types.rule_execution_status.deserialize_cbor(
            data["status"]
        )
    if data.get("input") is not None:
        import capo_codepipeline.types.rule_execution_input

        out["input"] = capo_codepipeline.types.rule_execution_input.deserialize_cbor(
            data["input"]
        )
    if data.get("output") is not None:
        import capo_codepipeline.types.rule_execution_output

        out["output"] = capo_codepipeline.types.rule_execution_output.deserialize_cbor(
            data["output"]
        )
    return out
