"""Generated from Smithy shape ``com.amazonaws.datazone#DataProductListingItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.created_at
    import capo_datazone.types.created_by
    import capo_datazone.types.data_product_id
    import capo_datazone.types.data_product_listing_item_additional_attributes
    import capo_datazone.types.data_product_name
    import capo_datazone.types.description
    import capo_datazone.types.detailed_glossary_terms
    import capo_datazone.types.listing_id
    import capo_datazone.types.listing_summary_items
    import capo_datazone.types.project_id
    import capo_datazone.types.revision
    import capo_datazone.types.updated_by


class DataProductListingItem(TypedDict, closed=True):
    listing_id: NotRequired["capo_datazone.types.listing_id.ListingId"]
    """<p>The ID of the listing.</p>"""
    listing_revision: NotRequired["capo_datazone.types.revision.Revision"]
    """<p>The revision of the listing.</p>"""
    name: NotRequired["capo_datazone.types.data_product_name.DataProductName"]
    """<p>The name of the asset of the data product. </p>"""
    entity_id: NotRequired["capo_datazone.types.data_product_id.DataProductId"]
    """<p>The entity ID of the asset of the asset of the data product. </p>"""
    entity_revision: NotRequired["capo_datazone.types.revision.Revision"]
    """<p>The revision of the asset of the asset of the data product. </p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of the asset of the asset of the data product. </p>"""
    created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp at which the asset of the data product listing was created. </p>"""
    listing_created_by: NotRequired["capo_datazone.types.created_by.CreatedBy"]
    """<p>The timestamp at which the listing was created.</p>"""
    listing_updated_by: NotRequired["capo_datazone.types.updated_by.UpdatedBy"]
    """<p>The user who updated the listing.</p>"""
    glossary_terms: NotRequired[
        "capo_datazone.types.detailed_glossary_terms.DetailedGlossaryTerms"
    ]
    """<p>The glossary terms of the asset of the asset of the data product. </p>"""
    owning_project_id: NotRequired["capo_datazone.types.project_id.ProjectId"]
    """<p>The ID of the owning project of the asset of the data product. </p>"""
    additional_attributes: NotRequired[
        "capo_datazone.types.data_product_listing_item_additional_attributes.DataProductListingItemAdditionalAttributes"
    ]
    """<p>The additional attributes of the asset of the data product.</p>"""
    items: NotRequired["capo_datazone.types.listing_summary_items.ListingSummaryItems"]
    """<p>The data of the asset of the data product. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataProductListingItem) -> dict:
    out: dict = {}
    if "listing_id" in value:
        out["listingId"] = value["listing_id"]
    if "listing_revision" in value:
        out["listingRevision"] = value["listing_revision"]
    if "name" in value:
        out["name"] = value["name"]
    if "entity_id" in value:
        out["entityId"] = value["entity_id"]
    if "entity_revision" in value:
        out["entityRevision"] = value["entity_revision"]
    if "description" in value:
        out["description"] = value["description"]
    if "created_at" in value:
        import capo_datazone.types.created_at

        out["createdAt"] = capo_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "listing_created_by" in value:
        out["listingCreatedBy"] = value["listing_created_by"]
    if "listing_updated_by" in value:
        out["listingUpdatedBy"] = value["listing_updated_by"]
    if "glossary_terms" in value:
        import capo_datazone.types.detailed_glossary_terms

        out["glossaryTerms"] = (
            capo_datazone.types.detailed_glossary_terms.serialize_json(
                value["glossary_terms"]
            )
        )
    if "owning_project_id" in value:
        out["owningProjectId"] = value["owning_project_id"]
    if "additional_attributes" in value:
        import capo_datazone.types.data_product_listing_item_additional_attributes

        out["additionalAttributes"] = (
            capo_datazone.types.data_product_listing_item_additional_attributes.serialize_json(
                value["additional_attributes"]
            )
        )
    if "items" in value:
        import capo_datazone.types.listing_summary_items

        out["items"] = capo_datazone.types.listing_summary_items.serialize_json(
            value["items"]
        )
    return out


def deserialize_json(data: dict) -> DataProductListingItem:
    out: DataProductListingItem = {}  # type: ignore[typeddict-item]
    if data.get("listingId") is not None:
        out["listing_id"] = data["listingId"]
    if data.get("listingRevision") is not None:
        out["listing_revision"] = data["listingRevision"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("entityId") is not None:
        out["entity_id"] = data["entityId"]
    if data.get("entityRevision") is not None:
        out["entity_revision"] = data["entityRevision"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("createdAt") is not None:
        import capo_datazone.types.created_at

        out["created_at"] = capo_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if data.get("listingCreatedBy") is not None:
        out["listing_created_by"] = data["listingCreatedBy"]
    if data.get("listingUpdatedBy") is not None:
        out["listing_updated_by"] = data["listingUpdatedBy"]
    if data.get("glossaryTerms") is not None:
        import capo_datazone.types.detailed_glossary_terms

        out["glossary_terms"] = (
            capo_datazone.types.detailed_glossary_terms.deserialize_json(
                data["glossaryTerms"]
            )
        )
    if data.get("owningProjectId") is not None:
        out["owning_project_id"] = data["owningProjectId"]
    if data.get("additionalAttributes") is not None:
        import capo_datazone.types.data_product_listing_item_additional_attributes

        out["additional_attributes"] = (
            capo_datazone.types.data_product_listing_item_additional_attributes.deserialize_json(
                data["additionalAttributes"]
            )
        )
    if data.get("items") is not None:
        import capo_datazone.types.listing_summary_items

        out["items"] = capo_datazone.types.listing_summary_items.deserialize_json(
            data["items"]
        )
    return out


def redact_sensitive(value: DataProductListingItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "glossary_terms" in value:
        import capo_datazone.types.detailed_glossary_terms

        out["glossary_terms"] = (
            capo_datazone.types.detailed_glossary_terms.redact_sensitive(
                value["glossary_terms"]
            )
        )
    if "items" in value:
        import capo_datazone.types.listing_summary_items

        out["items"] = capo_datazone.types.listing_summary_items.redact_sensitive(
            value["items"]
        )
    return out
