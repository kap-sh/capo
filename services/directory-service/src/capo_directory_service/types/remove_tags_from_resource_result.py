"""Generated from Smithy shape ``com.amazonaws.directoryservice#RemoveTagsFromResourceResult``."""

from typing_extensions import TypedDict


class RemoveTagsFromResourceResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveTagsFromResourceResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveTagsFromResourceResult:
    out: RemoveTagsFromResourceResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RemoveTagsFromResourceResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> RemoveTagsFromResourceResult:
    out: RemoveTagsFromResourceResult = {}  # type: ignore[typeddict-item]
    return out
