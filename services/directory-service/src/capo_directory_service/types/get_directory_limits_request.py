"""Generated from Smithy shape ``com.amazonaws.directoryservice#GetDirectoryLimitsRequest``."""

from typing_extensions import TypedDict


class GetDirectoryLimitsRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDirectoryLimitsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDirectoryLimitsRequest:
    out: GetDirectoryLimitsRequest = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetDirectoryLimitsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> GetDirectoryLimitsRequest:
    out: GetDirectoryLimitsRequest = {}  # type: ignore[typeddict-item]
    return out
