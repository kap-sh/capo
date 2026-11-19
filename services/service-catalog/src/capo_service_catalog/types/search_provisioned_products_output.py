"""Generated from Smithy shape ``com.amazonaws.servicecatalog#SearchProvisionedProductsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.page_token
    import capo_service_catalog.types.provisioned_product_attributes
    import capo_service_catalog.types.total_results_count


class SearchProvisionedProductsOutput(TypedDict, closed=True):
    provisioned_products: NotRequired[
        "capo_service_catalog.types.provisioned_product_attributes.ProvisionedProductAttributes"
    ]
    """<p>Information about the provisioned products.</p>"""
    total_results_count: (
        "capo_service_catalog.types.total_results_count.TotalResultsCount"
    )
    """<p>The number of provisioned products found.</p>"""
    next_page_token: NotRequired["capo_service_catalog.types.page_token.PageToken"]
    """<p>The page token to use to retrieve the next set of results. If there are no additional results, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchProvisionedProductsOutput) -> dict:
    out: dict = {}
    if "provisioned_products" in value:
        import capo_service_catalog.types.provisioned_product_attributes

        out["ProvisionedProducts"] = (
            capo_service_catalog.types.provisioned_product_attributes.serialize_aws_json_1_1(
                value["provisioned_products"]
            )
        )
    out["TotalResultsCount"] = value.get("total_results_count", 0)
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchProvisionedProductsOutput:
    out: SearchProvisionedProductsOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProvisionedProducts") is not None:
        import capo_service_catalog.types.provisioned_product_attributes

        out["provisioned_products"] = (
            capo_service_catalog.types.provisioned_product_attributes.deserialize_aws_json_1_1(
                data["ProvisionedProducts"]
            )
        )
    if data.get("TotalResultsCount") is not None:
        out["total_results_count"] = data["TotalResultsCount"]
    else:
        out["total_results_count"] = 0
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SearchProvisionedProductsOutput) -> dict:
    out: dict = {}
    if "provisioned_products" in value:
        import capo_service_catalog.types.provisioned_product_attributes

        out["ProvisionedProducts"] = (
            capo_service_catalog.types.provisioned_product_attributes.serialize_cbor(
                value["provisioned_products"]
            )
        )
    out["TotalResultsCount"] = value.get("total_results_count", 0)
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_cbor(data: dict) -> SearchProvisionedProductsOutput:
    out: SearchProvisionedProductsOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProvisionedProducts") is not None:
        import capo_service_catalog.types.provisioned_product_attributes

        out["provisioned_products"] = (
            capo_service_catalog.types.provisioned_product_attributes.deserialize_cbor(
                data["ProvisionedProducts"]
            )
        )
    if data.get("TotalResultsCount") is not None:
        out["total_results_count"] = data["TotalResultsCount"]
    else:
        out["total_results_count"] = 0
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out
