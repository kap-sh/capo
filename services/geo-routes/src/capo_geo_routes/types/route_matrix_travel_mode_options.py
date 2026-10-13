"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixTravelModeOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.route_matrix_car_options
    import capo_geo_routes.types.route_matrix_scooter_options
    import capo_geo_routes.types.route_matrix_truck_options


class RouteMatrixTravelModeOptions(TypedDict, closed=True):
    car: NotRequired[
        "capo_geo_routes.types.route_matrix_car_options.RouteMatrixCarOptions"
    ]
    """<p>Travel mode options when the provided travel mode is <code>Car</code>.</p>"""
    scooter: NotRequired[
        "capo_geo_routes.types.route_matrix_scooter_options.RouteMatrixScooterOptions"
    ]
    """<p>Travel mode options when the provided travel mode is <code>Scooter</code>. </p> <note> <p>When travel mode is set to <code>Scooter</code>, then the avoidance option <code>ControlledAccessHighways</code> defaults to <code>true</code>.</p> </note>"""
    truck: NotRequired[
        "capo_geo_routes.types.route_matrix_truck_options.RouteMatrixTruckOptions"
    ]
    """<p>Travel mode options when the provided travel mode is <code>Truck</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixTravelModeOptions) -> dict:
    out: dict = {}
    if "car" in value:
        import capo_geo_routes.types.route_matrix_car_options

        out["Car"] = capo_geo_routes.types.route_matrix_car_options.serialize_json(
            value["car"]
        )
    if "scooter" in value:
        import capo_geo_routes.types.route_matrix_scooter_options

        out["Scooter"] = (
            capo_geo_routes.types.route_matrix_scooter_options.serialize_json(
                value["scooter"]
            )
        )
    if "truck" in value:
        import capo_geo_routes.types.route_matrix_truck_options

        out["Truck"] = capo_geo_routes.types.route_matrix_truck_options.serialize_json(
            value["truck"]
        )
    return out


def deserialize_json(data: dict) -> RouteMatrixTravelModeOptions:
    out: RouteMatrixTravelModeOptions = {}  # type: ignore[typeddict-item]
    if data.get("Car") is not None:
        import capo_geo_routes.types.route_matrix_car_options

        out["car"] = capo_geo_routes.types.route_matrix_car_options.deserialize_json(
            data["Car"]
        )
    if data.get("Scooter") is not None:
        import capo_geo_routes.types.route_matrix_scooter_options

        out["scooter"] = (
            capo_geo_routes.types.route_matrix_scooter_options.deserialize_json(
                data["Scooter"]
            )
        )
    if data.get("Truck") is not None:
        import capo_geo_routes.types.route_matrix_truck_options

        out["truck"] = (
            capo_geo_routes.types.route_matrix_truck_options.deserialize_json(
                data["Truck"]
            )
        )
    return out


def redact_sensitive(value: RouteMatrixTravelModeOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "car" in value:
        import capo_geo_routes.types.route_matrix_car_options

        out["car"] = capo_geo_routes.types.route_matrix_car_options.redact_sensitive(
            value["car"]
        )
    if "scooter" in value:
        import capo_geo_routes.types.route_matrix_scooter_options

        out["scooter"] = (
            capo_geo_routes.types.route_matrix_scooter_options.redact_sensitive(
                value["scooter"]
            )
        )
    if "truck" in value:
        import capo_geo_routes.types.route_matrix_truck_options

        out["truck"] = (
            capo_geo_routes.types.route_matrix_truck_options.redact_sensitive(
                value["truck"]
            )
        )
    return out
