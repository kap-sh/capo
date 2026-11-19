"""Generated from Smithy shape ``com.amazonaws.networkfirewall#OverrideAction``."""

from typing import Literal, TypeAlias, cast

OverrideAction: TypeAlias = Literal["DROP_TO_ALERT",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OverrideAction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OverrideAction:
    return cast(OverrideAction, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OverrideAction) -> str:
    return value


def deserialize_cbor(data: str) -> OverrideAction:
    return cast(OverrideAction, data)
