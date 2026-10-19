"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessMessage``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.harness_content_blocks
    import capo_bedrock_agentcore.types.harness_conversation_role


class HarnessMessage(TypedDict, closed=True):
    role: (
        "capo_bedrock_agentcore.types.harness_conversation_role.HarnessConversationRole"
    )
    """<p>The role of the message sender.</p>"""
    content: "capo_bedrock_agentcore.types.harness_content_blocks.HarnessContentBlocks"
    """<p>The content blocks of the message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessMessage) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.harness_conversation_role

    out["role"] = capo_bedrock_agentcore.types.harness_conversation_role.serialize_json(
        value["role"]
    )
    import capo_bedrock_agentcore.types.harness_content_blocks

    out["content"] = capo_bedrock_agentcore.types.harness_content_blocks.serialize_json(
        value["content"]
    )
    return out


def deserialize_json(data: dict) -> HarnessMessage:
    out: HarnessMessage = {}  # type: ignore[typeddict-item]
    if data.get("role") is not None:
        import capo_bedrock_agentcore.types.harness_conversation_role

        out["role"] = (
            capo_bedrock_agentcore.types.harness_conversation_role.deserialize_json(
                data["role"]
            )
        )
    else:
        import typing

        out["role"] = typing.cast(
            "capo_bedrock_agentcore.types.harness_conversation_role.HarnessConversationRole",
            "",
        )
    if data.get("content") is not None:
        import capo_bedrock_agentcore.types.harness_content_blocks

        out["content"] = (
            capo_bedrock_agentcore.types.harness_content_blocks.deserialize_json(
                data["content"]
            )
        )
    else:
        out["content"] = []
    return out


def redact_sensitive(value: HarnessMessage) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        import capo_bedrock_agentcore.types.harness_content_blocks

        out["content"] = (
            capo_bedrock_agentcore.types.harness_content_blocks.redact_sensitive(
                value["content"]
            )
        )
    return out
