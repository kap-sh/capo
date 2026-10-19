"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailConverseTextBlock``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_converse_content_qualifier_list


class GuardrailConverseTextBlock(TypedDict, closed=True):
    text: "str"
    """<p>The text that you want to guard.</p>"""
    qualifiers: NotRequired[
        "capo_bedrock_runtime.types.guardrail_converse_content_qualifier_list.GuardrailConverseContentQualifierList"
    ]
    """<p>The qualifier details for the guardrails contextual grounding filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailConverseTextBlock) -> dict:
    out: dict = {}
    out["text"] = value["text"]
    if "qualifiers" in value:
        import capo_bedrock_runtime.types.guardrail_converse_content_qualifier_list

        out["qualifiers"] = (
            capo_bedrock_runtime.types.guardrail_converse_content_qualifier_list.serialize_json(
                value["qualifiers"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailConverseTextBlock:
    out: GuardrailConverseTextBlock = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        out["text"] = data["text"]
    else:
        out["text"] = ""
    if data.get("qualifiers") is not None:
        import capo_bedrock_runtime.types.guardrail_converse_content_qualifier_list

        out["qualifiers"] = (
            capo_bedrock_runtime.types.guardrail_converse_content_qualifier_list.deserialize_json(
                data["qualifiers"]
            )
        )
    return out
