"""Generated from Smithy shape ``com.amazonaws.mailmanager#StopArchiveSearchResponse``."""

from typing_extensions import TypedDict


class StopArchiveSearchResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StopArchiveSearchResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> StopArchiveSearchResponse:
    out: StopArchiveSearchResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StopArchiveSearchResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> StopArchiveSearchResponse:
    out: StopArchiveSearchResponse = {}  # type: ignore[typeddict-item]
    return out
