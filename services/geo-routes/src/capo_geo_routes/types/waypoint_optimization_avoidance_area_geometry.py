"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationAvoidanceAreaGeometry``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.bounding_box


class WaypointOptimizationAvoidanceAreaGeometry(TypedDict, closed=True):
    bounding_box: NotRequired["capo_geo_routes.types.bounding_box.BoundingBox"]
    """<p>Geometry defined as a bounding box. The first pair represents the X and Y coordinates (longitude and latitude,) of the southwest corner of the bounding box; the second pair represents the X and Y coordinates (longitude and latitude) of the northeast corner.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationAvoidanceAreaGeometry) -> dict:
    out: dict = {}
    if "bounding_box" in value:
        import capo_geo_routes.types.bounding_box

        out["BoundingBox"] = capo_geo_routes.types.bounding_box.serialize_json(
            value["bounding_box"]
        )
    return out


def deserialize_json(data: dict) -> WaypointOptimizationAvoidanceAreaGeometry:
    out: WaypointOptimizationAvoidanceAreaGeometry = {}  # type: ignore[typeddict-item]
    if data.get("BoundingBox") is not None:
        import capo_geo_routes.types.bounding_box

        out["bounding_box"] = capo_geo_routes.types.bounding_box.deserialize_json(
            data["BoundingBox"]
        )
    return out


def redact_sensitive(
    value: WaypointOptimizationAvoidanceAreaGeometry,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "bounding_box" in value:
        out["bounding_box"] = "*** Sensitive Data Redacted ***"
    return out
