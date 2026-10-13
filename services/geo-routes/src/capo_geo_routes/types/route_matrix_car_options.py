"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixCarOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.route_matrix_vehicle_license_plate
    import capo_geo_routes.types.sensitive_integer
    import capo_geo_routes.types.speed_kilometers_per_hour


class RouteMatrixCarOptions(TypedDict, closed=True):
    license_plate: NotRequired[
        "capo_geo_routes.types.route_matrix_vehicle_license_plate.RouteMatrixVehicleLicensePlate"
    ]
    """<p>The vehicle License Plate.</p>"""
    max_speed: NotRequired[
        "capo_geo_routes.types.speed_kilometers_per_hour.SpeedKilometersPerHour"
    ]
    """<p>Maximum speed</p> <p> <b>Unit</b>: <code>kilometers per hour</code> </p>"""
    occupancy: NotRequired["capo_geo_routes.types.sensitive_integer.SensitiveInteger"]
    """<p>The number of occupants in the vehicle.</p> <p>Default value: <code>1</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixCarOptions) -> dict:
    out: dict = {}
    if "license_plate" in value:
        import capo_geo_routes.types.route_matrix_vehicle_license_plate

        out["LicensePlate"] = (
            capo_geo_routes.types.route_matrix_vehicle_license_plate.serialize_json(
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


def deserialize_json(data: dict) -> RouteMatrixCarOptions:
    out: RouteMatrixCarOptions = {}  # type: ignore[typeddict-item]
    if data.get("LicensePlate") is not None:
        import capo_geo_routes.types.route_matrix_vehicle_license_plate

        out["license_plate"] = (
            capo_geo_routes.types.route_matrix_vehicle_license_plate.deserialize_json(
                data["LicensePlate"]
            )
        )
    if data.get("MaxSpeed") is not None:
        out["max_speed"] = float(data["MaxSpeed"])
    if data.get("Occupancy") is not None:
        out["occupancy"] = data["Occupancy"]
    return out


def redact_sensitive(value: RouteMatrixCarOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "license_plate" in value:
        out["license_plate"] = "*** Sensitive Data Redacted ***"
    if "max_speed" in value:
        out["max_speed"] = "*** Sensitive Data Redacted ***"
    if "occupancy" in value:
        out["occupancy"] = "*** Sensitive Data Redacted ***"
    return out
