"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DisassociateBudgetFromResourceOutput``."""

from typing_extensions import TypedDict


class DisassociateBudgetFromResourceOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateBudgetFromResourceOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateBudgetFromResourceOutput:
    out: DisassociateBudgetFromResourceOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DisassociateBudgetFromResourceOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DisassociateBudgetFromResourceOutput:
    out: DisassociateBudgetFromResourceOutput = {}  # type: ignore[typeddict-item]
    return out
