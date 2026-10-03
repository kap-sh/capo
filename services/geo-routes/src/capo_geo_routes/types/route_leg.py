"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteLeg``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.language_tag
    import capo_geo_routes.types.route_ferry_leg_details
    import capo_geo_routes.types.route_leg_geometry
    import capo_geo_routes.types.route_leg_travel_mode
    import capo_geo_routes.types.route_leg_type
    import capo_geo_routes.types.route_pedestrian_leg_details
    import capo_geo_routes.types.route_rental_leg_details
    import capo_geo_routes.types.route_taxi_leg_details
    import capo_geo_routes.types.route_transit_leg_details
    import capo_geo_routes.types.route_vehicle_leg_details


class RouteLeg(TypedDict, closed=True):
    ferry_leg_details: NotRequired[
        "capo_geo_routes.types.route_ferry_leg_details.RouteFerryLegDetails"
    ]
    """<p> FerryLegDetails is populated when the Leg type is Ferry, and provides additional information that is specific to ferry travel. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    geometry: "capo_geo_routes.types.route_leg_geometry.RouteLegGeometry"
    """<p>Geometry of the area to be avoided.</p>"""
    language: NotRequired["capo_geo_routes.types.language_tag.LanguageTag"]
    """<p> List of languages for instructions within steps in the response. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    pedestrian_leg_details: NotRequired[
        "capo_geo_routes.types.route_pedestrian_leg_details.RoutePedestrianLegDetails"
    ]
    """<p>Details related to the pedestrian leg.</p>"""
    travel_mode: "capo_geo_routes.types.route_leg_travel_mode.RouteLegTravelMode"
    """<p>Specifies the mode of transport when calculating a route. Used in estimating the speed of travel and road compatibility.</p> <p>Default value: <code>Car</code> </p>"""
    type: "capo_geo_routes.types.route_leg_type.RouteLegType"
    """<p>Type of the leg.</p>"""
    vehicle_leg_details: NotRequired[
        "capo_geo_routes.types.route_vehicle_leg_details.RouteVehicleLegDetails"
    ]
    """<p>Details related to the vehicle leg.</p>"""
    rental_leg_details: NotRequired[
        "capo_geo_routes.types.route_rental_leg_details.RouteRentalLegDetails"
    ]
    """<p>Details related to the rental leg.</p> <note> <p>Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers.</p> </note>"""
    taxi_leg_details: NotRequired[
        "capo_geo_routes.types.route_taxi_leg_details.RouteTaxiLegDetails"
    ]
    """<p>Details related to the taxi leg.</p> <note> <p>Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers.</p> </note>"""
    transit_leg_details: NotRequired[
        "capo_geo_routes.types.route_transit_leg_details.RouteTransitLegDetails"
    ]
    """<p>Details related to the transit leg.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteLeg) -> dict:
    out: dict = {}
    if "ferry_leg_details" in value:
        import capo_geo_routes.types.route_ferry_leg_details

        out["FerryLegDetails"] = (
            capo_geo_routes.types.route_ferry_leg_details.serialize_json(
                value["ferry_leg_details"]
            )
        )
    import capo_geo_routes.types.route_leg_geometry

    out["Geometry"] = capo_geo_routes.types.route_leg_geometry.serialize_json(
        value["geometry"]
    )
    if "language" in value:
        out["Language"] = value["language"]
    if "pedestrian_leg_details" in value:
        import capo_geo_routes.types.route_pedestrian_leg_details

        out["PedestrianLegDetails"] = (
            capo_geo_routes.types.route_pedestrian_leg_details.serialize_json(
                value["pedestrian_leg_details"]
            )
        )
    import capo_geo_routes.types.route_leg_travel_mode

    out["TravelMode"] = capo_geo_routes.types.route_leg_travel_mode.serialize_json(
        value["travel_mode"]
    )
    import capo_geo_routes.types.route_leg_type

    out["Type"] = capo_geo_routes.types.route_leg_type.serialize_json(value["type"])
    if "vehicle_leg_details" in value:
        import capo_geo_routes.types.route_vehicle_leg_details

        out["VehicleLegDetails"] = (
            capo_geo_routes.types.route_vehicle_leg_details.serialize_json(
                value["vehicle_leg_details"]
            )
        )
    if "rental_leg_details" in value:
        import capo_geo_routes.types.route_rental_leg_details

        out["RentalLegDetails"] = (
            capo_geo_routes.types.route_rental_leg_details.serialize_json(
                value["rental_leg_details"]
            )
        )
    if "taxi_leg_details" in value:
        import capo_geo_routes.types.route_taxi_leg_details

        out["TaxiLegDetails"] = (
            capo_geo_routes.types.route_taxi_leg_details.serialize_json(
                value["taxi_leg_details"]
            )
        )
    if "transit_leg_details" in value:
        import capo_geo_routes.types.route_transit_leg_details

        out["TransitLegDetails"] = (
            capo_geo_routes.types.route_transit_leg_details.serialize_json(
                value["transit_leg_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteLeg:
    out: RouteLeg = {}  # type: ignore[typeddict-item]
    if data.get("FerryLegDetails") is not None:
        import capo_geo_routes.types.route_ferry_leg_details

        out["ferry_leg_details"] = (
            capo_geo_routes.types.route_ferry_leg_details.deserialize_json(
                data["FerryLegDetails"]
            )
        )
    if data.get("Geometry") is not None:
        import capo_geo_routes.types.route_leg_geometry

        out["geometry"] = capo_geo_routes.types.route_leg_geometry.deserialize_json(
            data["Geometry"]
        )
    else:
        raise DeserializationError("RouteLeg.geometry required")
    if data.get("Language") is not None:
        out["language"] = data["Language"]
    if data.get("PedestrianLegDetails") is not None:
        import capo_geo_routes.types.route_pedestrian_leg_details

        out["pedestrian_leg_details"] = (
            capo_geo_routes.types.route_pedestrian_leg_details.deserialize_json(
                data["PedestrianLegDetails"]
            )
        )
    if data.get("TravelMode") is not None:
        import capo_geo_routes.types.route_leg_travel_mode

        out["travel_mode"] = (
            capo_geo_routes.types.route_leg_travel_mode.deserialize_json(
                data["TravelMode"]
            )
        )
    else:
        raise DeserializationError("RouteLeg.travel_mode required")
    if data.get("Type") is not None:
        import capo_geo_routes.types.route_leg_type

        out["type"] = capo_geo_routes.types.route_leg_type.deserialize_json(
            data["Type"]
        )
    else:
        raise DeserializationError("RouteLeg.type required")
    if data.get("VehicleLegDetails") is not None:
        import capo_geo_routes.types.route_vehicle_leg_details

        out["vehicle_leg_details"] = (
            capo_geo_routes.types.route_vehicle_leg_details.deserialize_json(
                data["VehicleLegDetails"]
            )
        )
    if data.get("RentalLegDetails") is not None:
        import capo_geo_routes.types.route_rental_leg_details

        out["rental_leg_details"] = (
            capo_geo_routes.types.route_rental_leg_details.deserialize_json(
                data["RentalLegDetails"]
            )
        )
    if data.get("TaxiLegDetails") is not None:
        import capo_geo_routes.types.route_taxi_leg_details

        out["taxi_leg_details"] = (
            capo_geo_routes.types.route_taxi_leg_details.deserialize_json(
                data["TaxiLegDetails"]
            )
        )
    if data.get("TransitLegDetails") is not None:
        import capo_geo_routes.types.route_transit_leg_details

        out["transit_leg_details"] = (
            capo_geo_routes.types.route_transit_leg_details.deserialize_json(
                data["TransitLegDetails"]
            )
        )
    return out
