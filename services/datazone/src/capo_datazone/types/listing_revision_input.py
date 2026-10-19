"""Generated from Smithy shape ``com.amazonaws.datazone#ListingRevisionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.listing_id
    import capo_datazone.types.revision


class ListingRevisionInput(TypedDict, closed=True):
    identifier: "capo_datazone.types.listing_id.ListingId"
    """<p>An identifier of revision to be made to an asset published in a Amazon DataZone catalog.</p>"""
    revision: "capo_datazone.types.revision.Revision"
    """<p>The details of a revision to be made to an asset published in a Amazon DataZone catalog.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListingRevisionInput) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    out["revision"] = value["revision"]
    return out


def deserialize_json(data: dict) -> ListingRevisionInput:
    out: ListingRevisionInput = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    if data.get("revision") is not None:
        out["revision"] = data["revision"]
    else:
        out["revision"] = ""
    return out
