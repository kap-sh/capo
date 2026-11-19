"""Generated from Smithy shape ``com.amazonaws.transcribe#MedicalScribeNoteTemplate``."""

from typing import Literal, TypeAlias, cast

MedicalScribeNoteTemplate: TypeAlias = Literal[
    "HISTORY_AND_PHYSICAL",
    "GIRPP",
    "BIRP",
    "SIRP",
    "DAP",
    "BEHAVIORAL_SOAP",
    "PHYSICAL_SOAP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MedicalScribeNoteTemplate) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MedicalScribeNoteTemplate:
    return cast(MedicalScribeNoteTemplate, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MedicalScribeNoteTemplate) -> str:
    return value


def deserialize_cbor(data: str) -> MedicalScribeNoteTemplate:
    return cast(MedicalScribeNoteTemplate, data)
