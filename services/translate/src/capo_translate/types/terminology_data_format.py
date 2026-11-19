"""Generated from Smithy shape ``com.amazonaws.translate#TerminologyDataFormat``."""

from typing import Literal, TypeAlias, cast

TerminologyDataFormat: TypeAlias = Literal[
    "CSV",
    "TMX",
    "TSV",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminologyDataFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TerminologyDataFormat:
    return cast(TerminologyDataFormat, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TerminologyDataFormat) -> str:
    return value


def deserialize_cbor(data: str) -> TerminologyDataFormat:
    return cast(TerminologyDataFormat, data)
