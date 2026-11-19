"""Generated from Smithy shape ``com.amazonaws.shield#DisableProactiveEngagementRequest``."""

from typing_extensions import TypedDict


class DisableProactiveEngagementRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisableProactiveEngagementRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DisableProactiveEngagementRequest:
    out: DisableProactiveEngagementRequest = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DisableProactiveEngagementRequest) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DisableProactiveEngagementRequest:
    out: DisableProactiveEngagementRequest = {}  # type: ignore[typeddict-item]
    return out
