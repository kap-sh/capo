"""Generated from Smithy shape ``com.amazonaws.servicecatalog#AssociateTagOptionWithResourceOutput``."""

from typing_extensions import TypedDict


class AssociateTagOptionWithResourceOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateTagOptionWithResourceOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateTagOptionWithResourceOutput:
    out: AssociateTagOptionWithResourceOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AssociateTagOptionWithResourceOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> AssociateTagOptionWithResourceOutput:
    out: AssociateTagOptionWithResourceOutput = {}  # type: ignore[typeddict-item]
    return out
