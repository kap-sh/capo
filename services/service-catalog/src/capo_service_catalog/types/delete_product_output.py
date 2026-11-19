"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DeleteProductOutput``."""

from typing_extensions import TypedDict


class DeleteProductOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteProductOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteProductOutput:
    out: DeleteProductOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteProductOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteProductOutput:
    out: DeleteProductOutput = {}  # type: ignore[typeddict-item]
    return out
