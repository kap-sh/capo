"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProductViewSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.product_view_summary

ProductViewSummaries: TypeAlias = list[
    "capo_service_catalog.types.product_view_summary.ProductViewSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductViewSummaries) -> list:
    import capo_service_catalog.types.product_view_summary

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.product_view_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProductViewSummaries:
    import capo_service_catalog.types.product_view_summary

    out: ProductViewSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_service_catalog.types.product_view_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProductViewSummaries) -> list:
    import capo_service_catalog.types.product_view_summary

    out: list = []
    for item in value:
        out.append(capo_service_catalog.types.product_view_summary.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ProductViewSummaries:
    import capo_service_catalog.types.product_view_summary

    out: ProductViewSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_service_catalog.types.product_view_summary.deserialize_cbor(item)
        )
    return out
