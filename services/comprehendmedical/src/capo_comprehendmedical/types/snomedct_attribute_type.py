"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#SNOMEDCTAttributeType``."""

from typing import Literal, TypeAlias, cast

SNOMEDCTAttributeType: TypeAlias = Literal[
    "ACUITY",
    "QUALITY",
    "DIRECTION",
    "SYSTEM_ORGAN_SITE",
    "TEST_VALUE",
    "TEST_UNIT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SNOMEDCTAttributeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SNOMEDCTAttributeType:
    return cast(SNOMEDCTAttributeType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SNOMEDCTAttributeType) -> str:
    return value


def deserialize_cbor(data: str) -> SNOMEDCTAttributeType:
    return cast(SNOMEDCTAttributeType, data)
