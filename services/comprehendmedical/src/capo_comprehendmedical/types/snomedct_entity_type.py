"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#SNOMEDCTEntityType``."""

from typing import Literal, TypeAlias, cast

SNOMEDCTEntityType: TypeAlias = Literal[
    "DX_NAME",
    "TEST_NAME",
    "PROCEDURE_NAME",
    "TREATMENT_NAME",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SNOMEDCTEntityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SNOMEDCTEntityType:
    return cast(SNOMEDCTEntityType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SNOMEDCTEntityType) -> str:
    return value


def deserialize_cbor(data: str) -> SNOMEDCTEntityType:
    return cast(SNOMEDCTEntityType, data)
