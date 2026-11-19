"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#SNOMEDCTTraitName``."""

from typing import Literal, TypeAlias, cast

SNOMEDCTTraitName: TypeAlias = Literal[
    "NEGATION",
    "DIAGNOSIS",
    "SIGN",
    "SYMPTOM",
    "PERTAINS_TO_FAMILY",
    "HYPOTHETICAL",
    "LOW_CONFIDENCE",
    "PAST_HISTORY",
    "FUTURE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SNOMEDCTTraitName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SNOMEDCTTraitName:
    return cast(SNOMEDCTTraitName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SNOMEDCTTraitName) -> str:
    return value


def deserialize_cbor(data: str) -> SNOMEDCTTraitName:
    return cast(SNOMEDCTTraitName, data)
