"""Generated from Smithy shape ``com.amazonaws.mailmanager#DeleteAddressListResponse``."""

from typing_extensions import TypedDict


class DeleteAddressListResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteAddressListResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteAddressListResponse:
    out: DeleteAddressListResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteAddressListResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteAddressListResponse:
    out: DeleteAddressListResponse = {}  # type: ignore[typeddict-item]
    return out
