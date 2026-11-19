"""Generated from Smithy shape ``com.amazonaws.applicationinsights#CreateComponentResponse``."""

from typing_extensions import TypedDict


class CreateComponentResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateComponentResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateComponentResponse:
    out: CreateComponentResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateComponentResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> CreateComponentResponse:
    out: CreateComponentResponse = {}  # type: ignore[typeddict-item]
    return out
