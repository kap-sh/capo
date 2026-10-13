"""Generated from Smithy shape ``com.amazonaws.georoutes#LinearRings``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.linear_ring

LinearRings: TypeAlias = list["capo_geo_routes.types.linear_ring.LinearRing"]


# --- restJson1 ser/de ---
def serialize_json(value: LinearRings) -> list:
    import capo_geo_routes.types.linear_ring

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.linear_ring.serialize_json(item))
    return out


def deserialize_json(data: list) -> LinearRings:
    import capo_geo_routes.types.linear_ring

    out: LinearRings = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_routes.types.linear_ring.deserialize_json(item))
    return out


def redact_sensitive(value: LinearRings) -> list[Any]:
    import capo_geo_routes.types.linear_ring

    return [capo_geo_routes.types.linear_ring.redact_sensitive(item) for item in value]
