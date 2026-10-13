"""Generated from Smithy shape ``com.amazonaws.healthlake#UpdateProfileWithAgentRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import capo_healthlake.types.agent_input_message
    import capo_healthlake.types.conversation_id_string
    import capo_healthlake.types.profile_id_string
    import capo_healthlake.types.source_format


class UpdateProfileWithAgentRequest(TypedDict, closed=True):
    profile_id: "capo_healthlake.types.profile_id_string.ProfileIdString"
    """<p>The unique identifier of the profile to update via the agent.</p>"""
    source_format: "capo_healthlake.types.source_format.SourceFormat"
    """<p>The source data format for the transformation.</p>"""
    input_message: "capo_healthlake.types.agent_input_message.AgentInputMessage"
    """<p>The message to send to the agent.</p>"""
    conversation_id: NotRequired[
        "capo_healthlake.types.conversation_id_string.ConversationIdString"
    ]
    """<p>The conversation identifier for multi-turn interactions. Omit to start a new conversation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateProfileWithAgentRequest) -> dict:
    out: dict = {}
    out["ProfileId"] = value["profile_id"]
    import capo_healthlake.types.source_format

    out["SourceFormat"] = capo_healthlake.types.source_format.serialize_aws_json_1_0(
        value["source_format"]
    )
    import capo_healthlake.types.agent_input_message

    out["InputMessage"] = (
        capo_healthlake.types.agent_input_message.serialize_aws_json_1_0(
            value["input_message"]
        )
    )
    if "conversation_id" in value:
        out["ConversationId"] = value["conversation_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateProfileWithAgentRequest:
    out: UpdateProfileWithAgentRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    else:
        raise DeserializationError("UpdateProfileWithAgentRequest.profile_id required")
    if data.get("SourceFormat") is not None:
        import capo_healthlake.types.source_format

        out["source_format"] = (
            capo_healthlake.types.source_format.deserialize_aws_json_1_0(
                data["SourceFormat"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateProfileWithAgentRequest.source_format required"
        )
    if data.get("InputMessage") is not None:
        import capo_healthlake.types.agent_input_message

        out["input_message"] = (
            capo_healthlake.types.agent_input_message.deserialize_aws_json_1_0(
                data["InputMessage"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateProfileWithAgentRequest.input_message required"
        )
    if data.get("ConversationId") is not None:
        out["conversation_id"] = data["ConversationId"]
    return out


def redact_sensitive(value: UpdateProfileWithAgentRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "input_message" in value:
        import capo_healthlake.types.agent_input_message

        out["input_message"] = (
            capo_healthlake.types.agent_input_message.redact_sensitive(
                value["input_message"]
            )
        )
    return out
