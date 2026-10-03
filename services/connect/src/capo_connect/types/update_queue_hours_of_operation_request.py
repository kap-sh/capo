"""Generated from Smithy shape ``com.amazonaws.connect#UpdateQueueHoursOfOperationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.hours_of_operation_id
    import capo_connect.types.instance_id
    import capo_connect.types.queue_id


class UpdateQueueHoursOfOperationRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    queue_id: "capo_connect.types.queue_id.QueueId"
    """<p>The identifier for the queue.</p>"""
    hours_of_operation_id: "capo_connect.types.hours_of_operation_id.HoursOfOperationId"
    """<p>The identifier for the hours of operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQueueHoursOfOperationRequest) -> dict:
    out: dict = {}
    out["HoursOfOperationId"] = value["hours_of_operation_id"]
    return out


def deserialize_json(data: dict) -> UpdateQueueHoursOfOperationRequest:
    out: UpdateQueueHoursOfOperationRequest = {}  # type: ignore[typeddict-item]
    if data.get("HoursOfOperationId") is not None:
        out["hours_of_operation_id"] = data["HoursOfOperationId"]
    else:
        raise DeserializationError(
            "UpdateQueueHoursOfOperationRequest.hours_of_operation_id required"
        )
    return out
