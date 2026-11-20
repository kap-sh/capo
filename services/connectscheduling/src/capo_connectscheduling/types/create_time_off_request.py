"""Generated from Smithy shape ``com.amazonaws.connectscheduling#CreateTimeOffRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_connectscheduling.types.approval_type
    import capo_connectscheduling.types.client_token
    import capo_connectscheduling.types.description
    import capo_connectscheduling.types.instance_id_or_arn
    import capo_connectscheduling.types.rule_failure_action
    import capo_connectscheduling.types.shift_activity_id_or_arn
    import capo_connectscheduling.types.user_id_or_arn


class CreateTimeOffRequest(TypedDict, closed=True):
    instance_id: "capo_connectscheduling.types.instance_id_or_arn.InstanceIdOrArn"
    """<p>The identifier of the Connect Customer instance. This can be the ID or the ARN of the instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    user_id: "capo_connectscheduling.types.user_id_or_arn.UserIdOrArn"
    """<p>The identifier of the user who the time off request is for. This can be the ID or the ARN of the user.</p>"""
    shift_activity_id: (
        "capo_connectscheduling.types.shift_activity_id_or_arn.ShiftActivityIdOrArn"
    )
    """<p>The identifier of the shift activity that defines the type of time off being requested. This can be the ID or the ARN of the shift activity. It must be a time off activity. Activities that aren't set as <i>Requestable</i> are accepted.</p>"""
    start_at: "datetime.datetime"
    """<p>The start of the time off window, inclusive. It must be no earlier than one year before the current date. Connect Customer stores the value as sent, to the millisecond.</p>"""
    end_at: "datetime.datetime"
    """<p>The end of the time off window, exclusive. It must be after <code>StartAt</code> and no later than 24 months after the current date. Connect Customer stores the value as sent, to the millisecond.</p>"""
    description: NotRequired["capo_connectscheduling.types.description.Description"]
    """<p>A description recorded on the time off request. If you omit it, the request has no description.</p>"""
    approval_type: "capo_connectscheduling.types.approval_type.ApprovalType"
    """<p>Controls who approves the request. <code>AWAIT_APPROVAL</code> waits for an <code>ApproveTimeOff</code> or <code>RejectTimeOff</code> call. <code>AUTOMATIC</code> has Connect Customer decide the request. For details, see <code>CreateTimeOff</code>.</p>"""
    rule_failure_action: NotRequired[
        "capo_connectscheduling.types.rule_failure_action.RuleFailureAction"
    ]
    """<p>Controls what happens when a configured rule fails. <code>REJECT</code>, the default, records an <code>ERROR</code> and ends the request <code>REJECTED</code>, unless the whole window is in the past. <code>OVERRIDE</code> records a <code>WARNING</code> and ends the request <code>APPROVED</code>, like the <i>Override time off rules</i> option in the Connect Customer admin website. <code>OVERRIDE</code> requires <code>AUTOMATIC</code>. With <code>AWAIT_APPROVAL</code>, <code>OVERRIDE</code> fails with <code>ValidationException</code>. Set it on <code>ApproveTimeOff</code> instead. <code>OVERRIDE</code> never waives <code>CONFLICTING_TIME_OFF_REQUEST</code>.</p>"""
    client_token: NotRequired["capo_connectscheduling.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If this token matches a previous request, Connect Customer returns the result of that request and doesn't create another time off request. If you don't provide a token, the AWS SDK populates this field. If you reuse a client token with a different request body, the request fails with <code>ValidationException</code>. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTimeOffRequest) -> dict:
    out: dict = {}
    out["ShiftActivityId"] = value["shift_activity_id"]
    import capo_connectscheduling.types._prelude.timestamp

    out["StartAt"] = capo_connectscheduling.types._prelude.timestamp.serialize_json(
        value["start_at"]
    )
    import capo_connectscheduling.types._prelude.timestamp

    out["EndAt"] = capo_connectscheduling.types._prelude.timestamp.serialize_json(
        value["end_at"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    import capo_connectscheduling.types.approval_type

    out["ApprovalType"] = capo_connectscheduling.types.approval_type.serialize_json(
        value["approval_type"]
    )
    if "rule_failure_action" in value:
        import capo_connectscheduling.types.rule_failure_action

        out["RuleFailureAction"] = (
            capo_connectscheduling.types.rule_failure_action.serialize_json(
                value["rule_failure_action"]
            )
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateTimeOffRequest:
    out: CreateTimeOffRequest = {}  # type: ignore[typeddict-item]
    if data.get("ShiftActivityId") is not None:
        out["shift_activity_id"] = data["ShiftActivityId"]
    else:
        out["shift_activity_id"] = ""
    if data.get("StartAt") is not None:
        import capo_connectscheduling.types._prelude.timestamp

        out["start_at"] = (
            capo_connectscheduling.types._prelude.timestamp.deserialize_json(
                data["StartAt"]
            )
        )
    else:
        import datetime

        out["start_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("EndAt") is not None:
        import capo_connectscheduling.types._prelude.timestamp

        out["end_at"] = (
            capo_connectscheduling.types._prelude.timestamp.deserialize_json(
                data["EndAt"]
            )
        )
    else:
        import datetime

        out["end_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ApprovalType") is not None:
        import capo_connectscheduling.types.approval_type

        out["approval_type"] = (
            capo_connectscheduling.types.approval_type.deserialize_json(
                data["ApprovalType"]
            )
        )
    else:
        import typing

        out["approval_type"] = typing.cast(
            "capo_connectscheduling.types.approval_type.ApprovalType", ""
        )
    if data.get("RuleFailureAction") is not None:
        import capo_connectscheduling.types.rule_failure_action

        out["rule_failure_action"] = (
            capo_connectscheduling.types.rule_failure_action.deserialize_json(
                data["RuleFailureAction"]
            )
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out


def redact_sensitive(value: CreateTimeOffRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
