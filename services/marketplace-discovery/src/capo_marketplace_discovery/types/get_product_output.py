"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#GetProductOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.catalog
    import capo_marketplace_discovery.types.category_list
    import capo_marketplace_discovery.types.deployed_on_aws_status
    import capo_marketplace_discovery.types.fulfillment_option_summary_list
    import capo_marketplace_discovery.types.highlight_list
    import capo_marketplace_discovery.types.listing_id
    import capo_marketplace_discovery.types.locale
    import capo_marketplace_discovery.types.non_empty_string
    import capo_marketplace_discovery.types.product_id
    import capo_marketplace_discovery.types.promotional_media_list
    import capo_marketplace_discovery.types.resource_list
    import capo_marketplace_discovery.types.seller_engagement_list
    import capo_marketplace_discovery.types.seller_information
    import capo_marketplace_discovery.types.url


class GetProductOutput(TypedDict, closed=True):
    locale: NotRequired["capo_marketplace_discovery.types.locale.Locale"]
    """<p>The locale of the returned content. Indicates whether the response contains content in the requested locale, or fell back to the default locale. See <code>Locale</code> for details.</p>"""
    product_id: "capo_marketplace_discovery.types.product_id.ProductId"
    """<p>The unique identifier of the product.</p>"""
    catalog: "capo_marketplace_discovery.types.catalog.Catalog"
    """<p>The name of the catalog that the product belongs to.</p>"""
    product_name: "capo_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The human-readable display name of the product.</p>"""
    manufacturer: (
        "capo_marketplace_discovery.types.seller_information.SellerInformation"
    )
    """<p>The entity who manufactured the product.</p>"""
    deployed_on_aws: (
        "capo_marketplace_discovery.types.deployed_on_aws_status.DeployedOnAwsStatus"
    )
    """<p>Indicates whether the product is deployed on AWS infrastructure.</p>"""
    short_description: (
        "capo_marketplace_discovery.types.non_empty_string.NonEmptyString"
    )
    """<p>A 1–3 sentence summary describing the key aspects of the product.</p>"""
    long_description: "capo_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>A detailed description of what the product does, in paragraph format.</p>"""
    logo_thumbnail_url: "capo_marketplace_discovery.types.url.URL"
    """<p>The URL of the logo thumbnail image for the product.</p>"""
    fulfillment_option_summaries: "capo_marketplace_discovery.types.fulfillment_option_summary_list.FulfillmentOptionSummaryList"
    """<p>A summary of fulfillment options available for deploying or accessing the product, such as AMI, SaaS, or Container.</p>"""
    categories: "capo_marketplace_discovery.types.category_list.CategoryList"
    """<p>The categories used to classify this product into logical groups.</p>"""
    highlights: "capo_marketplace_discovery.types.highlight_list.HighlightList"
    """<p>A list of key features that the product offers to customers.</p>"""
    promotional_media: (
        "capo_marketplace_discovery.types.promotional_media_list.PromotionalMediaList"
    )
    """<p>Embedded promotional media provided by the creator of the product, such as images and videos.</p>"""
    resources: "capo_marketplace_discovery.types.resource_list.ResourceList"
    """<p>Resources that provide further information about using the product or requesting support, such as documentation links, support contacts, and usage instructions.</p>"""
    seller_engagements: (
        "capo_marketplace_discovery.types.seller_engagement_list.SellerEngagementList"
    )
    """<p>Engagement options available to potential buyers, such as requesting a private offer or requesting a demo.</p>"""
    listing_id: "capo_marketplace_discovery.types.listing_id.ListingId"
    """<p>The default listing identifier associated with the product.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProductOutput) -> dict:
    out: dict = {}
    if "locale" in value:
        out["locale"] = value["locale"]
    out["productId"] = value["product_id"]
    out["catalog"] = value["catalog"]
    out["productName"] = value["product_name"]
    import capo_marketplace_discovery.types.seller_information

    out["manufacturer"] = (
        capo_marketplace_discovery.types.seller_information.serialize_json(
            value["manufacturer"]
        )
    )
    import capo_marketplace_discovery.types.deployed_on_aws_status

    out["deployedOnAws"] = (
        capo_marketplace_discovery.types.deployed_on_aws_status.serialize_json(
            value["deployed_on_aws"]
        )
    )
    out["shortDescription"] = value["short_description"]
    out["longDescription"] = value["long_description"]
    out["logoThumbnailUrl"] = value["logo_thumbnail_url"]
    import capo_marketplace_discovery.types.fulfillment_option_summary_list

    out["fulfillmentOptionSummaries"] = (
        capo_marketplace_discovery.types.fulfillment_option_summary_list.serialize_json(
            value["fulfillment_option_summaries"]
        )
    )
    import capo_marketplace_discovery.types.category_list

    out["categories"] = capo_marketplace_discovery.types.category_list.serialize_json(
        value["categories"]
    )
    import capo_marketplace_discovery.types.highlight_list

    out["highlights"] = capo_marketplace_discovery.types.highlight_list.serialize_json(
        value["highlights"]
    )
    import capo_marketplace_discovery.types.promotional_media_list

    out["promotionalMedia"] = (
        capo_marketplace_discovery.types.promotional_media_list.serialize_json(
            value["promotional_media"]
        )
    )
    import capo_marketplace_discovery.types.resource_list

    out["resources"] = capo_marketplace_discovery.types.resource_list.serialize_json(
        value["resources"]
    )
    import capo_marketplace_discovery.types.seller_engagement_list

    out["sellerEngagements"] = (
        capo_marketplace_discovery.types.seller_engagement_list.serialize_json(
            value["seller_engagements"]
        )
    )
    out["listingId"] = value["listing_id"]
    return out


def deserialize_json(data: dict) -> GetProductOutput:
    out: GetProductOutput = {}  # type: ignore[typeddict-item]
    if data.get("locale") is not None:
        out["locale"] = data["locale"]
    if data.get("productId") is not None:
        out["product_id"] = data["productId"]
    else:
        out["product_id"] = ""
    if data.get("catalog") is not None:
        out["catalog"] = data["catalog"]
    else:
        out["catalog"] = ""
    if data.get("productName") is not None:
        out["product_name"] = data["productName"]
    else:
        out["product_name"] = ""
    if data.get("manufacturer") is not None:
        import capo_marketplace_discovery.types.seller_information

        out["manufacturer"] = (
            capo_marketplace_discovery.types.seller_information.deserialize_json(
                data["manufacturer"]
            )
        )
    else:
        raise DeserializationError("GetProductOutput.manufacturer required")
    if data.get("deployedOnAws") is not None:
        import capo_marketplace_discovery.types.deployed_on_aws_status

        out["deployed_on_aws"] = (
            capo_marketplace_discovery.types.deployed_on_aws_status.deserialize_json(
                data["deployedOnAws"]
            )
        )
    else:
        import typing

        out["deployed_on_aws"] = typing.cast(
            "capo_marketplace_discovery.types.deployed_on_aws_status.DeployedOnAwsStatus",
            "",
        )
    if data.get("shortDescription") is not None:
        out["short_description"] = data["shortDescription"]
    else:
        out["short_description"] = ""
    if data.get("longDescription") is not None:
        out["long_description"] = data["longDescription"]
    else:
        out["long_description"] = ""
    if data.get("logoThumbnailUrl") is not None:
        out["logo_thumbnail_url"] = data["logoThumbnailUrl"]
    else:
        out["logo_thumbnail_url"] = ""
    if data.get("fulfillmentOptionSummaries") is not None:
        import capo_marketplace_discovery.types.fulfillment_option_summary_list

        out["fulfillment_option_summaries"] = (
            capo_marketplace_discovery.types.fulfillment_option_summary_list.deserialize_json(
                data["fulfillmentOptionSummaries"]
            )
        )
    else:
        out["fulfillment_option_summaries"] = []
    if data.get("categories") is not None:
        import capo_marketplace_discovery.types.category_list

        out["categories"] = (
            capo_marketplace_discovery.types.category_list.deserialize_json(
                data["categories"]
            )
        )
    else:
        out["categories"] = []
    if data.get("highlights") is not None:
        import capo_marketplace_discovery.types.highlight_list

        out["highlights"] = (
            capo_marketplace_discovery.types.highlight_list.deserialize_json(
                data["highlights"]
            )
        )
    else:
        out["highlights"] = []
    if data.get("promotionalMedia") is not None:
        import capo_marketplace_discovery.types.promotional_media_list

        out["promotional_media"] = (
            capo_marketplace_discovery.types.promotional_media_list.deserialize_json(
                data["promotionalMedia"]
            )
        )
    else:
        out["promotional_media"] = []
    if data.get("resources") is not None:
        import capo_marketplace_discovery.types.resource_list

        out["resources"] = (
            capo_marketplace_discovery.types.resource_list.deserialize_json(
                data["resources"]
            )
        )
    else:
        out["resources"] = []
    if data.get("sellerEngagements") is not None:
        import capo_marketplace_discovery.types.seller_engagement_list

        out["seller_engagements"] = (
            capo_marketplace_discovery.types.seller_engagement_list.deserialize_json(
                data["sellerEngagements"]
            )
        )
    else:
        out["seller_engagements"] = []
    if data.get("listingId") is not None:
        out["listing_id"] = data["listingId"]
    else:
        out["listing_id"] = ""
    return out
