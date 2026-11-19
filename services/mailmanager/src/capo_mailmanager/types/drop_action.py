"""Generated from Smithy shape ``com.amazonaws.mailmanager#DropAction``."""

from typing_extensions import TypedDict


class DropAction(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DropAction) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DropAction:
    out: DropAction = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DropAction) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DropAction:
    out: DropAction = {}  # type: ignore[typeddict-item]
    return out
