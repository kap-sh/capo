"""Generated from Smithy shape ``com.amazonaws.qconnect#SendMessageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.message_configuration
    import capo_qconnect.types.next_token
    import capo_qconnect.types.uuid


class SendMessageResponse(TypedDict, closed=True):
    request_message_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the submitted message.</p>"""
    configuration: NotRequired[
        "capo_qconnect.types.message_configuration.MessageConfiguration"
    ]
    """<p>The configuration of the <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_SendMessage.html">SendMessage</a> request.</p>"""
    next_message_token: "capo_qconnect.types.next_token.NextToken"
    """<p>The token for the next message, used by GetNextMessage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendMessageResponse) -> dict:
    out: dict = {}
    out["requestMessageId"] = value["request_message_id"]
    if "configuration" in value:
        import capo_qconnect.types.message_configuration

        out["configuration"] = capo_qconnect.types.message_configuration.serialize_json(
            value["configuration"]
        )
    out["nextMessageToken"] = value["next_message_token"]
    return out


def deserialize_json(data: dict) -> SendMessageResponse:
    out: SendMessageResponse = {}  # type: ignore[typeddict-item]
    if data.get("requestMessageId") is not None:
        out["request_message_id"] = data["requestMessageId"]
    else:
        raise DeserializationError("SendMessageResponse.request_message_id required")
    if data.get("configuration") is not None:
        import capo_qconnect.types.message_configuration

        out["configuration"] = (
            capo_qconnect.types.message_configuration.deserialize_json(
                data["configuration"]
            )
        )
    if data.get("nextMessageToken") is not None:
        out["next_message_token"] = data["nextMessageToken"]
    else:
        raise DeserializationError("SendMessageResponse.next_message_token required")
    return out
