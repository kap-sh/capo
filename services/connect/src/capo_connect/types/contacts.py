"""Generated from Smithy shape ``com.amazonaws.connect#Contacts``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.contact_search_summary

Contacts: TypeAlias = list[
    "capo_connect.types.contact_search_summary.ContactSearchSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: Contacts) -> list:
    import capo_connect.types.contact_search_summary

    out: list = []
    for item in value:
        out.append(capo_connect.types.contact_search_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> Contacts:
    import capo_connect.types.contact_search_summary

    out: Contacts = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connect.types.contact_search_summary.deserialize_json(item))
    return out


def redact_sensitive(value: Contacts) -> list[Any]:
    import capo_connect.types.contact_search_summary

    return [
        capo_connect.types.contact_search_summary.redact_sensitive(item)
        for item in value
    ]
