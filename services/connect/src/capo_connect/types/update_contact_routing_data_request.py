"""Generated from Smithy shape ``com.amazonaws.connect#UpdateContactRoutingDataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_id
    import capo_connect.types.instance_id
    import capo_connect.types.queue_priority
    import capo_connect.types.queue_time_adjustment_seconds
    import capo_connect.types.routing_criteria_input


class UpdateContactRoutingDataRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_id: "capo_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact in this instance of Connect Customer. </p>"""
    queue_time_adjustment_seconds: NotRequired[
        "capo_connect.types.queue_time_adjustment_seconds.QueueTimeAdjustmentSeconds"
    ]
    """<p>The number of seconds to add or subtract from the contact's routing age. Contacts are routed to agents on a first-come, first-serve basis. This means that changing their amount of time in queue compared to others also changes their position in queue.</p>"""
    queue_priority: NotRequired["capo_connect.types.queue_priority.QueuePriority"]
    """<p>Priority of the contact in the queue. The default priority for new contacts is 5. You can raise the priority of a contact compared to other contacts in the queue by assigning them a higher priority, such as 1 or 2.</p>"""
    routing_criteria: NotRequired[
        "capo_connect.types.routing_criteria_input.RoutingCriteriaInput"
    ]
    """<p>Updates the routing criteria on the contact. These properties can be used to change how a contact is routed within the queue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateContactRoutingDataRequest) -> dict:
    out: dict = {}
    if "queue_time_adjustment_seconds" in value:
        out["QueueTimeAdjustmentSeconds"] = value["queue_time_adjustment_seconds"]
    if "queue_priority" in value:
        out["QueuePriority"] = value["queue_priority"]
    if "routing_criteria" in value:
        import capo_connect.types.routing_criteria_input

        out["RoutingCriteria"] = (
            capo_connect.types.routing_criteria_input.serialize_json(
                value["routing_criteria"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateContactRoutingDataRequest:
    out: UpdateContactRoutingDataRequest = {}  # type: ignore[typeddict-item]
    if data.get("QueueTimeAdjustmentSeconds") is not None:
        out["queue_time_adjustment_seconds"] = data["QueueTimeAdjustmentSeconds"]
    if data.get("QueuePriority") is not None:
        out["queue_priority"] = data["QueuePriority"]
    if data.get("RoutingCriteria") is not None:
        import capo_connect.types.routing_criteria_input

        out["routing_criteria"] = (
            capo_connect.types.routing_criteria_input.deserialize_json(
                data["RoutingCriteria"]
            )
        )
    return out
