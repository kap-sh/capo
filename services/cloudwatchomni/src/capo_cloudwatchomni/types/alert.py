"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#Alert``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cloudwatchomni.types.account_id
    import capo_cloudwatchomni.types.alert_id
    import capo_cloudwatchomni.types.alert_state_info
    import capo_cloudwatchomni.types.arn
    import capo_cloudwatchomni.types.notification_rule_list
    import capo_cloudwatchomni.types.notification_status
    import capo_cloudwatchomni.types.profile_id
    import capo_cloudwatchomni.types.rule
    import capo_cloudwatchomni.types.space_id


class Alert(TypedDict, closed=True):
    name: "str"
    """The name of the alert."""
    alert_id: NotRequired["capo_cloudwatchomni.types.alert_id.AlertId"]
    """The stable alert identifier (see {@link AlertId}), minted on create and immutable across updates. Use it (not {@code name}) to address the alert on GetAlert/UpdateAlert/DeleteAlert; it is also the ARN's resource id."""
    description: NotRequired["str"]
    """An optional description of the alert."""
    account_id: "capo_cloudwatchomni.types.account_id.AccountId"
    """The AWS account ID that owns the alert."""
    space_id: NotRequired["capo_cloudwatchomni.types.space_id.SpaceId"]
    """The ID of the space the alert belongs to."""
    profile_id: NotRequired["capo_cloudwatchomni.types.profile_id.ProfileId"]
    """The ID of the access profile associated with the alert."""
    rule: "capo_cloudwatchomni.types.rule.Rule"
    """The rule that defines how the alert is evaluated."""
    notification_status: NotRequired[
        "capo_cloudwatchomni.types.notification_status.NotificationStatus"
    ]
    """Whether notifications are enabled."""
    state: NotRequired["capo_cloudwatchomni.types.alert_state_info.AlertStateInfo"]
    """Live evaluation state (read-only, system-managed). Populated by GetAlert. ListAlerts reports state on `AlertSummary` instead, where it stays required. Absent on CreateAlert: a newly created alert has never been evaluated, so any state reported there would be a default rather than an observation. Call GetAlert for live state. Not @required for that reason — GetAlert always populates it. `contributorSummary` is nested inside this member, so it too is absent on CreateAlert."""
    notification_rules: NotRequired[
        "capo_cloudwatchomni.types.notification_rule_list.NotificationRuleList"
    ]
    """The notification rules for the alert."""
    created_at: "datetime.datetime"
    """The timestamp when the alert was created."""
    updated_at: "datetime.datetime"
    """The timestamp when the alert was last updated."""
    alert_arn: "capo_cloudwatchomni.types.arn.Arn"
    """The Amazon Resource Name (ARN) of the alert."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Alert) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "alert_id" in value:
        out["alertId"] = value["alert_id"]
    if "description" in value:
        out["description"] = value["description"]
    out["accountId"] = value["account_id"]
    if "space_id" in value:
        out["spaceId"] = value["space_id"]
    if "profile_id" in value:
        out["profileId"] = value["profile_id"]
    import capo_cloudwatchomni.types.rule

    out["rule"] = capo_cloudwatchomni.types.rule.serialize_cbor(value["rule"])
    if "notification_status" in value:
        import capo_cloudwatchomni.types.notification_status

        out["notificationStatus"] = (
            capo_cloudwatchomni.types.notification_status.serialize_cbor(
                value["notification_status"]
            )
        )
    if "state" in value:
        import capo_cloudwatchomni.types.alert_state_info

        out["state"] = capo_cloudwatchomni.types.alert_state_info.serialize_cbor(
            value["state"]
        )
    if "notification_rules" in value:
        import capo_cloudwatchomni.types.notification_rule_list

        out["notificationRules"] = (
            capo_cloudwatchomni.types.notification_rule_list.serialize_cbor(
                value["notification_rules"]
            )
        )
    import capo_cloudwatchomni.types._prelude.timestamp

    out["createdAt"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
        value["created_at"]
    )
    import capo_cloudwatchomni.types._prelude.timestamp

    out["updatedAt"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
        value["updated_at"]
    )
    out["alertArn"] = value["alert_arn"]
    return out


def deserialize_cbor(data: dict) -> Alert:
    out: Alert = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("alertId") is not None:
        out["alert_id"] = data["alertId"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    if data.get("profileId") is not None:
        out["profile_id"] = data["profileId"]
    if data.get("rule") is not None:
        import capo_cloudwatchomni.types.rule

        out["rule"] = capo_cloudwatchomni.types.rule.deserialize_cbor(data["rule"])
    else:
        import capo_cloudwatchomni.types._unknown

        out["rule"] = capo_cloudwatchomni.types._unknown.UnknownUnionMember("")
    if data.get("notificationStatus") is not None:
        import capo_cloudwatchomni.types.notification_status

        out["notification_status"] = (
            capo_cloudwatchomni.types.notification_status.deserialize_cbor(
                data["notificationStatus"]
            )
        )
    if data.get("state") is not None:
        import capo_cloudwatchomni.types.alert_state_info

        out["state"] = capo_cloudwatchomni.types.alert_state_info.deserialize_cbor(
            data["state"]
        )
    if data.get("notificationRules") is not None:
        import capo_cloudwatchomni.types.notification_rule_list

        out["notification_rules"] = (
            capo_cloudwatchomni.types.notification_rule_list.deserialize_cbor(
                data["notificationRules"]
            )
        )
    if data.get("createdAt") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["created_at"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["updated_at"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("alertArn") is not None:
        out["alert_arn"] = data["alertArn"]
    else:
        out["alert_arn"] = ""
    return out
