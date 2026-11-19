"""Generated from Smithy shape ``com.amazonaws.snowball#UpdateJobResult``."""

from typing_extensions import TypedDict


class UpdateJobResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateJobResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateJobResult:
    out: UpdateJobResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateJobResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdateJobResult:
    out: UpdateJobResult = {}  # type: ignore[typeddict-item]
    return out
