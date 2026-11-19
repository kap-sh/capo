"""Generated from Smithy shape ``com.amazonaws.shield#DisassociateDRTRoleResponse``."""

from typing_extensions import TypedDict


class DisassociateDRTRoleResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateDRTRoleResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateDRTRoleResponse:
    out: DisassociateDRTRoleResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DisassociateDRTRoleResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DisassociateDRTRoleResponse:
    out: DisassociateDRTRoleResponse = {}  # type: ignore[typeddict-item]
    return out
