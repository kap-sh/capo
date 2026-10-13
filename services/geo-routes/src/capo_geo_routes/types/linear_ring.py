"""Generated from Smithy shape ``com.amazonaws.georoutes#LinearRing``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.position

LinearRing: TypeAlias = list["capo_geo_routes.types.position.Position"]


# --- restJson1 ser/de ---
def serialize_json(value: LinearRing) -> list:
    import capo_geo_routes.types.position

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.position.serialize_json(item))
    return out


def deserialize_json(data: list) -> LinearRing:
    import capo_geo_routes.types.position

    out: LinearRing = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_routes.types.position.deserialize_json(item))
    return out


def redact_sensitive(value: LinearRing) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
