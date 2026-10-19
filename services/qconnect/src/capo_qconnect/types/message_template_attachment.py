"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateAttachment``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_qconnect.types.attachment_file_name
    import capo_qconnect.types.content_disposition
    import capo_qconnect.types.url
    import capo_qconnect.types.uuid


class MessageTemplateAttachment(TypedDict, closed=True):
    content_disposition: "capo_qconnect.types.content_disposition.ContentDisposition"
    """<p>The presentation information for the attachment file.</p>"""
    name: "capo_qconnect.types.attachment_file_name.AttachmentFileName"
    """<p>The name of the attachment file being uploaded. The name should include the file extension.</p>"""
    uploaded_time: "datetime.datetime"
    """<p>The timestamp when the attachment file was uploaded.</p>"""
    url: "capo_qconnect.types.url.Url"
    """<p>A pre-signed Amazon S3 URL that can be used to download the attachment file.</p>"""
    url_expiry: "datetime.datetime"
    """<p>The expiration time of the pre-signed Amazon S3 URL.</p>"""
    attachment_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the attachment file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateAttachment) -> dict:
    out: dict = {}
    out["contentDisposition"] = value["content_disposition"]
    out["name"] = value["name"]
    import capo_qconnect._protocol.serialize

    out["uploadedTime"] = capo_qconnect._protocol.serialize.fmt_date_time(
        value["uploaded_time"]
    )
    out["url"] = value["url"]
    import capo_qconnect._protocol.serialize

    out["urlExpiry"] = capo_qconnect._protocol.serialize.fmt_date_time(
        value["url_expiry"]
    )
    out["attachmentId"] = value["attachment_id"]
    return out


def deserialize_json(data: dict) -> MessageTemplateAttachment:
    out: MessageTemplateAttachment = {}  # type: ignore[typeddict-item]
    if data.get("contentDisposition") is not None:
        out["content_disposition"] = data["contentDisposition"]
    else:
        out["content_disposition"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("uploadedTime") is not None:
        import datetime

        out["uploaded_time"] = datetime.datetime.fromisoformat(
            data["uploadedTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["uploaded_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("url") is not None:
        out["url"] = data["url"]
    else:
        out["url"] = ""
    if data.get("urlExpiry") is not None:
        import datetime

        out["url_expiry"] = datetime.datetime.fromisoformat(
            data["urlExpiry"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["url_expiry"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("attachmentId") is not None:
        out["attachment_id"] = data["attachmentId"]
    else:
        out["attachment_id"] = ""
    return out


def redact_sensitive(value: MessageTemplateAttachment) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "url" in value:
        out["url"] = "*** Sensitive Data Redacted ***"
    return out
