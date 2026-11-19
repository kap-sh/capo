"""Generated from Smithy shape ``com.amazonaws.servicecatalog#AcceptPortfolioShareOutput``."""

from typing_extensions import TypedDict


class AcceptPortfolioShareOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcceptPortfolioShareOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> AcceptPortfolioShareOutput:
    out: AcceptPortfolioShareOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AcceptPortfolioShareOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> AcceptPortfolioShareOutput:
    out: AcceptPortfolioShareOutput = {}  # type: ignore[typeddict-item]
    return out
