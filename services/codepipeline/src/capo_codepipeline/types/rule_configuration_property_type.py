"""Generated from Smithy shape ``com.amazonaws.codepipeline#RuleConfigurationPropertyType``."""

from typing import Literal, TypeAlias, cast

RuleConfigurationPropertyType: TypeAlias = Literal[
    "String",
    "Number",
    "Boolean",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleConfigurationPropertyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RuleConfigurationPropertyType:
    return cast(RuleConfigurationPropertyType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleConfigurationPropertyType) -> str:
    return value


def deserialize_cbor(data: str) -> RuleConfigurationPropertyType:
    return cast(RuleConfigurationPropertyType, data)
