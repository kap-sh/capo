"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineTravelModeOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.isoline_car_options
    import capo_geo_routes.types.isoline_scooter_options
    import capo_geo_routes.types.isoline_truck_options


class IsolineTravelModeOptions(TypedDict, closed=True):
    car: NotRequired["capo_geo_routes.types.isoline_car_options.IsolineCarOptions"]
    """<p>Options specific to passenger vehicle routing (<code>Car</code>, such as vehicle characteristics and license plate restrictions.</p>"""
    scooter: NotRequired[
        "capo_geo_routes.types.isoline_scooter_options.IsolineScooterOptions"
    ]
    """<p>Options specific to scooter routing (<code>Scooter</code>, such as vehicle characteristics and license plate restrictions.</p> <note> <p>When using the <code>Scooter</code> travel mode, controlled-access highways are automatically avoided unless explicitly allowed.</p> </note>"""
    truck: NotRequired[
        "capo_geo_routes.types.isoline_truck_options.IsolineTruckOptions"
    ]
    """<p>Options specific to commercial truck routing (<code>Truck</code>, including vehicle dimensions, weight limits, and hazardous cargo specifications.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IsolineTravelModeOptions) -> dict:
    out: dict = {}
    if "car" in value:
        import capo_geo_routes.types.isoline_car_options

        out["Car"] = capo_geo_routes.types.isoline_car_options.serialize_json(
            value["car"]
        )
    if "scooter" in value:
        import capo_geo_routes.types.isoline_scooter_options

        out["Scooter"] = capo_geo_routes.types.isoline_scooter_options.serialize_json(
            value["scooter"]
        )
    if "truck" in value:
        import capo_geo_routes.types.isoline_truck_options

        out["Truck"] = capo_geo_routes.types.isoline_truck_options.serialize_json(
            value["truck"]
        )
    return out


def deserialize_json(data: dict) -> IsolineTravelModeOptions:
    out: IsolineTravelModeOptions = {}  # type: ignore[typeddict-item]
    if data.get("Car") is not None:
        import capo_geo_routes.types.isoline_car_options

        out["car"] = capo_geo_routes.types.isoline_car_options.deserialize_json(
            data["Car"]
        )
    if data.get("Scooter") is not None:
        import capo_geo_routes.types.isoline_scooter_options

        out["scooter"] = capo_geo_routes.types.isoline_scooter_options.deserialize_json(
            data["Scooter"]
        )
    if data.get("Truck") is not None:
        import capo_geo_routes.types.isoline_truck_options

        out["truck"] = capo_geo_routes.types.isoline_truck_options.deserialize_json(
            data["Truck"]
        )
    return out


def redact_sensitive(value: IsolineTravelModeOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "car" in value:
        import capo_geo_routes.types.isoline_car_options

        out["car"] = capo_geo_routes.types.isoline_car_options.redact_sensitive(
            value["car"]
        )
    if "scooter" in value:
        import capo_geo_routes.types.isoline_scooter_options

        out["scooter"] = capo_geo_routes.types.isoline_scooter_options.redact_sensitive(
            value["scooter"]
        )
    if "truck" in value:
        import capo_geo_routes.types.isoline_truck_options

        out["truck"] = capo_geo_routes.types.isoline_truck_options.redact_sensitive(
            value["truck"]
        )
    return out
