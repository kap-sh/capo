"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTaxiTravelStep``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.distance_meters
    import capo_geo_routes.types.duration_seconds
    import capo_geo_routes.types.route_continue_step_details
    import capo_geo_routes.types.route_exit_step_details
    import capo_geo_routes.types.route_keep_step_details
    import capo_geo_routes.types.route_ramp_step_details
    import capo_geo_routes.types.route_roundabout_enter_step_details
    import capo_geo_routes.types.route_roundabout_exit_step_details
    import capo_geo_routes.types.route_roundabout_pass_step_details
    import capo_geo_routes.types.route_taxi_travel_step_type
    import capo_geo_routes.types.route_turn_step_details
    import capo_geo_routes.types.route_u_turn_step_details
    import capo_geo_routes.types.sensitive_string


class RouteTaxiTravelStep(TypedDict, closed=True):
    continue_step_details: NotRequired[
        "capo_geo_routes.types.route_continue_step_details.RouteContinueStepDetails"
    ]
    distance: NotRequired["capo_geo_routes.types.distance_meters.DistanceMeters"]
    """<p>Distance of the step.</p> <p> <b>Unit</b>: <code>meters</code> </p>"""
    duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the step.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    exit_step_details: NotRequired[
        "capo_geo_routes.types.route_exit_step_details.RouteExitStepDetails"
    ]
    geometry_offset: NotRequired["int"]
    """<p>Offset in the leg geometry corresponding to the start of this step.</p>"""
    instruction: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>Brief description of the step in the requested language.</p>"""
    keep_step_details: NotRequired[
        "capo_geo_routes.types.route_keep_step_details.RouteKeepStepDetails"
    ]
    ramp_step_details: NotRequired[
        "capo_geo_routes.types.route_ramp_step_details.RouteRampStepDetails"
    ]
    roundabout_enter_step_details: NotRequired[
        "capo_geo_routes.types.route_roundabout_enter_step_details.RouteRoundaboutEnterStepDetails"
    ]
    roundabout_exit_step_details: NotRequired[
        "capo_geo_routes.types.route_roundabout_exit_step_details.RouteRoundaboutExitStepDetails"
    ]
    roundabout_pass_step_details: NotRequired[
        "capo_geo_routes.types.route_roundabout_pass_step_details.RouteRoundaboutPassStepDetails"
    ]
    turn_step_details: NotRequired[
        "capo_geo_routes.types.route_turn_step_details.RouteTurnStepDetails"
    ]
    type: "capo_geo_routes.types.route_taxi_travel_step_type.RouteTaxiTravelStepType"
    """<p>Type of the step.</p>"""
    u_turn_step_details: NotRequired[
        "capo_geo_routes.types.route_u_turn_step_details.RouteUTurnStepDetails"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTaxiTravelStep) -> dict:
    out: dict = {}
    if "continue_step_details" in value:
        import capo_geo_routes.types.route_continue_step_details

        out["ContinueStepDetails"] = (
            capo_geo_routes.types.route_continue_step_details.serialize_json(
                value["continue_step_details"]
            )
        )
    if "distance" in value:
        out["Distance"] = value["distance"]
    out["Duration"] = value["duration"]
    if "exit_step_details" in value:
        import capo_geo_routes.types.route_exit_step_details

        out["ExitStepDetails"] = (
            capo_geo_routes.types.route_exit_step_details.serialize_json(
                value["exit_step_details"]
            )
        )
    if "geometry_offset" in value:
        out["GeometryOffset"] = value["geometry_offset"]
    if "instruction" in value:
        out["Instruction"] = value["instruction"]
    if "keep_step_details" in value:
        import capo_geo_routes.types.route_keep_step_details

        out["KeepStepDetails"] = (
            capo_geo_routes.types.route_keep_step_details.serialize_json(
                value["keep_step_details"]
            )
        )
    if "ramp_step_details" in value:
        import capo_geo_routes.types.route_ramp_step_details

        out["RampStepDetails"] = (
            capo_geo_routes.types.route_ramp_step_details.serialize_json(
                value["ramp_step_details"]
            )
        )
    if "roundabout_enter_step_details" in value:
        import capo_geo_routes.types.route_roundabout_enter_step_details

        out["RoundaboutEnterStepDetails"] = (
            capo_geo_routes.types.route_roundabout_enter_step_details.serialize_json(
                value["roundabout_enter_step_details"]
            )
        )
    if "roundabout_exit_step_details" in value:
        import capo_geo_routes.types.route_roundabout_exit_step_details

        out["RoundaboutExitStepDetails"] = (
            capo_geo_routes.types.route_roundabout_exit_step_details.serialize_json(
                value["roundabout_exit_step_details"]
            )
        )
    if "roundabout_pass_step_details" in value:
        import capo_geo_routes.types.route_roundabout_pass_step_details

        out["RoundaboutPassStepDetails"] = (
            capo_geo_routes.types.route_roundabout_pass_step_details.serialize_json(
                value["roundabout_pass_step_details"]
            )
        )
    if "turn_step_details" in value:
        import capo_geo_routes.types.route_turn_step_details

        out["TurnStepDetails"] = (
            capo_geo_routes.types.route_turn_step_details.serialize_json(
                value["turn_step_details"]
            )
        )
    import capo_geo_routes.types.route_taxi_travel_step_type

    out["Type"] = capo_geo_routes.types.route_taxi_travel_step_type.serialize_json(
        value["type"]
    )
    if "u_turn_step_details" in value:
        import capo_geo_routes.types.route_u_turn_step_details

        out["UTurnStepDetails"] = (
            capo_geo_routes.types.route_u_turn_step_details.serialize_json(
                value["u_turn_step_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteTaxiTravelStep:
    out: RouteTaxiTravelStep = {}  # type: ignore[typeddict-item]
    if data.get("ContinueStepDetails") is not None:
        import capo_geo_routes.types.route_continue_step_details

        out["continue_step_details"] = (
            capo_geo_routes.types.route_continue_step_details.deserialize_json(
                data["ContinueStepDetails"]
            )
        )
    if data.get("Distance") is not None:
        out["distance"] = data["Distance"]
    if data.get("Duration") is not None:
        out["duration"] = data["Duration"]
    else:
        raise DeserializationError("RouteTaxiTravelStep.duration required")
    if data.get("ExitStepDetails") is not None:
        import capo_geo_routes.types.route_exit_step_details

        out["exit_step_details"] = (
            capo_geo_routes.types.route_exit_step_details.deserialize_json(
                data["ExitStepDetails"]
            )
        )
    if data.get("GeometryOffset") is not None:
        out["geometry_offset"] = data["GeometryOffset"]
    if data.get("Instruction") is not None:
        out["instruction"] = data["Instruction"]
    if data.get("KeepStepDetails") is not None:
        import capo_geo_routes.types.route_keep_step_details

        out["keep_step_details"] = (
            capo_geo_routes.types.route_keep_step_details.deserialize_json(
                data["KeepStepDetails"]
            )
        )
    if data.get("RampStepDetails") is not None:
        import capo_geo_routes.types.route_ramp_step_details

        out["ramp_step_details"] = (
            capo_geo_routes.types.route_ramp_step_details.deserialize_json(
                data["RampStepDetails"]
            )
        )
    if data.get("RoundaboutEnterStepDetails") is not None:
        import capo_geo_routes.types.route_roundabout_enter_step_details

        out["roundabout_enter_step_details"] = (
            capo_geo_routes.types.route_roundabout_enter_step_details.deserialize_json(
                data["RoundaboutEnterStepDetails"]
            )
        )
    if data.get("RoundaboutExitStepDetails") is not None:
        import capo_geo_routes.types.route_roundabout_exit_step_details

        out["roundabout_exit_step_details"] = (
            capo_geo_routes.types.route_roundabout_exit_step_details.deserialize_json(
                data["RoundaboutExitStepDetails"]
            )
        )
    if data.get("RoundaboutPassStepDetails") is not None:
        import capo_geo_routes.types.route_roundabout_pass_step_details

        out["roundabout_pass_step_details"] = (
            capo_geo_routes.types.route_roundabout_pass_step_details.deserialize_json(
                data["RoundaboutPassStepDetails"]
            )
        )
    if data.get("TurnStepDetails") is not None:
        import capo_geo_routes.types.route_turn_step_details

        out["turn_step_details"] = (
            capo_geo_routes.types.route_turn_step_details.deserialize_json(
                data["TurnStepDetails"]
            )
        )
    if data.get("Type") is not None:
        import capo_geo_routes.types.route_taxi_travel_step_type

        out["type"] = (
            capo_geo_routes.types.route_taxi_travel_step_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("RouteTaxiTravelStep.type required")
    if data.get("UTurnStepDetails") is not None:
        import capo_geo_routes.types.route_u_turn_step_details

        out["u_turn_step_details"] = (
            capo_geo_routes.types.route_u_turn_step_details.deserialize_json(
                data["UTurnStepDetails"]
            )
        )
    return out


def redact_sensitive(value: RouteTaxiTravelStep) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "continue_step_details" in value:
        import capo_geo_routes.types.route_continue_step_details

        out["continue_step_details"] = (
            capo_geo_routes.types.route_continue_step_details.redact_sensitive(
                value["continue_step_details"]
            )
        )
    if "distance" in value:
        out["distance"] = "*** Sensitive Data Redacted ***"
    if "duration" in value:
        out["duration"] = "*** Sensitive Data Redacted ***"
    if "exit_step_details" in value:
        import capo_geo_routes.types.route_exit_step_details

        out["exit_step_details"] = (
            capo_geo_routes.types.route_exit_step_details.redact_sensitive(
                value["exit_step_details"]
            )
        )
    if "instruction" in value:
        out["instruction"] = "*** Sensitive Data Redacted ***"
    if "keep_step_details" in value:
        import capo_geo_routes.types.route_keep_step_details

        out["keep_step_details"] = (
            capo_geo_routes.types.route_keep_step_details.redact_sensitive(
                value["keep_step_details"]
            )
        )
    if "ramp_step_details" in value:
        import capo_geo_routes.types.route_ramp_step_details

        out["ramp_step_details"] = (
            capo_geo_routes.types.route_ramp_step_details.redact_sensitive(
                value["ramp_step_details"]
            )
        )
    if "roundabout_enter_step_details" in value:
        import capo_geo_routes.types.route_roundabout_enter_step_details

        out["roundabout_enter_step_details"] = (
            capo_geo_routes.types.route_roundabout_enter_step_details.redact_sensitive(
                value["roundabout_enter_step_details"]
            )
        )
    if "roundabout_exit_step_details" in value:
        import capo_geo_routes.types.route_roundabout_exit_step_details

        out["roundabout_exit_step_details"] = (
            capo_geo_routes.types.route_roundabout_exit_step_details.redact_sensitive(
                value["roundabout_exit_step_details"]
            )
        )
    if "roundabout_pass_step_details" in value:
        import capo_geo_routes.types.route_roundabout_pass_step_details

        out["roundabout_pass_step_details"] = (
            capo_geo_routes.types.route_roundabout_pass_step_details.redact_sensitive(
                value["roundabout_pass_step_details"]
            )
        )
    if "turn_step_details" in value:
        import capo_geo_routes.types.route_turn_step_details

        out["turn_step_details"] = (
            capo_geo_routes.types.route_turn_step_details.redact_sensitive(
                value["turn_step_details"]
            )
        )
    if "type" in value:
        out["type"] = "*** Sensitive Data Redacted ***"
    if "u_turn_step_details" in value:
        import capo_geo_routes.types.route_u_turn_step_details

        out["u_turn_step_details"] = (
            capo_geo_routes.types.route_u_turn_step_details.redact_sensitive(
                value["u_turn_step_details"]
            )
        )
    return out
