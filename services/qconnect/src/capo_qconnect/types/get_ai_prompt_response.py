"""Generated from Smithy shape ``com.amazonaws.qconnect#GetAIPromptResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.ai_prompt_data
    import capo_qconnect.types.version


class GetAIPromptResponse(TypedDict, closed=True):
    ai_prompt: NotRequired["capo_qconnect.types.ai_prompt_data.AIPromptData"]
    """<p>The data of the AI Prompt.</p>"""
    version_number: NotRequired["capo_qconnect.types.version.Version"]
    """<p>The version number of the AI Prompt version (returned if an AI Prompt version was specified via use of a qualifier for the <code>aiPromptId</code> on the request). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAIPromptResponse) -> dict:
    out: dict = {}
    if "ai_prompt" in value:
        import capo_qconnect.types.ai_prompt_data

        out["aiPrompt"] = capo_qconnect.types.ai_prompt_data.serialize_json(
            value["ai_prompt"]
        )
    if "version_number" in value:
        out["versionNumber"] = value["version_number"]
    return out


def deserialize_json(data: dict) -> GetAIPromptResponse:
    out: GetAIPromptResponse = {}  # type: ignore[typeddict-item]
    if data.get("aiPrompt") is not None:
        import capo_qconnect.types.ai_prompt_data

        out["ai_prompt"] = capo_qconnect.types.ai_prompt_data.deserialize_json(
            data["aiPrompt"]
        )
    if data.get("versionNumber") is not None:
        out["version_number"] = data["versionNumber"]
    return out


def redact_sensitive(value: GetAIPromptResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ai_prompt" in value:
        import capo_qconnect.types.ai_prompt_data

        out["ai_prompt"] = capo_qconnect.types.ai_prompt_data.redact_sensitive(
            value["ai_prompt"]
        )
    return out
