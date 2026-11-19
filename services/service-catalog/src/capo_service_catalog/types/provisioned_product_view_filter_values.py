"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisionedProductViewFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.provisioned_product_view_filter_value

ProvisionedProductViewFilterValues: TypeAlias = list[
    "capo_service_catalog.types.provisioned_product_view_filter_value.ProvisionedProductViewFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisionedProductViewFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ProvisionedProductViewFilterValues:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProvisionedProductViewFilterValues) -> list:
    return list(value)


def deserialize_cbor(data: list) -> ProvisionedProductViewFilterValues:
    return [item for item in data if item is not None]
