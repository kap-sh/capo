"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMajorRoadLabel``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.localized_string
    import capo_geo_routes.types.route_number


class RouteMajorRoadLabel(TypedDict, closed=True):
    road_name: NotRequired["capo_geo_routes.types.localized_string.LocalizedString"]
    """<p>Name of the road (localized).</p>"""
    route_number: NotRequired["capo_geo_routes.types.route_number.RouteNumber"]
    """<p>Route number of the road.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteMajorRoadLabel) -> dict:
    out: dict = {}
    if "road_name" in value:
        import capo_geo_routes.types.localized_string

        out["RoadName"] = capo_geo_routes.types.localized_string.serialize_json(
            value["road_name"]
        )
    if "route_number" in value:
        import capo_geo_routes.types.route_number

        out["RouteNumber"] = capo_geo_routes.types.route_number.serialize_json(
            value["route_number"]
        )
    return out


def deserialize_json(data: dict) -> RouteMajorRoadLabel:
    out: RouteMajorRoadLabel = {}  # type: ignore[typeddict-item]
    if data.get("RoadName") is not None:
        import capo_geo_routes.types.localized_string

        out["road_name"] = capo_geo_routes.types.localized_string.deserialize_json(
            data["RoadName"]
        )
    if data.get("RouteNumber") is not None:
        import capo_geo_routes.types.route_number

        out["route_number"] = capo_geo_routes.types.route_number.deserialize_json(
            data["RouteNumber"]
        )
    return out


def redact_sensitive(value: RouteMajorRoadLabel) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "road_name" in value:
        import capo_geo_routes.types.localized_string

        out["road_name"] = capo_geo_routes.types.localized_string.redact_sensitive(
            value["road_name"]
        )
    if "route_number" in value:
        import capo_geo_routes.types.route_number

        out["route_number"] = capo_geo_routes.types.route_number.redact_sensitive(
            value["route_number"]
        )
    return out
