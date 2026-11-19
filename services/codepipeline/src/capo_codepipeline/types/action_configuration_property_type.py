"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionConfigurationPropertyType``."""

from typing import Literal, TypeAlias, cast

ActionConfigurationPropertyType: TypeAlias = Literal[
    "String",
    "Number",
    "Boolean",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionConfigurationPropertyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActionConfigurationPropertyType:
    return cast(ActionConfigurationPropertyType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ActionConfigurationPropertyType) -> str:
    return value


def deserialize_cbor(data: str) -> ActionConfigurationPropertyType:
    return cast(ActionConfigurationPropertyType, data)
