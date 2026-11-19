"""Generated from Smithy shape ``com.amazonaws.shield#EnableProactiveEngagementResponse``."""

from typing_extensions import TypedDict


class EnableProactiveEngagementResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnableProactiveEngagementResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> EnableProactiveEngagementResponse:
    out: EnableProactiveEngagementResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EnableProactiveEngagementResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> EnableProactiveEngagementResponse:
    out: EnableProactiveEngagementResponse = {}  # type: ignore[typeddict-item]
    return out
