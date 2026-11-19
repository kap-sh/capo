"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#ICD10CMAttributeType``."""

from typing import Literal, TypeAlias, cast

ICD10CMAttributeType: TypeAlias = Literal[
    "ACUITY",
    "DIRECTION",
    "SYSTEM_ORGAN_SITE",
    "QUALITY",
    "QUANTITY",
    "TIME_TO_DX_NAME",
    "TIME_EXPRESSION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ICD10CMAttributeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ICD10CMAttributeType:
    return cast(ICD10CMAttributeType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ICD10CMAttributeType) -> str:
    return value


def deserialize_cbor(data: str) -> ICD10CMAttributeType:
    return cast(ICD10CMAttributeType, data)
