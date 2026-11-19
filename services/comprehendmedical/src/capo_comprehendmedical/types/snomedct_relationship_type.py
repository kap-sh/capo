"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#SNOMEDCTRelationshipType``."""

from typing import Literal, TypeAlias, cast

SNOMEDCTRelationshipType: TypeAlias = Literal[
    "ACUITY",
    "QUALITY",
    "TEST_VALUE",
    "TEST_UNITS",
    "DIRECTION",
    "SYSTEM_ORGAN_SITE",
    "TEST_UNIT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SNOMEDCTRelationshipType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SNOMEDCTRelationshipType:
    return cast(SNOMEDCTRelationshipType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SNOMEDCTRelationshipType) -> str:
    return value


def deserialize_cbor(data: str) -> SNOMEDCTRelationshipType:
    return cast(SNOMEDCTRelationshipType, data)
