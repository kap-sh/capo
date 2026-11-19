"""Generated from Smithy shape ``com.amazonaws.shield#DisassociateDRTRoleRequest``."""

from typing_extensions import TypedDict


class DisassociateDRTRoleRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateDRTRoleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateDRTRoleRequest:
    out: DisassociateDRTRoleRequest = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DisassociateDRTRoleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DisassociateDRTRoleRequest:
    out: DisassociateDRTRoleRequest = {}  # type: ignore[typeddict-item]
    return out
