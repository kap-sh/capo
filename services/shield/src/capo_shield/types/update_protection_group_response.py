"""Generated from Smithy shape ``com.amazonaws.shield#UpdateProtectionGroupResponse``."""

from typing_extensions import TypedDict


class UpdateProtectionGroupResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateProtectionGroupResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateProtectionGroupResponse:
    out: UpdateProtectionGroupResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateProtectionGroupResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdateProtectionGroupResponse:
    out: UpdateProtectionGroupResponse = {}  # type: ignore[typeddict-item]
    return out
