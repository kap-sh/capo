"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProductType``."""

from typing import Literal, TypeAlias, cast

ProductType: TypeAlias = Literal[
    "CLOUD_FORMATION_TEMPLATE",
    "MARKETPLACE",
    "TERRAFORM_OPEN_SOURCE",
    "TERRAFORM_CLOUD",
    "EXTERNAL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProductType:
    return cast(ProductType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProductType) -> str:
    return value


def deserialize_cbor(data: str) -> ProductType:
    return cast(ProductType, data)
