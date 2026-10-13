"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomInstruction``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.inline_custom_instruction


class CustomInstruction(TypedDict, closed=True):
    inline_custom_instruction: NotRequired[
        "capo_quicksight.types.inline_custom_instruction.InlineCustomInstruction"
    ]
    """<p>An inline custom instruction containing text and optional uploaded document metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomInstruction) -> dict:
    out: dict = {}
    if "inline_custom_instruction" in value:
        import capo_quicksight.types.inline_custom_instruction

        out["InlineCustomInstruction"] = (
            capo_quicksight.types.inline_custom_instruction.serialize_json(
                value["inline_custom_instruction"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomInstruction:
    out: CustomInstruction = {}  # type: ignore[typeddict-item]
    if data.get("InlineCustomInstruction") is not None:
        import capo_quicksight.types.inline_custom_instruction

        out["inline_custom_instruction"] = (
            capo_quicksight.types.inline_custom_instruction.deserialize_json(
                data["InlineCustomInstruction"]
            )
        )
    return out


def redact_sensitive(value: CustomInstruction) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "inline_custom_instruction" in value:
        import capo_quicksight.types.inline_custom_instruction

        out["inline_custom_instruction"] = (
            capo_quicksight.types.inline_custom_instruction.redact_sensitive(
                value["inline_custom_instruction"]
            )
        )
    return out
