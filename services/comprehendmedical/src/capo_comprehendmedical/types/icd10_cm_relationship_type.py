"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#ICD10CMRelationshipType``."""

from typing import Literal, TypeAlias, cast

ICD10CMRelationshipType: TypeAlias = Literal[
    "OVERLAP",
    "SYSTEM_ORGAN_SITE",
    "QUALITY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ICD10CMRelationshipType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ICD10CMRelationshipType:
    return cast(ICD10CMRelationshipType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ICD10CMRelationshipType) -> str:
    return value


def deserialize_cbor(data: str) -> ICD10CMRelationshipType:
    return cast(ICD10CMRelationshipType, data)
