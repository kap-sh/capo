"""Generated from Smithy shape ``com.amazonaws.datazone#SubscribedListings``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.subscribed_listing

SubscribedListings: TypeAlias = list[
    "capo_datazone.types.subscribed_listing.SubscribedListing"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubscribedListings) -> list:
    import capo_datazone.types.subscribed_listing

    out: list = []
    for item in value:
        out.append(capo_datazone.types.subscribed_listing.serialize_json(item))
    return out


def deserialize_json(data: list) -> SubscribedListings:
    import capo_datazone.types.subscribed_listing

    out: SubscribedListings = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datazone.types.subscribed_listing.deserialize_json(item))
    return out


def redact_sensitive(value: SubscribedListings) -> list[Any]:
    import capo_datazone.types.subscribed_listing

    return [
        capo_datazone.types.subscribed_listing.redact_sensitive(item) for item in value
    ]
