"""Generated from Smithy shape ``com.amazonaws.qconnect#SpanTextValue``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.ai_guardrail_assessment
    import capo_qconnect.types.non_empty_sensitive_string
    import capo_qconnect.types.span_citation_list


class SpanTextValue(TypedDict, closed=True):
    value: "capo_qconnect.types.non_empty_sensitive_string.NonEmptySensitiveString"
    """<p>String content of the message text</p>"""
    citations: NotRequired["capo_qconnect.types.span_citation_list.SpanCitationList"]
    """<p>The citations associated with the span text.</p>"""
    ai_guardrail_assessment: NotRequired[
        "capo_qconnect.types.ai_guardrail_assessment.AIGuardrailAssessment"
    ]
    """<p>The AI Guardrail assessment for the span text.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpanTextValue) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    if "citations" in value:
        import capo_qconnect.types.span_citation_list

        out["citations"] = capo_qconnect.types.span_citation_list.serialize_json(
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


def deserialize_json(data: dict) -> SpanTextValue:
    out: SpanTextValue = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        raise DeserializationError("SpanTextValue.value required")
    if data.get("citations") is not None:
        import capo_qconnect.types.span_citation_list

        out["citations"] = capo_qconnect.types.span_citation_list.deserialize_json(
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


def redact_sensitive(value: SpanTextValue) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "value" in value:
        out["value"] = "*** Sensitive Data Redacted ***"
    if "citations" in value:
        import capo_qconnect.types.span_citation_list

        out["citations"] = capo_qconnect.types.span_citation_list.redact_sensitive(
            value["citations"]
        )
    return out
