"""Generated from Smithy shape ``com.amazonaws.securityagent#ActorMessage``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_securityagent.types.sensitive_message_body
    import capo_securityagent.types.sensitive_message_sender
    import capo_securityagent.types.sensitive_message_subject


class ActorMessage(TypedDict, closed=True):
    sender: NotRequired[
        "capo_securityagent.types.sensitive_message_sender.SensitiveMessageSender"
    ]
    """<p>The address the message was sent from.</p>"""
    subject: NotRequired[
        "capo_securityagent.types.sensitive_message_subject.SensitiveMessageSubject"
    ]
    """<p>The subject line of the message.</p>"""
    body: NotRequired[
        "capo_securityagent.types.sensitive_message_body.SensitiveMessageBody"
    ]
    """<p>The plain-text body of the message, containing the MFA code or verification link.</p>"""
    received_at: NotRequired["datetime.datetime"]
    """<p>The time the message was received.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActorMessage) -> dict:
    out: dict = {}
    if "sender" in value:
        out["sender"] = value["sender"]
    if "subject" in value:
        out["subject"] = value["subject"]
    if "body" in value:
        out["body"] = value["body"]
    if "received_at" in value:
        import capo_securityagent._protocol.serialize

        out["receivedAt"] = capo_securityagent._protocol.serialize.fmt_date_time(
            value["received_at"]
        )
    return out


def deserialize_json(data: dict) -> ActorMessage:
    out: ActorMessage = {}  # type: ignore[typeddict-item]
    if data.get("sender") is not None:
        out["sender"] = data["sender"]
    if data.get("subject") is not None:
        out["subject"] = data["subject"]
    if data.get("body") is not None:
        out["body"] = data["body"]
    if data.get("receivedAt") is not None:
        import datetime

        out["received_at"] = datetime.datetime.fromisoformat(
            data["receivedAt"].replace("Z", "+00:00")
        )
    return out


def redact_sensitive(value: ActorMessage) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sender" in value:
        out["sender"] = "*** Sensitive Data Redacted ***"
    if "subject" in value:
        out["subject"] = "*** Sensitive Data Redacted ***"
    if "body" in value:
        out["body"] = "*** Sensitive Data Redacted ***"
    return out
