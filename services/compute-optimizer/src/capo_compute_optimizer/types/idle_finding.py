"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#IdleFinding``."""

from typing import Literal, TypeAlias, cast

IdleFinding: TypeAlias = Literal[
    "Idle",
    "Unattached",
    "Unused",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IdleFinding) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IdleFinding:
    return cast(IdleFinding, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IdleFinding) -> str:
    return value


def deserialize_cbor(data: str) -> IdleFinding:
    return cast(IdleFinding, data)
