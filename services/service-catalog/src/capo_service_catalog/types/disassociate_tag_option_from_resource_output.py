"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DisassociateTagOptionFromResourceOutput``."""

from typing_extensions import TypedDict


class DisassociateTagOptionFromResourceOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateTagOptionFromResourceOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateTagOptionFromResourceOutput:
    out: DisassociateTagOptionFromResourceOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DisassociateTagOptionFromResourceOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DisassociateTagOptionFromResourceOutput:
    out: DisassociateTagOptionFromResourceOutput = {}  # type: ignore[typeddict-item]
    return out
