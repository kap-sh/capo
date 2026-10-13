"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#OptimizePromptRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.input_prompt


class OptimizePromptRequest(TypedDict, closed=True):
    input: "capo_bedrock_agent_runtime.types.input_prompt.InputPrompt"
    """<p>Contains the prompt to optimize.</p>"""
    target_model_id: "str"
    """<p>The unique identifier of the model that you want to optimize the prompt for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OptimizePromptRequest) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.input_prompt

    out["input"] = capo_bedrock_agent_runtime.types.input_prompt.serialize_json(
        value["input"]
    )
    out["targetModelId"] = value["target_model_id"]
    return out


def deserialize_json(data: dict) -> OptimizePromptRequest:
    out: OptimizePromptRequest = {}  # type: ignore[typeddict-item]
    if data.get("input") is not None:
        import capo_bedrock_agent_runtime.types.input_prompt

        out["input"] = capo_bedrock_agent_runtime.types.input_prompt.deserialize_json(
            data["input"]
        )
    else:
        raise DeserializationError("OptimizePromptRequest.input required")
    if data.get("targetModelId") is not None:
        out["target_model_id"] = data["targetModelId"]
    else:
        raise DeserializationError("OptimizePromptRequest.target_model_id required")
    return out


def redact_sensitive(value: OptimizePromptRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "input" in value:
        import capo_bedrock_agent_runtime.types.input_prompt

        out["input"] = capo_bedrock_agent_runtime.types.input_prompt.redact_sensitive(
            value["input"]
        )
    return out
