"""Generated from Smithy shape ``com.amazonaws.connectscheduling#GetTimeOffRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectscheduling.types.instance_id_or_arn
    import capo_connectscheduling.types.time_off_id
    import capo_connectscheduling.types.user_id_or_arn


class GetTimeOffRequest(TypedDict, closed=True):
    instance_id: "capo_connectscheduling.types.instance_id_or_arn.InstanceIdOrArn"
    """<p>The identifier of the Connect Customer instance. This can be the ID or the ARN of the instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    user_id: "capo_connectscheduling.types.user_id_or_arn.UserIdOrArn"
    """<p>The identifier of the user who the time off request belongs to. This can be the ID or the ARN of the user.</p>"""
    time_off_id: "capo_connectscheduling.types.time_off_id.TimeOffId"
    """<p>The identifier of the time off request. If the time off request doesn't belong to <code>UserId</code>, the operation returns <code>ResourceNotFoundException</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTimeOffRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTimeOffRequest:
    out: GetTimeOffRequest = {}  # type: ignore[typeddict-item]
    return out
