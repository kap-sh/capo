"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteRentalAfterTravelStep``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.duration_seconds
    import capo_geo_routes.types.route_rental_after_travel_step_type
    import capo_geo_routes.types.sensitive_string


class RouteRentalAfterTravelStep(TypedDict, closed=True):
    duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the step.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    instruction: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>Brief description of the step in the requested language.</p>"""
    type: "capo_geo_routes.types.route_rental_after_travel_step_type.RouteRentalAfterTravelStepType"
    """<p>Type of the step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteRentalAfterTravelStep) -> dict:
    out: dict = {}
    out["Duration"] = value["duration"]
    if "instruction" in value:
        out["Instruction"] = value["instruction"]
    import capo_geo_routes.types.route_rental_after_travel_step_type

    out["Type"] = (
        capo_geo_routes.types.route_rental_after_travel_step_type.serialize_json(
            value["type"]
        )
    )
    return out


def deserialize_json(data: dict) -> RouteRentalAfterTravelStep:
    out: RouteRentalAfterTravelStep = {}  # type: ignore[typeddict-item]
    if data.get("Duration") is not None:
        out["duration"] = data["Duration"]
    else:
        out["duration"] = 0
    if data.get("Instruction") is not None:
        out["instruction"] = data["Instruction"]
    if data.get("Type") is not None:
        import capo_geo_routes.types.route_rental_after_travel_step_type

        out["type"] = (
            capo_geo_routes.types.route_rental_after_travel_step_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_geo_routes.types.route_rental_after_travel_step_type.RouteRentalAfterTravelStepType",
            "",
        )
    return out


def redact_sensitive(value: RouteRentalAfterTravelStep) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "duration" in value:
        out["duration"] = "*** Sensitive Data Redacted ***"
    if "instruction" in value:
        out["instruction"] = "*** Sensitive Data Redacted ***"
    if "type" in value:
        out["type"] = "*** Sensitive Data Redacted ***"
    return out
