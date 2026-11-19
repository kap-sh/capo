"""Generated from Smithy shape ``com.amazonaws.shield#CountAction``."""

from typing_extensions import TypedDict


class CountAction(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CountAction) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> CountAction:
    out: CountAction = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CountAction) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> CountAction:
    out: CountAction = {}  # type: ignore[typeddict-item]
    return out
