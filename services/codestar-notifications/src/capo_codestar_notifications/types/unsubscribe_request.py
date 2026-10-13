"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#UnsubscribeRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_codestar_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codestar_notifications.types.notification_rule_arn
    import capo_codestar_notifications.types.target_address


class UnsubscribeRequest(TypedDict, closed=True):
    arn: "capo_codestar_notifications.types.notification_rule_arn.NotificationRuleArn"
    """<p>The Amazon Resource Name (ARN) of the notification rule.</p>"""
    target_address: "capo_codestar_notifications.types.target_address.TargetAddress"
    """<p>The ARN of the Amazon Q Developer in chat applications topic to unsubscribe from the notification rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnsubscribeRequest) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["TargetAddress"] = value["target_address"]
    return out


def deserialize_json(data: dict) -> UnsubscribeRequest:
    out: UnsubscribeRequest = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("UnsubscribeRequest.arn required")
    if data.get("TargetAddress") is not None:
        out["target_address"] = data["TargetAddress"]
    else:
        raise DeserializationError("UnsubscribeRequest.target_address required")
    return out


def redact_sensitive(value: UnsubscribeRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "target_address" in value:
        out["target_address"] = "*** Sensitive Data Redacted ***"
    return out
