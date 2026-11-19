"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribePortfolioShareType``."""

from typing import Literal, TypeAlias, cast

DescribePortfolioShareType: TypeAlias = Literal[
    "ACCOUNT",
    "ORGANIZATION",
    "ORGANIZATIONAL_UNIT",
    "ORGANIZATION_MEMBER_ACCOUNT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePortfolioShareType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DescribePortfolioShareType:
    return cast(DescribePortfolioShareType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribePortfolioShareType) -> str:
    return value


def deserialize_cbor(data: str) -> DescribePortfolioShareType:
    return cast(DescribePortfolioShareType, data)
