"""Generated from Smithy shape ``com.amazonaws.datasync#UpdateLocationNfsResponse``."""

from typing_extensions import TypedDict


class UpdateLocationNfsResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLocationNfsResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLocationNfsResponse:
    out: UpdateLocationNfsResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateLocationNfsResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdateLocationNfsResponse:
    out: UpdateLocationNfsResponse = {}  # type: ignore[typeddict-item]
    return out
