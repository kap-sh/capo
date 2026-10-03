"""Generated from Smithy shape ``com.amazonaws.connect#Notification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.notification_content
    import capo_connect.types.notification_id
    import capo_connect.types.notification_priority
    import capo_connect.types.recipient_list
    import capo_connect.types.region_name
    import capo_connect.types.tag_map
    import capo_connect.types.timestamp


class Notification(TypedDict, closed=True):
    content: NotRequired["capo_connect.types.notification_content.NotificationContent"]
    """<p>The localized content of the notification. A map where keys are locale codes and values are the notification text in that locale.</p>"""
    id: "capo_connect.types.notification_id.NotificationId"
    """<p>The unique identifier for the notification.</p>"""
    arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the notification.</p>"""
    priority: NotRequired[
        "capo_connect.types.notification_priority.NotificationPriority"
    ]
    """<p>The priority level of the notification. Valid values are URGENT, HIGH, and LOW.</p>"""
    recipients: NotRequired["capo_connect.types.recipient_list.RecipientList"]
    """<p>A list of Amazon Resource Names (ARNs) identifying the recipients of the notification. Maximum of 200 recipients.</p>"""
    last_modified_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The timestamp when the notification was last modified.</p>"""
    created_at: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the notification was created.</p>"""
    expires_at: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the notification expires and is no longer displayed to users.</p>"""
    last_modified_region: NotRequired["capo_connect.types.region_name.RegionName"]
    """<p>The AWS Region where the notification was last modified.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, <code>{ "Tags": {"key1":"value1", "key2":"value2"} }</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Notification) -> dict:
    out: dict = {}
    if "content" in value:
        import capo_connect.types.notification_content

        out["Content"] = capo_connect.types.notification_content.serialize_json(
            value["content"]
        )
    out["Id"] = value["id"]
    out["Arn"] = value["arn"]
    if "priority" in value:
        import capo_connect.types.notification_priority

        out["Priority"] = capo_connect.types.notification_priority.serialize_json(
            value["priority"]
        )
    if "recipients" in value:
        import capo_connect.types.recipient_list

        out["Recipients"] = capo_connect.types.recipient_list.serialize_json(
            value["recipients"]
        )
    import capo_connect.types.timestamp

    out["LastModifiedTime"] = capo_connect.types.timestamp.serialize_json(
        value["last_modified_time"]
    )
    if "created_at" in value:
        import capo_connect.types.timestamp

        out["CreatedAt"] = capo_connect.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "expires_at" in value:
        import capo_connect.types.timestamp

        out["ExpiresAt"] = capo_connect.types.timestamp.serialize_json(
            value["expires_at"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> Notification:
    out: Notification = {}  # type: ignore[typeddict-item]
    if data.get("Content") is not None:
        import capo_connect.types.notification_content

        out["content"] = capo_connect.types.notification_content.deserialize_json(
            data["Content"]
        )
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("Notification.id required")
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("Notification.arn required")
    if data.get("Priority") is not None:
        import capo_connect.types.notification_priority

        out["priority"] = capo_connect.types.notification_priority.deserialize_json(
            data["Priority"]
        )
    if data.get("Recipients") is not None:
        import capo_connect.types.recipient_list

        out["recipients"] = capo_connect.types.recipient_list.deserialize_json(
            data["Recipients"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_connect.types.timestamp

        out["last_modified_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    else:
        raise DeserializationError("Notification.last_modified_time required")
    if data.get("CreatedAt") is not None:
        import capo_connect.types.timestamp

        out["created_at"] = capo_connect.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if data.get("ExpiresAt") is not None:
        import capo_connect.types.timestamp

        out["expires_at"] = capo_connect.types.timestamp.deserialize_json(
            data["ExpiresAt"]
        )
    if data.get("LastModifiedRegion") is not None:
        out["last_modified_region"] = data["LastModifiedRegion"]
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
