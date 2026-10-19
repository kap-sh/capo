"""Generated from Smithy shape ``com.amazonaws.notifications#UpdateEventRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_notifications.types.event_rule_arn
    import capo_notifications.types.notification_configuration_arn
    import capo_notifications.types.status_summary_by_region


class UpdateEventRuleResponse(TypedDict, closed=True):
    arn: "capo_notifications.types.event_rule_arn.EventRuleArn"
    """<p>The Amazon Resource Name (ARN) to use to update the <code>EventRule</code>.</p>"""
    notification_configuration_arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn"
    """<p>The ARN of the <code>NotificationConfiguration</code>.</p>"""
    status_summary_by_region: (
        "capo_notifications.types.status_summary_by_region.StatusSummaryByRegion"
    )
    """<p>The status of the action by Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEventRuleResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["notificationConfigurationArn"] = value["notification_configuration_arn"]
    import capo_notifications.types.status_summary_by_region

    out["statusSummaryByRegion"] = (
        capo_notifications.types.status_summary_by_region.serialize_json(
            value["status_summary_by_region"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateEventRuleResponse:
    out: UpdateEventRuleResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("notificationConfigurationArn") is not None:
        out["notification_configuration_arn"] = data["notificationConfigurationArn"]
    else:
        out["notification_configuration_arn"] = ""
    if data.get("statusSummaryByRegion") is not None:
        import capo_notifications.types.status_summary_by_region

        out["status_summary_by_region"] = (
            capo_notifications.types.status_summary_by_region.deserialize_json(
                data["statusSummaryByRegion"]
            )
        )
    else:
        out["status_summary_by_region"] = {}
    return out
