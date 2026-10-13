"""Generated from Smithy shape ``com.amazonaws.healthlake#UpdateProfileWithAgentResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import capo_healthlake.types.agent_output_message
    import capo_healthlake.types.conversation_id_string


class UpdateProfileWithAgentResponse(TypedDict, closed=True):
    agent_response: "capo_healthlake.types.agent_output_message.AgentOutputMessage"
    """<p>The response message from the agent.</p>"""
    conversation_id: "capo_healthlake.types.conversation_id_string.ConversationIdString"
    """<p>The conversation identifier to use for follow-up messages in this conversation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateProfileWithAgentResponse) -> dict:
    out: dict = {}
    import capo_healthlake.types.agent_output_message

    out["AgentResponse"] = (
        capo_healthlake.types.agent_output_message.serialize_aws_json_1_0(
            value["agent_response"]
        )
    )
    out["ConversationId"] = value["conversation_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateProfileWithAgentResponse:
    out: UpdateProfileWithAgentResponse = {}  # type: ignore[typeddict-item]
    if data.get("AgentResponse") is not None:
        import capo_healthlake.types.agent_output_message

        out["agent_response"] = (
            capo_healthlake.types.agent_output_message.deserialize_aws_json_1_0(
                data["AgentResponse"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateProfileWithAgentResponse.agent_response required"
        )
    if data.get("ConversationId") is not None:
        out["conversation_id"] = data["ConversationId"]
    else:
        raise DeserializationError(
            "UpdateProfileWithAgentResponse.conversation_id required"
        )
    return out


def redact_sensitive(value: UpdateProfileWithAgentResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "agent_response" in value:
        import capo_healthlake.types.agent_output_message

        out["agent_response"] = (
            capo_healthlake.types.agent_output_message.redact_sensitive(
                value["agent_response"]
            )
        )
    return out
