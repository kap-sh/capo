"""Generated from Smithy shape ``com.amazonaws.servicecatalog#SearchProductsAsAdminOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.page_token
    import capo_service_catalog.types.product_view_details


class SearchProductsAsAdminOutput(TypedDict, closed=True):
    product_view_details: NotRequired[
        "capo_service_catalog.types.product_view_details.ProductViewDetails"
    ]
    """<p>Information about the product views.</p>"""
    next_page_token: NotRequired["capo_service_catalog.types.page_token.PageToken"]
    """<p>The page token to use to retrieve the next set of results. If there are no additional results, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchProductsAsAdminOutput) -> dict:
    out: dict = {}
    if "product_view_details" in value:
        import capo_service_catalog.types.product_view_details

        out["ProductViewDetails"] = (
            capo_service_catalog.types.product_view_details.serialize_aws_json_1_1(
                value["product_view_details"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchProductsAsAdminOutput:
    out: SearchProductsAsAdminOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProductViewDetails") is not None:
        import capo_service_catalog.types.product_view_details

        out["product_view_details"] = (
            capo_service_catalog.types.product_view_details.deserialize_aws_json_1_1(
                data["ProductViewDetails"]
            )
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SearchProductsAsAdminOutput) -> dict:
    out: dict = {}
    if "product_view_details" in value:
        import capo_service_catalog.types.product_view_details

        out["ProductViewDetails"] = (
            capo_service_catalog.types.product_view_details.serialize_cbor(
                value["product_view_details"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_cbor(data: dict) -> SearchProductsAsAdminOutput:
    out: SearchProductsAsAdminOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProductViewDetails") is not None:
        import capo_service_catalog.types.product_view_details

        out["product_view_details"] = (
            capo_service_catalog.types.product_view_details.deserialize_cbor(
                data["ProductViewDetails"]
            )
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out
