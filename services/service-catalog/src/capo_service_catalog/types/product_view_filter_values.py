"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProductViewFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.product_view_filter_value

ProductViewFilterValues: TypeAlias = list[
    "capo_service_catalog.types.product_view_filter_value.ProductViewFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductViewFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ProductViewFilterValues:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProductViewFilterValues) -> list:
    return list(value)


def deserialize_cbor(data: list) -> ProductViewFilterValues:
    return [item for item in data if item is not None]
