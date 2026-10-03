"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#Conversational``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.content
    import capo_bedrock_agentcore.types.role


class Conversational(TypedDict, closed=True):
    content: "capo_bedrock_agentcore.types.content.Content"
    """<p>The content of the conversation message.</p>"""
    role: "capo_bedrock_agentcore.types.role.Role"
    """<p>The role of the participant in the conversation (for example, "user" or "assistant").</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Conversational) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.content

    out["content"] = capo_bedrock_agentcore.types.content.serialize_json(
        value["content"]
    )
    import capo_bedrock_agentcore.types.role

    out["role"] = capo_bedrock_agentcore.types.role.serialize_json(value["role"])
    return out


def deserialize_json(data: dict) -> Conversational:
    out: Conversational = {}  # type: ignore[typeddict-item]
    if data.get("content") is not None:
        import capo_bedrock_agentcore.types.content

        out["content"] = capo_bedrock_agentcore.types.content.deserialize_json(
            data["content"]
        )
    else:
        raise DeserializationError("Conversational.content required")
    if data.get("role") is not None:
        import capo_bedrock_agentcore.types.role

        out["role"] = capo_bedrock_agentcore.types.role.deserialize_json(data["role"])
    else:
        raise DeserializationError("Conversational.role required")
    return out
