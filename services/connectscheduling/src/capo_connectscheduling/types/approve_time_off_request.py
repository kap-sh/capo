"""Generated from Smithy shape ``com.amazonaws.connectscheduling#ApproveTimeOffRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectscheduling.types.description
    import capo_connectscheduling.types.instance_id_or_arn
    import capo_connectscheduling.types.rule_failure_action
    import capo_connectscheduling.types.time_off_id
    import capo_connectscheduling.types.user_id_or_arn


class ApproveTimeOffRequest(TypedDict, closed=True):
    instance_id: "capo_connectscheduling.types.instance_id_or_arn.InstanceIdOrArn"
    """<p>The identifier of the Connect Customer instance. This can be the ID or the ARN of the instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    user_id: "capo_connectscheduling.types.user_id_or_arn.UserIdOrArn"
    """<p>The identifier of the user who the time off request belongs to. This can be the ID or the ARN of the user.</p>"""
    time_off_id: "capo_connectscheduling.types.time_off_id.TimeOffId"
    """<p>The unique identifier of the time off request to approve. If the time off request doesn't belong to <code>UserId</code>, the operation returns <code>ResourceNotFoundException</code>.</p>"""
    description: NotRequired["capo_connectscheduling.types.description.Description"]
    """<p>A description recorded with the approval. <code>GetTimeOff</code> doesn't return it.</p>"""
    rule_failure_action: NotRequired[
        "capo_connectscheduling.types.rule_failure_action.RuleFailureAction"
    ]
    """<p>Controls what happens when a configured rule fails. <code>REJECT</code>, the default, records an <code>ERROR</code> and leaves the request <code>REJECTED</code>. <code>OVERRIDE</code> records a <code>WARNING</code> and approves the request, like the <i>Override time off rules</i> option in the Connect Customer admin website. <code>OVERRIDE</code> never waives <code>CONFLICTING_TIME_OFF_REQUEST</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApproveTimeOffRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "rule_failure_action" in value:
        import capo_connectscheduling.types.rule_failure_action

        out["RuleFailureAction"] = (
            capo_connectscheduling.types.rule_failure_action.serialize_json(
                value["rule_failure_action"]
            )
        )
    return out


def deserialize_json(data: dict) -> ApproveTimeOffRequest:
    out: ApproveTimeOffRequest = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("RuleFailureAction") is not None:
        import capo_connectscheduling.types.rule_failure_action

        out["rule_failure_action"] = (
            capo_connectscheduling.types.rule_failure_action.deserialize_json(
                data["RuleFailureAction"]
            )
        )
    return out


def redact_sensitive(value: ApproveTimeOffRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
