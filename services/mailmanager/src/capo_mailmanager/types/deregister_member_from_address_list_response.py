"""Generated from Smithy shape ``com.amazonaws.mailmanager#DeregisterMemberFromAddressListResponse``."""

from typing_extensions import TypedDict


class DeregisterMemberFromAddressListResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeregisterMemberFromAddressListResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeregisterMemberFromAddressListResponse:
    out: DeregisterMemberFromAddressListResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeregisterMemberFromAddressListResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeregisterMemberFromAddressListResponse:
    out: DeregisterMemberFromAddressListResponse = {}  # type: ignore[typeddict-item]
    return out
