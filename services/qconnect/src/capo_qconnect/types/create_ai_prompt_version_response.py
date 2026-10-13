"""Generated from Smithy shape ``com.amazonaws.qconnect#CreateAIPromptVersionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.ai_prompt_data
    import capo_qconnect.types.version


class CreateAIPromptVersionResponse(TypedDict, closed=True):
    ai_prompt: NotRequired["capo_qconnect.types.ai_prompt_data.AIPromptData"]
    """<p>The data of the AI Prompt version.</p>"""
    version_number: NotRequired["capo_qconnect.types.version.Version"]
    """<p>The version number of the AI Prompt version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAIPromptVersionResponse) -> dict:
    out: dict = {}
    if "ai_prompt" in value:
        import capo_qconnect.types.ai_prompt_data

        out["aiPrompt"] = capo_qconnect.types.ai_prompt_data.serialize_json(
            value["ai_prompt"]
        )
    if "version_number" in value:
        out["versionNumber"] = value["version_number"]
    return out


def deserialize_json(data: dict) -> CreateAIPromptVersionResponse:
    out: CreateAIPromptVersionResponse = {}  # type: ignore[typeddict-item]
    if data.get("aiPrompt") is not None:
        import capo_qconnect.types.ai_prompt_data

        out["ai_prompt"] = capo_qconnect.types.ai_prompt_data.deserialize_json(
            data["aiPrompt"]
        )
    if data.get("versionNumber") is not None:
        out["version_number"] = data["versionNumber"]
    return out


def redact_sensitive(value: CreateAIPromptVersionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ai_prompt" in value:
        import capo_qconnect.types.ai_prompt_data

        out["ai_prompt"] = capo_qconnect.types.ai_prompt_data.redact_sensitive(
            value["ai_prompt"]
        )
    return out
