"""Generated from Smithy shape ``com.amazonaws.codepipeline#DeployTargetEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.deploy_target_event

DeployTargetEventList: TypeAlias = list[
    "capo_codepipeline.types.deploy_target_event.DeployTargetEvent"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeployTargetEventList) -> list:
    import capo_codepipeline.types.deploy_target_event

    out: list = []
    for item in value:
        out.append(
            capo_codepipeline.types.deploy_target_event.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeployTargetEventList:
    import capo_codepipeline.types.deploy_target_event

    out: DeployTargetEventList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codepipeline.types.deploy_target_event.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeployTargetEventList) -> list:
    import capo_codepipeline.types.deploy_target_event

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.deploy_target_event.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> DeployTargetEventList:
    import capo_codepipeline.types.deploy_target_event

    out: DeployTargetEventList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codepipeline.types.deploy_target_event.deserialize_cbor(item))
    return out
