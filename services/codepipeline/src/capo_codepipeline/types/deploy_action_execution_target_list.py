"""Generated from Smithy shape ``com.amazonaws.codepipeline#DeployActionExecutionTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.deploy_action_execution_target

DeployActionExecutionTargetList: TypeAlias = list[
    "capo_codepipeline.types.deploy_action_execution_target.DeployActionExecutionTarget"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeployActionExecutionTargetList) -> list:
    import capo_codepipeline.types.deploy_action_execution_target

    out: list = []
    for item in value:
        out.append(
            capo_codepipeline.types.deploy_action_execution_target.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeployActionExecutionTargetList:
    import capo_codepipeline.types.deploy_action_execution_target

    out: DeployActionExecutionTargetList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codepipeline.types.deploy_action_execution_target.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeployActionExecutionTargetList) -> list:
    import capo_codepipeline.types.deploy_action_execution_target

    out: list = []
    for item in value:
        out.append(
            capo_codepipeline.types.deploy_action_execution_target.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> DeployActionExecutionTargetList:
    import capo_codepipeline.types.deploy_action_execution_target

    out: DeployActionExecutionTargetList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codepipeline.types.deploy_action_execution_target.deserialize_cbor(
                item
            )
        )
    return out
