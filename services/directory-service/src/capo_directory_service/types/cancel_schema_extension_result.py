"""Generated from Smithy shape ``com.amazonaws.directoryservice#CancelSchemaExtensionResult``."""

from typing_extensions import TypedDict


class CancelSchemaExtensionResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelSchemaExtensionResult) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelSchemaExtensionResult:
    out: CancelSchemaExtensionResult = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CancelSchemaExtensionResult) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> CancelSchemaExtensionResult:
    out: CancelSchemaExtensionResult = {}  # type: ignore[typeddict-item]
    return out
