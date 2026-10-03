"""Generated from Smithy shape ``com.amazonaws.connect#AssociateRoutingProfileQueuesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.routing_profile_id
    import capo_connect.types.routing_profile_manual_assignment_queue_config_list
    import capo_connect.types.routing_profile_queue_config_list


class AssociateRoutingProfileQueuesRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    routing_profile_id: "capo_connect.types.routing_profile_id.RoutingProfileId"
    """<p>The identifier of the routing profile.</p>"""
    queue_configs: NotRequired[
        "capo_connect.types.routing_profile_queue_config_list.RoutingProfileQueueConfigList"
    ]
    """<p>The queues to associate with this routing profile.</p>"""
    manual_assignment_queue_configs: NotRequired[
        "capo_connect.types.routing_profile_manual_assignment_queue_config_list.RoutingProfileManualAssignmentQueueConfigList"
    ]
    """<p>The manual assignment queues to associate with this routing profile.</p> <note> <p>For voice contacts, manual assignment supports only agent-first callback contacts. Chat, email, and task contacts are fully supported.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateRoutingProfileQueuesRequest) -> dict:
    out: dict = {}
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
    return out


def deserialize_json(data: dict) -> AssociateRoutingProfileQueuesRequest:
    out: AssociateRoutingProfileQueuesRequest = {}  # type: ignore[typeddict-item]
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
    return out
