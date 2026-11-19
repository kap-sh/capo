"""Generated from Smithy shape ``com.amazonaws.gamelift#TerminationMode``."""

from typing import Literal, TypeAlias, cast

TerminationMode: TypeAlias = Literal[
    "TRIGGER_ON_PROCESS_TERMINATE",
    "FORCE_TERMINATE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminationMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TerminationMode:
    return cast(TerminationMode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TerminationMode) -> str:
    return value


def deserialize_cbor(data: str) -> TerminationMode:
    return cast(TerminationMode, data)
