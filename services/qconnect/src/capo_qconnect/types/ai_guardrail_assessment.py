"""Generated from Smithy shape ``com.amazonaws.qconnect#AIGuardrailAssessment``."""

from typing_extensions import TypedDict


class AIGuardrailAssessment(TypedDict, closed=True):
    blocked: "bool"
    """<p>Indicates whether the AI Guardrail blocked the content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AIGuardrailAssessment) -> dict:
    out: dict = {}
    out["blocked"] = value["blocked"]
    return out


def deserialize_json(data: dict) -> AIGuardrailAssessment:
    out: AIGuardrailAssessment = {}  # type: ignore[typeddict-item]
    if data.get("blocked") is not None:
        out["blocked"] = data["blocked"]
    else:
        out["blocked"] = False
    return out
