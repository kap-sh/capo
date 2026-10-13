"""Generated from Smithy shape ``com.amazonaws.datazone#DataProductListing``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.created_at
    import capo_datazone.types.data_product_id
    import capo_datazone.types.detailed_glossary_terms
    import capo_datazone.types.forms
    import capo_datazone.types.listing_summaries
    import capo_datazone.types.project_id
    import capo_datazone.types.revision


class DataProductListing(TypedDict, closed=True):
    data_product_id: NotRequired["capo_datazone.types.data_product_id.DataProductId"]
    """<p>The ID of the data product listing.</p>"""
    data_product_revision: NotRequired["capo_datazone.types.revision.Revision"]
    """<p>The revision of the data product listing.</p>"""
    created_at: NotRequired["capo_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp at which the data product listing was created.</p>"""
    forms: NotRequired["capo_datazone.types.forms.Forms"]
    """<p>The metadata forms of the data product listing.</p>"""
    glossary_terms: NotRequired[
        "capo_datazone.types.detailed_glossary_terms.DetailedGlossaryTerms"
    ]
    """<p>The glossary terms of the data product listing.</p>"""
    owning_project_id: NotRequired["capo_datazone.types.project_id.ProjectId"]
    """<p>The ID of the owning project of the data product listing.</p>"""
    items: NotRequired["capo_datazone.types.listing_summaries.ListingSummaries"]
    """<p>The data assets of the data product listing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataProductListing) -> dict:
    out: dict = {}
    if "data_product_id" in value:
        out["dataProductId"] = value["data_product_id"]
    if "data_product_revision" in value:
        out["dataProductRevision"] = value["data_product_revision"]
    if "created_at" in value:
        import capo_datazone.types.created_at

        out["createdAt"] = capo_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "forms" in value:
        out["forms"] = value["forms"]
    if "glossary_terms" in value:
        import capo_datazone.types.detailed_glossary_terms

        out["glossaryTerms"] = (
            capo_datazone.types.detailed_glossary_terms.serialize_json(
                value["glossary_terms"]
            )
        )
    if "owning_project_id" in value:
        out["owningProjectId"] = value["owning_project_id"]
    if "items" in value:
        import capo_datazone.types.listing_summaries

        out["items"] = capo_datazone.types.listing_summaries.serialize_json(
            value["items"]
        )
    return out


def deserialize_json(data: dict) -> DataProductListing:
    out: DataProductListing = {}  # type: ignore[typeddict-item]
    if data.get("dataProductId") is not None:
        out["data_product_id"] = data["dataProductId"]
    if data.get("dataProductRevision") is not None:
        out["data_product_revision"] = data["dataProductRevision"]
    if data.get("createdAt") is not None:
        import capo_datazone.types.created_at

        out["created_at"] = capo_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if data.get("forms") is not None:
        out["forms"] = data["forms"]
    if data.get("glossaryTerms") is not None:
        import capo_datazone.types.detailed_glossary_terms

        out["glossary_terms"] = (
            capo_datazone.types.detailed_glossary_terms.deserialize_json(
                data["glossaryTerms"]
            )
        )
    if data.get("owningProjectId") is not None:
        out["owning_project_id"] = data["owningProjectId"]
    if data.get("items") is not None:
        import capo_datazone.types.listing_summaries

        out["items"] = capo_datazone.types.listing_summaries.deserialize_json(
            data["items"]
        )
    return out


def redact_sensitive(value: DataProductListing) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "glossary_terms" in value:
        import capo_datazone.types.detailed_glossary_terms

        out["glossary_terms"] = (
            capo_datazone.types.detailed_glossary_terms.redact_sensitive(
                value["glossary_terms"]
            )
        )
    if "items" in value:
        import capo_datazone.types.listing_summaries

        out["items"] = capo_datazone.types.listing_summaries.redact_sensitive(
            value["items"]
        )
    return out
