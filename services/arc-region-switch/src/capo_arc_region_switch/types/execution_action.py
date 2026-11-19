"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ExecutionAction``."""

from typing import Literal, TypeAlias, cast

ExecutionAction: TypeAlias = Literal[
    "activate",
    "deactivate",
    "postRecovery",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecutionAction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExecutionAction:
    return cast(ExecutionAction, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExecutionAction) -> str:
    return value


def deserialize_cbor(data: str) -> ExecutionAction:
    return cast(ExecutionAction, data)
