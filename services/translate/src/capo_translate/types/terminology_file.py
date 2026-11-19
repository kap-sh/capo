"""Generated from Smithy shape ``com.amazonaws.translate#TerminologyFile``."""

import base64
from typing import TypeAlias

TerminologyFile: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminologyFile) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> TerminologyFile:
    return base64.b64decode(data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TerminologyFile) -> TerminologyFile:
    return value


def deserialize_cbor(data: TerminologyFile) -> TerminologyFile:
    return data
