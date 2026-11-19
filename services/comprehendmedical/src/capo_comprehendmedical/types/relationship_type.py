"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#RelationshipType``."""

from typing import Literal, TypeAlias, cast

RelationshipType: TypeAlias = Literal[
    "EVERY",
    "WITH_DOSAGE",
    "ADMINISTERED_VIA",
    "FOR",
    "NEGATIVE",
    "OVERLAP",
    "DOSAGE",
    "ROUTE_OR_MODE",
    "FORM",
    "FREQUENCY",
    "DURATION",
    "STRENGTH",
    "RATE",
    "ACUITY",
    "TEST_VALUE",
    "TEST_UNITS",
    "TEST_UNIT",
    "DIRECTION",
    "SYSTEM_ORGAN_SITE",
    "AMOUNT",
    "USAGE",
    "QUALITY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelationshipType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RelationshipType:
    return cast(RelationshipType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RelationshipType) -> str:
    return value


def deserialize_cbor(data: str) -> RelationshipType:
    return cast(RelationshipType, data)
