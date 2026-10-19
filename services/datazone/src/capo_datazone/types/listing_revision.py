"""Generated from Smithy shape ``com.amazonaws.datazone#ListingRevision``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.listing_id
    import capo_datazone.types.revision


class ListingRevision(TypedDict, closed=True):
    id: "capo_datazone.types.listing_id.ListingId"
    """<p>An identifier of a revision of an asset published in a Amazon DataZone catalog.</p>"""
    revision: "capo_datazone.types.revision.Revision"
    """<p>The details of a revision of an asset published in a Amazon DataZone catalog.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListingRevision) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["revision"] = value["revision"]
    return out


def deserialize_json(data: dict) -> ListingRevision:
    out: ListingRevision = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("revision") is not None:
        out["revision"] = data["revision"]
    else:
        out["revision"] = ""
    return out
