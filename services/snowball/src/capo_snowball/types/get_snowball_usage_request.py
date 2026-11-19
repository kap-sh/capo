"""Generated from Smithy shape ``com.amazonaws.snowball#GetSnowballUsageRequest``."""

from typing_extensions import TypedDict


class GetSnowballUsageRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSnowballUsageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSnowballUsageRequest:
    out: GetSnowballUsageRequest = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetSnowballUsageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> GetSnowballUsageRequest:
    out: GetSnowballUsageRequest = {}  # type: ignore[typeddict-item]
    return out
