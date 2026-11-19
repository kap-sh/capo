"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#HttpTokensEnum``."""

from typing import Literal, TypeAlias, cast

HttpTokensEnum: TypeAlias = Literal[
    "optional",
    "required",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HttpTokensEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> HttpTokensEnum:
    return cast(HttpTokensEnum, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: HttpTokensEnum) -> str:
    return value


def deserialize_cbor(data: str) -> HttpTokensEnum:
    return cast(HttpTokensEnum, data)
