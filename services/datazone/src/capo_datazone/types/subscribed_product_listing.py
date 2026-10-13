"""Generated from Smithy shape ``com.amazonaws.datazone#SubscribedProductListing``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.asset_id
    import capo_datazone.types.asset_in_data_product_listing_items
    import capo_datazone.types.detailed_glossary_terms
    import capo_datazone.types.revision


class SubscribedProductListing(TypedDict, closed=True):
    entity_id: NotRequired["capo_datazone.types.asset_id.AssetId"]
    """<p>The ID of the data product listing.</p>"""
    entity_revision: NotRequired["capo_datazone.types.revision.Revision"]
    """<p>The revision of the data product listing.</p>"""
    glossary_terms: NotRequired[
        "capo_datazone.types.detailed_glossary_terms.DetailedGlossaryTerms"
    ]
    """<p>The glossary terms of the data product listing.</p>"""
    name: NotRequired["str"]
    """<p>The name of the data product listing.</p>"""
    description: NotRequired["str"]
    """<p>The description of the data product listing.</p>"""
    asset_listings: NotRequired[
        "capo_datazone.types.asset_in_data_product_listing_items.AssetInDataProductListingItems"
    ]
    """<p>The data assets of the data product listing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscribedProductListing) -> dict:
    out: dict = {}
    if "entity_id" in value:
        out["entityId"] = value["entity_id"]
    if "entity_revision" in value:
        out["entityRevision"] = value["entity_revision"]
    if "glossary_terms" in value:
        import capo_datazone.types.detailed_glossary_terms

        out["glossaryTerms"] = (
            capo_datazone.types.detailed_glossary_terms.serialize_json(
                value["glossary_terms"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "asset_listings" in value:
        import capo_datazone.types.asset_in_data_product_listing_items

        out["assetListings"] = (
            capo_datazone.types.asset_in_data_product_listing_items.serialize_json(
                value["asset_listings"]
            )
        )
    return out


def deserialize_json(data: dict) -> SubscribedProductListing:
    out: SubscribedProductListing = {}  # type: ignore[typeddict-item]
    if data.get("entityId") is not None:
        out["entity_id"] = data["entityId"]
    if data.get("entityRevision") is not None:
        out["entity_revision"] = data["entityRevision"]
    if data.get("glossaryTerms") is not None:
        import capo_datazone.types.detailed_glossary_terms

        out["glossary_terms"] = (
            capo_datazone.types.detailed_glossary_terms.deserialize_json(
                data["glossaryTerms"]
            )
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("assetListings") is not None:
        import capo_datazone.types.asset_in_data_product_listing_items

        out["asset_listings"] = (
            capo_datazone.types.asset_in_data_product_listing_items.deserialize_json(
                data["assetListings"]
            )
        )
    return out


def redact_sensitive(value: SubscribedProductListing) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "glossary_terms" in value:
        import capo_datazone.types.detailed_glossary_terms

        out["glossary_terms"] = (
            capo_datazone.types.detailed_glossary_terms.redact_sensitive(
                value["glossary_terms"]
            )
        )
    return out
