"""Generated from Smithy shape ``com.amazonaws.bedrock#PromptTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.text_prompt_template


class PromptTemplate(TypedDict, closed=True):
    text_prompt_template: NotRequired[
        "capo_bedrock.types.text_prompt_template.TextPromptTemplate"
    ]
    """<p>The template for the prompt that's sent to the model for response generation. You can include prompt placeholders, which become replaced before the prompt is sent to the model to provide instructions and context to the model. In addition, you can include XML tags to delineate meaningful sections of the prompt template.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html">Knowledge base prompt template</a> and <a href="https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags">Use XML tags with Anthropic Claude models</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PromptTemplate) -> dict:
    out: dict = {}
    if "text_prompt_template" in value:
        out["textPromptTemplate"] = value["text_prompt_template"]
    return out


def deserialize_json(data: dict) -> PromptTemplate:
    out: PromptTemplate = {}  # type: ignore[typeddict-item]
    if data.get("textPromptTemplate") is not None:
        out["text_prompt_template"] = data["textPromptTemplate"]
    return out
