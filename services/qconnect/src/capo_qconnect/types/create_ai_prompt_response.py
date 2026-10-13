"""Generated from Smithy shape ``com.amazonaws.qconnect#CreateAIPromptResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.ai_prompt_data


class CreateAIPromptResponse(TypedDict, closed=True):
    ai_prompt: NotRequired["capo_qconnect.types.ai_prompt_data.AIPromptData"]
    """<p>The data of the AI Prompt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAIPromptResponse) -> dict:
    out: dict = {}
    if "ai_prompt" in value:
        import capo_qconnect.types.ai_prompt_data

        out["aiPrompt"] = capo_qconnect.types.ai_prompt_data.serialize_json(
            value["ai_prompt"]
        )
    return out


def deserialize_json(data: dict) -> CreateAIPromptResponse:
    out: CreateAIPromptResponse = {}  # type: ignore[typeddict-item]
    if data.get("aiPrompt") is not None:
        import capo_qconnect.types.ai_prompt_data

        out["ai_prompt"] = capo_qconnect.types.ai_prompt_data.deserialize_json(
            data["aiPrompt"]
        )
    return out


def redact_sensitive(value: CreateAIPromptResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ai_prompt" in value:
        import capo_qconnect.types.ai_prompt_data

        out["ai_prompt"] = capo_qconnect.types.ai_prompt_data.redact_sensitive(
            value["ai_prompt"]
        )
    return out
