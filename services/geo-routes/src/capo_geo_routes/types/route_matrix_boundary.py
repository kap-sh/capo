"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixBoundary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.route_matrix_boundary_geometry
    import capo_geo_routes.types.sensitive_boolean


class RouteMatrixBoundary(TypedDict, closed=True):
    geometry: NotRequired[
        "capo_geo_routes.types.route_matrix_boundary_geometry.RouteMatrixBoundaryGeometry"
    ]
    """<p>Geometry of the area to be avoided.</p>"""
    unbounded: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>No restrictions in terms of a routing boundary, and is typically used for longer routes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixBoundary) -> dict:
    out: dict = {}
    if "geometry" in value:
        import capo_geo_routes.types.route_matrix_boundary_geometry

        out["Geometry"] = (
            capo_geo_routes.types.route_matrix_boundary_geometry.serialize_json(
                value["geometry"]
            )
        )
    if "unbounded" in value:
        out["Unbounded"] = value["unbounded"]
    return out


def deserialize_json(data: dict) -> RouteMatrixBoundary:
    out: RouteMatrixBoundary = {}  # type: ignore[typeddict-item]
    if data.get("Geometry") is not None:
        import capo_geo_routes.types.route_matrix_boundary_geometry

        out["geometry"] = (
            capo_geo_routes.types.route_matrix_boundary_geometry.deserialize_json(
                data["Geometry"]
            )
        )
    if data.get("Unbounded") is not None:
        out["unbounded"] = data["Unbounded"]
    return out


def redact_sensitive(value: RouteMatrixBoundary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "geometry" in value:
        import capo_geo_routes.types.route_matrix_boundary_geometry

        out["geometry"] = (
            capo_geo_routes.types.route_matrix_boundary_geometry.redact_sensitive(
                value["geometry"]
            )
        )
    if "unbounded" in value:
        out["unbounded"] = "*** Sensitive Data Redacted ***"
    return out
