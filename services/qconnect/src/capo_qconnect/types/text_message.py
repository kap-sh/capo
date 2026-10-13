"""Generated from Smithy shape ``com.amazonaws.qconnect#TextMessage``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.ai_guardrail_assessment
    import capo_qconnect.types.citations
    import capo_qconnect.types.sensitive_string


class TextMessage(TypedDict, closed=True):
    value: NotRequired["capo_qconnect.types.sensitive_string.SensitiveString"]
    """<p>The value of the message data in text type.</p>"""
    citations: NotRequired["capo_qconnect.types.citations.Citations"]
    """<p>The citations associated with the text message.</p>"""
    ai_guardrail_assessment: NotRequired[
        "capo_qconnect.types.ai_guardrail_assessment.AIGuardrailAssessment"
    ]
    """<p>The AI Guardrail assessment for the text message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextMessage) -> dict:
    out: dict = {}
    if "value" in value:
        out["value"] = value["value"]
    if "citations" in value:
        import capo_qconnect.types.citations

        out["citations"] = capo_qconnect.types.citations.serialize_json(
            value["citations"]
        )
    if "ai_guardrail_assessment" in value:
        import capo_qconnect.types.ai_guardrail_assessment

        out["aiGuardrailAssessment"] = (
            capo_qconnect.types.ai_guardrail_assessment.serialize_json(
                value["ai_guardrail_assessment"]
            )
        )
    return out


def deserialize_json(data: dict) -> TextMessage:
    out: TextMessage = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        out["value"] = data["value"]
    if data.get("citations") is not None:
        import capo_qconnect.types.citations

        out["citations"] = capo_qconnect.types.citations.deserialize_json(
            data["citations"]
        )
    if data.get("aiGuardrailAssessment") is not None:
        import capo_qconnect.types.ai_guardrail_assessment

        out["ai_guardrail_assessment"] = (
            capo_qconnect.types.ai_guardrail_assessment.deserialize_json(
                data["aiGuardrailAssessment"]
            )
        )
    return out


def redact_sensitive(value: TextMessage) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "value" in value:
        out["value"] = "*** Sensitive Data Redacted ***"
    if "citations" in value:
        import capo_qconnect.types.citations

        out["citations"] = capo_qconnect.types.citations.redact_sensitive(
            value["citations"]
        )
    return out
