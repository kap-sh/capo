"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteAvoidanceZoneCategory``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.route_zone_category


class RouteAvoidanceZoneCategory(TypedDict, closed=True):
    category: "capo_geo_routes.types.route_zone_category.RouteZoneCategory"
    """<p>Zone category to be avoided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteAvoidanceZoneCategory) -> dict:
    out: dict = {}
    import capo_geo_routes.types.route_zone_category

    out["Category"] = capo_geo_routes.types.route_zone_category.serialize_json(
        value["category"]
    )
    return out


def deserialize_json(data: dict) -> RouteAvoidanceZoneCategory:
    out: RouteAvoidanceZoneCategory = {}  # type: ignore[typeddict-item]
    if data.get("Category") is not None:
        import capo_geo_routes.types.route_zone_category

        out["category"] = capo_geo_routes.types.route_zone_category.deserialize_json(
            data["Category"]
        )
    else:
        raise DeserializationError("RouteAvoidanceZoneCategory.category required")
    return out


def redact_sensitive(value: RouteAvoidanceZoneCategory) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "category" in value:
        out["category"] = "*** Sensitive Data Redacted ***"
    return out
