"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ScanProvisionedProductsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.page_token
    import capo_service_catalog.types.provisioned_product_details


class ScanProvisionedProductsOutput(TypedDict, closed=True):
    provisioned_products: NotRequired[
        "capo_service_catalog.types.provisioned_product_details.ProvisionedProductDetails"
    ]
    """<p>Information about the provisioned products.</p>"""
    next_page_token: NotRequired["capo_service_catalog.types.page_token.PageToken"]
    """<p>The page token to use to retrieve the next set of results. If there are no additional results, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScanProvisionedProductsOutput) -> dict:
    out: dict = {}
    if "provisioned_products" in value:
        import capo_service_catalog.types.provisioned_product_details

        out["ProvisionedProducts"] = (
            capo_service_catalog.types.provisioned_product_details.serialize_aws_json_1_1(
                value["provisioned_products"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ScanProvisionedProductsOutput:
    out: ScanProvisionedProductsOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProvisionedProducts") is not None:
        import capo_service_catalog.types.provisioned_product_details

        out["provisioned_products"] = (
            capo_service_catalog.types.provisioned_product_details.deserialize_aws_json_1_1(
                data["ProvisionedProducts"]
            )
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ScanProvisionedProductsOutput) -> dict:
    out: dict = {}
    if "provisioned_products" in value:
        import capo_service_catalog.types.provisioned_product_details

        out["ProvisionedProducts"] = (
            capo_service_catalog.types.provisioned_product_details.serialize_cbor(
                value["provisioned_products"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_cbor(data: dict) -> ScanProvisionedProductsOutput:
    out: ScanProvisionedProductsOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProvisionedProducts") is not None:
        import capo_service_catalog.types.provisioned_product_details

        out["provisioned_products"] = (
            capo_service_catalog.types.provisioned_product_details.deserialize_cbor(
                data["ProvisionedProducts"]
            )
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out
