"""Generated from Smithy shape ``com.amazonaws.transcribe#MedicalScribeLanguageCode``."""

from typing import Literal, TypeAlias, cast

MedicalScribeLanguageCode: TypeAlias = Literal["en-US",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MedicalScribeLanguageCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MedicalScribeLanguageCode:
    return cast(MedicalScribeLanguageCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MedicalScribeLanguageCode) -> str:
    return value


def deserialize_cbor(data: str) -> MedicalScribeLanguageCode:
    return cast(MedicalScribeLanguageCode, data)
