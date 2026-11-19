"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#HsmState``."""

from typing import Literal, TypeAlias, cast

HsmState: TypeAlias = Literal[
    "CREATE_IN_PROGRESS",
    "ACTIVE",
    "DEGRADED",
    "DELETE_IN_PROGRESS",
    "DELETED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HsmState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HsmState:
    return cast(HsmState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: HsmState) -> str:
    return value


def deserialize_cbor(data: str) -> HsmState:
    return cast(HsmState, data)
