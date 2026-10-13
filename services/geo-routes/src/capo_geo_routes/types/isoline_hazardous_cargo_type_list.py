"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineHazardousCargoTypeList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.isoline_hazardous_cargo_type

IsolineHazardousCargoTypeList: TypeAlias = list[
    "capo_geo_routes.types.isoline_hazardous_cargo_type.IsolineHazardousCargoType"
]


# --- restJson1 ser/de ---
def serialize_json(value: IsolineHazardousCargoTypeList) -> list:
    import capo_geo_routes.types.isoline_hazardous_cargo_type

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.isoline_hazardous_cargo_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IsolineHazardousCargoTypeList:
    import capo_geo_routes.types.isoline_hazardous_cargo_type

    out: IsolineHazardousCargoTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_geo_routes.types.isoline_hazardous_cargo_type.deserialize_json(item)
        )
    return out


def redact_sensitive(value: IsolineHazardousCargoTypeList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
