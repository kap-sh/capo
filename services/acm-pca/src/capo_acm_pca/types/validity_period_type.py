"""Generated from Smithy shape ``com.amazonaws.acmpca#ValidityPeriodType``."""

from typing import Literal, TypeAlias, cast

ValidityPeriodType: TypeAlias = Literal[
    "END_DATE",
    "ABSOLUTE",
    "DAYS",
    "MONTHS",
    "YEARS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidityPeriodType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ValidityPeriodType:
    return cast(ValidityPeriodType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ValidityPeriodType) -> str:
    return value


def deserialize_cbor(data: str) -> ValidityPeriodType:
    return cast(ValidityPeriodType, data)
