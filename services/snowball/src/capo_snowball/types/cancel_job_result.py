"""Generated from Smithy shape ``com.amazonaws.snowball#CancelJobResult``."""

from typing_extensions import TypedDict


class CancelJobResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelJobResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelJobResult:
    out: CancelJobResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CancelJobResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> CancelJobResult:
    out: CancelJobResult = {}  # type: ignore[typeddict-item]
    return out
