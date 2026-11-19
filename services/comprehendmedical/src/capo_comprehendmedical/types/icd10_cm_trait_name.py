"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#ICD10CMTraitName``."""

from typing import Literal, TypeAlias, cast

ICD10CMTraitName: TypeAlias = Literal[
    "NEGATION",
    "DIAGNOSIS",
    "SIGN",
    "SYMPTOM",
    "PERTAINS_TO_FAMILY",
    "HYPOTHETICAL",
    "LOW_CONFIDENCE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ICD10CMTraitName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ICD10CMTraitName:
    return cast(ICD10CMTraitName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ICD10CMTraitName) -> str:
    return value


def deserialize_cbor(data: str) -> ICD10CMTraitName:
    return cast(ICD10CMTraitName, data)
