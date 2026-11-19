"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#UpdatePurchaseOrdersOutput``."""

from typing_extensions import TypedDict


class UpdatePurchaseOrdersOutput(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdatePurchaseOrdersOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdatePurchaseOrdersOutput:
    out: UpdatePurchaseOrdersOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdatePurchaseOrdersOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> UpdatePurchaseOrdersOutput:
    out: UpdatePurchaseOrdersOutput = {}  # type: ignore[typeddict-item]
    return out
