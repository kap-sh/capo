"""Generated from Smithy shape ``com.amazonaws.mediaconnect#StartRouterInputResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.maintenance_schedule
    import capo_mediaconnect.types.maintenance_schedule_type
    import capo_mediaconnect.types.router_input_arn
    import capo_mediaconnect.types.router_input_state


class StartRouterInputResponse(TypedDict, closed=True):
    arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn"
    """<p>The ARN of the router input that was started.</p>"""
    name: "str"
    """<p>The name of the router input that was started.</p>"""
    state: "capo_mediaconnect.types.router_input_state.RouterInputState"
    """<p>The current state of the router input after being started.</p>"""
    maintenance_schedule_type: (
        "capo_mediaconnect.types.maintenance_schedule_type.MaintenanceScheduleType"
    )
    """<p>The type of maintenance schedule associated with the router input.</p>"""
    maintenance_schedule: (
        "capo_mediaconnect.types.maintenance_schedule.MaintenanceSchedule"
    )
    """<p>The details of the maintenance schedule for the router input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartRouterInputResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    import capo_mediaconnect.types.router_input_state

    out["state"] = capo_mediaconnect.types.router_input_state.serialize_json(
        value["state"]
    )
    import capo_mediaconnect.types.maintenance_schedule_type

    out["maintenanceScheduleType"] = (
        capo_mediaconnect.types.maintenance_schedule_type.serialize_json(
            value["maintenance_schedule_type"]
        )
    )
    import capo_mediaconnect.types.maintenance_schedule

    out["maintenanceSchedule"] = (
        capo_mediaconnect.types.maintenance_schedule.serialize_json(
            value["maintenance_schedule"]
        )
    )
    return out


def deserialize_json(data: dict) -> StartRouterInputResponse:
    out: StartRouterInputResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("state") is not None:
        import capo_mediaconnect.types.router_input_state

        out["state"] = capo_mediaconnect.types.router_input_state.deserialize_json(
            data["state"]
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_mediaconnect.types.router_input_state.RouterInputState", ""
        )
    if data.get("maintenanceScheduleType") is not None:
        import capo_mediaconnect.types.maintenance_schedule_type

        out["maintenance_schedule_type"] = (
            capo_mediaconnect.types.maintenance_schedule_type.deserialize_json(
                data["maintenanceScheduleType"]
            )
        )
    else:
        import typing

        out["maintenance_schedule_type"] = typing.cast(
            "capo_mediaconnect.types.maintenance_schedule_type.MaintenanceScheduleType",
            "",
        )
    if data.get("maintenanceSchedule") is not None:
        import capo_mediaconnect.types.maintenance_schedule

        out["maintenance_schedule"] = (
            capo_mediaconnect.types.maintenance_schedule.deserialize_json(
                data["maintenanceSchedule"]
            )
        )
    else:
        import capo_mediaconnect.types._unknown

        out["maintenance_schedule"] = (
            capo_mediaconnect.types._unknown.UnknownUnionMember("")
        )
    return out
