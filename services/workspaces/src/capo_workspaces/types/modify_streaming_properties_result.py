"""Generated from Smithy shape ``com.amazonaws.workspaces#ModifyStreamingPropertiesResult``."""

from typing_extensions import TypedDict


class ModifyStreamingPropertiesResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyStreamingPropertiesResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyStreamingPropertiesResult:
    out: ModifyStreamingPropertiesResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ModifyStreamingPropertiesResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> ModifyStreamingPropertiesResult:
    out: ModifyStreamingPropertiesResult = {}  # type: ignore[typeddict-item]
    return out
