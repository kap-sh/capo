"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixAvoidanceZoneCategory``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.route_matrix_zone_category


class RouteMatrixAvoidanceZoneCategory(TypedDict, closed=True):
    category: NotRequired[
        "capo_geo_routes.types.route_matrix_zone_category.RouteMatrixZoneCategory"
    ]
    """<p>Zone category to be avoided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixAvoidanceZoneCategory) -> dict:
    out: dict = {}
    if "category" in value:
        import capo_geo_routes.types.route_matrix_zone_category

        out["Category"] = (
            capo_geo_routes.types.route_matrix_zone_category.serialize_json(
                value["category"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteMatrixAvoidanceZoneCategory:
    out: RouteMatrixAvoidanceZoneCategory = {}  # type: ignore[typeddict-item]
    if data.get("Category") is not None:
        import capo_geo_routes.types.route_matrix_zone_category

        out["category"] = (
            capo_geo_routes.types.route_matrix_zone_category.deserialize_json(
                data["Category"]
            )
        )
    return out


def redact_sensitive(value: RouteMatrixAvoidanceZoneCategory) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "category" in value:
        out["category"] = "*** Sensitive Data Redacted ***"
    return out
