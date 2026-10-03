"""Generated from Smithy shape ``com.amazonaws.connect#CreateNotificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.client_token
    import capo_connect.types.configurable_notification_priority
    import capo_connect.types.instance_id
    import capo_connect.types.notification_content
    import capo_connect.types.notification_id
    import capo_connect.types.recipient_list
    import capo_connect.types.tag_map
    import capo_connect.types.timestamp


class CreateNotificationRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Amazon Connect instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    expires_at: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the notification should expire and no longer be displayed to users. If not specified, defaults to one week from creation.</p>"""
    recipients: "capo_connect.types.recipient_list.RecipientList"
    """<p>A list of Amazon Resource Names (ARNs) identifying the recipients of the notification. Can include user ARNs or instance ARNs to target all users in an instance. Maximum of 200 recipients.</p>"""
    priority: NotRequired[
        "capo_connect.types.configurable_notification_priority.ConfigurableNotificationPriority"
    ]
    """<p>The priority level of the notification. Valid values are HIGH and LOW. High priority notifications are displayed above low priority notifications.</p>"""
    content: "capo_connect.types.notification_content.NotificationContent"
    """<p>The localized content of the notification. A map where keys are locale codes and values are the notification text in that locale. Content supports links. Maximum 250 characters per locale.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, <code>{ "Tags": {"key1":"value1", "key2":"value2"} }</code>.</p>"""
    predefined_notification_id: NotRequired[
        "capo_connect.types.notification_id.NotificationId"
    ]
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNotificationRequest) -> dict:
    out: dict = {}
    if "expires_at" in value:
        import capo_connect.types.timestamp

        out["ExpiresAt"] = capo_connect.types.timestamp.serialize_json(
            value["expires_at"]
        )
    import capo_connect.types.recipient_list

    out["Recipients"] = capo_connect.types.recipient_list.serialize_json(
        value["recipients"]
    )
    if "priority" in value:
        import capo_connect.types.configurable_notification_priority

        out["Priority"] = (
            capo_connect.types.configurable_notification_priority.serialize_json(
                value["priority"]
            )
        )
    import capo_connect.types.notification_content

    out["Content"] = capo_connect.types.notification_content.serialize_json(
        value["content"]
    )
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    if "predefined_notification_id" in value:
        out["PredefinedNotificationId"] = value["predefined_notification_id"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateNotificationRequest:
    out: CreateNotificationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ExpiresAt") is not None:
        import capo_connect.types.timestamp

        out["expires_at"] = capo_connect.types.timestamp.deserialize_json(
            data["ExpiresAt"]
        )
    if data.get("Recipients") is not None:
        import capo_connect.types.recipient_list

        out["recipients"] = capo_connect.types.recipient_list.deserialize_json(
            data["Recipients"]
        )
    else:
        raise DeserializationError("CreateNotificationRequest.recipients required")
    if data.get("Priority") is not None:
        import capo_connect.types.configurable_notification_priority

        out["priority"] = (
            capo_connect.types.configurable_notification_priority.deserialize_json(
                data["Priority"]
            )
        )
    if data.get("Content") is not None:
        import capo_connect.types.notification_content

        out["content"] = capo_connect.types.notification_content.deserialize_json(
            data["Content"]
        )
    else:
        raise DeserializationError("CreateNotificationRequest.content required")
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    if data.get("PredefinedNotificationId") is not None:
        out["predefined_notification_id"] = data["PredefinedNotificationId"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
