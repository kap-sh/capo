"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineConnectionList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.isoline_connection

IsolineConnectionList: TypeAlias = list[
    "capo_geo_routes.types.isoline_connection.IsolineConnection"
]


# --- restJson1 ser/de ---
def serialize_json(value: IsolineConnectionList) -> list:
    import capo_geo_routes.types.isoline_connection

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.isoline_connection.serialize_json(item))
    return out


def deserialize_json(data: list) -> IsolineConnectionList:
    import capo_geo_routes.types.isoline_connection

    out: IsolineConnectionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_routes.types.isoline_connection.deserialize_json(item))
    return out


def redact_sensitive(value: IsolineConnectionList) -> list[Any]:
    import capo_geo_routes.types.isoline_connection

    return [
        capo_geo_routes.types.isoline_connection.redact_sensitive(item)
        for item in value
    ]
