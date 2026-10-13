"""Generated from Smithy shape ``com.amazonaws.geoplaces#ContactDetailsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.contact_details

ContactDetailsList: TypeAlias = list[
    "capo_geo_places.types.contact_details.ContactDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactDetailsList) -> list:
    import capo_geo_places.types.contact_details

    out: list = []
    for item in value:
        out.append(capo_geo_places.types.contact_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContactDetailsList:
    import capo_geo_places.types.contact_details

    out: ContactDetailsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_places.types.contact_details.deserialize_json(item))
    return out


def redact_sensitive(value: ContactDetailsList) -> list[Any]:
    import capo_geo_places.types.contact_details

    return [
        capo_geo_places.types.contact_details.redact_sensitive(item) for item in value
    ]
