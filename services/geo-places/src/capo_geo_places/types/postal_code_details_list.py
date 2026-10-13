"""Generated from Smithy shape ``com.amazonaws.geoplaces#PostalCodeDetailsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.postal_code_details

PostalCodeDetailsList: TypeAlias = list[
    "capo_geo_places.types.postal_code_details.PostalCodeDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: PostalCodeDetailsList) -> list:
    import capo_geo_places.types.postal_code_details

    out: list = []
    for item in value:
        out.append(capo_geo_places.types.postal_code_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> PostalCodeDetailsList:
    import capo_geo_places.types.postal_code_details

    out: PostalCodeDetailsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_places.types.postal_code_details.deserialize_json(item))
    return out


def redact_sensitive(value: PostalCodeDetailsList) -> list[Any]:
    import capo_geo_places.types.postal_code_details

    return [
        capo_geo_places.types.postal_code_details.redact_sensitive(item)
        for item in value
    ]
