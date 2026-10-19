"""Generated from Smithy shape ``com.amazonaws.codepipeline#PutApprovalResultInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codepipeline.types.action_name
    import capo_codepipeline.types.approval_result
    import capo_codepipeline.types.approval_token
    import capo_codepipeline.types.pipeline_name
    import capo_codepipeline.types.stage_name


class PutApprovalResultInput(TypedDict, closed=True):
    pipeline_name: "capo_codepipeline.types.pipeline_name.PipelineName"
    """<p>The name of the pipeline that contains the action. </p>"""
    stage_name: "capo_codepipeline.types.stage_name.StageName"
    """<p>The name of the stage that contains the action.</p>"""
    action_name: "capo_codepipeline.types.action_name.ActionName"
    """<p>The name of the action for which approval is requested.</p>"""
    result: "capo_codepipeline.types.approval_result.ApprovalResult"
    """<p>Represents information about the result of the approval request.</p>"""
    token: "capo_codepipeline.types.approval_token.ApprovalToken"
    """<p>The system-generated token used to identify a unique approval request. The token for each open approval request can be obtained using the <a>GetPipelineState</a> action. It is used to validate that the approval request corresponding to this token is still valid.</p> <important> <p>For a pipeline where the execution mode is set to PARALLEL, the token required to approve/reject an approval request as detailed above is not available. Instead, use the <code>externalExecutionId</code> in the response output from the <a>ListActionExecutions</a> action as the token in the approval request.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutApprovalResultInput) -> dict:
    out: dict = {}
    out["pipelineName"] = value["pipeline_name"]
    out["stageName"] = value["stage_name"]
    out["actionName"] = value["action_name"]
    import capo_codepipeline.types.approval_result

    out["result"] = capo_codepipeline.types.approval_result.serialize_aws_json_1_1(
        value["result"]
    )
    out["token"] = value["token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutApprovalResultInput:
    out: PutApprovalResultInput = {}  # type: ignore[typeddict-item]
    if data.get("pipelineName") is not None:
        out["pipeline_name"] = data["pipelineName"]
    else:
        out["pipeline_name"] = ""
    if data.get("stageName") is not None:
        out["stage_name"] = data["stageName"]
    else:
        out["stage_name"] = ""
    if data.get("actionName") is not None:
        out["action_name"] = data["actionName"]
    else:
        out["action_name"] = ""
    if data.get("result") is not None:
        import capo_codepipeline.types.approval_result

        out["result"] = (
            capo_codepipeline.types.approval_result.deserialize_aws_json_1_1(
                data["result"]
            )
        )
    else:
        raise DeserializationError("PutApprovalResultInput.result required")
    if data.get("token") is not None:
        out["token"] = data["token"]
    else:
        out["token"] = ""
    return out
