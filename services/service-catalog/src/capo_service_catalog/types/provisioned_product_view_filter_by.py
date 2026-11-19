"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisionedProductViewFilterBy``."""

from typing import Literal, TypeAlias, cast

ProvisionedProductViewFilterBy: TypeAlias = Literal["SearchQuery",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisionedProductViewFilterBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProvisionedProductViewFilterBy:
    return cast(ProvisionedProductViewFilterBy, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProvisionedProductViewFilterBy) -> str:
    return value


def deserialize_cbor(data: str) -> ProvisionedProductViewFilterBy:
    return cast(ProvisionedProductViewFilterBy, data)
