"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#DescribeNotificationRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codestar_notifications.types.notification_rule_arn


class DescribeNotificationRuleRequest(TypedDict, closed=True):
    arn: "capo_codestar_notifications.types.notification_rule_arn.NotificationRuleArn"
    """<p>The Amazon Resource Name (ARN) of the notification rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeNotificationRuleRequest) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DescribeNotificationRuleRequest:
    out: DescribeNotificationRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    return out
