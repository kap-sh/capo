"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomInstructions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.custom_instructions_string


class CustomInstructions(TypedDict, closed=True):
    custom_instructions_string: (
        "capo_quicksight.types.custom_instructions_string.CustomInstructionsString"
    )
    """<p>A text field for providing additional guidance or context for response generation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomInstructions) -> dict:
    out: dict = {}
    out["CustomInstructionsString"] = value["custom_instructions_string"]
    return out


def deserialize_json(data: dict) -> CustomInstructions:
    out: CustomInstructions = {}  # type: ignore[typeddict-item]
    if data.get("CustomInstructionsString") is not None:
        out["custom_instructions_string"] = data["CustomInstructionsString"]
    else:
        raise DeserializationError(
            "CustomInstructions.custom_instructions_string required"
        )
    return out


def redact_sensitive(value: CustomInstructions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "custom_instructions_string" in value:
        out["custom_instructions_string"] = "*** Sensitive Data Redacted ***"
    return out
