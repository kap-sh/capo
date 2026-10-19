"""Generated from Smithy shape ``com.amazonaws.iotevents#EmailConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_events.types.email_content
    import capo_iot_events.types.email_recipients
    import capo_iot_events.types.from_email

EmailConfiguration = TypedDict(
    "EmailConfiguration",
    {
        "from": "capo_iot_events.types.from_email.FromEmail",
        "content": NotRequired["capo_iot_events.types.email_content.EmailContent"],
        "recipients": "capo_iot_events.types.email_recipients.EmailRecipients",
    },
    closed=True,
)


# --- restJson1 ser/de ---
def serialize_json(value: EmailConfiguration) -> dict:
    out: dict = {}
    out["from"] = value["from"]
    if "content" in value:
        import capo_iot_events.types.email_content

        out["content"] = capo_iot_events.types.email_content.serialize_json(
            value["content"]
        )
    import capo_iot_events.types.email_recipients

    out["recipients"] = capo_iot_events.types.email_recipients.serialize_json(
        value["recipients"]
    )
    return out


def deserialize_json(data: dict) -> EmailConfiguration:
    out: EmailConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("from") is not None:
        out["from"] = data["from"]
    else:
        out["from"] = ""
    if data.get("content") is not None:
        import capo_iot_events.types.email_content

        out["content"] = capo_iot_events.types.email_content.deserialize_json(
            data["content"]
        )
    if data.get("recipients") is not None:
        import capo_iot_events.types.email_recipients

        out["recipients"] = capo_iot_events.types.email_recipients.deserialize_json(
            data["recipients"]
        )
    else:
        raise DeserializationError("EmailConfiguration.recipients required")
    return out
