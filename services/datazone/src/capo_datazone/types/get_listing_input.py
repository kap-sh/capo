"""Generated from Smithy shape ``com.amazonaws.datazone#GetListingInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.listing_id
    import capo_datazone.types.revision


class GetListingInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain.</p>"""
    identifier: "capo_datazone.types.listing_id.ListingId"
    """<p>The ID of the listing.</p>"""
    listing_revision: NotRequired["capo_datazone.types.revision.Revision"]
    """<p>The revision of the listing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetListingInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetListingInput:
    out: GetListingInput = {}  # type: ignore[typeddict-item]
    return out
