"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#SNOMEDCTEntityCategory``."""

from typing import Literal, TypeAlias, cast

SNOMEDCTEntityCategory: TypeAlias = Literal[
    "MEDICAL_CONDITION",
    "ANATOMY",
    "TEST_TREATMENT_PROCEDURE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SNOMEDCTEntityCategory) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SNOMEDCTEntityCategory:
    return cast(SNOMEDCTEntityCategory, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SNOMEDCTEntityCategory) -> str:
    return value


def deserialize_cbor(data: str) -> SNOMEDCTEntityCategory:
    return cast(SNOMEDCTEntityCategory, data)
