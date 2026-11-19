"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#TenancyEnum``."""

from typing import Literal, TypeAlias, cast

TenancyEnum: TypeAlias = Literal[
    "default",
    "dedicated",
    "host",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TenancyEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TenancyEnum:
    return cast(TenancyEnum, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TenancyEnum) -> str:
    return value


def deserialize_cbor(data: str) -> TenancyEnum:
    return cast(TenancyEnum, data)
