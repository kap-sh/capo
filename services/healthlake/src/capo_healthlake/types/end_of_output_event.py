"""Generated from Smithy shape ``com.amazonaws.healthlake#EndOfOutputEvent``."""

import json
from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_healthlake._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_healthlake.types.agent_message_string
    import capo_healthlake.types.conversation_id_string
    import capo_healthlake.types.data_transformation_chat_options_list


class EndOfOutputEvent(TypedDict, closed=True):
    final_response_message: (
        "capo_healthlake.types.agent_message_string.AgentMessageString"
    )
    """<p>The final response message from the agent.</p>"""
    options: NotRequired[
        "capo_healthlake.types.data_transformation_chat_options_list.DataTransformationChatOptionsList"
    ]
    """<p>The response options that you can use to easily answer follow-up questions from the agent.</p>"""
    conversation_id: NotRequired[
        "capo_healthlake.types.conversation_id_string.ConversationIdString"
    ]
    """<p>The conversation ID of the request. You can use this ID to continue the profile mapping based on this request's context at a later time.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EndOfOutputEvent) -> dict:
    out: dict = {}
    out["FinalResponseMessage"] = value["final_response_message"]
    if "options" in value:
        import capo_healthlake.types.data_transformation_chat_options_list

        out["Options"] = (
            capo_healthlake.types.data_transformation_chat_options_list.serialize_aws_json_1_0(
                value["options"]
            )
        )
    if "conversation_id" in value:
        out["ConversationId"] = value["conversation_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EndOfOutputEvent:
    out: EndOfOutputEvent = {}  # type: ignore[typeddict-item]
    if data.get("FinalResponseMessage") is not None:
        out["final_response_message"] = data["FinalResponseMessage"]
    else:
        out["final_response_message"] = ""
    if data.get("Options") is not None:
        import capo_healthlake.types.data_transformation_chat_options_list

        out["options"] = (
            capo_healthlake.types.data_transformation_chat_options_list.deserialize_aws_json_1_0(
                data["Options"]
            )
        )
    if data.get("ConversationId") is not None:
        out["conversation_id"] = data["ConversationId"]
    return out


def serialize_event_aws_json_1_0(value: EndOfOutputEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "EndOfOutputEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_aws_json_1_0(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_aws_json_1_0(message: Message) -> EndOfOutputEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: EndOfOutputEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_aws_json_1_0(json.loads(payload))
    return out


def redact_sensitive(value: EndOfOutputEvent) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "final_response_message" in value:
        out["final_response_message"] = "*** Sensitive Data Redacted ***"
    if "options" in value:
        import capo_healthlake.types.data_transformation_chat_options_list

        out["options"] = (
            capo_healthlake.types.data_transformation_chat_options_list.redact_sensitive(
                value["options"]
            )
        )
    return out
