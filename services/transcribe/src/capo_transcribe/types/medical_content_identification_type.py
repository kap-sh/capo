"""Generated from Smithy shape ``com.amazonaws.transcribe#MedicalContentIdentificationType``."""

from typing import Literal, TypeAlias, cast

MedicalContentIdentificationType: TypeAlias = Literal["PHI",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MedicalContentIdentificationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MedicalContentIdentificationType:
    return cast(MedicalContentIdentificationType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MedicalContentIdentificationType) -> str:
    return value


def deserialize_cbor(data: str) -> MedicalContentIdentificationType:
    return cast(MedicalContentIdentificationType, data)
