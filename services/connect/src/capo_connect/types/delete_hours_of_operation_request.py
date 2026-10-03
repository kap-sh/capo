"""Generated from Smithy shape ``com.amazonaws.connect#DeleteHoursOfOperationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.hours_of_operation_id
    import capo_connect.types.instance_id


class DeleteHoursOfOperationRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    hours_of_operation_id: "capo_connect.types.hours_of_operation_id.HoursOfOperationId"
    """<p>The identifier for the hours of operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteHoursOfOperationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteHoursOfOperationRequest:
    out: DeleteHoursOfOperationRequest = {}  # type: ignore[typeddict-item]
    return out
