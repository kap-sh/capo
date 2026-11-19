"""Generated from Smithy shape ``com.amazonaws.shield#BlockAction``."""

from typing_extensions import TypedDict


class BlockAction(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BlockAction) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> BlockAction:
    out: BlockAction = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BlockAction) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> BlockAction:
    out: BlockAction = {}  # type: ignore[typeddict-item]
    return out
