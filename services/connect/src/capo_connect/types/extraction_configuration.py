"""Generated from Smithy shape ``com.amazonaws.connect#ExtractionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.extraction_definition_not_found_behavior
    import capo_connect.types.extraction_definition_prompt_hint


class ExtractionConfiguration(TypedDict, closed=True):
    prompt_hint: "capo_connect.types.extraction_definition_prompt_hint.ExtractionDefinitionPromptHint"
    """<p>The prompt hint that guides the extraction. This text tells the generative AI model what data to look for in the customer interaction.</p>"""
    not_found_behavior: NotRequired[
        "capo_connect.types.extraction_definition_not_found_behavior.ExtractionDefinitionNotFoundBehavior"
    ]
    """<p>The behavior when the extraction cannot find the specified data in the interaction.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExtractionConfiguration) -> dict:
    out: dict = {}
    out["PromptHint"] = value["prompt_hint"]
    if "not_found_behavior" in value:
        import capo_connect.types.extraction_definition_not_found_behavior

        out["NotFoundBehavior"] = (
            capo_connect.types.extraction_definition_not_found_behavior.serialize_json(
                value["not_found_behavior"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExtractionConfiguration:
    out: ExtractionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("PromptHint") is not None:
        out["prompt_hint"] = data["PromptHint"]
    else:
        out["prompt_hint"] = ""
    if data.get("NotFoundBehavior") is not None:
        import capo_connect.types.extraction_definition_not_found_behavior

        out["not_found_behavior"] = (
            capo_connect.types.extraction_definition_not_found_behavior.deserialize_json(
                data["NotFoundBehavior"]
            )
        )
    return out
