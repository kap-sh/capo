"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#ICD10CMEntityType``."""

from typing import Literal, TypeAlias, cast

ICD10CMEntityType: TypeAlias = Literal[
    "DX_NAME",
    "TIME_EXPRESSION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ICD10CMEntityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ICD10CMEntityType:
    return cast(ICD10CMEntityType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ICD10CMEntityType) -> str:
    return value


def deserialize_cbor(data: str) -> ICD10CMEntityType:
    return cast(ICD10CMEntityType, data)
