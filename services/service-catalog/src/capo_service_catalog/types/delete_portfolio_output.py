"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DeletePortfolioOutput``."""

from typing_extensions import TypedDict


class DeletePortfolioOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletePortfolioOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeletePortfolioOutput:
    out: DeletePortfolioOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeletePortfolioOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeletePortfolioOutput:
    out: DeletePortfolioOutput = {}  # type: ignore[typeddict-item]
    return out
