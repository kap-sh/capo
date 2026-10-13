"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineAvoidanceAreaList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.isoline_avoidance_area

IsolineAvoidanceAreaList: TypeAlias = list[
    "capo_geo_routes.types.isoline_avoidance_area.IsolineAvoidanceArea"
]


# --- restJson1 ser/de ---
def serialize_json(value: IsolineAvoidanceAreaList) -> list:
    import capo_geo_routes.types.isoline_avoidance_area

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.isoline_avoidance_area.serialize_json(item))
    return out


def deserialize_json(data: list) -> IsolineAvoidanceAreaList:
    import capo_geo_routes.types.isoline_avoidance_area

    out: IsolineAvoidanceAreaList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_routes.types.isoline_avoidance_area.deserialize_json(item))
    return out


def redact_sensitive(value: IsolineAvoidanceAreaList) -> list[Any]:
    import capo_geo_routes.types.isoline_avoidance_area

    return [
        capo_geo_routes.types.isoline_avoidance_area.redact_sensitive(item)
        for item in value
    ]
