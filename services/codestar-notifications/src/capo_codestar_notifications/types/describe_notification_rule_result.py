"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#DescribeNotificationRuleResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codestar_notifications.types.created_timestamp
    import capo_codestar_notifications.types.detail_type
    import capo_codestar_notifications.types.event_type_batch
    import capo_codestar_notifications.types.last_modified_timestamp
    import capo_codestar_notifications.types.notification_rule_arn
    import capo_codestar_notifications.types.notification_rule_created_by
    import capo_codestar_notifications.types.notification_rule_name
    import capo_codestar_notifications.types.notification_rule_resource
    import capo_codestar_notifications.types.notification_rule_status
    import capo_codestar_notifications.types.tags
    import capo_codestar_notifications.types.targets_batch


class DescribeNotificationRuleResult(TypedDict, closed=True):
    arn: "capo_codestar_notifications.types.notification_rule_arn.NotificationRuleArn"
    """<p>The Amazon Resource Name (ARN) of the notification rule.</p>"""
    name: NotRequired[
        "capo_codestar_notifications.types.notification_rule_name.NotificationRuleName"
    ]
    """<p>The name of the notification rule.</p>"""
    event_types: NotRequired[
        "capo_codestar_notifications.types.event_type_batch.EventTypeBatch"
    ]
    """<p>A list of the event types associated with the notification rule.</p>"""
    resource: NotRequired[
        "capo_codestar_notifications.types.notification_rule_resource.NotificationRuleResource"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource associated with the notification rule.</p>"""
    targets: NotRequired["capo_codestar_notifications.types.targets_batch.TargetsBatch"]
    """<p>A list of the Amazon Q Developer in chat applications topics and Amazon Q Developer in chat applications clients associated with the notification rule.</p>"""
    detail_type: NotRequired["capo_codestar_notifications.types.detail_type.DetailType"]
    """<p>The level of detail included in the notifications for this resource. BASIC will include only the contents of the event as it would appear in Amazon CloudWatch. FULL will include any supplemental information provided by CodeStar Notifications and/or the service for the resource for which the notification is created.</p>"""
    created_by: NotRequired[
        "capo_codestar_notifications.types.notification_rule_created_by.NotificationRuleCreatedBy"
    ]
    """<p>The name or email alias of the person who created the notification rule.</p>"""
    status: NotRequired[
        "capo_codestar_notifications.types.notification_rule_status.NotificationRuleStatus"
    ]
    """<p>The status of the notification rule. Valid statuses are on (sending notifications) or off (not sending notifications).</p>"""
    created_timestamp: NotRequired[
        "capo_codestar_notifications.types.created_timestamp.CreatedTimestamp"
    ]
    """<p>The date and time the notification rule was created, in timestamp format.</p>"""
    last_modified_timestamp: NotRequired[
        "capo_codestar_notifications.types.last_modified_timestamp.LastModifiedTimestamp"
    ]
    """<p>The date and time the notification rule was most recently updated, in timestamp format.</p>"""
    tags: NotRequired["capo_codestar_notifications.types.tags.Tags"]
    """<p>The tags associated with the notification rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeNotificationRuleResult) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "event_types" in value:
        import capo_codestar_notifications.types.event_type_batch

        out["EventTypes"] = (
            capo_codestar_notifications.types.event_type_batch.serialize_json(
                value["event_types"]
            )
        )
    if "resource" in value:
        out["Resource"] = value["resource"]
    if "targets" in value:
        import capo_codestar_notifications.types.targets_batch

        out["Targets"] = capo_codestar_notifications.types.targets_batch.serialize_json(
            value["targets"]
        )
    if "detail_type" in value:
        import capo_codestar_notifications.types.detail_type

        out["DetailType"] = (
            capo_codestar_notifications.types.detail_type.serialize_json(
                value["detail_type"]
            )
        )
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "status" in value:
        import capo_codestar_notifications.types.notification_rule_status

        out["Status"] = (
            capo_codestar_notifications.types.notification_rule_status.serialize_json(
                value["status"]
            )
        )
    if "created_timestamp" in value:
        import capo_codestar_notifications.types.created_timestamp

        out["CreatedTimestamp"] = (
            capo_codestar_notifications.types.created_timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "last_modified_timestamp" in value:
        import capo_codestar_notifications.types.last_modified_timestamp

        out["LastModifiedTimestamp"] = (
            capo_codestar_notifications.types.last_modified_timestamp.serialize_json(
                value["last_modified_timestamp"]
            )
        )
    if "tags" in value:
        import capo_codestar_notifications.types.tags

        out["Tags"] = capo_codestar_notifications.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> DescribeNotificationRuleResult:
    out: DescribeNotificationRuleResult = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("EventTypes") is not None:
        import capo_codestar_notifications.types.event_type_batch

        out["event_types"] = (
            capo_codestar_notifications.types.event_type_batch.deserialize_json(
                data["EventTypes"]
            )
        )
    if data.get("Resource") is not None:
        out["resource"] = data["Resource"]
    if data.get("Targets") is not None:
        import capo_codestar_notifications.types.targets_batch

        out["targets"] = (
            capo_codestar_notifications.types.targets_batch.deserialize_json(
                data["Targets"]
            )
        )
    if data.get("DetailType") is not None:
        import capo_codestar_notifications.types.detail_type

        out["detail_type"] = (
            capo_codestar_notifications.types.detail_type.deserialize_json(
                data["DetailType"]
            )
        )
    if data.get("CreatedBy") is not None:
        out["created_by"] = data["CreatedBy"]
    if data.get("Status") is not None:
        import capo_codestar_notifications.types.notification_rule_status

        out["status"] = (
            capo_codestar_notifications.types.notification_rule_status.deserialize_json(
                data["Status"]
            )
        )
    if data.get("CreatedTimestamp") is not None:
        import capo_codestar_notifications.types.created_timestamp

        out["created_timestamp"] = (
            capo_codestar_notifications.types.created_timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if data.get("LastModifiedTimestamp") is not None:
        import capo_codestar_notifications.types.last_modified_timestamp

        out["last_modified_timestamp"] = (
            capo_codestar_notifications.types.last_modified_timestamp.deserialize_json(
                data["LastModifiedTimestamp"]
            )
        )
    if data.get("Tags") is not None:
        import capo_codestar_notifications.types.tags

        out["tags"] = capo_codestar_notifications.types.tags.deserialize_json(
            data["Tags"]
        )
    return out


def redact_sensitive(value: DescribeNotificationRuleResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "targets" in value:
        import capo_codestar_notifications.types.targets_batch

        out["targets"] = (
            capo_codestar_notifications.types.targets_batch.redact_sensitive(
                value["targets"]
            )
        )
    return out
