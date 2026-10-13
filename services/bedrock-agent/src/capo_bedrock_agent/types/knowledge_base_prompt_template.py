"""Generated from Smithy shape ``com.amazonaws.bedrockagent#KnowledgeBasePromptTemplate``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.knowledge_base_text_prompt


class KnowledgeBasePromptTemplate(TypedDict, closed=True):
    text_prompt_template: NotRequired[
        "capo_bedrock_agent.types.knowledge_base_text_prompt.KnowledgeBaseTextPrompt"
    ]
    """<p>The text of the prompt template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBasePromptTemplate) -> dict:
    out: dict = {}
    if "text_prompt_template" in value:
        out["textPromptTemplate"] = value["text_prompt_template"]
    return out


def deserialize_json(data: dict) -> KnowledgeBasePromptTemplate:
    out: KnowledgeBasePromptTemplate = {}  # type: ignore[typeddict-item]
    if data.get("textPromptTemplate") is not None:
        out["text_prompt_template"] = data["textPromptTemplate"]
    return out


def redact_sensitive(value: KnowledgeBasePromptTemplate) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text_prompt_template" in value:
        out["text_prompt_template"] = "*** Sensitive Data Redacted ***"
    return out
