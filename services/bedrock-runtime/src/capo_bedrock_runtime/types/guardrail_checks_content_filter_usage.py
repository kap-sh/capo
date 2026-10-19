"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailChecksContentFilterUsage``."""

from typing_extensions import TypedDict


class GuardrailChecksContentFilterUsage(TypedDict, closed=True):
    text_units: "int"
    """<p>The number of text units consumed by the content filter check.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailChecksContentFilterUsage) -> dict:
    out: dict = {}
    out["textUnits"] = value["text_units"]
    return out


def deserialize_json(data: dict) -> GuardrailChecksContentFilterUsage:
    out: GuardrailChecksContentFilterUsage = {}  # type: ignore[typeddict-item]
    if data.get("textUnits") is not None:
        out["text_units"] = data["textUnits"]
    else:
        out["text_units"] = 0
    return out
