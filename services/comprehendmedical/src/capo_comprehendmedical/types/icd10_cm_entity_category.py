"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#ICD10CMEntityCategory``."""

from typing import Literal, TypeAlias, cast

ICD10CMEntityCategory: TypeAlias = Literal["MEDICAL_CONDITION",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ICD10CMEntityCategory) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ICD10CMEntityCategory:
    return cast(ICD10CMEntityCategory, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ICD10CMEntityCategory) -> str:
    return value


def deserialize_cbor(data: str) -> ICD10CMEntityCategory:
    return cast(ICD10CMEntityCategory, data)
