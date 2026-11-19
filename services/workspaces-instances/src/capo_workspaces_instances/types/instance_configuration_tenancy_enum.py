"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#InstanceConfigurationTenancyEnum``."""

from typing import Literal, TypeAlias, cast

InstanceConfigurationTenancyEnum: TypeAlias = Literal[
    "SHARED",
    "DEDICATED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceConfigurationTenancyEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InstanceConfigurationTenancyEnum:
    return cast(InstanceConfigurationTenancyEnum, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InstanceConfigurationTenancyEnum) -> str:
    return value


def deserialize_cbor(data: str) -> InstanceConfigurationTenancyEnum:
    return cast(InstanceConfigurationTenancyEnum, data)
