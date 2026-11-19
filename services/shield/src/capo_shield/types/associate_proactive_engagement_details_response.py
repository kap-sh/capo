"""Generated from Smithy shape ``com.amazonaws.shield#AssociateProactiveEngagementDetailsResponse``."""

from typing_extensions import TypedDict


class AssociateProactiveEngagementDetailsResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateProactiveEngagementDetailsResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateProactiveEngagementDetailsResponse:
    out: AssociateProactiveEngagementDetailsResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AssociateProactiveEngagementDetailsResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> AssociateProactiveEngagementDetailsResponse:
    out: AssociateProactiveEngagementDetailsResponse = {}  # type: ignore[typeddict-item]
    return out
