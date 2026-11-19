"""Generated from Smithy shape ``com.amazonaws.applicationinsights#ConfigurationEventResourceType``."""

from typing import Literal, TypeAlias, cast

ConfigurationEventResourceType: TypeAlias = Literal[
    "CLOUDWATCH_ALARM",
    "CLOUDWATCH_LOG",
    "CLOUDFORMATION",
    "SSM_ASSOCIATION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationEventResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConfigurationEventResourceType:
    return cast(ConfigurationEventResourceType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConfigurationEventResourceType) -> str:
    return value


def deserialize_cbor(data: str) -> ConfigurationEventResourceType:
    return cast(ConfigurationEventResourceType, data)
