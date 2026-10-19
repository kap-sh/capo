"""Generated from Smithy shape ``com.amazonaws.qconnect#GuardrailContentFilterConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.guardrail_content_filter_type
    import capo_qconnect.types.guardrail_filter_strength


class GuardrailContentFilterConfig(TypedDict, closed=True):
    type: "capo_qconnect.types.guardrail_content_filter_type.GuardrailContentFilterType"
    """<p>The harmful category that the content filter is applied to.</p>"""
    input_strength: (
        "capo_qconnect.types.guardrail_filter_strength.GuardrailFilterStrength"
    )
    """<p>The strength of the content filter to apply to prompts. As you increase the filter strength, the likelihood of filtering harmful content increases and the probability of seeing harmful content in your application reduces.</p>"""
    output_strength: (
        "capo_qconnect.types.guardrail_filter_strength.GuardrailFilterStrength"
    )
    """<p>The strength of the content filter to apply to model responses. As you increase the filter strength, the likelihood of filtering harmful content increases and the probability of seeing harmful content in your application reduces.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContentFilterConfig) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    out["inputStrength"] = value["input_strength"]
    out["outputStrength"] = value["output_strength"]
    return out


def deserialize_json(data: dict) -> GuardrailContentFilterConfig:
    out: GuardrailContentFilterConfig = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("inputStrength") is not None:
        out["input_strength"] = data["inputStrength"]
    else:
        out["input_strength"] = ""
    if data.get("outputStrength") is not None:
        out["output_strength"] = data["outputStrength"]
    else:
        out["output_strength"] = ""
    return out


def redact_sensitive(value: GuardrailContentFilterConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "type" in value:
        out["type"] = "*** Sensitive Data Redacted ***"
    if "input_strength" in value:
        out["input_strength"] = "*** Sensitive Data Redacted ***"
    if "output_strength" in value:
        out["output_strength"] = "*** Sensitive Data Redacted ***"
    return out
