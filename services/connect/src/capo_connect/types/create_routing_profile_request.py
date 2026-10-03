"""Generated from Smithy shape ``com.amazonaws.connect#CreateRoutingProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.agent_availability_timer
    import capo_connect.types.instance_id
    import capo_connect.types.media_concurrencies
    import capo_connect.types.queue_id
    import capo_connect.types.routing_profile_description
    import capo_connect.types.routing_profile_manual_assignment_queue_config_list
    import capo_connect.types.routing_profile_name
    import capo_connect.types.routing_profile_queue_config_list
    import capo_connect.types.tag_map


class CreateRoutingProfileRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    name: "capo_connect.types.routing_profile_name.RoutingProfileName"
    """<p>The name of the routing profile. Must not be more than 127 characters.</p>"""
    description: (
        "capo_connect.types.routing_profile_description.RoutingProfileDescription"
    )
    """<p>Description of the routing profile. Must not be more than 250 characters.</p>"""
    default_outbound_queue_id: "capo_connect.types.queue_id.QueueId"
    """<p>The default outbound queue for the routing profile.</p>"""
    queue_configs: NotRequired[
        "capo_connect.types.routing_profile_queue_config_list.RoutingProfileQueueConfigList"
    ]
    """<p>The inbound queues associated with the routing profile. If no queue is added, the agent can make only outbound calls.</p> <p>The limit of 10 array members applies to the maximum number of <code>RoutingProfileQueueConfig</code> objects that can be passed during a CreateRoutingProfile API request. It is different from the quota of 50 queues per routing profile per instance that is listed in <a href="https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html">Connect Customer service quotas</a>. </p>"""
    manual_assignment_queue_configs: NotRequired[
        "capo_connect.types.routing_profile_manual_assignment_queue_config_list.RoutingProfileManualAssignmentQueueConfigList"
    ]
    """<p>The manual assignment queues associated with the routing profile. If no queue is added, agents and supervisors can't pick or assign any contacts from this routing profile. The limit of 10 array members applies to the maximum number of RoutingProfileManualAssignmentQueueConfig objects that can be passed during a CreateRoutingProfile API request. It is different from the quota of 50 queues per routing profile per instance that is listed in Connect Customer service quotas.</p> <note> <p>For voice contacts, manual assignment supports only agent-first callback contacts. Chat, email, and task contacts are fully supported.</p> </note>"""
    media_concurrencies: "capo_connect.types.media_concurrencies.MediaConcurrencies"
    """<p>The channels that agents can handle in the Contact Control Panel (CCP) for this routing profile.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.</p>"""
    agent_availability_timer: NotRequired[
        "capo_connect.types.agent_availability_timer.AgentAvailabilityTimer"
    ]
    """<p>Whether agents with this routing profile will have their routing order calculated based on <i>longest idle time</i> or <i>time since their last inbound contact</i>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRoutingProfileRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Description"] = value["description"]
    out["DefaultOutboundQueueId"] = value["default_outbound_queue_id"]
    if "queue_configs" in value:
        import capo_connect.types.routing_profile_queue_config_list

        out["QueueConfigs"] = (
            capo_connect.types.routing_profile_queue_config_list.serialize_json(
                value["queue_configs"]
            )
        )
    if "manual_assignment_queue_configs" in value:
        import capo_connect.types.routing_profile_manual_assignment_queue_config_list

        out["ManualAssignmentQueueConfigs"] = (
            capo_connect.types.routing_profile_manual_assignment_queue_config_list.serialize_json(
                value["manual_assignment_queue_configs"]
            )
        )
    import capo_connect.types.media_concurrencies

    out["MediaConcurrencies"] = capo_connect.types.media_concurrencies.serialize_json(
        value["media_concurrencies"]
    )
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    if "agent_availability_timer" in value:
        import capo_connect.types.agent_availability_timer

        out["AgentAvailabilityTimer"] = (
            capo_connect.types.agent_availability_timer.serialize_json(
                value["agent_availability_timer"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateRoutingProfileRequest:
    out: CreateRoutingProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateRoutingProfileRequest.name required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("CreateRoutingProfileRequest.description required")
    if data.get("DefaultOutboundQueueId") is not None:
        out["default_outbound_queue_id"] = data["DefaultOutboundQueueId"]
    else:
        raise DeserializationError(
            "CreateRoutingProfileRequest.default_outbound_queue_id required"
        )
    if data.get("QueueConfigs") is not None:
        import capo_connect.types.routing_profile_queue_config_list

        out["queue_configs"] = (
            capo_connect.types.routing_profile_queue_config_list.deserialize_json(
                data["QueueConfigs"]
            )
        )
    if data.get("ManualAssignmentQueueConfigs") is not None:
        import capo_connect.types.routing_profile_manual_assignment_queue_config_list

        out["manual_assignment_queue_configs"] = (
            capo_connect.types.routing_profile_manual_assignment_queue_config_list.deserialize_json(
                data["ManualAssignmentQueueConfigs"]
            )
        )
    if data.get("MediaConcurrencies") is not None:
        import capo_connect.types.media_concurrencies

        out["media_concurrencies"] = (
            capo_connect.types.media_concurrencies.deserialize_json(
                data["MediaConcurrencies"]
            )
        )
    else:
        raise DeserializationError(
            "CreateRoutingProfileRequest.media_concurrencies required"
        )
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    if data.get("AgentAvailabilityTimer") is not None:
        import capo_connect.types.agent_availability_timer

        out["agent_availability_timer"] = (
            capo_connect.types.agent_availability_timer.deserialize_json(
                data["AgentAvailabilityTimer"]
            )
        )
    return out
