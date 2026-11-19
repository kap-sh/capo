"""Generated from Smithy shape ``com.amazonaws.codedeploy#ECSServiceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.ecs_service

ECSServiceList: TypeAlias = list["capo_codedeploy.types.ecs_service.ECSService"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ECSServiceList) -> list:
    import capo_codedeploy.types.ecs_service

    out: list = []
    for item in value:
        out.append(capo_codedeploy.types.ecs_service.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ECSServiceList:
    import capo_codedeploy.types.ecs_service

    out: ECSServiceList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codedeploy.types.ecs_service.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ECSServiceList) -> list:
    import capo_codedeploy.types.ecs_service

    out: list = []
    for item in value:
        out.append(capo_codedeploy.types.ecs_service.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ECSServiceList:
    import capo_codedeploy.types.ecs_service

    out: ECSServiceList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codedeploy.types.ecs_service.deserialize_cbor(item))
    return out
