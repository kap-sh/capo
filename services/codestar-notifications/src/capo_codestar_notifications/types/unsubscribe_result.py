"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#UnsubscribeResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codestar_notifications.types.notification_rule_arn


class UnsubscribeResult(TypedDict, closed=True):
    arn: "capo_codestar_notifications.types.notification_rule_arn.NotificationRuleArn"
    """<p>The Amazon Resource Name (ARN) of the the notification rule from which you have removed a subscription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnsubscribeResult) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> UnsubscribeResult:
    out: UnsubscribeResult = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    return out
