"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleTravelStep``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.distance_meters
    import capo_geo_routes.types.duration_seconds
    import capo_geo_routes.types.localized_string_list
    import capo_geo_routes.types.route_continue_highway_step_details
    import capo_geo_routes.types.route_continue_step_details
    import capo_geo_routes.types.route_enter_highway_step_details
    import capo_geo_routes.types.route_exit_step_details
    import capo_geo_routes.types.route_keep_step_details
    import capo_geo_routes.types.route_ramp_step_details
    import capo_geo_routes.types.route_road
    import capo_geo_routes.types.route_roundabout_enter_step_details
    import capo_geo_routes.types.route_roundabout_exit_step_details
    import capo_geo_routes.types.route_roundabout_pass_step_details
    import capo_geo_routes.types.route_signpost
    import capo_geo_routes.types.route_turn_step_details
    import capo_geo_routes.types.route_u_turn_step_details
    import capo_geo_routes.types.route_vehicle_travel_step_type
    import capo_geo_routes.types.sensitive_string


class RouteVehicleTravelStep(TypedDict, closed=True):
    continue_highway_step_details: NotRequired[
        "capo_geo_routes.types.route_continue_highway_step_details.RouteContinueHighwayStepDetails"
    ]
    """<p>Details that are specific to a Continue Highway step.</p>"""
    continue_step_details: NotRequired[
        "capo_geo_routes.types.route_continue_step_details.RouteContinueStepDetails"
    ]
    """<p>Details that are specific to a Continue step.</p>"""
    current_road: NotRequired["capo_geo_routes.types.route_road.RouteRoad"]
    """<p>Details of the current road.</p>"""
    distance: "capo_geo_routes.types.distance_meters.DistanceMeters"
    """<p>Distance of the step.</p>"""
    duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the step.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    enter_highway_step_details: NotRequired[
        "capo_geo_routes.types.route_enter_highway_step_details.RouteEnterHighwayStepDetails"
    ]
    """<p>Details that are specific to a Enter Highway step.</p>"""
    exit_number: NotRequired[
        "capo_geo_routes.types.localized_string_list.LocalizedStringList"
    ]
    """<p>Exit number of the road exit, if applicable.</p>"""
    exit_step_details: NotRequired[
        "capo_geo_routes.types.route_exit_step_details.RouteExitStepDetails"
    ]
    """<p>Details that are specific to a Roundabout Exit step.</p>"""
    geometry_offset: NotRequired["int"]
    """<p>Offset in the leg geometry corresponding to the start of this step.</p>"""
    instruction: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>Brief description of the step in the requested language.</p> <note> <p>Only available when the TravelStepType is Default.</p> </note>"""
    keep_step_details: NotRequired[
        "capo_geo_routes.types.route_keep_step_details.RouteKeepStepDetails"
    ]
    """<p>Details that are specific to a Keep step.</p>"""
    next_road: NotRequired["capo_geo_routes.types.route_road.RouteRoad"]
    """<p>Details of the next road. See RouteRoad for details of sub-attributes.</p>"""
    ramp_step_details: NotRequired[
        "capo_geo_routes.types.route_ramp_step_details.RouteRampStepDetails"
    ]
    """<p>Details that are specific to a Ramp step.</p>"""
    roundabout_enter_step_details: NotRequired[
        "capo_geo_routes.types.route_roundabout_enter_step_details.RouteRoundaboutEnterStepDetails"
    ]
    """<p>Details that are specific to a Roundabout Enter step.</p>"""
    roundabout_exit_step_details: NotRequired[
        "capo_geo_routes.types.route_roundabout_exit_step_details.RouteRoundaboutExitStepDetails"
    ]
    """<p>Details that are specific to a Roundabout Exit step.</p>"""
    roundabout_pass_step_details: NotRequired[
        "capo_geo_routes.types.route_roundabout_pass_step_details.RouteRoundaboutPassStepDetails"
    ]
    """<p>Details that are specific to a Roundabout Pass step.</p>"""
    signpost: NotRequired["capo_geo_routes.types.route_signpost.RouteSignpost"]
    """<p>Sign post information of the action, applicable only for TurnByTurn steps. See RouteSignpost for details of sub-attributes.</p>"""
    turn_step_details: NotRequired[
        "capo_geo_routes.types.route_turn_step_details.RouteTurnStepDetails"
    ]
    """<p>Details that are specific to a Turn step.</p>"""
    type: "capo_geo_routes.types.route_vehicle_travel_step_type.RouteVehicleTravelStepType"
    """<p>Type of the step.</p>"""
    u_turn_step_details: NotRequired[
        "capo_geo_routes.types.route_u_turn_step_details.RouteUTurnStepDetails"
    ]
    """<p>Details that are specific to a Turn step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehicleTravelStep) -> dict:
    out: dict = {}
    if "continue_highway_step_details" in value:
        import capo_geo_routes.types.route_continue_highway_step_details

        out["ContinueHighwayStepDetails"] = (
            capo_geo_routes.types.route_continue_highway_step_details.serialize_json(
                value["continue_highway_step_details"]
            )
        )
    if "continue_step_details" in value:
        import capo_geo_routes.types.route_continue_step_details

        out["ContinueStepDetails"] = (
            capo_geo_routes.types.route_continue_step_details.serialize_json(
                value["continue_step_details"]
            )
        )
    if "current_road" in value:
        import capo_geo_routes.types.route_road

        out["CurrentRoad"] = capo_geo_routes.types.route_road.serialize_json(
            value["current_road"]
        )
    out["Distance"] = value.get("distance", 0)
    out["Duration"] = value.get("duration", 0)
    if "enter_highway_step_details" in value:
        import capo_geo_routes.types.route_enter_highway_step_details

        out["EnterHighwayStepDetails"] = (
            capo_geo_routes.types.route_enter_highway_step_details.serialize_json(
                value["enter_highway_step_details"]
            )
        )
    if "exit_number" in value:
        import capo_geo_routes.types.localized_string_list

        out["ExitNumber"] = capo_geo_routes.types.localized_string_list.serialize_json(
            value["exit_number"]
        )
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
    if "next_road" in value:
        import capo_geo_routes.types.route_road

        out["NextRoad"] = capo_geo_routes.types.route_road.serialize_json(
            value["next_road"]
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
    if "signpost" in value:
        import capo_geo_routes.types.route_signpost

        out["Signpost"] = capo_geo_routes.types.route_signpost.serialize_json(
            value["signpost"]
        )
    if "turn_step_details" in value:
        import capo_geo_routes.types.route_turn_step_details

        out["TurnStepDetails"] = (
            capo_geo_routes.types.route_turn_step_details.serialize_json(
                value["turn_step_details"]
            )
        )
    import capo_geo_routes.types.route_vehicle_travel_step_type

    out["Type"] = capo_geo_routes.types.route_vehicle_travel_step_type.serialize_json(
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


def deserialize_json(data: dict) -> RouteVehicleTravelStep:
    out: RouteVehicleTravelStep = {}  # type: ignore[typeddict-item]
    if data.get("ContinueHighwayStepDetails") is not None:
        import capo_geo_routes.types.route_continue_highway_step_details

        out["continue_highway_step_details"] = (
            capo_geo_routes.types.route_continue_highway_step_details.deserialize_json(
                data["ContinueHighwayStepDetails"]
            )
        )
    if data.get("ContinueStepDetails") is not None:
        import capo_geo_routes.types.route_continue_step_details

        out["continue_step_details"] = (
            capo_geo_routes.types.route_continue_step_details.deserialize_json(
                data["ContinueStepDetails"]
            )
        )
    if data.get("CurrentRoad") is not None:
        import capo_geo_routes.types.route_road

        out["current_road"] = capo_geo_routes.types.route_road.deserialize_json(
            data["CurrentRoad"]
        )
    if data.get("Distance") is not None:
        out["distance"] = data["Distance"]
    else:
        out["distance"] = 0
    if data.get("Duration") is not None:
        out["duration"] = data["Duration"]
    else:
        out["duration"] = 0
    if data.get("EnterHighwayStepDetails") is not None:
        import capo_geo_routes.types.route_enter_highway_step_details

        out["enter_highway_step_details"] = (
            capo_geo_routes.types.route_enter_highway_step_details.deserialize_json(
                data["EnterHighwayStepDetails"]
            )
        )
    if data.get("ExitNumber") is not None:
        import capo_geo_routes.types.localized_string_list

        out["exit_number"] = (
            capo_geo_routes.types.localized_string_list.deserialize_json(
                data["ExitNumber"]
            )
        )
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
    if data.get("NextRoad") is not None:
        import capo_geo_routes.types.route_road

        out["next_road"] = capo_geo_routes.types.route_road.deserialize_json(
            data["NextRoad"]
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
    if data.get("Signpost") is not None:
        import capo_geo_routes.types.route_signpost

        out["signpost"] = capo_geo_routes.types.route_signpost.deserialize_json(
            data["Signpost"]
        )
    if data.get("TurnStepDetails") is not None:
        import capo_geo_routes.types.route_turn_step_details

        out["turn_step_details"] = (
            capo_geo_routes.types.route_turn_step_details.deserialize_json(
                data["TurnStepDetails"]
            )
        )
    if data.get("Type") is not None:
        import capo_geo_routes.types.route_vehicle_travel_step_type

        out["type"] = (
            capo_geo_routes.types.route_vehicle_travel_step_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_geo_routes.types.route_vehicle_travel_step_type.RouteVehicleTravelStepType",
            "",
        )
    if data.get("UTurnStepDetails") is not None:
        import capo_geo_routes.types.route_u_turn_step_details

        out["u_turn_step_details"] = (
            capo_geo_routes.types.route_u_turn_step_details.deserialize_json(
                data["UTurnStepDetails"]
            )
        )
    return out


def redact_sensitive(value: RouteVehicleTravelStep) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "continue_highway_step_details" in value:
        import capo_geo_routes.types.route_continue_highway_step_details

        out["continue_highway_step_details"] = (
            capo_geo_routes.types.route_continue_highway_step_details.redact_sensitive(
                value["continue_highway_step_details"]
            )
        )
    if "continue_step_details" in value:
        import capo_geo_routes.types.route_continue_step_details

        out["continue_step_details"] = (
            capo_geo_routes.types.route_continue_step_details.redact_sensitive(
                value["continue_step_details"]
            )
        )
    if "current_road" in value:
        import capo_geo_routes.types.route_road

        out["current_road"] = capo_geo_routes.types.route_road.redact_sensitive(
            value["current_road"]
        )
    if "distance" in value:
        out["distance"] = "*** Sensitive Data Redacted ***"
    if "duration" in value:
        out["duration"] = "*** Sensitive Data Redacted ***"
    if "enter_highway_step_details" in value:
        import capo_geo_routes.types.route_enter_highway_step_details

        out["enter_highway_step_details"] = (
            capo_geo_routes.types.route_enter_highway_step_details.redact_sensitive(
                value["enter_highway_step_details"]
            )
        )
    if "exit_number" in value:
        import capo_geo_routes.types.localized_string_list

        out["exit_number"] = (
            capo_geo_routes.types.localized_string_list.redact_sensitive(
                value["exit_number"]
            )
        )
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
    if "next_road" in value:
        import capo_geo_routes.types.route_road

        out["next_road"] = capo_geo_routes.types.route_road.redact_sensitive(
            value["next_road"]
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
    if "signpost" in value:
        import capo_geo_routes.types.route_signpost

        out["signpost"] = capo_geo_routes.types.route_signpost.redact_sensitive(
            value["signpost"]
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
