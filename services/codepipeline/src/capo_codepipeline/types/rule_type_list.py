"""Generated from Smithy shape ``com.amazonaws.codepipeline#RuleTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.rule_type

RuleTypeList: TypeAlias = list["capo_codepipeline.types.rule_type.RuleType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleTypeList) -> list:
    import capo_codepipeline.types.rule_type

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.rule_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RuleTypeList:
    import capo_codepipeline.types.rule_type

    out: RuleTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codepipeline.types.rule_type.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleTypeList) -> list:
    import capo_codepipeline.types.rule_type

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.rule_type.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> RuleTypeList:
    import capo_codepipeline.types.rule_type

    out: RuleTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codepipeline.types.rule_type.deserialize_cbor(item))
    return out
