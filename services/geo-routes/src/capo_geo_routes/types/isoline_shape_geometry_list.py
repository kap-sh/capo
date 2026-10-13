"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineShapeGeometryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.isoline_shape_geometry

IsolineShapeGeometryList: TypeAlias = list[
    "capo_geo_routes.types.isoline_shape_geometry.IsolineShapeGeometry"
]


# --- restJson1 ser/de ---
def serialize_json(value: IsolineShapeGeometryList) -> list:
    import capo_geo_routes.types.isoline_shape_geometry

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.isoline_shape_geometry.serialize_json(item))
    return out


def deserialize_json(data: list) -> IsolineShapeGeometryList:
    import capo_geo_routes.types.isoline_shape_geometry

    out: IsolineShapeGeometryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_routes.types.isoline_shape_geometry.deserialize_json(item))
    return out


def redact_sensitive(value: IsolineShapeGeometryList) -> list[Any]:
    import capo_geo_routes.types.isoline_shape_geometry

    return [
        capo_geo_routes.types.isoline_shape_geometry.redact_sensitive(item)
        for item in value
    ]
