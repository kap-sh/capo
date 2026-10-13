"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineAvoidanceArea``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.isoline_avoidance_area_geometry
    import capo_geo_routes.types.isoline_avoidance_area_geometry_list

IsolineAvoidanceArea = TypedDict(
    "IsolineAvoidanceArea",
    {
        "except": NotRequired[
            "capo_geo_routes.types.isoline_avoidance_area_geometry_list.IsolineAvoidanceAreaGeometryList"
        ],
        "geometry": "capo_geo_routes.types.isoline_avoidance_area_geometry.IsolineAvoidanceAreaGeometry",
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: IsolineAvoidanceArea) -> dict:
    out: dict = {}
    if "except" in value:
        import capo_geo_routes.types.isoline_avoidance_area_geometry_list

        out["Except"] = (
            capo_geo_routes.types.isoline_avoidance_area_geometry_list.serialize_json(
                value["except"]
            )
        )
    import capo_geo_routes.types.isoline_avoidance_area_geometry

    out["Geometry"] = (
        capo_geo_routes.types.isoline_avoidance_area_geometry.serialize_json(
            value["geometry"]
        )
    )
    return out


def deserialize_json(data: dict) -> IsolineAvoidanceArea:
    out: IsolineAvoidanceArea = {}  # type: ignore[typeddict-item]
    if data.get("Except") is not None:
        import capo_geo_routes.types.isoline_avoidance_area_geometry_list

        out["except"] = (
            capo_geo_routes.types.isoline_avoidance_area_geometry_list.deserialize_json(
                data["Except"]
            )
        )
    if data.get("Geometry") is not None:
        import capo_geo_routes.types.isoline_avoidance_area_geometry

        out["geometry"] = (
            capo_geo_routes.types.isoline_avoidance_area_geometry.deserialize_json(
                data["Geometry"]
            )
        )
    else:
        raise DeserializationError("IsolineAvoidanceArea.geometry required")
    return out


def redact_sensitive(value: IsolineAvoidanceArea) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "except" in value:
        import capo_geo_routes.types.isoline_avoidance_area_geometry_list

        out["except"] = (
            capo_geo_routes.types.isoline_avoidance_area_geometry_list.redact_sensitive(
                value["except"]
            )
        )
    if "geometry" in value:
        import capo_geo_routes.types.isoline_avoidance_area_geometry

        out["geometry"] = (
            capo_geo_routes.types.isoline_avoidance_area_geometry.redact_sensitive(
                value["geometry"]
            )
        )
    return out
