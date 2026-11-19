"""Generated from Smithy shape ``com.amazonaws.datasync#UpdateLocationEfsResponse``."""

from typing_extensions import TypedDict


class UpdateLocationEfsResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLocationEfsResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLocationEfsResponse:
    out: UpdateLocationEfsResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateLocationEfsResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdateLocationEfsResponse:
    out: UpdateLocationEfsResponse = {}  # type: ignore[typeddict-item]
    return out
