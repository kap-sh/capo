"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProductViewFilterBy``."""

from typing import Literal, TypeAlias, cast

ProductViewFilterBy: TypeAlias = Literal[
    "FullTextSearch",
    "Owner",
    "ProductType",
    "SourceProductId",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductViewFilterBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProductViewFilterBy:
    return cast(ProductViewFilterBy, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProductViewFilterBy) -> str:
    return value


def deserialize_cbor(data: str) -> ProductViewFilterBy:
    return cast(ProductViewFilterBy, data)
