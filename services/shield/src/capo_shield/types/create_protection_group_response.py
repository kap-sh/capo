"""Generated from Smithy shape ``com.amazonaws.shield#CreateProtectionGroupResponse``."""

from typing_extensions import TypedDict


class CreateProtectionGroupResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateProtectionGroupResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateProtectionGroupResponse:
    out: CreateProtectionGroupResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateProtectionGroupResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> CreateProtectionGroupResponse:
    out: CreateProtectionGroupResponse = {}  # type: ignore[typeddict-item]
    return out
