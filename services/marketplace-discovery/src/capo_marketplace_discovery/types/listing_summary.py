"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ListingSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.catalog
    import capo_marketplace_discovery.types.category_list
    import capo_marketplace_discovery.types.fulfillment_option_summary_list
    import capo_marketplace_discovery.types.listing_badge_list
    import capo_marketplace_discovery.types.listing_id
    import capo_marketplace_discovery.types.listing_summary_associated_entity_list
    import capo_marketplace_discovery.types.non_empty_string
    import capo_marketplace_discovery.types.pricing_model_list
    import capo_marketplace_discovery.types.pricing_unit_list
    import capo_marketplace_discovery.types.review_summary
    import capo_marketplace_discovery.types.seller_information
    import capo_marketplace_discovery.types.url


class ListingSummary(TypedDict, closed=True):
    listing_id: "capo_marketplace_discovery.types.listing_id.ListingId"
    """<p>The unique identifier of the listing.</p>"""
    listing_name: "capo_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The human-readable display name of the listing.</p>"""
    publisher: "capo_marketplace_discovery.types.seller_information.SellerInformation"
    """<p>The entity who created and published the listing.</p>"""
    fulfillment_option_summaries: "capo_marketplace_discovery.types.fulfillment_option_summary_list.FulfillmentOptionSummaryList"
    """<p>A summary of fulfillment options available for the listing.</p>"""
    catalog: "capo_marketplace_discovery.types.catalog.Catalog"
    """<p>The name of the catalog that the listing belongs to.</p>"""
    short_description: (
        "capo_marketplace_discovery.types.non_empty_string.NonEmptyString"
    )
    """<p>A 1–3 sentence summary describing the key aspects of the listing.</p>"""
    logo_thumbnail_url: "capo_marketplace_discovery.types.url.URL"
    """<p>The URL of the logo thumbnail image for the listing.</p>"""
    categories: "capo_marketplace_discovery.types.category_list.CategoryList"
    """<p>The categories used to classify this listing into logical groups.</p>"""
    badges: "capo_marketplace_discovery.types.listing_badge_list.ListingBadgeList"
    """<p>Badges indicating special attributes of the listing.</p>"""
    review_summary: "capo_marketplace_discovery.types.review_summary.ReviewSummary"
    """<p>A summary of customer reviews for the listing.</p>"""
    pricing_models: (
        "capo_marketplace_discovery.types.pricing_model_list.PricingModelList"
    )
    """<p>The pricing models for offers associated with this listing.</p>"""
    pricing_units: "capo_marketplace_discovery.types.pricing_unit_list.PricingUnitList"
    """<p>The pricing units that define the billing dimensions for offers associated with this listing.</p>"""
    associated_entities: "capo_marketplace_discovery.types.listing_summary_associated_entity_list.ListingSummaryAssociatedEntityList"
    """<p>The products associated with this listing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListingSummary) -> dict:
    out: dict = {}
    out["listingId"] = value["listing_id"]
    out["listingName"] = value["listing_name"]
    import capo_marketplace_discovery.types.seller_information

    out["publisher"] = (
        capo_marketplace_discovery.types.seller_information.serialize_json(
            value["publisher"]
        )
    )
    import capo_marketplace_discovery.types.fulfillment_option_summary_list

    out["fulfillmentOptionSummaries"] = (
        capo_marketplace_discovery.types.fulfillment_option_summary_list.serialize_json(
            value["fulfillment_option_summaries"]
        )
    )
    out["catalog"] = value["catalog"]
    out["shortDescription"] = value["short_description"]
    out["logoThumbnailUrl"] = value["logo_thumbnail_url"]
    import capo_marketplace_discovery.types.category_list

    out["categories"] = capo_marketplace_discovery.types.category_list.serialize_json(
        value["categories"]
    )
    import capo_marketplace_discovery.types.listing_badge_list

    out["badges"] = capo_marketplace_discovery.types.listing_badge_list.serialize_json(
        value["badges"]
    )
    import capo_marketplace_discovery.types.review_summary

    out["reviewSummary"] = (
        capo_marketplace_discovery.types.review_summary.serialize_json(
            value["review_summary"]
        )
    )
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
    import capo_marketplace_discovery.types.listing_summary_associated_entity_list

    out["associatedEntities"] = (
        capo_marketplace_discovery.types.listing_summary_associated_entity_list.serialize_json(
            value["associated_entities"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListingSummary:
    out: ListingSummary = {}  # type: ignore[typeddict-item]
    if data.get("listingId") is not None:
        out["listing_id"] = data["listingId"]
    else:
        out["listing_id"] = ""
    if data.get("listingName") is not None:
        out["listing_name"] = data["listingName"]
    else:
        out["listing_name"] = ""
    if data.get("publisher") is not None:
        import capo_marketplace_discovery.types.seller_information

        out["publisher"] = (
            capo_marketplace_discovery.types.seller_information.deserialize_json(
                data["publisher"]
            )
        )
    else:
        raise DeserializationError("ListingSummary.publisher required")
    if data.get("fulfillmentOptionSummaries") is not None:
        import capo_marketplace_discovery.types.fulfillment_option_summary_list

        out["fulfillment_option_summaries"] = (
            capo_marketplace_discovery.types.fulfillment_option_summary_list.deserialize_json(
                data["fulfillmentOptionSummaries"]
            )
        )
    else:
        out["fulfillment_option_summaries"] = []
    if data.get("catalog") is not None:
        out["catalog"] = data["catalog"]
    else:
        out["catalog"] = ""
    if data.get("shortDescription") is not None:
        out["short_description"] = data["shortDescription"]
    else:
        out["short_description"] = ""
    if data.get("logoThumbnailUrl") is not None:
        out["logo_thumbnail_url"] = data["logoThumbnailUrl"]
    else:
        out["logo_thumbnail_url"] = ""
    if data.get("categories") is not None:
        import capo_marketplace_discovery.types.category_list

        out["categories"] = (
            capo_marketplace_discovery.types.category_list.deserialize_json(
                data["categories"]
            )
        )
    else:
        out["categories"] = []
    if data.get("badges") is not None:
        import capo_marketplace_discovery.types.listing_badge_list

        out["badges"] = (
            capo_marketplace_discovery.types.listing_badge_list.deserialize_json(
                data["badges"]
            )
        )
    else:
        out["badges"] = []
    if data.get("reviewSummary") is not None:
        import capo_marketplace_discovery.types.review_summary

        out["review_summary"] = (
            capo_marketplace_discovery.types.review_summary.deserialize_json(
                data["reviewSummary"]
            )
        )
    else:
        raise DeserializationError("ListingSummary.review_summary required")
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
    if data.get("associatedEntities") is not None:
        import capo_marketplace_discovery.types.listing_summary_associated_entity_list

        out["associated_entities"] = (
            capo_marketplace_discovery.types.listing_summary_associated_entity_list.deserialize_json(
                data["associatedEntities"]
            )
        )
    else:
        out["associated_entities"] = []
    return out
