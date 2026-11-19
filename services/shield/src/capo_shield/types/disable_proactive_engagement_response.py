"""Generated from Smithy shape ``com.amazonaws.shield#DisableProactiveEngagementResponse``."""

from typing_extensions import TypedDict


class DisableProactiveEngagementResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisableProactiveEngagementResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DisableProactiveEngagementResponse:
    out: DisableProactiveEngagementResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DisableProactiveEngagementResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DisableProactiveEngagementResponse:
    out: DisableProactiveEngagementResponse = {}  # type: ignore[typeddict-item]
    return out
