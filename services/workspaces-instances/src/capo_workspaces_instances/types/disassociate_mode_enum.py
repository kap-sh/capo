"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#DisassociateModeEnum``."""

from typing import Literal, TypeAlias, cast

DisassociateModeEnum: TypeAlias = Literal[
    "FORCE",
    "NO_FORCE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisassociateModeEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DisassociateModeEnum:
    return cast(DisassociateModeEnum, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DisassociateModeEnum) -> str:
    return value


def deserialize_cbor(data: str) -> DisassociateModeEnum:
    return cast(DisassociateModeEnum, data)
