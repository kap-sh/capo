"""Generated from Smithy shape ``com.amazonaws.healthlake#AgentInputMessage``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import capo_healthlake.types.agent_input_message_type
    import capo_healthlake.types.agent_message_string


class AgentInputMessage(TypedDict, closed=True):
    body: "capo_healthlake.types.agent_message_string.AgentMessageString"
    """<p>The text of your message to the agent.</p>"""
    type: "capo_healthlake.types.agent_input_message_type.AgentInputMessageType"
    """<p>The type of input message, which determines how the agent processes your request. Valid values:</p> <ul> <li> <p> <code>normal</code>: A regular message to the agent.</p> </li> <li> <p> <code>confirmation_response</code>: A response to a confirmation request from the agent.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgentInputMessage) -> dict:
    out: dict = {}
    out["Body"] = value["body"]
    import capo_healthlake.types.agent_input_message_type

    out["Type"] = capo_healthlake.types.agent_input_message_type.serialize_aws_json_1_0(
        value["type"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> AgentInputMessage:
    out: AgentInputMessage = {}  # type: ignore[typeddict-item]
    if data.get("Body") is not None:
        out["body"] = data["Body"]
    else:
        raise DeserializationError("AgentInputMessage.body required")
    if data.get("Type") is not None:
        import capo_healthlake.types.agent_input_message_type

        out["type"] = (
            capo_healthlake.types.agent_input_message_type.deserialize_aws_json_1_0(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("AgentInputMessage.type required")
    return out


def redact_sensitive(value: AgentInputMessage) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "body" in value:
        out["body"] = "*** Sensitive Data Redacted ***"
    return out
