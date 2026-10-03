"""Generated from Smithy shape ``com.amazonaws.pinpointemail#RawMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_pinpoint_email.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_email.types.raw_message_data


class RawMessage(TypedDict, closed=True):
    data: "capo_pinpoint_email.types.raw_message_data.RawMessageData"
    """<p>The raw email message. The message has to meet the following criteria:</p> <ul> <li> <p>The message has to contain a header and a body, separated by one blank line.</p> </li> <li> <p>All of the required header fields must be present in the message.</p> </li> <li> <p>Each part of a multipart MIME message must be formatted properly.</p> </li> <li> <p>Attachments must be in a file format that Amazon Pinpoint supports. </p> </li> <li> <p>The entire message must be Base64 encoded.</p> </li> <li> <p>If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII character range, you should encode that content to ensure that recipients' email clients render the message properly.</p> </li> <li> <p>The length of any single line of text in the message can't exceed 1,000 characters. This restriction is defined in <a href="https://tools.ietf.org/html/rfc5321">RFC 5321</a>.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: RawMessage) -> dict:
    out: dict = {}
    import capo_pinpoint_email.types.raw_message_data

    out["Data"] = capo_pinpoint_email.types.raw_message_data.serialize_json(
        value["data"]
    )
    return out


def deserialize_json(data: dict) -> RawMessage:
    out: RawMessage = {}  # type: ignore[typeddict-item]
    if data.get("Data") is not None:
        import capo_pinpoint_email.types.raw_message_data

        out["data"] = capo_pinpoint_email.types.raw_message_data.deserialize_json(
            data["Data"]
        )
    else:
        raise DeserializationError("RawMessage.data required")
    return out
