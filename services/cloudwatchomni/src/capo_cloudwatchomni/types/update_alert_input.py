"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#UpdateAlertInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.alert_id
    import capo_cloudwatchomni.types.notification_rule_list
    import capo_cloudwatchomni.types.profile_id
    import capo_cloudwatchomni.types.rule
    import capo_cloudwatchomni.types.space_id


class UpdateAlertInput(TypedDict, closed=True):
    space_id: "capo_cloudwatchomni.types.space_id.SpaceId"
    """The unique ID of the space."""
    alert_id: "capo_cloudwatchomni.types.alert_id.AlertId"
    """The alert to update."""
    profile_id: NotRequired["capo_cloudwatchomni.types.profile_id.ProfileId"]
    """The ID of the access profile associated with the alert."""
    name: NotRequired["str"]
    """A new display name for the alert. Omit to leave the name unchanged (apply-if-present / PATCH). Same constraints as CreateAlert.name; the name is not the alert's identity, so a rename never changes the alertId."""
    description: NotRequired["str"]
    """A new description of the alert. Omit to leave unchanged."""
    rule: NotRequired["capo_cloudwatchomni.types.rule.Rule"]
    """The rule that defines how the alert is evaluated. Omit to leave unchanged. Each sub-block is replaced whole when present: {@code query}, {@code condition}, {@code evaluation} and {@code noData} are applied only when supplied, and within a supplied block an omitted optional member is cleared to unset (null/absent) rather than preserved from the stored alert or defaulted. See {@link AlertCondition} and {@link AlertEvaluation}."""
    notifications_enabled: NotRequired["bool"]
    """Whether actions (notifications) are enabled for this alert. Omitted = leave existing value unchanged."""
    notification_rules: NotRequired[
        "capo_cloudwatchomni.types.notification_rule_list.NotificationRuleList"
    ]
    """Replaces the entire notification rule list when present; full-replace, not merge. Omitted = leave existing rules unchanged. An empty list clears all rules (the alert keeps evaluating; only notifications stop)."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateAlertInput) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    out["alertId"] = value["alert_id"]
    if "profile_id" in value:
        out["profileId"] = value["profile_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "rule" in value:
        import capo_cloudwatchomni.types.rule

        out["rule"] = capo_cloudwatchomni.types.rule.serialize_cbor(value["rule"])
    if "notifications_enabled" in value:
        out["notificationsEnabled"] = value["notifications_enabled"]
    if "notification_rules" in value:
        import capo_cloudwatchomni.types.notification_rule_list

        out["notificationRules"] = (
            capo_cloudwatchomni.types.notification_rule_list.serialize_cbor(
                value["notification_rules"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> UpdateAlertInput:
    out: UpdateAlertInput = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    if data.get("alertId") is not None:
        out["alert_id"] = data["alertId"]
    else:
        out["alert_id"] = ""
    if data.get("profileId") is not None:
        out["profile_id"] = data["profileId"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("rule") is not None:
        import capo_cloudwatchomni.types.rule

        out["rule"] = capo_cloudwatchomni.types.rule.deserialize_cbor(data["rule"])
    if data.get("notificationsEnabled") is not None:
        out["notifications_enabled"] = data["notificationsEnabled"]
    if data.get("notificationRules") is not None:
        import capo_cloudwatchomni.types.notification_rule_list

        out["notification_rules"] = (
            capo_cloudwatchomni.types.notification_rule_list.deserialize_cbor(
                data["notificationRules"]
            )
        )
    return out
