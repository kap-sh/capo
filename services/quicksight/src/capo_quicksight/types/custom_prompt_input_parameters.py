"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomPromptInputParameters``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.style_description


class CustomPromptInputParameters(TypedDict, closed=True):
    response_length: NotRequired[
        "capo_quicksight.types.style_description.StyleDescription"
    ]
    """<p>Instructions for the desired response length.</p>"""
    output_style: NotRequired[
        "capo_quicksight.types.style_description.StyleDescription"
    ]
    """<p>Instructions for the desired output style.</p>"""
    identity: NotRequired["capo_quicksight.types.style_description.StyleDescription"]
    """<p>Instructions that define the agent's identity and persona.</p>"""
    tone: NotRequired["capo_quicksight.types.style_description.StyleDescription"]
    """<p>Instructions for the desired tone of responses.</p>"""
    custom_instructions: NotRequired[
        "capo_quicksight.types.style_description.StyleDescription"
    ]
    """<p>Custom instructions for the agent's behavior.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomPromptInputParameters) -> dict:
    out: dict = {}
    if "response_length" in value:
        out["ResponseLength"] = value["response_length"]
    if "output_style" in value:
        out["OutputStyle"] = value["output_style"]
    if "identity" in value:
        out["Identity"] = value["identity"]
    if "tone" in value:
        out["Tone"] = value["tone"]
    if "custom_instructions" in value:
        out["CustomInstructions"] = value["custom_instructions"]
    return out


def deserialize_json(data: dict) -> CustomPromptInputParameters:
    out: CustomPromptInputParameters = {}  # type: ignore[typeddict-item]
    if data.get("ResponseLength") is not None:
        out["response_length"] = data["ResponseLength"]
    if data.get("OutputStyle") is not None:
        out["output_style"] = data["OutputStyle"]
    if data.get("Identity") is not None:
        out["identity"] = data["Identity"]
    if data.get("Tone") is not None:
        out["tone"] = data["Tone"]
    if data.get("CustomInstructions") is not None:
        out["custom_instructions"] = data["CustomInstructions"]
    return out


def redact_sensitive(value: CustomPromptInputParameters) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "response_length" in value:
        out["response_length"] = "*** Sensitive Data Redacted ***"
    if "output_style" in value:
        out["output_style"] = "*** Sensitive Data Redacted ***"
    if "identity" in value:
        out["identity"] = "*** Sensitive Data Redacted ***"
    if "tone" in value:
        out["tone"] = "*** Sensitive Data Redacted ***"
    if "custom_instructions" in value:
        out["custom_instructions"] = "*** Sensitive Data Redacted ***"
    return out
