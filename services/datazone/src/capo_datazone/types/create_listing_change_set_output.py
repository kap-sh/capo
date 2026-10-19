"""Generated from Smithy shape ``com.amazonaws.datazone#CreateListingChangeSetOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.listing_id
    import capo_datazone.types.listing_status
    import capo_datazone.types.revision


class CreateListingChangeSetOutput(TypedDict, closed=True):
    listing_id: "capo_datazone.types.listing_id.ListingId"
    """<p>The ID of the listing (a record of an asset at a given time).</p>"""
    listing_revision: "capo_datazone.types.revision.Revision"
    """<p>The revision of a listing.</p>"""
    status: "capo_datazone.types.listing_status.ListingStatus"
    """<p>Specifies the status of the listing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateListingChangeSetOutput) -> dict:
    out: dict = {}
    out["listingId"] = value["listing_id"]
    out["listingRevision"] = value["listing_revision"]
    import capo_datazone.types.listing_status

    out["status"] = capo_datazone.types.listing_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> CreateListingChangeSetOutput:
    out: CreateListingChangeSetOutput = {}  # type: ignore[typeddict-item]
    if data.get("listingId") is not None:
        out["listing_id"] = data["listingId"]
    else:
        out["listing_id"] = ""
    if data.get("listingRevision") is not None:
        out["listing_revision"] = data["listingRevision"]
    else:
        out["listing_revision"] = ""
    if data.get("status") is not None:
        import capo_datazone.types.listing_status

        out["status"] = capo_datazone.types.listing_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_datazone.types.listing_status.ListingStatus", ""
        )
    return out
