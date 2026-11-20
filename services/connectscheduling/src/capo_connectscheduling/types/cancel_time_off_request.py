"""Generated from Smithy shape ``com.amazonaws.connectscheduling#CancelTimeOffRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectscheduling.types.description
    import capo_connectscheduling.types.instance_id_or_arn
    import capo_connectscheduling.types.time_off_id
    import capo_connectscheduling.types.user_id_or_arn


class CancelTimeOffRequest(TypedDict, closed=True):
    instance_id: "capo_connectscheduling.types.instance_id_or_arn.InstanceIdOrArn"
    """<p>The identifier of the Connect Customer instance. This can be the ID or the ARN of the instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    user_id: "capo_connectscheduling.types.user_id_or_arn.UserIdOrArn"
    """<p>The identifier of the user who the time off request belongs to. This can be the ID or the ARN of the user.</p>"""
    time_off_id: "capo_connectscheduling.types.time_off_id.TimeOffId"
    """<p>The unique identifier of the time off request to cancel. If the time off request doesn't belong to <code>UserId</code>, the operation returns <code>ResourceNotFoundException</code>.</p>"""
    description: NotRequired["capo_connectscheduling.types.description.Description"]
    """<p>A description recorded with the cancellation. It replaces the description of the time off request. If you omit it, the request's description is removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelTimeOffRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> CancelTimeOffRequest:
    out: CancelTimeOffRequest = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out


def redact_sensitive(value: CancelTimeOffRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
