"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTaxiTransportModeDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.route_engine_type
    import capo_geo_routes.types.route_taxi_mode
    import capo_geo_routes.types.sensitive_integer
    import capo_geo_routes.types.sensitive_string


class RouteTaxiTransportModeDetails(TypedDict, closed=True):
    available_seats: NotRequired[
        "capo_geo_routes.types.sensitive_integer.SensitiveInteger"
    ]
    """<p>Number of available seats in the vehicle.</p>"""
    category: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>Human readable transport category.</p>"""
    color: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>Color of the transport polyline and background for the transport name.</p>"""
    engine: NotRequired["capo_geo_routes.types.route_engine_type.RouteEngineType"]
    """<p>Vehicle engine type.</p>"""
    license_plate: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>Vehicle license plate number.</p>"""
    mode: "capo_geo_routes.types.route_taxi_mode.RouteTaxiMode"
    """<p>Mode of the taxi transport.</p>"""
    model: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>Vehicle model.</p>"""
    name: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>Vehicle name or mobility provider name.</p>"""
    text_color: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>Color of the transport name text.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTaxiTransportModeDetails) -> dict:
    out: dict = {}
    if "available_seats" in value:
        out["AvailableSeats"] = value["available_seats"]
    if "category" in value:
        out["Category"] = value["category"]
    if "color" in value:
        out["Color"] = value["color"]
    if "engine" in value:
        import capo_geo_routes.types.route_engine_type

        out["Engine"] = capo_geo_routes.types.route_engine_type.serialize_json(
            value["engine"]
        )
    if "license_plate" in value:
        out["LicensePlate"] = value["license_plate"]
    import capo_geo_routes.types.route_taxi_mode

    out["Mode"] = capo_geo_routes.types.route_taxi_mode.serialize_json(value["mode"])
    if "model" in value:
        out["Model"] = value["model"]
    if "name" in value:
        out["Name"] = value["name"]
    if "text_color" in value:
        out["TextColor"] = value["text_color"]
    return out


def deserialize_json(data: dict) -> RouteTaxiTransportModeDetails:
    out: RouteTaxiTransportModeDetails = {}  # type: ignore[typeddict-item]
    if data.get("AvailableSeats") is not None:
        out["available_seats"] = data["AvailableSeats"]
    if data.get("Category") is not None:
        out["category"] = data["Category"]
    if data.get("Color") is not None:
        out["color"] = data["Color"]
    if data.get("Engine") is not None:
        import capo_geo_routes.types.route_engine_type

        out["engine"] = capo_geo_routes.types.route_engine_type.deserialize_json(
            data["Engine"]
        )
    if data.get("LicensePlate") is not None:
        out["license_plate"] = data["LicensePlate"]
    if data.get("Mode") is not None:
        import capo_geo_routes.types.route_taxi_mode

        out["mode"] = capo_geo_routes.types.route_taxi_mode.deserialize_json(
            data["Mode"]
        )
    else:
        raise DeserializationError("RouteTaxiTransportModeDetails.mode required")
    if data.get("Model") is not None:
        out["model"] = data["Model"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("TextColor") is not None:
        out["text_color"] = data["TextColor"]
    return out


def redact_sensitive(value: RouteTaxiTransportModeDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "available_seats" in value:
        out["available_seats"] = "*** Sensitive Data Redacted ***"
    if "category" in value:
        out["category"] = "*** Sensitive Data Redacted ***"
    if "color" in value:
        out["color"] = "*** Sensitive Data Redacted ***"
    if "engine" in value:
        out["engine"] = "*** Sensitive Data Redacted ***"
    if "license_plate" in value:
        out["license_plate"] = "*** Sensitive Data Redacted ***"
    if "mode" in value:
        out["mode"] = "*** Sensitive Data Redacted ***"
    if "model" in value:
        out["model"] = "*** Sensitive Data Redacted ***"
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "text_color" in value:
        out["text_color"] = "*** Sensitive Data Redacted ***"
    return out
