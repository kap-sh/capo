"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#LineItemGroupBy``."""

from typing import Literal, TypeAlias, cast

LineItemGroupBy: TypeAlias = Literal["INVOICE_ID",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LineItemGroupBy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LineItemGroupBy:
    return cast(LineItemGroupBy, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LineItemGroupBy) -> str:
    return value


def deserialize_cbor(data: str) -> LineItemGroupBy:
    return cast(LineItemGroupBy, data)
