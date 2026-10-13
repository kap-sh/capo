"""Generated from Smithy shape ``com.amazonaws.georoutes#LineString``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.position

LineString: TypeAlias = list["capo_geo_routes.types.position.Position"]


# --- restJson1 ser/de ---
def serialize_json(value: LineString) -> list:
    import capo_geo_routes.types.position

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.position.serialize_json(item))
    return out


def deserialize_json(data: list) -> LineString:
    import capo_geo_routes.types.position

    out: LineString = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_routes.types.position.deserialize_json(item))
    return out


def redact_sensitive(value: LineString) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
