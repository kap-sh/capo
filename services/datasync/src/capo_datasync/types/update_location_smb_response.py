"""Generated from Smithy shape ``com.amazonaws.datasync#UpdateLocationSmbResponse``."""

from typing_extensions import TypedDict


class UpdateLocationSmbResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLocationSmbResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLocationSmbResponse:
    out: UpdateLocationSmbResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateLocationSmbResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdateLocationSmbResponse:
    out: UpdateLocationSmbResponse = {}  # type: ignore[typeddict-item]
    return out
