"""Generated from Smithy shape ``com.amazonaws.servicecatalog#AssociateProductWithPortfolioOutput``."""

from typing_extensions import TypedDict


class AssociateProductWithPortfolioOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateProductWithPortfolioOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateProductWithPortfolioOutput:
    out: AssociateProductWithPortfolioOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AssociateProductWithPortfolioOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> AssociateProductWithPortfolioOutput:
    out: AssociateProductWithPortfolioOutput = {}  # type: ignore[typeddict-item]
    return out
