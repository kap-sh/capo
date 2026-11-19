"""Generated from Smithy shape ``com.amazonaws.shield#EnableProactiveEngagementRequest``."""

from typing_extensions import TypedDict


class EnableProactiveEngagementRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnableProactiveEngagementRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> EnableProactiveEngagementRequest:
    out: EnableProactiveEngagementRequest = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EnableProactiveEngagementRequest) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> EnableProactiveEngagementRequest:
    out: EnableProactiveEngagementRequest = {}  # type: ignore[typeddict-item]
    return out
