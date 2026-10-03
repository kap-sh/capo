"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.position
    import capo_geo_routes.types.route_matrix_destination_options


class RouteMatrixDestination(TypedDict, closed=True):
    options: NotRequired[
        "capo_geo_routes.types.route_matrix_destination_options.RouteMatrixDestinationOptions"
    ]
    """<p> Destination related options. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    position: "capo_geo_routes.types.position.Position"
    """<p>Position in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixDestination) -> dict:
    out: dict = {}
    if "options" in value:
        import capo_geo_routes.types.route_matrix_destination_options

        out["Options"] = (
            capo_geo_routes.types.route_matrix_destination_options.serialize_json(
                value["options"]
            )
        )
    import capo_geo_routes.types.position

    out["Position"] = capo_geo_routes.types.position.serialize_json(value["position"])
    return out


def deserialize_json(data: dict) -> RouteMatrixDestination:
    out: RouteMatrixDestination = {}  # type: ignore[typeddict-item]
    if data.get("Options") is not None:
        import capo_geo_routes.types.route_matrix_destination_options

        out["options"] = (
            capo_geo_routes.types.route_matrix_destination_options.deserialize_json(
                data["Options"]
            )
        )
    if data.get("Position") is not None:
        import capo_geo_routes.types.position

        out["position"] = capo_geo_routes.types.position.deserialize_json(
            data["Position"]
        )
    else:
        raise DeserializationError("RouteMatrixDestination.position required")
    return out
