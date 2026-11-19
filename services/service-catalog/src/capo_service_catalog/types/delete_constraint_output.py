"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DeleteConstraintOutput``."""

from typing_extensions import TypedDict


class DeleteConstraintOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteConstraintOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteConstraintOutput:
    out: DeleteConstraintOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteConstraintOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteConstraintOutput:
    out: DeleteConstraintOutput = {}  # type: ignore[typeddict-item]
    return out
