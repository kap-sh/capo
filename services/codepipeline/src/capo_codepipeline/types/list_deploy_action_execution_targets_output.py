"""Generated from Smithy shape ``com.amazonaws.codepipeline#ListDeployActionExecutionTargetsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.deploy_action_execution_target_list
    import capo_codepipeline.types.next_token


class ListDeployActionExecutionTargetsOutput(TypedDict, closed=True):
    targets: NotRequired[
        "capo_codepipeline.types.deploy_action_execution_target_list.DeployActionExecutionTargetList"
    ]
    """<p>The targets for the deploy action.</p>"""
    next_token: NotRequired["capo_codepipeline.types.next_token.NextToken"]
    """<p>An identifier that was returned from the previous list action types call, which can be used to return the next set of action types in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDeployActionExecutionTargetsOutput) -> dict:
    out: dict = {}
    if "targets" in value:
        import capo_codepipeline.types.deploy_action_execution_target_list

        out["targets"] = (
            capo_codepipeline.types.deploy_action_execution_target_list.serialize_aws_json_1_1(
                value["targets"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDeployActionExecutionTargetsOutput:
    out: ListDeployActionExecutionTargetsOutput = {}  # type: ignore[typeddict-item]
    if data.get("targets") is not None:
        import capo_codepipeline.types.deploy_action_execution_target_list

        out["targets"] = (
            capo_codepipeline.types.deploy_action_execution_target_list.deserialize_aws_json_1_1(
                data["targets"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListDeployActionExecutionTargetsOutput) -> dict:
    out: dict = {}
    if "targets" in value:
        import capo_codepipeline.types.deploy_action_execution_target_list

        out["targets"] = (
            capo_codepipeline.types.deploy_action_execution_target_list.serialize_cbor(
                value["targets"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListDeployActionExecutionTargetsOutput:
    out: ListDeployActionExecutionTargetsOutput = {}  # type: ignore[typeddict-item]
    if data.get("targets") is not None:
        import capo_codepipeline.types.deploy_action_execution_target_list

        out["targets"] = (
            capo_codepipeline.types.deploy_action_execution_target_list.deserialize_cbor(
                data["targets"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
