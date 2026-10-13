"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#OptimizedPrompt``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.text_prompt


class _OptimizedPrompt_textPrompt(TypedDict, closed=True):
    textPrompt: "capo_bedrock_agent_runtime.types.text_prompt.TextPrompt"


OptimizedPrompt: TypeAlias = _OptimizedPrompt_textPrompt


# --- restJson1 ser/de ---
def serialize_json(value: OptimizedPrompt) -> dict:
    if "textPrompt" in value:
        import capo_bedrock_agent_runtime.types.text_prompt

        return {
            "textPrompt": capo_bedrock_agent_runtime.types.text_prompt.serialize_json(
                value["textPrompt"]
            )
        }
    else:
        raise SerializationError("OptimizedPrompt: no variant present")


def deserialize_json(data: dict) -> OptimizedPrompt:
    if data.get("textPrompt") is not None:
        import capo_bedrock_agent_runtime.types.text_prompt

        return {
            "textPrompt": capo_bedrock_agent_runtime.types.text_prompt.deserialize_json(
                data["textPrompt"]
            )
        }
    else:
        raise DeserializationError("OptimizedPrompt: no recognized variant key")


def redact_sensitive(value: OptimizedPrompt) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "textPrompt" in value:
        out["textPrompt"] = "*** Sensitive Data Redacted ***"
    return out
