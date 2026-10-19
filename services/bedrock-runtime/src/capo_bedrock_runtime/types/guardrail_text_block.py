"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailTextBlock``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_content_qualifier_list


class GuardrailTextBlock(TypedDict, closed=True):
    text: "str"
    """<p>The input text details to be evaluated by the guardrail.</p>"""
    qualifiers: NotRequired[
        "capo_bedrock_runtime.types.guardrail_content_qualifier_list.GuardrailContentQualifierList"
    ]
    """<p>The qualifiers describing the text block.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailTextBlock) -> dict:
    out: dict = {}
    out["text"] = value["text"]
    if "qualifiers" in value:
        import capo_bedrock_runtime.types.guardrail_content_qualifier_list

        out["qualifiers"] = (
            capo_bedrock_runtime.types.guardrail_content_qualifier_list.serialize_json(
                value["qualifiers"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailTextBlock:
    out: GuardrailTextBlock = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        out["text"] = data["text"]
    else:
        out["text"] = ""
    if data.get("qualifiers") is not None:
        import capo_bedrock_runtime.types.guardrail_content_qualifier_list

        out["qualifiers"] = (
            capo_bedrock_runtime.types.guardrail_content_qualifier_list.deserialize_json(
                data["qualifiers"]
            )
        )
    return out
