"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailChecksPromptAttackUsage``."""

from typing_extensions import TypedDict


class GuardrailChecksPromptAttackUsage(TypedDict, closed=True):
    text_units: "int"
    """<p>The number of text units consumed by the prompt attack check.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailChecksPromptAttackUsage) -> dict:
    out: dict = {}
    out["textUnits"] = value["text_units"]
    return out


def deserialize_json(data: dict) -> GuardrailChecksPromptAttackUsage:
    out: GuardrailChecksPromptAttackUsage = {}  # type: ignore[typeddict-item]
    if data.get("textUnits") is not None:
        out["text_units"] = data["textUnits"]
    else:
        out["text_units"] = 0
    return out
