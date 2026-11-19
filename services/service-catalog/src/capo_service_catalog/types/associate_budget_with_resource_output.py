"""Generated from Smithy shape ``com.amazonaws.servicecatalog#AssociateBudgetWithResourceOutput``."""

from typing_extensions import TypedDict


class AssociateBudgetWithResourceOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateBudgetWithResourceOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateBudgetWithResourceOutput:
    out: AssociateBudgetWithResourceOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AssociateBudgetWithResourceOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> AssociateBudgetWithResourceOutput:
    out: AssociateBudgetWithResourceOutput = {}  # type: ignore[typeddict-item]
    return out
