"""Generated from Smithy shape ``com.amazonaws.mediaconnect#StartRouterOutputResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.maintenance_schedule
    import capo_mediaconnect.types.maintenance_schedule_type
    import capo_mediaconnect.types.router_output_arn
    import capo_mediaconnect.types.router_output_state


class StartRouterOutputResponse(TypedDict, closed=True):
    arn: "capo_mediaconnect.types.router_output_arn.RouterOutputArn"
    """<p>The Amazon Resource Name (ARN) of the router output that was started.</p>"""
    name: "str"
    """<p>The name of the router output that was started.</p>"""
    state: "capo_mediaconnect.types.router_output_state.RouterOutputState"
    """<p>The current state of the router output after being started.</p>"""
    maintenance_schedule_type: (
        "capo_mediaconnect.types.maintenance_schedule_type.MaintenanceScheduleType"
    )
    """<p>The type of maintenance schedule associated with the router output.</p>"""
    maintenance_schedule: (
        "capo_mediaconnect.types.maintenance_schedule.MaintenanceSchedule"
    )
    """<p>The details of the maintenance schedule for the router output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartRouterOutputResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    import capo_mediaconnect.types.router_output_state

    out["state"] = capo_mediaconnect.types.router_output_state.serialize_json(
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


def deserialize_json(data: dict) -> StartRouterOutputResponse:
    out: StartRouterOutputResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("state") is not None:
        import capo_mediaconnect.types.router_output_state

        out["state"] = capo_mediaconnect.types.router_output_state.deserialize_json(
            data["state"]
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_mediaconnect.types.router_output_state.RouterOutputState", ""
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
