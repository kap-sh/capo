"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mediaconnect.types.__map_of_string
    import capo_mediaconnect.types.fabric_configuration
    import capo_mediaconnect.types.maintenance_configuration
    import capo_mediaconnect.types.maintenance_schedule
    import capo_mediaconnect.types.maintenance_schedule_type
    import capo_mediaconnect.types.maintenance_type
    import capo_mediaconnect.types.router_input_arn
    import capo_mediaconnect.types.router_output_arn
    import capo_mediaconnect.types.router_output_configuration
    import capo_mediaconnect.types.router_output_messages
    import capo_mediaconnect.types.router_output_routed_state
    import capo_mediaconnect.types.router_output_state
    import capo_mediaconnect.types.router_output_stream_details
    import capo_mediaconnect.types.router_output_tier
    import capo_mediaconnect.types.router_output_type
    import capo_mediaconnect.types.routing_scope


class RouterOutput(TypedDict, closed=True):
    name: "str"
    """<p>The name of the router output.</p>"""
    arn: "capo_mediaconnect.types.router_output_arn.RouterOutputArn"
    """<p>The Amazon Resource Name (ARN) of the router output.</p>"""
    id: "str"
    """<p>The unique identifier of the router output.</p>"""
    state: "capo_mediaconnect.types.router_output_state.RouterOutputState"
    """<p>The overall state of the router output.</p>"""
    output_type: "capo_mediaconnect.types.router_output_type.RouterOutputType"
    """<p>The type of the router output.</p>"""
    configuration: (
        "capo_mediaconnect.types.router_output_configuration.RouterOutputConfiguration"
    )
    routed_state: (
        "capo_mediaconnect.types.router_output_routed_state.RouterOutputRoutedState"
    )
    """<p>The current state of the association between the router output and its input.</p>"""
    region_name: "str"
    """<p>The Amazon Web Services Region where the router output is located.</p>"""
    availability_zone: "str"
    """<p>The Availability Zone of the router output.</p>"""
    maximum_bitrate: "int"
    """<p>The maximum bitrate for the router output.</p>"""
    routing_scope: "capo_mediaconnect.types.routing_scope.RoutingScope"
    """<p>Indicates whether the router output is configured for Regional or global routing.</p>"""
    tier: "capo_mediaconnect.types.router_output_tier.RouterOutputTier"
    """<p>The tier level for the router output. The tier sets the maximum bitrate, in Mbps, for the router output. Valid values include the following:</p> <ul> <li> <p> <code>OUTPUT_20</code> – 20 Mbps</p> </li> <li> <p> <code>OUTPUT_50</code> – 50 Mbps</p> </li> <li> <p> <code>OUTPUT_100</code> – 100 Mbps</p> </li> <li> <p> <code>OUTPUT_250</code> – 250 Mbps</p> </li> <li> <p> <code>OUTPUT_500</code> – 500 Mbps</p> </li> </ul> <p>The 250 Mbps and 500 Mbps tiers are high-bitrate tiers that support TR-07 (JPEG XS) workflows.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the router output was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp when the router output was last updated.</p>"""
    messages: "capo_mediaconnect.types.router_output_messages.RouterOutputMessages"
    """<p>The messages associated with the router output.</p>"""
    tags: "capo_mediaconnect.types.__map_of_string.__mapOfString"
    """<p>Key-value pairs that can be used to tag and organize this router output.</p>"""
    stream_details: (
        "capo_mediaconnect.types.router_output_stream_details.RouterOutputStreamDetails"
    )
    ip_address: NotRequired["str"]
    """<p>The IP address of the router output.</p>"""
    routed_input_arn: NotRequired[
        "capo_mediaconnect.types.router_input_arn.RouterInputArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the router input associated with the output.</p>"""
    maintenance_type: "capo_mediaconnect.types.maintenance_type.MaintenanceType"
    """<p>The type of maintenance configuration applied to this router output.</p>"""
    maintenance_configuration: (
        "capo_mediaconnect.types.maintenance_configuration.MaintenanceConfiguration"
    )
    """<p>The maintenance configuration settings applied to this router output.</p>"""
    maintenance_schedule_type: NotRequired[
        "capo_mediaconnect.types.maintenance_schedule_type.MaintenanceScheduleType"
    ]
    """<p>The type of maintenance schedule currently in effect for this router output.</p>"""
    maintenance_schedule: NotRequired[
        "capo_mediaconnect.types.maintenance_schedule.MaintenanceSchedule"
    ]
    """<p>The current maintenance schedule details for this router output.</p>"""
    fabric_configuration: NotRequired[
        "capo_mediaconnect.types.fabric_configuration.FabricConfiguration"
    ]
    """<p>The fabric configuration settings for the router output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouterOutput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    import capo_mediaconnect.types.router_output_state

    out["state"] = capo_mediaconnect.types.router_output_state.serialize_json(
        value["state"]
    )
    import capo_mediaconnect.types.router_output_type

    out["outputType"] = capo_mediaconnect.types.router_output_type.serialize_json(
        value["output_type"]
    )
    import capo_mediaconnect.types.router_output_configuration

    out["configuration"] = (
        capo_mediaconnect.types.router_output_configuration.serialize_json(
            value["configuration"]
        )
    )
    import capo_mediaconnect.types.router_output_routed_state

    out["routedState"] = (
        capo_mediaconnect.types.router_output_routed_state.serialize_json(
            value["routed_state"]
        )
    )
    out["regionName"] = value["region_name"]
    out["availabilityZone"] = value["availability_zone"]
    out["maximumBitrate"] = value["maximum_bitrate"]
    import capo_mediaconnect.types.routing_scope

    out["routingScope"] = capo_mediaconnect.types.routing_scope.serialize_json(
        value["routing_scope"]
    )
    import capo_mediaconnect.types.router_output_tier

    out["tier"] = capo_mediaconnect.types.router_output_tier.serialize_json(
        value["tier"]
    )
    import capo_mediaconnect._protocol.serialize

    out["createdAt"] = capo_mediaconnect._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    import capo_mediaconnect._protocol.serialize

    out["updatedAt"] = capo_mediaconnect._protocol.serialize.fmt_date_time(
        value["updated_at"]
    )
    import capo_mediaconnect.types.router_output_messages

    out["messages"] = capo_mediaconnect.types.router_output_messages.serialize_json(
        value["messages"]
    )
    import capo_mediaconnect.types.__map_of_string

    out["tags"] = capo_mediaconnect.types.__map_of_string.serialize_json(value["tags"])
    import capo_mediaconnect.types.router_output_stream_details

    out["streamDetails"] = (
        capo_mediaconnect.types.router_output_stream_details.serialize_json(
            value["stream_details"]
        )
    )
    if "ip_address" in value:
        out["ipAddress"] = value["ip_address"]
    if "routed_input_arn" in value:
        out["routedInputArn"] = value["routed_input_arn"]
    import capo_mediaconnect.types.maintenance_type

    out["maintenanceType"] = capo_mediaconnect.types.maintenance_type.serialize_json(
        value["maintenance_type"]
    )
    import capo_mediaconnect.types.maintenance_configuration

    out["maintenanceConfiguration"] = (
        capo_mediaconnect.types.maintenance_configuration.serialize_json(
            value["maintenance_configuration"]
        )
    )
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
    if "fabric_configuration" in value:
        import capo_mediaconnect.types.fabric_configuration

        out["fabricConfiguration"] = (
            capo_mediaconnect.types.fabric_configuration.serialize_json(
                value["fabric_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouterOutput:
    out: RouterOutput = {}  # type: ignore[typeddict-item]
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
    if data.get("outputType") is not None:
        import capo_mediaconnect.types.router_output_type

        out["output_type"] = (
            capo_mediaconnect.types.router_output_type.deserialize_json(
                data["outputType"]
            )
        )
    else:
        import typing

        out["output_type"] = typing.cast(
            "capo_mediaconnect.types.router_output_type.RouterOutputType", ""
        )
    if data.get("configuration") is not None:
        import capo_mediaconnect.types.router_output_configuration

        out["configuration"] = (
            capo_mediaconnect.types.router_output_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        import capo_mediaconnect.types._unknown

        out["configuration"] = capo_mediaconnect.types._unknown.UnknownUnionMember("")
    if data.get("routedState") is not None:
        import capo_mediaconnect.types.router_output_routed_state

        out["routed_state"] = (
            capo_mediaconnect.types.router_output_routed_state.deserialize_json(
                data["routedState"]
            )
        )
    else:
        import typing

        out["routed_state"] = typing.cast(
            "capo_mediaconnect.types.router_output_routed_state.RouterOutputRoutedState",
            "",
        )
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
    if data.get("tier") is not None:
        import capo_mediaconnect.types.router_output_tier

        out["tier"] = capo_mediaconnect.types.router_output_tier.deserialize_json(
            data["tier"]
        )
    else:
        import typing

        out["tier"] = typing.cast(
            "capo_mediaconnect.types.router_output_tier.RouterOutputTier", ""
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
    if data.get("messages") is not None:
        import capo_mediaconnect.types.router_output_messages

        out["messages"] = (
            capo_mediaconnect.types.router_output_messages.deserialize_json(
                data["messages"]
            )
        )
    else:
        out["messages"] = []
    if data.get("tags") is not None:
        import capo_mediaconnect.types.__map_of_string

        out["tags"] = capo_mediaconnect.types.__map_of_string.deserialize_json(
            data["tags"]
        )
    else:
        out["tags"] = {}
    if data.get("streamDetails") is not None:
        import capo_mediaconnect.types.router_output_stream_details

        out["stream_details"] = (
            capo_mediaconnect.types.router_output_stream_details.deserialize_json(
                data["streamDetails"]
            )
        )
    else:
        import capo_mediaconnect.types._unknown

        out["stream_details"] = capo_mediaconnect.types._unknown.UnknownUnionMember("")
    if data.get("ipAddress") is not None:
        out["ip_address"] = data["ipAddress"]
    if data.get("routedInputArn") is not None:
        out["routed_input_arn"] = data["routedInputArn"]
    if data.get("maintenanceType") is not None:
        import capo_mediaconnect.types.maintenance_type

        out["maintenance_type"] = (
            capo_mediaconnect.types.maintenance_type.deserialize_json(
                data["maintenanceType"]
            )
        )
    else:
        import typing

        out["maintenance_type"] = typing.cast(
            "capo_mediaconnect.types.maintenance_type.MaintenanceType", ""
        )
    if data.get("maintenanceConfiguration") is not None:
        import capo_mediaconnect.types.maintenance_configuration

        out["maintenance_configuration"] = (
            capo_mediaconnect.types.maintenance_configuration.deserialize_json(
                data["maintenanceConfiguration"]
            )
        )
    else:
        import capo_mediaconnect.types._unknown

        out["maintenance_configuration"] = (
            capo_mediaconnect.types._unknown.UnknownUnionMember("")
        )
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
    if data.get("fabricConfiguration") is not None:
        import capo_mediaconnect.types.fabric_configuration

        out["fabric_configuration"] = (
            capo_mediaconnect.types.fabric_configuration.deserialize_json(
                data["fabricConfiguration"]
            )
        )
    return out
