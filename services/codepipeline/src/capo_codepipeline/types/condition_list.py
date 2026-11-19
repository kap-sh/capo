"""Generated from Smithy shape ``com.amazonaws.codepipeline#ConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.condition

ConditionList: TypeAlias = list["capo_codepipeline.types.condition.Condition"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConditionList) -> list:
    import capo_codepipeline.types.condition

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.condition.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ConditionList:
    import capo_codepipeline.types.condition

    out: ConditionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codepipeline.types.condition.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConditionList) -> list:
    import capo_codepipeline.types.condition

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.condition.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ConditionList:
    import capo_codepipeline.types.condition

    out: ConditionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codepipeline.types.condition.deserialize_cbor(item))
    return out
