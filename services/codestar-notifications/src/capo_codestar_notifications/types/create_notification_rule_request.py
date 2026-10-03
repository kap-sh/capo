"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#CreateNotificationRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codestar_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codestar_notifications.types.client_request_token
    import capo_codestar_notifications.types.detail_type
    import capo_codestar_notifications.types.event_type_ids
    import capo_codestar_notifications.types.notification_rule_name
    import capo_codestar_notifications.types.notification_rule_resource
    import capo_codestar_notifications.types.notification_rule_status
    import capo_codestar_notifications.types.tags
    import capo_codestar_notifications.types.targets


class CreateNotificationRuleRequest(TypedDict, closed=True):
    name: (
        "capo_codestar_notifications.types.notification_rule_name.NotificationRuleName"
    )
    """<p>The name for the notification rule. Notification rule names must be unique in your Amazon Web Services account.</p>"""
    event_type_ids: "capo_codestar_notifications.types.event_type_ids.EventTypeIds"
    """<p>A list of event types associated with this notification rule. For a list of allowed events, see <a>EventTypeSummary</a>.</p>"""
    resource: "capo_codestar_notifications.types.notification_rule_resource.NotificationRuleResource"
    """<p>The Amazon Resource Name (ARN) of the resource to associate with the notification rule. Supported resources include pipelines in CodePipeline, repositories in CodeCommit, and build projects in CodeBuild.</p>"""
    targets: "capo_codestar_notifications.types.targets.Targets"
    """<p>A list of Amazon Resource Names (ARNs) of Amazon Simple Notification Service topics and Amazon Q Developer in chat applications clients to associate with the notification rule.</p>"""
    detail_type: "capo_codestar_notifications.types.detail_type.DetailType"
    """<p>The level of detail to include in the notifications for this resource. <code>BASIC</code> will include only the contents of the event as it would appear in Amazon CloudWatch. <code>FULL</code> will include any supplemental information provided by CodeStar Notifications and/or the service for the resource for which the notification is created.</p>"""
    client_request_token: NotRequired[
        "capo_codestar_notifications.types.client_request_token.ClientRequestToken"
    ]
    """<p>A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request with the same parameters is received and a token is included, the request returns information about the initial request that used that token.</p> <note> <p>The Amazon Web Services SDKs prepopulate client request tokens. If you are using an Amazon Web Services SDK, an idempotency token is created for you.</p> </note>"""
    tags: NotRequired["capo_codestar_notifications.types.tags.Tags"]
    """<p>A list of tags to apply to this notification rule. Key names cannot start with "<code>aws</code>". </p>"""
    status: NotRequired[
        "capo_codestar_notifications.types.notification_rule_status.NotificationRuleStatus"
    ]
    """<p>The status of the notification rule. The default value is <code>ENABLED</code>. If the status is set to <code>DISABLED</code>, notifications aren't sent for the notification rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNotificationRuleRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_codestar_notifications.types.event_type_ids

    out["EventTypeIds"] = (
        capo_codestar_notifications.types.event_type_ids.serialize_json(
            value["event_type_ids"]
        )
    )
    out["Resource"] = value["resource"]
    import capo_codestar_notifications.types.targets

    out["Targets"] = capo_codestar_notifications.types.targets.serialize_json(
        value["targets"]
    )
    import capo_codestar_notifications.types.detail_type

    out["DetailType"] = capo_codestar_notifications.types.detail_type.serialize_json(
        value["detail_type"]
    )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import capo_codestar_notifications.types.tags

        out["Tags"] = capo_codestar_notifications.types.tags.serialize_json(
            value["tags"]
        )
    if "status" in value:
        import capo_codestar_notifications.types.notification_rule_status

        out["Status"] = (
            capo_codestar_notifications.types.notification_rule_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateNotificationRuleRequest:
    out: CreateNotificationRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateNotificationRuleRequest.name required")
    if data.get("EventTypeIds") is not None:
        import capo_codestar_notifications.types.event_type_ids

        out["event_type_ids"] = (
            capo_codestar_notifications.types.event_type_ids.deserialize_json(
                data["EventTypeIds"]
            )
        )
    else:
        raise DeserializationError(
            "CreateNotificationRuleRequest.event_type_ids required"
        )
    if data.get("Resource") is not None:
        out["resource"] = data["Resource"]
    else:
        raise DeserializationError("CreateNotificationRuleRequest.resource required")
    if data.get("Targets") is not None:
        import capo_codestar_notifications.types.targets

        out["targets"] = capo_codestar_notifications.types.targets.deserialize_json(
            data["Targets"]
        )
    else:
        raise DeserializationError("CreateNotificationRuleRequest.targets required")
    if data.get("DetailType") is not None:
        import capo_codestar_notifications.types.detail_type

        out["detail_type"] = (
            capo_codestar_notifications.types.detail_type.deserialize_json(
                data["DetailType"]
            )
        )
    else:
        raise DeserializationError("CreateNotificationRuleRequest.detail_type required")
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("Tags") is not None:
        import capo_codestar_notifications.types.tags

        out["tags"] = capo_codestar_notifications.types.tags.deserialize_json(
            data["Tags"]
        )
    if data.get("Status") is not None:
        import capo_codestar_notifications.types.notification_rule_status

        out["status"] = (
            capo_codestar_notifications.types.notification_rule_status.deserialize_json(
                data["Status"]
            )
        )
    return out
