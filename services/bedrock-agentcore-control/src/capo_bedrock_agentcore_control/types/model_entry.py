"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ModelEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.model_pattern


class ModelEntry(TypedDict, closed=True):
    model: "capo_bedrock_agentcore_control.types.model_pattern.ModelPattern"
    """<p>The model ID or glob pattern that identifies the model (for example, <code>anthropic.claude-opus-*</code> or <code>openai.gpt-oss-*</code>).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelEntry) -> dict:
    out: dict = {}
    out["model"] = value["model"]
    return out


def deserialize_json(data: dict) -> ModelEntry:
    out: ModelEntry = {}  # type: ignore[typeddict-item]
    if data.get("model") is not None:
        out["model"] = data["model"]
    else:
        out["model"] = ""
    return out
