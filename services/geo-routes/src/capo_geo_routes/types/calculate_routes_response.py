"""Generated from Smithy shape ``com.amazonaws.georoutes#CalculateRoutesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.geometry_format
    import capo_geo_routes.types.route_list
    import capo_geo_routes.types.route_response_notice_list


class CalculateRoutesResponse(TypedDict, closed=True):
    leg_geometry_format: "capo_geo_routes.types.geometry_format.GeometryFormat"
    """<p>Specifies the format of the geometry returned for each leg of the route.</p>"""
    notices: "capo_geo_routes.types.route_response_notice_list.RouteResponseNoticeList"
    """<p> Notices are additional information returned that indicate issues that occurred during route calculation. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    pricing_bucket: "str"
    """<p>The pricing bucket for which the query is charged at.</p>"""
    routes: "capo_geo_routes.types.route_list.RouteList"
    """<p>The path from the origin to the destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CalculateRoutesResponse) -> dict:
    out: dict = {}
    import capo_geo_routes.types.geometry_format

    out["LegGeometryFormat"] = capo_geo_routes.types.geometry_format.serialize_json(
        value["leg_geometry_format"]
    )
    import capo_geo_routes.types.route_response_notice_list

    out["Notices"] = capo_geo_routes.types.route_response_notice_list.serialize_json(
        value["notices"]
    )
    import capo_geo_routes.types.route_list

    out["Routes"] = capo_geo_routes.types.route_list.serialize_json(value["routes"])
    return out


def deserialize_json(data: dict) -> CalculateRoutesResponse:
    out: CalculateRoutesResponse = {}  # type: ignore[typeddict-item]
    if data.get("LegGeometryFormat") is not None:
        import capo_geo_routes.types.geometry_format

        out["leg_geometry_format"] = (
            capo_geo_routes.types.geometry_format.deserialize_json(
                data["LegGeometryFormat"]
            )
        )
    else:
        raise DeserializationError(
            "CalculateRoutesResponse.leg_geometry_format required"
        )
    if data.get("Notices") is not None:
        import capo_geo_routes.types.route_response_notice_list

        out["notices"] = (
            capo_geo_routes.types.route_response_notice_list.deserialize_json(
                data["Notices"]
            )
        )
    else:
        raise DeserializationError("CalculateRoutesResponse.notices required")
    if data.get("Routes") is not None:
        import capo_geo_routes.types.route_list

        out["routes"] = capo_geo_routes.types.route_list.deserialize_json(
            data["Routes"]
        )
    else:
        raise DeserializationError("CalculateRoutesResponse.routes required")
    return out
