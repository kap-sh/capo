"""Generated from Smithy shape ``com.amazonaws.connectscheduling#PutTimeOffBalanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connectscheduling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectscheduling.types.duration
    import capo_connectscheduling.types.instance_id_or_arn
    import capo_connectscheduling.types.shift_activity_id_or_arn
    import capo_connectscheduling.types.user_id_or_arn


class PutTimeOffBalanceRequest(TypedDict, closed=True):
    instance_id: "capo_connectscheduling.types.instance_id_or_arn.InstanceIdOrArn"
    """<p>The identifier of the Connect Customer instance. This can be the ID or the ARN of the instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    user_id: "capo_connectscheduling.types.user_id_or_arn.UserIdOrArn"
    """<p>The identifier of the user whose balance is being updated. This can be the ID or the ARN of the user.</p>"""
    shift_activity_id: (
        "capo_connectscheduling.types.shift_activity_id_or_arn.ShiftActivityIdOrArn"
    )
    """<p>The identifier of the shift activity that the balance applies to. This can be the ID or the ARN of the shift activity.</p>"""
    balance: "capo_connectscheduling.types.duration.Duration"
    """<p>The new time off balance for the user and activity. It replaces the existing balance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutTimeOffBalanceRequest) -> dict:
    out: dict = {}
    import capo_connectscheduling.types.duration

    out["Balance"] = capo_connectscheduling.types.duration.serialize_json(
        value["balance"]
    )
    return out


def deserialize_json(data: dict) -> PutTimeOffBalanceRequest:
    out: PutTimeOffBalanceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Balance") is not None:
        import capo_connectscheduling.types.duration

        out["balance"] = capo_connectscheduling.types.duration.deserialize_json(
            data["Balance"]
        )
    else:
        raise DeserializationError("PutTimeOffBalanceRequest.balance required")
    return out
