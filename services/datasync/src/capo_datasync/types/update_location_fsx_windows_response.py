"""Generated from Smithy shape ``com.amazonaws.datasync#UpdateLocationFsxWindowsResponse``."""

from typing_extensions import TypedDict


class UpdateLocationFsxWindowsResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLocationFsxWindowsResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLocationFsxWindowsResponse:
    out: UpdateLocationFsxWindowsResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateLocationFsxWindowsResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdateLocationFsxWindowsResponse:
    out: UpdateLocationFsxWindowsResponse = {}  # type: ignore[typeddict-item]
    return out
