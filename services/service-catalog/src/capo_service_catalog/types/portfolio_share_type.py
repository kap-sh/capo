"""Generated from Smithy shape ``com.amazonaws.servicecatalog#PortfolioShareType``."""

from typing import Literal, TypeAlias, cast

PortfolioShareType: TypeAlias = Literal[
    "IMPORTED",
    "AWS_SERVICECATALOG",
    "AWS_ORGANIZATIONS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PortfolioShareType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PortfolioShareType:
    return cast(PortfolioShareType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PortfolioShareType) -> str:
    return value


def deserialize_cbor(data: str) -> PortfolioShareType:
    return cast(PortfolioShareType, data)
