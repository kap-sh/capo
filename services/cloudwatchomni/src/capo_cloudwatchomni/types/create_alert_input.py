"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#CreateAlertInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.notification_rule_list
    import capo_cloudwatchomni.types.profile_id
    import capo_cloudwatchomni.types.rule
    import capo_cloudwatchomni.types.space_id
    import capo_cloudwatchomni.types.tag_map


class CreateAlertInput(TypedDict, closed=True):
    space_id: "capo_cloudwatchomni.types.space_id.SpaceId"
    """The unique ID of the space to create the alert in."""
    profile_id: "capo_cloudwatchomni.types.profile_id.ProfileId"
    """The ID of the access profile the alert uses to evaluate its query and execute notifications. The caller supplies it: there is no managed alert profile, and the service does not pick one on the caller's behalf."""
    name: "str"
    """Alert name, for display. Max 256 (the AlarmName budget). Not the alert's identity: the backend mints a separate uuid as the {@link AlertId}, so the name need not be unique within a space and addressing an alert never depends on it. UpdateAlert accepts a new name to rename the alert."""
    description: NotRequired["str"]
    """An optional description of the alert."""
    rule: "capo_cloudwatchomni.types.rule.Rule"
    """The rule that defines how the alert is evaluated."""
    notifications_enabled: NotRequired["bool"]
    """Whether actions (notifications) are enabled for this alert. Defaults to true when omitted."""
    tags: NotRequired["capo_cloudwatchomni.types.tag_map.TagMap"]
    """The tags to associate with the alert."""
    notification_rules: NotRequired[
        "capo_cloudwatchomni.types.notification_rule_list.NotificationRuleList"
    ]
    """The notification rules that determine when and where notifications are sent."""
    client_token: NotRequired["str"]
    """Idempotency token for safe retries. Retrying with the same token within the idempotency window returns the original alert instead of creating a duplicate."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateAlertInput) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    out["profileId"] = value["profile_id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_cloudwatchomni.types.rule

    out["rule"] = capo_cloudwatchomni.types.rule.serialize_cbor(value["rule"])
    if "notifications_enabled" in value:
        out["notificationsEnabled"] = value["notifications_enabled"]
    if "tags" in value:
        import capo_cloudwatchomni.types.tag_map

        out["tags"] = capo_cloudwatchomni.types.tag_map.serialize_cbor(value["tags"])
    if "notification_rules" in value:
        import capo_cloudwatchomni.types.notification_rule_list

        out["notificationRules"] = (
            capo_cloudwatchomni.types.notification_rule_list.serialize_cbor(
                value["notification_rules"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_cbor(data: dict) -> CreateAlertInput:
    out: CreateAlertInput = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    if data.get("profileId") is not None:
        out["profile_id"] = data["profileId"]
    else:
        out["profile_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("rule") is not None:
        import capo_cloudwatchomni.types.rule

        out["rule"] = capo_cloudwatchomni.types.rule.deserialize_cbor(data["rule"])
    else:
        out["rule"] = {"$unknown": {"name": ""}}
    if data.get("notificationsEnabled") is not None:
        out["notifications_enabled"] = data["notificationsEnabled"]
    if data.get("tags") is not None:
        import capo_cloudwatchomni.types.tag_map

        out["tags"] = capo_cloudwatchomni.types.tag_map.deserialize_cbor(data["tags"])
    if data.get("notificationRules") is not None:
        import capo_cloudwatchomni.types.notification_rule_list

        out["notification_rules"] = (
            capo_cloudwatchomni.types.notification_rule_list.deserialize_cbor(
                data["notificationRules"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
