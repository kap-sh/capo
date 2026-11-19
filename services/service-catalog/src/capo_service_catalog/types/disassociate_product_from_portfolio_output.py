"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DisassociateProductFromPortfolioOutput``."""

from typing_extensions import TypedDict


class DisassociateProductFromPortfolioOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateProductFromPortfolioOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateProductFromPortfolioOutput:
    out: DisassociateProductFromPortfolioOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DisassociateProductFromPortfolioOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DisassociateProductFromPortfolioOutput:
    out: DisassociateProductFromPortfolioOutput = {}  # type: ignore[typeddict-item]
    return out
