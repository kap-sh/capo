"""Generated from Smithy shape ``com.amazonaws.notifications#NotificationEventAttachment``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import capo_notifications.types.attachment_content_type
    import capo_notifications.types.attachment_display_name
    import capo_notifications.types.sensitive_url


class NotificationEventAttachment(TypedDict, closed=True):
    display_name: (
        "capo_notifications.types.attachment_display_name.AttachmentDisplayName"
    )
    """<p>The name of the attachment that recipients see.</p>"""
    attachment_download_url: NotRequired[
        "capo_notifications.types.sensitive_url.SensitiveUrl"
    ]
    """<p>A temporary URL for downloading the attachment. The URL expires shortly after it's issued.</p>"""
    content_type: (
        "capo_notifications.types.attachment_content_type.AttachmentContentType"
    )
    """<p>The MIME content type of the attachment, for example <code>application/pdf</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationEventAttachment) -> dict:
    out: dict = {}
    out["displayName"] = value["display_name"]
    if "attachment_download_url" in value:
        out["attachmentDownloadUrl"] = value["attachment_download_url"]
    out["contentType"] = value["content_type"]
    return out


def deserialize_json(data: dict) -> NotificationEventAttachment:
    out: NotificationEventAttachment = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("NotificationEventAttachment.display_name required")
    if data.get("attachmentDownloadUrl") is not None:
        out["attachment_download_url"] = data["attachmentDownloadUrl"]
    if data.get("contentType") is not None:
        out["content_type"] = data["contentType"]
    else:
        raise DeserializationError("NotificationEventAttachment.content_type required")
    return out


def redact_sensitive(value: NotificationEventAttachment) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "attachment_download_url" in value:
        out["attachment_download_url"] = "*** Sensitive Data Redacted ***"
    return out
