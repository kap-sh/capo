"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_mediaconnect.types.__map_of_string
    import capo_mediaconnect.types.maintenance_configuration
    import capo_mediaconnect.types.maintenance_schedule
    import capo_mediaconnect.types.maintenance_schedule_type
    import capo_mediaconnect.types.maintenance_type
    import capo_mediaconnect.types.router_content_quality_analysis_configuration
    import capo_mediaconnect.types.router_content_quality_analysis_type
    import capo_mediaconnect.types.router_input_arn
    import capo_mediaconnect.types.router_input_configuration
    import capo_mediaconnect.types.router_input_messages
    import capo_mediaconnect.types.router_input_state
    import capo_mediaconnect.types.router_input_stream_details
    import capo_mediaconnect.types.router_input_tier
    import capo_mediaconnect.types.router_input_transit_encryption
    import capo_mediaconnect.types.router_input_type
    import capo_mediaconnect.types.routing_scope


class RouterInput(TypedDict, closed=True):
    name: "str"
    """<p>The name of the router input.</p>"""
    arn: "capo_mediaconnect.types.router_input_arn.RouterInputArn"
    """<p>The Amazon Resource Name (ARN) of the router input.</p>"""
    id: "str"
    """<p>The unique identifier of the router input.</p>"""
    state: "capo_mediaconnect.types.router_input_state.RouterInputState"
    """<p>The current state of the router input.</p>"""
    input_type: "capo_mediaconnect.types.router_input_type.RouterInputType"
    """<p>The type of the router input.</p>"""
    configuration: (
        "capo_mediaconnect.types.router_input_configuration.RouterInputConfiguration"
    )
    routed_outputs: "int"
    """<p>The number of router outputs associated with the router input.</p>"""
    maximum_routed_outputs: NotRequired["int"]
    """<p>The maximum number of outputs that can be simultaneously routed to this input.</p>"""
    region_name: "str"
    """<p>The Amazon Web Services Region where the router input is located.</p>"""
    availability_zone: "str"
    """<p>The Availability Zone of the router input.</p>"""
    maximum_bitrate: "int"
    """<p>The maximum bitrate for the router input.</p>"""
    tier: "capo_mediaconnect.types.router_input_tier.RouterInputTier"
    """<p>The tier level of the router input.</p>"""
    routing_scope: "capo_mediaconnect.types.routing_scope.RoutingScope"
    """<p>Indicates whether the router input is configured for Regional or global routing.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the router input was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp when the router input was last updated.</p>"""
    messages: "capo_mediaconnect.types.router_input_messages.RouterInputMessages"
    """<p>The messages associated with the router input.</p>"""
    transit_encryption: "capo_mediaconnect.types.router_input_transit_encryption.RouterInputTransitEncryption"
    tags: "capo_mediaconnect.types.__map_of_string.__mapOfString"
    """<p>Key-value pairs that can be used to tag and organize this router input.</p>"""
    stream_details: (
        "capo_mediaconnect.types.router_input_stream_details.RouterInputStreamDetails"
    )
    ip_address: NotRequired["str"]
    """<p>The IP address of the router input.</p>"""
    maintenance_type: "capo_mediaconnect.types.maintenance_type.MaintenanceType"
    """<p>The type of maintenance configuration applied to this router input.</p>"""
    maintenance_configuration: (
        "capo_mediaconnect.types.maintenance_configuration.MaintenanceConfiguration"
    )
    """<p>The maintenance configuration settings applied to this router input.</p>"""
    maintenance_schedule_type: NotRequired[
        "capo_mediaconnect.types.maintenance_schedule_type.MaintenanceScheduleType"
    ]
    """<p>The type of maintenance schedule currently in effect for this router input.</p>"""
    maintenance_schedule: NotRequired[
        "capo_mediaconnect.types.maintenance_schedule.MaintenanceSchedule"
    ]
    """<p>The current maintenance schedule details for this router input.</p>"""
    content_quality_analysis_type: NotRequired[
        "capo_mediaconnect.types.router_content_quality_analysis_type.RouterContentQualityAnalysisType"
    ]
    """<p>The type of content quality analysis applied to the router input.</p>"""
    content_quality_analysis_configuration: NotRequired[
        "capo_mediaconnect.types.router_content_quality_analysis_configuration.RouterContentQualityAnalysisConfiguration"
    ]
    """<p>The content quality analysis configuration for the router input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouterInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    import capo_mediaconnect.types.router_input_state

    out["state"] = capo_mediaconnect.types.router_input_state.serialize_json(
        value["state"]
    )
    import capo_mediaconnect.types.router_input_type

    out["inputType"] = capo_mediaconnect.types.router_input_type.serialize_json(
        value["input_type"]
    )
    import capo_mediaconnect.types.router_input_configuration

    out["configuration"] = (
        capo_mediaconnect.types.router_input_configuration.serialize_json(
            value["configuration"]
        )
    )
    out["routedOutputs"] = value["routed_outputs"]
    if "maximum_routed_outputs" in value:
        out["maximumRoutedOutputs"] = value["maximum_routed_outputs"]
    out["regionName"] = value["region_name"]
    out["availabilityZone"] = value["availability_zone"]
    out["maximumBitrate"] = value["maximum_bitrate"]
    import capo_mediaconnect.types.router_input_tier

    out["tier"] = capo_mediaconnect.types.router_input_tier.serialize_json(
        value["tier"]
    )
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
    import capo_mediaconnect.types.router_input_messages

    out["messages"] = capo_mediaconnect.types.router_input_messages.serialize_json(
        value["messages"]
    )
    import capo_mediaconnect.types.router_input_transit_encryption

    out["transitEncryption"] = (
        capo_mediaconnect.types.router_input_transit_encryption.serialize_json(
            value["transit_encryption"]
        )
    )
    import capo_mediaconnect.types.__map_of_string

    out["tags"] = capo_mediaconnect.types.__map_of_string.serialize_json(value["tags"])
    import capo_mediaconnect.types.router_input_stream_details

    out["streamDetails"] = (
        capo_mediaconnect.types.router_input_stream_details.serialize_json(
            value["stream_details"]
        )
    )
    if "ip_address" in value:
        out["ipAddress"] = value["ip_address"]
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
    if "content_quality_analysis_type" in value:
        import capo_mediaconnect.types.router_content_quality_analysis_type

        out["contentQualityAnalysisType"] = (
            capo_mediaconnect.types.router_content_quality_analysis_type.serialize_json(
                value["content_quality_analysis_type"]
            )
        )
    if "content_quality_analysis_configuration" in value:
        import capo_mediaconnect.types.router_content_quality_analysis_configuration

        out["contentQualityAnalysisConfiguration"] = (
            capo_mediaconnect.types.router_content_quality_analysis_configuration.serialize_json(
                value["content_quality_analysis_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouterInput:
    out: RouterInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("RouterInput.name required")
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("RouterInput.arn required")
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("RouterInput.id required")
    if data.get("state") is not None:
        import capo_mediaconnect.types.router_input_state

        out["state"] = capo_mediaconnect.types.router_input_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("RouterInput.state required")
    if data.get("inputType") is not None:
        import capo_mediaconnect.types.router_input_type

        out["input_type"] = capo_mediaconnect.types.router_input_type.deserialize_json(
            data["inputType"]
        )
    else:
        raise DeserializationError("RouterInput.input_type required")
    if data.get("configuration") is not None:
        import capo_mediaconnect.types.router_input_configuration

        out["configuration"] = (
            capo_mediaconnect.types.router_input_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError("RouterInput.configuration required")
    if data.get("routedOutputs") is not None:
        out["routed_outputs"] = data["routedOutputs"]
    else:
        raise DeserializationError("RouterInput.routed_outputs required")
    if data.get("maximumRoutedOutputs") is not None:
        out["maximum_routed_outputs"] = data["maximumRoutedOutputs"]
    if data.get("regionName") is not None:
        out["region_name"] = data["regionName"]
    else:
        raise DeserializationError("RouterInput.region_name required")
    if data.get("availabilityZone") is not None:
        out["availability_zone"] = data["availabilityZone"]
    else:
        raise DeserializationError("RouterInput.availability_zone required")
    if data.get("maximumBitrate") is not None:
        out["maximum_bitrate"] = data["maximumBitrate"]
    else:
        raise DeserializationError("RouterInput.maximum_bitrate required")
    if data.get("tier") is not None:
        import capo_mediaconnect.types.router_input_tier

        out["tier"] = capo_mediaconnect.types.router_input_tier.deserialize_json(
            data["tier"]
        )
    else:
        raise DeserializationError("RouterInput.tier required")
    if data.get("routingScope") is not None:
        import capo_mediaconnect.types.routing_scope

        out["routing_scope"] = capo_mediaconnect.types.routing_scope.deserialize_json(
            data["routingScope"]
        )
    else:
        raise DeserializationError("RouterInput.routing_scope required")
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError("RouterInput.created_at required")
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError("RouterInput.updated_at required")
    if data.get("messages") is not None:
        import capo_mediaconnect.types.router_input_messages

        out["messages"] = (
            capo_mediaconnect.types.router_input_messages.deserialize_json(
                data["messages"]
            )
        )
    else:
        raise DeserializationError("RouterInput.messages required")
    if data.get("transitEncryption") is not None:
        import capo_mediaconnect.types.router_input_transit_encryption

        out["transit_encryption"] = (
            capo_mediaconnect.types.router_input_transit_encryption.deserialize_json(
                data["transitEncryption"]
            )
        )
    else:
        raise DeserializationError("RouterInput.transit_encryption required")
    if data.get("tags") is not None:
        import capo_mediaconnect.types.__map_of_string

        out["tags"] = capo_mediaconnect.types.__map_of_string.deserialize_json(
            data["tags"]
        )
    else:
        raise DeserializationError("RouterInput.tags required")
    if data.get("streamDetails") is not None:
        import capo_mediaconnect.types.router_input_stream_details

        out["stream_details"] = (
            capo_mediaconnect.types.router_input_stream_details.deserialize_json(
                data["streamDetails"]
            )
        )
    else:
        raise DeserializationError("RouterInput.stream_details required")
    if data.get("ipAddress") is not None:
        out["ip_address"] = data["ipAddress"]
    if data.get("maintenanceType") is not None:
        import capo_mediaconnect.types.maintenance_type

        out["maintenance_type"] = (
            capo_mediaconnect.types.maintenance_type.deserialize_json(
                data["maintenanceType"]
            )
        )
    else:
        raise DeserializationError("RouterInput.maintenance_type required")
    if data.get("maintenanceConfiguration") is not None:
        import capo_mediaconnect.types.maintenance_configuration

        out["maintenance_configuration"] = (
            capo_mediaconnect.types.maintenance_configuration.deserialize_json(
                data["maintenanceConfiguration"]
            )
        )
    else:
        raise DeserializationError("RouterInput.maintenance_configuration required")
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
    if data.get("contentQualityAnalysisType") is not None:
        import capo_mediaconnect.types.router_content_quality_analysis_type

        out["content_quality_analysis_type"] = (
            capo_mediaconnect.types.router_content_quality_analysis_type.deserialize_json(
                data["contentQualityAnalysisType"]
            )
        )
    if data.get("contentQualityAnalysisConfiguration") is not None:
        import capo_mediaconnect.types.router_content_quality_analysis_configuration

        out["content_quality_analysis_configuration"] = (
            capo_mediaconnect.types.router_content_quality_analysis_configuration.deserialize_json(
                data["contentQualityAnalysisConfiguration"]
            )
        )
    return out
