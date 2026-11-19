"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#EntityType``."""

from typing import Literal, TypeAlias, cast

EntityType: TypeAlias = Literal[
    "MEDICATION",
    "MEDICAL_CONDITION",
    "PROTECTED_HEALTH_INFORMATION",
    "TEST_TREATMENT_PROCEDURE",
    "ANATOMY",
    "TIME_EXPRESSION",
    "BEHAVIORAL_ENVIRONMENTAL_SOCIAL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EntityType:
    return cast(EntityType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EntityType) -> str:
    return value


def deserialize_cbor(data: str) -> EntityType:
    return cast(EntityType, data)
