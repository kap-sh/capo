"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListedRouterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mediaconnect.types.maintenance_schedule
    import capo_mediaconnect.types.maintenance_schedule_type
    import capo_mediaconnect.types.router_input_arn
    import capo_mediaconnect.types.router_input_state
    import capo_mediaconnect.types.router_input_type
    import capo_mediaconnect.types.router_network_interface_arn
    import capo_mediaconnect.types.routing_scope


class ListedRouterInput(TypedDict, closed=True):
    name: "str"
    """<p>The name of the router input.</p>"""
    arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn"
    """<p>The Amazon Resource Name (ARN) of the router input.</p>"""
    id: "str"
    """<p>The unique identifier of the router input.</p>"""
    input_type: "capo_mediaconnect.types.router_input_type.RouterInputType"
    """<p>The type of the router input.</p>"""
    state: "capo_mediaconnect.types.router_input_state.RouterInputState"
    """<p>The overall state of the router input.</p>"""
    routed_outputs: "int"
    """<p>The number of router outputs that are associated with this router input.</p>"""
    region_name: "str"
    """<p>The Amazon Web Services Region where the router input is located.</p>"""
    availability_zone: "str"
    """<p>The Availability Zone of the router input.</p>"""
    maximum_bitrate: "int"
    """<p>The maximum bitrate of the router input.</p>"""
    routing_scope: "capo_mediaconnect.types.routing_scope.RoutingScope"
    """<p>Indicates whether the router input is configured for Regional or global routing.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the router input was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp when the router input was last updated.</p>"""
    message_count: "int"
    """<p>The number of messages associated with the router input.</p>"""
    network_interface_arn: NotRequired[
        "capo_mediaconnect.types.router_network_interface_arn.RouterNetworkInterfaceArn"
    ]
    """<p>The ARN of the network interface associated with the router input.</p>"""
    maintenance_schedule_type: NotRequired[
        "capo_mediaconnect.types.maintenance_schedule_type.MaintenanceScheduleType"
    ]
    """<p>The type of maintenance schedule currently associated with the listed router input.</p>"""
    maintenance_schedule: NotRequired[
        "capo_mediaconnect.types.maintenance_schedule.MaintenanceSchedule"
    ]
    """<p>The details of the maintenance schedule for the listed router input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListedRouterInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    import capo_mediaconnect.types.router_input_type

    out["inputType"] = capo_mediaconnect.types.router_input_type.serialize_json(
        value["input_type"]
    )
    import capo_mediaconnect.types.router_input_state

    out["state"] = capo_mediaconnect.types.router_input_state.serialize_json(
        value["state"]
    )
    out["routedOutputs"] = value["routed_outputs"]
    out["regionName"] = value["region_name"]
    out["availabilityZone"] = value["availability_zone"]
    out["maximumBitrate"] = value["maximum_bitrate"]
    import capo_mediaconnect.types.routing_scope

    out["routingScope"] = capo_mediaconnect.types.routing_scope.serialize_json(
        value["routing_scope"]
    )
    import capo_mediaconnect._protocol.serialize

    out["createdAt"] = capo_mediaconnect._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    import capo_mediaconnect._protocol.serialize

    out["updatedAt"] = capo_mediaconnect._protocol.serialize.fmt_date_time(
        value["updated_at"]
    )
    out["messageCount"] = value["message_count"]
    if "network_interface_arn" in value:
        out["networkInterfaceArn"] = value["network_interface_arn"]
    if "maintenance_schedule_type" in value:
        import capo_mediaconnect.types.maintenance_schedule_type

        out["maintenanceScheduleType"] = (
            capo_mediaconnect.types.maintenance_schedule_type.serialize_json(
                value["maintenance_schedule_type"]
            )
        )
    if "maintenance_schedule" in value:
        import capo_mediaconnect.types.maintenance_schedule

        out["maintenanceSchedule"] = (
            capo_mediaconnect.types.maintenance_schedule.serialize_json(
                value["maintenance_schedule"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListedRouterInput:
    out: ListedRouterInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("inputType") is not None:
        import capo_mediaconnect.types.router_input_type

        out["input_type"] = capo_mediaconnect.types.router_input_type.deserialize_json(
            data["inputType"]
        )
    else:
        import typing

        out["input_type"] = typing.cast(
            "capo_mediaconnect.types.router_input_type.RouterInputType", ""
        )
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
    if data.get("routedOutputs") is not None:
        out["routed_outputs"] = data["routedOutputs"]
    else:
        out["routed_outputs"] = 0
    if data.get("regionName") is not None:
        out["region_name"] = data["regionName"]
    else:
        out["region_name"] = ""
    if data.get("availabilityZone") is not None:
        out["availability_zone"] = data["availabilityZone"]
    else:
        out["availability_zone"] = ""
    if data.get("maximumBitrate") is not None:
        out["maximum_bitrate"] = data["maximumBitrate"]
    else:
        out["maximum_bitrate"] = 0
    if data.get("routingScope") is not None:
        import capo_mediaconnect.types.routing_scope

        out["routing_scope"] = capo_mediaconnect.types.routing_scope.deserialize_json(
            data["routingScope"]
        )
    else:
        import typing

        out["routing_scope"] = typing.cast(
            "capo_mediaconnect.types.routing_scope.RoutingScope", ""
        )
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("messageCount") is not None:
        out["message_count"] = data["messageCount"]
    else:
        out["message_count"] = 0
    if data.get("networkInterfaceArn") is not None:
        out["network_interface_arn"] = data["networkInterfaceArn"]
    if data.get("maintenanceScheduleType") is not None:
        import capo_mediaconnect.types.maintenance_schedule_type

        out["maintenance_schedule_type"] = (
            capo_mediaconnect.types.maintenance_schedule_type.deserialize_json(
                data["maintenanceScheduleType"]
            )
        )
    if data.get("maintenanceSchedule") is not None:
        import capo_mediaconnect.types.maintenance_schedule

        out["maintenance_schedule"] = (
            capo_mediaconnect.types.maintenance_schedule.deserialize_json(
                data["maintenanceSchedule"]
            )
        )
    return out
