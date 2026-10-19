"""Generated from Smithy shape ``com.amazonaws.qconnect#GetNextMessageResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.conversation_state
    import capo_qconnect.types.message_output
    import capo_qconnect.types.message_type
    import capo_qconnect.types.next_token
    import capo_qconnect.types.runtime_session_data_list
    import capo_qconnect.types.uuid


class GetNextMessageResponse(TypedDict, closed=True):
    type: "capo_qconnect.types.message_type.MessageType"
    """<p>The type of message response.</p>"""
    response: "capo_qconnect.types.message_output.MessageOutput"
    """<p>The message response to the requested message.</p>"""
    request_message_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the submitted message.</p>"""
    conversation_state: "capo_qconnect.types.conversation_state.ConversationState"
    """<p>The state of current conversation.</p>"""
    next_message_token: NotRequired["capo_qconnect.types.next_token.NextToken"]
    """<p>The token for the next message.</p>"""
    conversation_session_data: NotRequired[
        "capo_qconnect.types.runtime_session_data_list.RuntimeSessionDataList"
    ]
    """<p>The conversation data stored on an Amazon Q in Connect Session.</p>"""
    chunked_response_terminated: NotRequired["bool"]
    """<p>Indicates whether the chunked response has been terminated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNextMessageResponse) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    import capo_qconnect.types.message_output

    out["response"] = capo_qconnect.types.message_output.serialize_json(
        value["response"]
    )
    out["requestMessageId"] = value["request_message_id"]
    import capo_qconnect.types.conversation_state

    out["conversationState"] = capo_qconnect.types.conversation_state.serialize_json(
        value["conversation_state"]
    )
    if "next_message_token" in value:
        out["nextMessageToken"] = value["next_message_token"]
    if "conversation_session_data" in value:
        import capo_qconnect.types.runtime_session_data_list

        out["conversationSessionData"] = (
            capo_qconnect.types.runtime_session_data_list.serialize_json(
                value["conversation_session_data"]
            )
        )
    if "chunked_response_terminated" in value:
        out["chunkedResponseTerminated"] = value["chunked_response_terminated"]
    return out


def deserialize_json(data: dict) -> GetNextMessageResponse:
    out: GetNextMessageResponse = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("response") is not None:
        import capo_qconnect.types.message_output

        out["response"] = capo_qconnect.types.message_output.deserialize_json(
            data["response"]
        )
    else:
        raise DeserializationError("GetNextMessageResponse.response required")
    if data.get("requestMessageId") is not None:
        out["request_message_id"] = data["requestMessageId"]
    else:
        out["request_message_id"] = ""
    if data.get("conversationState") is not None:
        import capo_qconnect.types.conversation_state

        out["conversation_state"] = (
            capo_qconnect.types.conversation_state.deserialize_json(
                data["conversationState"]
            )
        )
    else:
        raise DeserializationError("GetNextMessageResponse.conversation_state required")
    if data.get("nextMessageToken") is not None:
        out["next_message_token"] = data["nextMessageToken"]
    if data.get("conversationSessionData") is not None:
        import capo_qconnect.types.runtime_session_data_list

        out["conversation_session_data"] = (
            capo_qconnect.types.runtime_session_data_list.deserialize_json(
                data["conversationSessionData"]
            )
        )
    if data.get("chunkedResponseTerminated") is not None:
        out["chunked_response_terminated"] = data["chunkedResponseTerminated"]
    return out


def redact_sensitive(value: GetNextMessageResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "response" in value:
        import capo_qconnect.types.message_output

        out["response"] = capo_qconnect.types.message_output.redact_sensitive(
            value["response"]
        )
    if "conversation_session_data" in value:
        import capo_qconnect.types.runtime_session_data_list

        out["conversation_session_data"] = (
            capo_qconnect.types.runtime_session_data_list.redact_sensitive(
                value["conversation_session_data"]
            )
        )
    return out
