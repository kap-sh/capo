"""Generated from Smithy shape ``com.amazonaws.applicationinsights#ConfigurationEventStatus``."""

from typing import Literal, TypeAlias, cast

ConfigurationEventStatus: TypeAlias = Literal[
    "INFO",
    "WARN",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationEventStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConfigurationEventStatus:
    return cast(ConfigurationEventStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConfigurationEventStatus) -> str:
    return value


def deserialize_cbor(data: str) -> ConfigurationEventStatus:
    return cast(ConfigurationEventStatus, data)
