"""Generated from Smithy shape ``com.amazonaws.transcribe#Pronouns``."""

from typing import Literal, TypeAlias, cast

Pronouns: TypeAlias = Literal[
    "HE_HIM",
    "SHE_HER",
    "THEY_THEM",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Pronouns) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Pronouns:
    return cast(Pronouns, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Pronouns) -> str:
    return value


def deserialize_cbor(data: str) -> Pronouns:
    return cast(Pronouns, data)
