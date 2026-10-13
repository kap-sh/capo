"""Generated from Smithy shape ``com.amazonaws.geoplaces#AdminNamesList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.admin_names

AdminNamesList: TypeAlias = list["capo_geo_places.types.admin_names.AdminNames"]


# --- restJson1 ser/de ---
def serialize_json(value: AdminNamesList) -> list:
    import capo_geo_places.types.admin_names

    out: list = []
    for item in value:
        out.append(capo_geo_places.types.admin_names.serialize_json(item))
    return out


def deserialize_json(data: list) -> AdminNamesList:
    import capo_geo_places.types.admin_names

    out: AdminNamesList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_places.types.admin_names.deserialize_json(item))
    return out


def redact_sensitive(value: AdminNamesList) -> list[Any]:
    import capo_geo_places.types.admin_names

    return [capo_geo_places.types.admin_names.redact_sensitive(item) for item in value]
