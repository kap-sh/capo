"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#AttributeName``."""

from typing import Literal, TypeAlias, cast

AttributeName: TypeAlias = Literal[
    "SIGN",
    "SYMPTOM",
    "DIAGNOSIS",
    "NEGATION",
    "PERTAINS_TO_FAMILY",
    "HYPOTHETICAL",
    "LOW_CONFIDENCE",
    "PAST_HISTORY",
    "FUTURE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttributeName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AttributeName:
    return cast(AttributeName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AttributeName) -> str:
    return value


def deserialize_cbor(data: str) -> AttributeName:
    return cast(AttributeName, data)
