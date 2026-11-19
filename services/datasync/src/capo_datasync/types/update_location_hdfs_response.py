"""Generated from Smithy shape ``com.amazonaws.datasync#UpdateLocationHdfsResponse``."""

from typing_extensions import TypedDict


class UpdateLocationHdfsResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLocationHdfsResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLocationHdfsResponse:
    out: UpdateLocationHdfsResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateLocationHdfsResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdateLocationHdfsResponse:
    out: UpdateLocationHdfsResponse = {}  # type: ignore[typeddict-item]
    return out
