"""Generated from Smithy shape ``com.amazonaws.gamelift#AcceptMatchOutput``."""

from typing_extensions import TypedDict


class AcceptMatchOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcceptMatchOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> AcceptMatchOutput:
    out: AcceptMatchOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AcceptMatchOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> AcceptMatchOutput:
    out: AcceptMatchOutput = {}  # type: ignore[typeddict-item]
    return out
