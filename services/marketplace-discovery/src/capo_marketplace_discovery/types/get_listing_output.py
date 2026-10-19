"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#GetListingOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.catalog
    import capo_marketplace_discovery.types.category_list
    import capo_marketplace_discovery.types.fulfillment_option_summary_list
    import capo_marketplace_discovery.types.highlight_list
    import capo_marketplace_discovery.types.listing_associated_entity_list
    import capo_marketplace_discovery.types.listing_badge_list
    import capo_marketplace_discovery.types.listing_id
    import capo_marketplace_discovery.types.locale
    import capo_marketplace_discovery.types.non_empty_string
    import capo_marketplace_discovery.types.nullable_string
    import capo_marketplace_discovery.types.pricing_model_list
    import capo_marketplace_discovery.types.pricing_unit_list
    import capo_marketplace_discovery.types.promotional_media_list
    import capo_marketplace_discovery.types.resource_list
    import capo_marketplace_discovery.types.review_summary
    import capo_marketplace_discovery.types.seller_engagement_list
    import capo_marketplace_discovery.types.seller_information
    import capo_marketplace_discovery.types.url
    import capo_marketplace_discovery.types.use_case_list


class GetListingOutput(TypedDict, closed=True):
    locale: NotRequired["capo_marketplace_discovery.types.locale.Locale"]
    """<p>The locale of the returned content. Indicates whether the response contains content in the requested locale, or fell back to the default locale. See <code>Locale</code> for details.</p>"""
    associated_entities: "capo_marketplace_discovery.types.listing_associated_entity_list.ListingAssociatedEntityList"
    """<p>The products and offers associated with this listing. Each entity contains product and offer information.</p>"""
    badges: "capo_marketplace_discovery.types.listing_badge_list.ListingBadgeList"
    """<p>Badges indicating special attributes of the listing, such as free tier eligibility, free trial availability, or Quick Launch support.</p>"""
    catalog: "capo_marketplace_discovery.types.catalog.Catalog"
    """<p>The name of the catalog that the listing belongs to.</p>"""
    categories: "capo_marketplace_discovery.types.category_list.CategoryList"
    """<p>The categories used to classify this listing into logical groups.</p>"""
    fulfillment_option_summaries: "capo_marketplace_discovery.types.fulfillment_option_summary_list.FulfillmentOptionSummaryList"
    """<p>A summary of fulfillment options available for deploying or accessing the listing, such as AMI, SaaS, or Container.</p>"""
    highlights: "capo_marketplace_discovery.types.highlight_list.HighlightList"
    """<p>A list of key features that the listing offers to customers.</p>"""
    integration_guide: NotRequired[
        "capo_marketplace_discovery.types.nullable_string.NullableString"
    ]
    """<p>Optional guidance explaining how to use data in this listing. Primarily defines how to integrate with a multi-product listing.</p>"""
    listing_id: "capo_marketplace_discovery.types.listing_id.ListingId"
    """<p>The unique identifier of the listing.</p>"""
    listing_name: "capo_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The human-readable display name of the listing.</p>"""
    logo_thumbnail_url: "capo_marketplace_discovery.types.url.URL"
    """<p>The URL of the logo thumbnail image for the listing.</p>"""
    long_description: "capo_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>A detailed description of what the listing offers, in paragraph format.</p>"""
    pricing_models: (
        "capo_marketplace_discovery.types.pricing_model_list.PricingModelList"
    )
    """<p>The pricing models for offers associated with this listing, such as usage-based, contract, BYOL, or free.</p>"""
    pricing_units: "capo_marketplace_discovery.types.pricing_unit_list.PricingUnitList"
    """<p>The pricing units that define the billing dimensions for offers associated with this listing, such as users, hosts, or data.</p>"""
    promotional_media: (
        "capo_marketplace_discovery.types.promotional_media_list.PromotionalMediaList"
    )
    """<p>Embedded promotional media provided by the creator of the product, such as images and videos.</p>"""
    publisher: "capo_marketplace_discovery.types.seller_information.SellerInformation"
    """<p>The entity who created and published the listing.</p>"""
    resources: "capo_marketplace_discovery.types.resource_list.ResourceList"
    """<p>Resources that provide further information about using the product or requesting support, such as documentation links, support contacts, and usage instructions.</p>"""
    review_summary: NotRequired[
        "capo_marketplace_discovery.types.review_summary.ReviewSummary"
    ]
    """<p>A summary of customer reviews available for the listing, including average rating and total review count by source.</p>"""
    seller_engagements: (
        "capo_marketplace_discovery.types.seller_engagement_list.SellerEngagementList"
    )
    """<p>Engagement options available to potential buyers, such as requesting a private offer or requesting a demo.</p>"""
    short_description: (
        "capo_marketplace_discovery.types.non_empty_string.NonEmptyString"
    )
    """<p>A 1–3 sentence summary describing the key aspects of the listing.</p>"""
    use_cases: "capo_marketplace_discovery.types.use_case_list.UseCaseList"
    """<p>Use cases associated with the listing, describing scenarios where the product can be applied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetListingOutput) -> dict:
    out: dict = {}
    if "locale" in value:
        out["locale"] = value["locale"]
    import capo_marketplace_discovery.types.listing_associated_entity_list

    out["associatedEntities"] = (
        capo_marketplace_discovery.types.listing_associated_entity_list.serialize_json(
            value["associated_entities"]
        )
    )
    import capo_marketplace_discovery.types.listing_badge_list

    out["badges"] = capo_marketplace_discovery.types.listing_badge_list.serialize_json(
        value["badges"]
    )
    out["catalog"] = value["catalog"]
    import capo_marketplace_discovery.types.category_list

    out["categories"] = capo_marketplace_discovery.types.category_list.serialize_json(
        value["categories"]
    )
    import capo_marketplace_discovery.types.fulfillment_option_summary_list

    out["fulfillmentOptionSummaries"] = (
        capo_marketplace_discovery.types.fulfillment_option_summary_list.serialize_json(
            value["fulfillment_option_summaries"]
        )
    )
    import capo_marketplace_discovery.types.highlight_list

    out["highlights"] = capo_marketplace_discovery.types.highlight_list.serialize_json(
        value["highlights"]
    )
    if "integration_guide" in value:
        out["integrationGuide"] = value["integration_guide"]
    out["listingId"] = value["listing_id"]
    out["listingName"] = value["listing_name"]
    out["logoThumbnailUrl"] = value["logo_thumbnail_url"]
    out["longDescription"] = value["long_description"]
    import capo_marketplace_discovery.types.pricing_model_list

    out["pricingModels"] = (
        capo_marketplace_discovery.types.pricing_model_list.serialize_json(
            value["pricing_models"]
        )
    )
    import capo_marketplace_discovery.types.pricing_unit_list

    out["pricingUnits"] = (
        capo_marketplace_discovery.types.pricing_unit_list.serialize_json(
            value["pricing_units"]
        )
    )
    import capo_marketplace_discovery.types.promotional_media_list

    out["promotionalMedia"] = (
        capo_marketplace_discovery.types.promotional_media_list.serialize_json(
            value["promotional_media"]
        )
    )
    import capo_marketplace_discovery.types.seller_information

    out["publisher"] = (
        capo_marketplace_discovery.types.seller_information.serialize_json(
            value["publisher"]
        )
    )
    import capo_marketplace_discovery.types.resource_list

    out["resources"] = capo_marketplace_discovery.types.resource_list.serialize_json(
        value["resources"]
    )
    if "review_summary" in value:
        import capo_marketplace_discovery.types.review_summary

        out["reviewSummary"] = (
            capo_marketplace_discovery.types.review_summary.serialize_json(
                value["review_summary"]
            )
        )
    import capo_marketplace_discovery.types.seller_engagement_list

    out["sellerEngagements"] = (
        capo_marketplace_discovery.types.seller_engagement_list.serialize_json(
            value["seller_engagements"]
        )
    )
    out["shortDescription"] = value["short_description"]
    import capo_marketplace_discovery.types.use_case_list

    out["useCases"] = capo_marketplace_discovery.types.use_case_list.serialize_json(
        value["use_cases"]
    )
    return out


def deserialize_json(data: dict) -> GetListingOutput:
    out: GetListingOutput = {}  # type: ignore[typeddict-item]
    if data.get("locale") is not None:
        out["locale"] = data["locale"]
    if data.get("associatedEntities") is not None:
        import capo_marketplace_discovery.types.listing_associated_entity_list

        out["associated_entities"] = (
            capo_marketplace_discovery.types.listing_associated_entity_list.deserialize_json(
                data["associatedEntities"]
            )
        )
    else:
        out["associated_entities"] = []
    if data.get("badges") is not None:
        import capo_marketplace_discovery.types.listing_badge_list

        out["badges"] = (
            capo_marketplace_discovery.types.listing_badge_list.deserialize_json(
                data["badges"]
            )
        )
    else:
        out["badges"] = []
    if data.get("catalog") is not None:
        out["catalog"] = data["catalog"]
    else:
        out["catalog"] = ""
    if data.get("categories") is not None:
        import capo_marketplace_discovery.types.category_list

        out["categories"] = (
            capo_marketplace_discovery.types.category_list.deserialize_json(
                data["categories"]
            )
        )
    else:
        out["categories"] = []
    if data.get("fulfillmentOptionSummaries") is not None:
        import capo_marketplace_discovery.types.fulfillment_option_summary_list

        out["fulfillment_option_summaries"] = (
            capo_marketplace_discovery.types.fulfillment_option_summary_list.deserialize_json(
                data["fulfillmentOptionSummaries"]
            )
        )
    else:
        out["fulfillment_option_summaries"] = []
    if data.get("highlights") is not None:
        import capo_marketplace_discovery.types.highlight_list

        out["highlights"] = (
            capo_marketplace_discovery.types.highlight_list.deserialize_json(
                data["highlights"]
            )
        )
    else:
        out["highlights"] = []
    if data.get("integrationGuide") is not None:
        out["integration_guide"] = data["integrationGuide"]
    if data.get("listingId") is not None:
        out["listing_id"] = data["listingId"]
    else:
        out["listing_id"] = ""
    if data.get("listingName") is not None:
        out["listing_name"] = data["listingName"]
    else:
        out["listing_name"] = ""
    if data.get("logoThumbnailUrl") is not None:
        out["logo_thumbnail_url"] = data["logoThumbnailUrl"]
    else:
        out["logo_thumbnail_url"] = ""
    if data.get("longDescription") is not None:
        out["long_description"] = data["longDescription"]
    else:
        out["long_description"] = ""
    if data.get("pricingModels") is not None:
        import capo_marketplace_discovery.types.pricing_model_list

        out["pricing_models"] = (
            capo_marketplace_discovery.types.pricing_model_list.deserialize_json(
                data["pricingModels"]
            )
        )
    else:
        out["pricing_models"] = []
    if data.get("pricingUnits") is not None:
        import capo_marketplace_discovery.types.pricing_unit_list

        out["pricing_units"] = (
            capo_marketplace_discovery.types.pricing_unit_list.deserialize_json(
                data["pricingUnits"]
            )
        )
    else:
        out["pricing_units"] = []
    if data.get("promotionalMedia") is not None:
        import capo_marketplace_discovery.types.promotional_media_list

        out["promotional_media"] = (
            capo_marketplace_discovery.types.promotional_media_list.deserialize_json(
                data["promotionalMedia"]
            )
        )
    else:
        out["promotional_media"] = []
    if data.get("publisher") is not None:
        import capo_marketplace_discovery.types.seller_information

        out["publisher"] = (
            capo_marketplace_discovery.types.seller_information.deserialize_json(
                data["publisher"]
            )
        )
    else:
        raise DeserializationError("GetListingOutput.publisher required")
    if data.get("resources") is not None:
        import capo_marketplace_discovery.types.resource_list

        out["resources"] = (
            capo_marketplace_discovery.types.resource_list.deserialize_json(
                data["resources"]
            )
        )
    else:
        out["resources"] = []
    if data.get("reviewSummary") is not None:
        import capo_marketplace_discovery.types.review_summary

        out["review_summary"] = (
            capo_marketplace_discovery.types.review_summary.deserialize_json(
                data["reviewSummary"]
            )
        )
    if data.get("sellerEngagements") is not None:
        import capo_marketplace_discovery.types.seller_engagement_list

        out["seller_engagements"] = (
            capo_marketplace_discovery.types.seller_engagement_list.deserialize_json(
                data["sellerEngagements"]
            )
        )
    else:
        out["seller_engagements"] = []
    if data.get("shortDescription") is not None:
        out["short_description"] = data["shortDescription"]
    else:
        out["short_description"] = ""
    if data.get("useCases") is not None:
        import capo_marketplace_discovery.types.use_case_list

        out["use_cases"] = (
            capo_marketplace_discovery.types.use_case_list.deserialize_json(
                data["useCases"]
            )
        )
    else:
        out["use_cases"] = []
    return out
