"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleAfterTravelStep``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.duration_seconds
    import capo_geo_routes.types.route_charge_step_details
    import capo_geo_routes.types.route_vehicle_after_travel_step_type
    import capo_geo_routes.types.sensitive_string


class RouteVehicleAfterTravelStep(TypedDict, closed=True):
    charge_step_details: NotRequired[
        "capo_geo_routes.types.route_charge_step_details.RouteChargeStepDetails"
    ]
    """<p>Details that are specific to a Charge step.</p> <p> <b>Unit</b>: <code>KwH </code> </p>"""
    duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the step.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    instruction: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>Brief description of the step in the requested language.</p> <note> <p>Only available when the TravelStepType is Default.</p> </note>"""
    type: "capo_geo_routes.types.route_vehicle_after_travel_step_type.RouteVehicleAfterTravelStepType"
    """<p>Type of the step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehicleAfterTravelStep) -> dict:
    out: dict = {}
    if "charge_step_details" in value:
        import capo_geo_routes.types.route_charge_step_details

        out["ChargeStepDetails"] = (
            capo_geo_routes.types.route_charge_step_details.serialize_json(
                value["charge_step_details"]
            )
        )
    out["Duration"] = value["duration"]
    if "instruction" in value:
        out["Instruction"] = value["instruction"]
    import capo_geo_routes.types.route_vehicle_after_travel_step_type

    out["Type"] = (
        capo_geo_routes.types.route_vehicle_after_travel_step_type.serialize_json(
            value["type"]
        )
    )
    return out


def deserialize_json(data: dict) -> RouteVehicleAfterTravelStep:
    out: RouteVehicleAfterTravelStep = {}  # type: ignore[typeddict-item]
    if data.get("ChargeStepDetails") is not None:
        import capo_geo_routes.types.route_charge_step_details

        out["charge_step_details"] = (
            capo_geo_routes.types.route_charge_step_details.deserialize_json(
                data["ChargeStepDetails"]
            )
        )
    if data.get("Duration") is not None:
        out["duration"] = data["Duration"]
    else:
        out["duration"] = 0
    if data.get("Instruction") is not None:
        out["instruction"] = data["Instruction"]
    if data.get("Type") is not None:
        import capo_geo_routes.types.route_vehicle_after_travel_step_type

        out["type"] = (
            capo_geo_routes.types.route_vehicle_after_travel_step_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_geo_routes.types.route_vehicle_after_travel_step_type.RouteVehicleAfterTravelStepType",
            "",
        )
    return out


def redact_sensitive(value: RouteVehicleAfterTravelStep) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "charge_step_details" in value:
        import capo_geo_routes.types.route_charge_step_details

        out["charge_step_details"] = (
            capo_geo_routes.types.route_charge_step_details.redact_sensitive(
                value["charge_step_details"]
            )
        )
    if "duration" in value:
        out["duration"] = "*** Sensitive Data Redacted ***"
    if "instruction" in value:
        out["instruction"] = "*** Sensitive Data Redacted ***"
    if "type" in value:
        out["type"] = "*** Sensitive Data Redacted ***"
    return out
