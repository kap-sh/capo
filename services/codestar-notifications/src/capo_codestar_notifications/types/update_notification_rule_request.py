"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#UpdateNotificationRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codestar_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codestar_notifications.types.detail_type
    import capo_codestar_notifications.types.event_type_ids
    import capo_codestar_notifications.types.notification_rule_arn
    import capo_codestar_notifications.types.notification_rule_name
    import capo_codestar_notifications.types.notification_rule_status
    import capo_codestar_notifications.types.targets


class UpdateNotificationRuleRequest(TypedDict, closed=True):
    arn: "capo_codestar_notifications.types.notification_rule_arn.NotificationRuleArn"
    """<p>The Amazon Resource Name (ARN) of the notification rule.</p>"""
    name: NotRequired[
        "capo_codestar_notifications.types.notification_rule_name.NotificationRuleName"
    ]
    """<p>The name of the notification rule.</p>"""
    status: NotRequired[
        "capo_codestar_notifications.types.notification_rule_status.NotificationRuleStatus"
    ]
    """<p>The status of the notification rule. Valid statuses include enabled (sending notifications) or disabled (not sending notifications).</p>"""
    event_type_ids: NotRequired[
        "capo_codestar_notifications.types.event_type_ids.EventTypeIds"
    ]
    """<p>A list of event types associated with this notification rule. For a complete list of event types and IDs, see <a href="https://docs.aws.amazon.com/codestar-notifications/latest/userguide/concepts.html#concepts-api">Notification concepts</a> in the <i>Developer Tools Console User Guide</i>.</p>"""
    targets: NotRequired["capo_codestar_notifications.types.targets.Targets"]
    """<p>The address and type of the targets to receive notifications from this notification rule.</p>"""
    detail_type: NotRequired["capo_codestar_notifications.types.detail_type.DetailType"]
    """<p>The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in Amazon CloudWatch. FULL will include any supplemental information provided by CodeStar Notifications and/or the service for the resource for which the notification is created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNotificationRuleRequest) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import capo_codestar_notifications.types.notification_rule_status

        out["Status"] = (
            capo_codestar_notifications.types.notification_rule_status.serialize_json(
                value["status"]
            )
        )
    if "event_type_ids" in value:
        import capo_codestar_notifications.types.event_type_ids

        out["EventTypeIds"] = (
            capo_codestar_notifications.types.event_type_ids.serialize_json(
                value["event_type_ids"]
            )
        )
    if "targets" in value:
        import capo_codestar_notifications.types.targets

        out["Targets"] = capo_codestar_notifications.types.targets.serialize_json(
            value["targets"]
        )
    if "detail_type" in value:
        import capo_codestar_notifications.types.detail_type

        out["DetailType"] = (
            capo_codestar_notifications.types.detail_type.serialize_json(
                value["detail_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateNotificationRuleRequest:
    out: UpdateNotificationRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("UpdateNotificationRuleRequest.arn required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Status") is not None:
        import capo_codestar_notifications.types.notification_rule_status

        out["status"] = (
            capo_codestar_notifications.types.notification_rule_status.deserialize_json(
                data["Status"]
            )
        )
    if data.get("EventTypeIds") is not None:
        import capo_codestar_notifications.types.event_type_ids

        out["event_type_ids"] = (
            capo_codestar_notifications.types.event_type_ids.deserialize_json(
                data["EventTypeIds"]
            )
        )
    if data.get("Targets") is not None:
        import capo_codestar_notifications.types.targets

        out["targets"] = capo_codestar_notifications.types.targets.deserialize_json(
            data["Targets"]
        )
    if data.get("DetailType") is not None:
        import capo_codestar_notifications.types.detail_type

        out["detail_type"] = (
            capo_codestar_notifications.types.detail_type.deserialize_json(
                data["DetailType"]
            )
        )
    return out
