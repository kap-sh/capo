"""Generated from Smithy shape ``com.amazonaws.fms#GetAdminAccountRequest``."""

from typing_extensions import TypedDict


class GetAdminAccountRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAdminAccountRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAdminAccountRequest:
    out: GetAdminAccountRequest = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetAdminAccountRequest) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> GetAdminAccountRequest:
    out: GetAdminAccountRequest = {}  # type: ignore[typeddict-item]
    return out
