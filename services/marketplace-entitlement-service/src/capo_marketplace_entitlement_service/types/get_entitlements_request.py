"""Generated from Smithy shape ``com.amazonaws.marketplaceentitlementservice#GetEntitlementsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_entitlement_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_entitlement_service.types.get_entitlement_filters
    import capo_marketplace_entitlement_service.types.non_empty_string
    import capo_marketplace_entitlement_service.types.page_size_integer
    import capo_marketplace_entitlement_service.types.product_code


class GetEntitlementsRequest(TypedDict, closed=True):
    product_code: "capo_marketplace_entitlement_service.types.product_code.ProductCode"
    """<p>Product code is used to uniquely identify a product in AWS Marketplace. The product code will be provided by AWS Marketplace when the product listing is created.</p>"""
    filter: NotRequired[
        "capo_marketplace_entitlement_service.types.get_entitlement_filters.GetEntitlementFilters"
    ]
    """<p>Filter is used to return entitlements for a specific customer or for a specific dimension. Filters are described as keys mapped to a lists of values. Filtered requests are <i>unioned</i> for each value in the value list, and then <i>intersected</i> for each filter key.</p> <p> <code>CustomerIdentifier</code> and <code>CustomerAWSAccountId</code> are mutually exclusive parameters. You must use one or the other, but not both in the same request. </p> <note> <p>If you're migrating an existing integration, use <a href="https://docs.aws.amazon.com/marketplace/latest/userguide/data-feed-account.html">Account Feeds</a> to map <code>CustomerIdentifier</code> to <code>CustomerAWSAccountId</code>, and <a href="https://docs.aws.amazon.com/marketplace/latest/userguide/data-feed-agreements.html">Agreements Feeds</a> to map <code>CustomerAWSAccountId</code> and <code>LicenseArn</code>.</p> </note>"""
    next_token: NotRequired[
        "capo_marketplace_entitlement_service.types.non_empty_string.NonEmptyString"
    ]
    """<p>For paginated calls to GetEntitlements, pass the NextToken from the previous GetEntitlementsResult.</p>"""
    max_results: NotRequired[
        "capo_marketplace_entitlement_service.types.page_size_integer.PageSizeInteger"
    ]
    """<p>The maximum number of items to retrieve from the GetEntitlements operation. For pagination, use the NextToken field in subsequent calls to GetEntitlements.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetEntitlementsRequest) -> dict:
    out: dict = {}
    out["ProductCode"] = value["product_code"]
    if "filter" in value:
        import capo_marketplace_entitlement_service.types.get_entitlement_filters

        out["Filter"] = (
            capo_marketplace_entitlement_service.types.get_entitlement_filters.serialize_aws_json_1_1(
                value["filter"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetEntitlementsRequest:
    out: GetEntitlementsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProductCode") is not None:
        out["product_code"] = data["ProductCode"]
    else:
        raise DeserializationError("GetEntitlementsRequest.product_code required")
    if data.get("Filter") is not None:
        import capo_marketplace_entitlement_service.types.get_entitlement_filters

        out["filter"] = (
            capo_marketplace_entitlement_service.types.get_entitlement_filters.deserialize_aws_json_1_1(
                data["Filter"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
