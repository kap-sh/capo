"""Generated from Smithy shape ``com.amazonaws.servicediscovery#UpdateServiceAttributesResponse``."""

from typing_extensions import TypedDict


class UpdateServiceAttributesResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateServiceAttributesResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateServiceAttributesResponse:
    out: UpdateServiceAttributesResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateServiceAttributesResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdateServiceAttributesResponse:
    out: UpdateServiceAttributesResponse = {}  # type: ignore[typeddict-item]
    return out
