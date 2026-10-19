"""Generated from Smithy shape ``com.amazonaws.datazone#SubscribedListingInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.listing_id


class SubscribedListingInput(TypedDict, closed=True):
    identifier: "capo_datazone.types.listing_id.ListingId"
    """<p>The identifier of the published asset for which the subscription grant is to be created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscribedListingInput) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    return out


def deserialize_json(data: dict) -> SubscribedListingInput:
    out: SubscribedListingInput = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    return out
