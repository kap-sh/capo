"""Generated from Smithy shape ``com.amazonaws.snowball#JobState``."""

from typing import Literal, TypeAlias, cast

JobState: TypeAlias = Literal[
    "New",
    "PreparingAppliance",
    "PreparingShipment",
    "InTransitToCustomer",
    "WithCustomer",
    "InTransitToAWS",
    "WithAWSSortingFacility",
    "WithAWS",
    "InProgress",
    "Complete",
    "Cancelled",
    "Listing",
    "Pending",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JobState:
    return cast(JobState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: JobState) -> str:
    return value


def deserialize_cbor(data: str) -> JobState:
    return cast(JobState, data)
