"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteScooterOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.route_engine_type
    import capo_geo_routes.types.route_vehicle_license_plate
    import capo_geo_routes.types.sensitive_integer
    import capo_geo_routes.types.speed_kilometers_per_hour


class RouteScooterOptions(TypedDict, closed=True):
    engine_type: NotRequired["capo_geo_routes.types.route_engine_type.RouteEngineType"]
    """<p> Engine type of the vehicle. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    license_plate: NotRequired[
        "capo_geo_routes.types.route_vehicle_license_plate.RouteVehicleLicensePlate"
    ]
    """<p>The vehicle License Plate.</p>"""
    max_speed: NotRequired[
        "capo_geo_routes.types.speed_kilometers_per_hour.SpeedKilometersPerHour"
    ]
    """<p> Maximum speed Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p> <p> <b>Unit</b>: <code>kilometers per hour</code> </p>"""
    occupancy: NotRequired["capo_geo_routes.types.sensitive_integer.SensitiveInteger"]
    """<p> The number of occupants in the vehicle. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p> <p>Default value: <code>1</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteScooterOptions) -> dict:
    out: dict = {}
    if "engine_type" in value:
        import capo_geo_routes.types.route_engine_type

        out["EngineType"] = capo_geo_routes.types.route_engine_type.serialize_json(
            value["engine_type"]
        )
    if "license_plate" in value:
        import capo_geo_routes.types.route_vehicle_license_plate

        out["LicensePlate"] = (
            capo_geo_routes.types.route_vehicle_license_plate.serialize_json(
                value["license_plate"]
            )
        )
    if "max_speed" in value:
        out["MaxSpeed"] = (
            "NaN"
            if value["max_speed"] != value["max_speed"]
            else "Infinity"
            if value["max_speed"] == float("inf")
            else "-Infinity"
            if value["max_speed"] == float("-inf")
            else value["max_speed"]
        )
    if "occupancy" in value:
        out["Occupancy"] = value["occupancy"]
    return out


def deserialize_json(data: dict) -> RouteScooterOptions:
    out: RouteScooterOptions = {}  # type: ignore[typeddict-item]
    if data.get("EngineType") is not None:
        import capo_geo_routes.types.route_engine_type

        out["engine_type"] = capo_geo_routes.types.route_engine_type.deserialize_json(
            data["EngineType"]
        )
    if data.get("LicensePlate") is not None:
        import capo_geo_routes.types.route_vehicle_license_plate

        out["license_plate"] = (
            capo_geo_routes.types.route_vehicle_license_plate.deserialize_json(
                data["LicensePlate"]
            )
        )
    if data.get("MaxSpeed") is not None:
        out["max_speed"] = float(data["MaxSpeed"])
    if data.get("Occupancy") is not None:
        out["occupancy"] = data["Occupancy"]
    return out
