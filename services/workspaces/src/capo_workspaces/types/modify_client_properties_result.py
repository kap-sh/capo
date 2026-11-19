"""Generated from Smithy shape ``com.amazonaws.workspaces#ModifyClientPropertiesResult``."""

from typing_extensions import TypedDict


class ModifyClientPropertiesResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyClientPropertiesResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyClientPropertiesResult:
    out: ModifyClientPropertiesResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ModifyClientPropertiesResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> ModifyClientPropertiesResult:
    out: ModifyClientPropertiesResult = {}  # type: ignore[typeddict-item]
    return out
