"""Generated from Smithy shape ``com.amazonaws.datazone#ListingSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.detailed_glossary_terms
    import capo_datazone.types.listing_id
    import capo_datazone.types.revision


class ListingSummary(TypedDict, closed=True):
    listing_id: NotRequired["capo_datazone.types.listing_id.ListingId"]
    """<p>The ID of the data product listing.</p>"""
    listing_revision: NotRequired["capo_datazone.types.revision.Revision"]
    """<p>The revision of the data product listing.</p>"""
    glossary_terms: NotRequired[
        "capo_datazone.types.detailed_glossary_terms.DetailedGlossaryTerms"
    ]
    """<p>The glossary terms of the data product.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListingSummary) -> dict:
    out: dict = {}
    if "listing_id" in value:
        out["listingId"] = value["listing_id"]
    if "listing_revision" in value:
        out["listingRevision"] = value["listing_revision"]
    if "glossary_terms" in value:
        import capo_datazone.types.detailed_glossary_terms

        out["glossaryTerms"] = (
            capo_datazone.types.detailed_glossary_terms.serialize_json(
                value["glossary_terms"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListingSummary:
    out: ListingSummary = {}  # type: ignore[typeddict-item]
    if data.get("listingId") is not None:
        out["listing_id"] = data["listingId"]
    if data.get("listingRevision") is not None:
        out["listing_revision"] = data["listingRevision"]
    if data.get("glossaryTerms") is not None:
        import capo_datazone.types.detailed_glossary_terms

        out["glossary_terms"] = (
            capo_datazone.types.detailed_glossary_terms.deserialize_json(
                data["glossaryTerms"]
            )
        )
    return out


def redact_sensitive(value: ListingSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "glossary_terms" in value:
        import capo_datazone.types.detailed_glossary_terms

        out["glossary_terms"] = (
            capo_datazone.types.detailed_glossary_terms.redact_sensitive(
                value["glossary_terms"]
            )
        )
    return out
