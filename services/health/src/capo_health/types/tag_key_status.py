"""Generated from Smithy shape ``com.amazonaws.health#TagKeyStatus``."""

from typing import Literal, TypeAlias, cast

TagKeyStatus: TypeAlias = Literal[
    "PENDING",
    "ACTIVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagKeyStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TagKeyStatus:
    return cast(TagKeyStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TagKeyStatus) -> str:
    return value


def deserialize_cbor(data: str) -> TagKeyStatus:
    return cast(TagKeyStatus, data)
