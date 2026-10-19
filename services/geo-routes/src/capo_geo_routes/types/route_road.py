"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteRoad``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.localized_string_list
    import capo_geo_routes.types.route_number_list
    import capo_geo_routes.types.route_road_type


class RouteRoad(TypedDict, closed=True):
    road_name: "capo_geo_routes.types.localized_string_list.LocalizedStringList"
    """<p>Name of the road (localized).</p>"""
    route_number: "capo_geo_routes.types.route_number_list.RouteNumberList"
    """<p>Route number of the road.</p>"""
    towards: "capo_geo_routes.types.localized_string_list.LocalizedStringList"
    """<p>Names of destinations that can be reached when traveling on the road.</p>"""
    type: NotRequired["capo_geo_routes.types.route_road_type.RouteRoadType"]
    """<p>The type of road.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteRoad) -> dict:
    out: dict = {}
    import capo_geo_routes.types.localized_string_list

    out["RoadName"] = capo_geo_routes.types.localized_string_list.serialize_json(
        value["road_name"]
    )
    import capo_geo_routes.types.route_number_list

    out["RouteNumber"] = capo_geo_routes.types.route_number_list.serialize_json(
        value["route_number"]
    )
    import capo_geo_routes.types.localized_string_list

    out["Towards"] = capo_geo_routes.types.localized_string_list.serialize_json(
        value["towards"]
    )
    if "type" in value:
        import capo_geo_routes.types.route_road_type

        out["Type"] = capo_geo_routes.types.route_road_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> RouteRoad:
    out: RouteRoad = {}  # type: ignore[typeddict-item]
    if data.get("RoadName") is not None:
        import capo_geo_routes.types.localized_string_list

        out["road_name"] = capo_geo_routes.types.localized_string_list.deserialize_json(
            data["RoadName"]
        )
    else:
        out["road_name"] = []
    if data.get("RouteNumber") is not None:
        import capo_geo_routes.types.route_number_list

        out["route_number"] = capo_geo_routes.types.route_number_list.deserialize_json(
            data["RouteNumber"]
        )
    else:
        out["route_number"] = []
    if data.get("Towards") is not None:
        import capo_geo_routes.types.localized_string_list

        out["towards"] = capo_geo_routes.types.localized_string_list.deserialize_json(
            data["Towards"]
        )
    else:
        out["towards"] = []
    if data.get("Type") is not None:
        import capo_geo_routes.types.route_road_type

        out["type"] = capo_geo_routes.types.route_road_type.deserialize_json(
            data["Type"]
        )
    return out


def redact_sensitive(value: RouteRoad) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "road_name" in value:
        import capo_geo_routes.types.localized_string_list

        out["road_name"] = capo_geo_routes.types.localized_string_list.redact_sensitive(
            value["road_name"]
        )
    if "route_number" in value:
        import capo_geo_routes.types.route_number_list

        out["route_number"] = capo_geo_routes.types.route_number_list.redact_sensitive(
            value["route_number"]
        )
    if "towards" in value:
        import capo_geo_routes.types.localized_string_list

        out["towards"] = capo_geo_routes.types.localized_string_list.redact_sensitive(
            value["towards"]
        )
    if "type" in value:
        out["type"] = "*** Sensitive Data Redacted ***"
    return out
