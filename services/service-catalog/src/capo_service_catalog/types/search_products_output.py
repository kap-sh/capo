"""Generated from Smithy shape ``com.amazonaws.servicecatalog#SearchProductsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.page_token
    import capo_service_catalog.types.product_view_aggregations
    import capo_service_catalog.types.product_view_summaries


class SearchProductsOutput(TypedDict, closed=True):
    product_view_summaries: NotRequired[
        "capo_service_catalog.types.product_view_summaries.ProductViewSummaries"
    ]
    """<p>Information about the product views.</p>"""
    product_view_aggregations: NotRequired[
        "capo_service_catalog.types.product_view_aggregations.ProductViewAggregations"
    ]
    """<p>The product view aggregations.</p>"""
    next_page_token: NotRequired["capo_service_catalog.types.page_token.PageToken"]
    """<p>The page token to use to retrieve the next set of results. If there are no additional results, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchProductsOutput) -> dict:
    out: dict = {}
    if "product_view_summaries" in value:
        import capo_service_catalog.types.product_view_summaries

        out["ProductViewSummaries"] = (
            capo_service_catalog.types.product_view_summaries.serialize_aws_json_1_1(
                value["product_view_summaries"]
            )
        )
    if "product_view_aggregations" in value:
        import capo_service_catalog.types.product_view_aggregations

        out["ProductViewAggregations"] = (
            capo_service_catalog.types.product_view_aggregations.serialize_aws_json_1_1(
                value["product_view_aggregations"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchProductsOutput:
    out: SearchProductsOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProductViewSummaries") is not None:
        import capo_service_catalog.types.product_view_summaries

        out["product_view_summaries"] = (
            capo_service_catalog.types.product_view_summaries.deserialize_aws_json_1_1(
                data["ProductViewSummaries"]
            )
        )
    if data.get("ProductViewAggregations") is not None:
        import capo_service_catalog.types.product_view_aggregations

        out["product_view_aggregations"] = (
            capo_service_catalog.types.product_view_aggregations.deserialize_aws_json_1_1(
                data["ProductViewAggregations"]
            )
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SearchProductsOutput) -> dict:
    out: dict = {}
    if "product_view_summaries" in value:
        import capo_service_catalog.types.product_view_summaries

        out["ProductViewSummaries"] = (
            capo_service_catalog.types.product_view_summaries.serialize_cbor(
                value["product_view_summaries"]
            )
        )
    if "product_view_aggregations" in value:
        import capo_service_catalog.types.product_view_aggregations

        out["ProductViewAggregations"] = (
            capo_service_catalog.types.product_view_aggregations.serialize_cbor(
                value["product_view_aggregations"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_cbor(data: dict) -> SearchProductsOutput:
    out: SearchProductsOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProductViewSummaries") is not None:
        import capo_service_catalog.types.product_view_summaries

        out["product_view_summaries"] = (
            capo_service_catalog.types.product_view_summaries.deserialize_cbor(
                data["ProductViewSummaries"]
            )
        )
    if data.get("ProductViewAggregations") is not None:
        import capo_service_catalog.types.product_view_aggregations

        out["product_view_aggregations"] = (
            capo_service_catalog.types.product_view_aggregations.deserialize_cbor(
                data["ProductViewAggregations"]
            )
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out
