"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codestar_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codestar_notifications.types.notification_rule_arn
    import capo_codestar_notifications.types.tags


class TagResourceRequest(TypedDict, closed=True):
    arn: "capo_codestar_notifications.types.notification_rule_arn.NotificationRuleArn"
    """<p>The Amazon Resource Name (ARN) of the notification rule to tag.</p>"""
    tags: "capo_codestar_notifications.types.tags.Tags"
    """<p>The list of tags to associate with the resource. Tag key names cannot start with "<code>aws</code>".</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    import capo_codestar_notifications.types.tags

    out["Tags"] = capo_codestar_notifications.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("TagResourceRequest.arn required")
    if data.get("Tags") is not None:
        import capo_codestar_notifications.types.tags

        out["tags"] = capo_codestar_notifications.types.tags.deserialize_json(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
