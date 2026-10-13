"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.isoline

IsolineList: TypeAlias = list["capo_geo_routes.types.isoline.Isoline"]


# --- restJson1 ser/de ---
def serialize_json(value: IsolineList) -> list:
    import capo_geo_routes.types.isoline

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.isoline.serialize_json(item))
    return out


def deserialize_json(data: list) -> IsolineList:
    import capo_geo_routes.types.isoline

    out: IsolineList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_routes.types.isoline.deserialize_json(item))
    return out


def redact_sensitive(value: IsolineList) -> list[Any]:
    import capo_geo_routes.types.isoline

    return [capo_geo_routes.types.isoline.redact_sensitive(item) for item in value]
