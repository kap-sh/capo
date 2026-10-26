"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#OptimizedPrompt``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_agent_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.text_prompt


class _OptimizedPrompt_textPrompt(TypedDict, closed=True):
    textPrompt: "capo_bedrock_agent_runtime.types.text_prompt.TextPrompt"


OptimizedPrompt: TypeAlias = _OptimizedPrompt_textPrompt | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: OptimizedPrompt) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"OptimizedPrompt: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "textPrompt" in value:
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
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("OptimizedPrompt: no recognized variant key")


def redact_sensitive(value: OptimizedPrompt) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "textPrompt" in value:
        out["textPrompt"] = "*** Sensitive Data Redacted ***"
    return out
