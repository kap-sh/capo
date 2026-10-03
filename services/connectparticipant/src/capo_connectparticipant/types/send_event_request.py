"""Generated from Smithy shape ``com.amazonaws.connectparticipant#SendEventRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connectparticipant.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectparticipant.types.chat_content
    import capo_connectparticipant.types.chat_content_type
    import capo_connectparticipant.types.client_token
    import capo_connectparticipant.types.participant_token


class SendEventRequest(TypedDict, closed=True):
    content_type: "capo_connectparticipant.types.chat_content_type.ChatContentType"
    """<p>The content type of the request. Supported types are:</p> <ul> <li> <p>application/vnd.amazonaws.connect.event.typing</p> </li> <li> <p>application/vnd.amazonaws.connect.event.connection.acknowledged (is no longer maintained since December 31, 2024) </p> </li> <li> <p>application/vnd.amazonaws.connect.event.message.delivered</p> </li> <li> <p>application/vnd.amazonaws.connect.event.message.read</p> </li> </ul>"""
    content: NotRequired["capo_connectparticipant.types.chat_content.ChatContent"]
    r"""<p>The content of the event to be sent (for example, message text). For content related to message receipts, this is supported in the form of a JSON string.</p> <p>Sample Content: "{\"messageId\":\"11111111-aaaa-bbbb-cccc-EXAMPLE01234\"}"</p>"""
    client_token: NotRequired["capo_connectparticipant.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""
    connection_token: "capo_connectparticipant.types.participant_token.ParticipantToken"
    """<p>The authentication token associated with the participant's connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendEventRequest) -> dict:
    out: dict = {}
    out["ContentType"] = value["content_type"]
    if "content" in value:
        out["Content"] = value["content"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> SendEventRequest:
    out: SendEventRequest = {}  # type: ignore[typeddict-item]
    if data.get("ContentType") is not None:
        out["content_type"] = data["ContentType"]
    else:
        raise DeserializationError("SendEventRequest.content_type required")
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
