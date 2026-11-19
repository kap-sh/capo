"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DeleteServiceActionOutput``."""

from typing_extensions import TypedDict


class DeleteServiceActionOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteServiceActionOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteServiceActionOutput:
    out: DeleteServiceActionOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteServiceActionOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteServiceActionOutput:
    out: DeleteServiceActionOutput = {}  # type: ignore[typeddict-item]
    return out
