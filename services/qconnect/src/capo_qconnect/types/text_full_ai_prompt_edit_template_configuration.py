"""Generated from Smithy shape ``com.amazonaws.qconnect#TextFullAIPromptEditTemplateConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.text_ai_prompt


class TextFullAIPromptEditTemplateConfiguration(TypedDict, closed=True):
    text: "capo_qconnect.types.text_ai_prompt.TextAIPrompt"
    """<p>The YAML text for the AI Prompt template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextFullAIPromptEditTemplateConfiguration) -> dict:
    out: dict = {}
    out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> TextFullAIPromptEditTemplateConfiguration:
    out: TextFullAIPromptEditTemplateConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        out["text"] = data["text"]
    else:
        raise DeserializationError(
            "TextFullAIPromptEditTemplateConfiguration.text required"
        )
    return out


def redact_sensitive(
    value: TextFullAIPromptEditTemplateConfiguration,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    return out
