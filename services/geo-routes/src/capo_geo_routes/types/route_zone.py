"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteZone``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.route_zone_category
    import capo_geo_routes.types.sensitive_string


class RouteZone(TypedDict, closed=True):
    category: NotRequired["capo_geo_routes.types.route_zone_category.RouteZoneCategory"]
    """<p>The zone category.</p>"""
    name: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>The name of the zone.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteZone) -> dict:
    out: dict = {}
    if "category" in value:
        import capo_geo_routes.types.route_zone_category

        out["Category"] = capo_geo_routes.types.route_zone_category.serialize_json(
            value["category"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> RouteZone:
    out: RouteZone = {}  # type: ignore[typeddict-item]
    if data.get("Category") is not None:
        import capo_geo_routes.types.route_zone_category

        out["category"] = capo_geo_routes.types.route_zone_category.deserialize_json(
            data["Category"]
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out


def redact_sensitive(value: RouteZone) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "category" in value:
        out["category"] = "*** Sensitive Data Redacted ***"
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
