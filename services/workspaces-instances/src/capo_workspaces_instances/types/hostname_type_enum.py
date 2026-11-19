"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#HostnameTypeEnum``."""

from typing import Literal, TypeAlias, cast

HostnameTypeEnum: TypeAlias = Literal[
    "ip-name",
    "resource-name",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HostnameTypeEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> HostnameTypeEnum:
    return cast(HostnameTypeEnum, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: HostnameTypeEnum) -> str:
    return value


def deserialize_cbor(data: str) -> HostnameTypeEnum:
    return cast(HostnameTypeEnum, data)
