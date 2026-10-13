"""Generated from Smithy shape ``com.amazonaws.qconnect#GuardrailContextualGroundingFilterConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.guardrail_contextual_grounding_filter_threshold
    import capo_qconnect.types.guardrail_contextual_grounding_filter_type


class GuardrailContextualGroundingFilterConfig(TypedDict, closed=True):
    type: "capo_qconnect.types.guardrail_contextual_grounding_filter_type.GuardrailContextualGroundingFilterType"
    """<p>The filter type for the AI Guardrail's contextual grounding filter.</p>"""
    threshold: "capo_qconnect.types.guardrail_contextual_grounding_filter_threshold.GuardrailContextualGroundingFilterThreshold"
    """<p>The threshold details for the AI Guardrail's contextual grounding filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContextualGroundingFilterConfig) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    out["threshold"] = (
        "NaN"
        if value.get("threshold", 0) != value.get("threshold", 0)
        else "Infinity"
        if value.get("threshold", 0) == float("inf")
        else "-Infinity"
        if value.get("threshold", 0) == float("-inf")
        else value.get("threshold", 0)
    )
    return out


def deserialize_json(data: dict) -> GuardrailContextualGroundingFilterConfig:
    out: GuardrailContextualGroundingFilterConfig = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        raise DeserializationError(
            "GuardrailContextualGroundingFilterConfig.type required"
        )
    if data.get("threshold") is not None:
        out["threshold"] = float(data["threshold"])
    else:
        out["threshold"] = 0
    return out


def redact_sensitive(value: GuardrailContextualGroundingFilterConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "type" in value:
        out["type"] = "*** Sensitive Data Redacted ***"
    if "threshold" in value:
        out["threshold"] = "*** Sensitive Data Redacted ***"
    return out
