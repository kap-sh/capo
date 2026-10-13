"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitTravelStep``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.distance_meters
    import capo_geo_routes.types.duration_seconds
    import capo_geo_routes.types.route_transit_travel_step_type
    import capo_geo_routes.types.sensitive_string


class RouteTransitTravelStep(TypedDict, closed=True):
    distance: NotRequired["capo_geo_routes.types.distance_meters.DistanceMeters"]
    """<p>Distance of the step.</p> <p> <b>Unit</b>: <code>meters</code> </p>"""
    duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the step.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    geometry_offset: NotRequired["int"]
    """<p>Offset in the leg geometry corresponding to the start of this step.</p>"""
    instruction: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>Brief description of the step in the requested language.</p>"""
    type: "capo_geo_routes.types.route_transit_travel_step_type.RouteTransitTravelStepType"
    """<p>Type of the step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitTravelStep) -> dict:
    out: dict = {}
    if "distance" in value:
        out["Distance"] = value["distance"]
    out["Duration"] = value["duration"]
    if "geometry_offset" in value:
        out["GeometryOffset"] = value["geometry_offset"]
    if "instruction" in value:
        out["Instruction"] = value["instruction"]
    import capo_geo_routes.types.route_transit_travel_step_type

    out["Type"] = capo_geo_routes.types.route_transit_travel_step_type.serialize_json(
        value["type"]
    )
    return out


def deserialize_json(data: dict) -> RouteTransitTravelStep:
    out: RouteTransitTravelStep = {}  # type: ignore[typeddict-item]
    if data.get("Distance") is not None:
        out["distance"] = data["Distance"]
    if data.get("Duration") is not None:
        out["duration"] = data["Duration"]
    else:
        raise DeserializationError("RouteTransitTravelStep.duration required")
    if data.get("GeometryOffset") is not None:
        out["geometry_offset"] = data["GeometryOffset"]
    if data.get("Instruction") is not None:
        out["instruction"] = data["Instruction"]
    if data.get("Type") is not None:
        import capo_geo_routes.types.route_transit_travel_step_type

        out["type"] = (
            capo_geo_routes.types.route_transit_travel_step_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("RouteTransitTravelStep.type required")
    return out


def redact_sensitive(value: RouteTransitTravelStep) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "distance" in value:
        out["distance"] = "*** Sensitive Data Redacted ***"
    if "duration" in value:
        out["duration"] = "*** Sensitive Data Redacted ***"
    if "instruction" in value:
        out["instruction"] = "*** Sensitive Data Redacted ***"
    if "type" in value:
        out["type"] = "*** Sensitive Data Redacted ***"
    return out
