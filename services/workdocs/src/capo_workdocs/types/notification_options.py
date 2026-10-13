"""Generated from Smithy shape ``com.amazonaws.workdocs#NotificationOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.boolean_type
    import capo_workdocs.types.message_type


class NotificationOptions(TypedDict, closed=True):
    send_email: "capo_workdocs.types.boolean_type.BooleanType"
    """<p>Boolean value to indicate an email notification should be sent to the recipients.</p>"""
    email_message: NotRequired["capo_workdocs.types.message_type.MessageType"]
    """<p>Text value to be included in the email body.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationOptions) -> dict:
    out: dict = {}
    out["SendEmail"] = value.get("send_email", False)
    if "email_message" in value:
        out["EmailMessage"] = value["email_message"]
    return out


def deserialize_json(data: dict) -> NotificationOptions:
    out: NotificationOptions = {}  # type: ignore[typeddict-item]
    if data.get("SendEmail") is not None:
        out["send_email"] = data["SendEmail"]
    else:
        out["send_email"] = False
    if data.get("EmailMessage") is not None:
        out["email_message"] = data["EmailMessage"]
    return out


def redact_sensitive(value: NotificationOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "email_message" in value:
        out["email_message"] = "*** Sensitive Data Redacted ***"
    return out
