"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ProxyModifyState``."""

from typing import Literal, TypeAlias, cast

ProxyModifyState: TypeAlias = Literal[
    "MODIFYING",
    "COMPLETED",
    "FAILED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProxyModifyState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ProxyModifyState:
    return cast(ProxyModifyState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProxyModifyState) -> str:
    return value


def deserialize_cbor(data: str) -> ProxyModifyState:
    return cast(ProxyModifyState, data)
