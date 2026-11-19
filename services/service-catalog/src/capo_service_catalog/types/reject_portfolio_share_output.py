"""Generated from Smithy shape ``com.amazonaws.servicecatalog#RejectPortfolioShareOutput``."""

from typing_extensions import TypedDict


class RejectPortfolioShareOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RejectPortfolioShareOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> RejectPortfolioShareOutput:
    out: RejectPortfolioShareOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RejectPortfolioShareOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> RejectPortfolioShareOutput:
    out: RejectPortfolioShareOutput = {}  # type: ignore[typeddict-item]
    return out
