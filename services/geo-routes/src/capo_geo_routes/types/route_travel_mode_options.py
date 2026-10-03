"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTravelModeOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.route_car_options
    import capo_geo_routes.types.route_intermodal_options
    import capo_geo_routes.types.route_pedestrian_options
    import capo_geo_routes.types.route_scooter_options
    import capo_geo_routes.types.route_transit_options
    import capo_geo_routes.types.route_truck_options


class RouteTravelModeOptions(TypedDict, closed=True):
    car: NotRequired["capo_geo_routes.types.route_car_options.RouteCarOptions"]
    """<p>Travel mode options when the provided travel mode is <code>Car</code>.</p>"""
    pedestrian: NotRequired[
        "capo_geo_routes.types.route_pedestrian_options.RoutePedestrianOptions"
    ]
    """<p>Travel mode options when the provided travel mode is <code>Pedestrian</code>.</p>"""
    scooter: NotRequired[
        "capo_geo_routes.types.route_scooter_options.RouteScooterOptions"
    ]
    """<p>Travel mode options when the provided travel mode is <code>Scooter</code>. </p> <note> <p>When travel mode is set to <code>Scooter</code>, then the avoidance option <code>ControlledAccessHighways</code> defaults to <code>true</code>.</p> </note>"""
    truck: NotRequired["capo_geo_routes.types.route_truck_options.RouteTruckOptions"]
    """<p>Travel mode options when the provided travel mode is <code>Truck</code>.</p>"""
    intermodal: NotRequired[
        "capo_geo_routes.types.route_intermodal_options.RouteIntermodalOptions"
    ]
    """<p>Travel mode options when the provided travel mode is <code>Intermodal</code>.</p> <note> <p>Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers.</p> </note>"""
    transit: NotRequired[
        "capo_geo_routes.types.route_transit_options.RouteTransitOptions"
    ]
    """<p>Travel mode options when the provided travel mode is <code>Transit</code>.</p> <note> <p>Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTravelModeOptions) -> dict:
    out: dict = {}
    if "car" in value:
        import capo_geo_routes.types.route_car_options

        out["Car"] = capo_geo_routes.types.route_car_options.serialize_json(
            value["car"]
        )
    if "pedestrian" in value:
        import capo_geo_routes.types.route_pedestrian_options

        out["Pedestrian"] = (
            capo_geo_routes.types.route_pedestrian_options.serialize_json(
                value["pedestrian"]
            )
        )
    if "scooter" in value:
        import capo_geo_routes.types.route_scooter_options

        out["Scooter"] = capo_geo_routes.types.route_scooter_options.serialize_json(
            value["scooter"]
        )
    if "truck" in value:
        import capo_geo_routes.types.route_truck_options

        out["Truck"] = capo_geo_routes.types.route_truck_options.serialize_json(
            value["truck"]
        )
    if "intermodal" in value:
        import capo_geo_routes.types.route_intermodal_options

        out["Intermodal"] = (
            capo_geo_routes.types.route_intermodal_options.serialize_json(
                value["intermodal"]
            )
        )
    if "transit" in value:
        import capo_geo_routes.types.route_transit_options

        out["Transit"] = capo_geo_routes.types.route_transit_options.serialize_json(
            value["transit"]
        )
    return out


def deserialize_json(data: dict) -> RouteTravelModeOptions:
    out: RouteTravelModeOptions = {}  # type: ignore[typeddict-item]
    if data.get("Car") is not None:
        import capo_geo_routes.types.route_car_options

        out["car"] = capo_geo_routes.types.route_car_options.deserialize_json(
            data["Car"]
        )
    if data.get("Pedestrian") is not None:
        import capo_geo_routes.types.route_pedestrian_options

        out["pedestrian"] = (
            capo_geo_routes.types.route_pedestrian_options.deserialize_json(
                data["Pedestrian"]
            )
        )
    if data.get("Scooter") is not None:
        import capo_geo_routes.types.route_scooter_options

        out["scooter"] = capo_geo_routes.types.route_scooter_options.deserialize_json(
            data["Scooter"]
        )
    if data.get("Truck") is not None:
        import capo_geo_routes.types.route_truck_options

        out["truck"] = capo_geo_routes.types.route_truck_options.deserialize_json(
            data["Truck"]
        )
    if data.get("Intermodal") is not None:
        import capo_geo_routes.types.route_intermodal_options

        out["intermodal"] = (
            capo_geo_routes.types.route_intermodal_options.deserialize_json(
                data["Intermodal"]
            )
        )
    if data.get("Transit") is not None:
        import capo_geo_routes.types.route_transit_options

        out["transit"] = capo_geo_routes.types.route_transit_options.deserialize_json(
            data["Transit"]
        )
    return out
