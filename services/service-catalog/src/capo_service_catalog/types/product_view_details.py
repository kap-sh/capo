"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProductViewDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.product_view_detail

ProductViewDetails: TypeAlias = list[
    "capo_service_catalog.types.product_view_detail.ProductViewDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductViewDetails) -> list:
    import capo_service_catalog.types.product_view_detail

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.product_view_detail.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProductViewDetails:
    import capo_service_catalog.types.product_view_detail

    out: ProductViewDetails = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_service_catalog.types.product_view_detail.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProductViewDetails) -> list:
    import capo_service_catalog.types.product_view_detail

    out: list = []
    for item in value:
        out.append(capo_service_catalog.types.product_view_detail.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ProductViewDetails:
    import capo_service_catalog.types.product_view_detail

    out: ProductViewDetails = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_service_catalog.types.product_view_detail.deserialize_cbor(item)
        )
    return out
