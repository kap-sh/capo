"""Generated from Smithy shape ``com.amazonaws.qconnect#AIGuardrailVersionSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.ai_guardrail_summary
    import capo_qconnect.types.version


class AIGuardrailVersionSummary(TypedDict, closed=True):
    ai_guardrail_summary: NotRequired[
        "capo_qconnect.types.ai_guardrail_summary.AIGuardrailSummary"
    ]
    """<p>The data for the summary of the AI Guardrail version.</p>"""
    version_number: NotRequired["capo_qconnect.types.version.Version"]
    """<p>The version number for this AI Guardrail version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AIGuardrailVersionSummary) -> dict:
    out: dict = {}
    if "ai_guardrail_summary" in value:
        import capo_qconnect.types.ai_guardrail_summary

        out["aiGuardrailSummary"] = (
            capo_qconnect.types.ai_guardrail_summary.serialize_json(
                value["ai_guardrail_summary"]
            )
        )
    if "version_number" in value:
        out["versionNumber"] = value["version_number"]
    return out


def deserialize_json(data: dict) -> AIGuardrailVersionSummary:
    out: AIGuardrailVersionSummary = {}  # type: ignore[typeddict-item]
    if data.get("aiGuardrailSummary") is not None:
        import capo_qconnect.types.ai_guardrail_summary

        out["ai_guardrail_summary"] = (
            capo_qconnect.types.ai_guardrail_summary.deserialize_json(
                data["aiGuardrailSummary"]
            )
        )
    if data.get("versionNumber") is not None:
        out["version_number"] = data["versionNumber"]
    return out


def redact_sensitive(value: AIGuardrailVersionSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ai_guardrail_summary" in value:
        import capo_qconnect.types.ai_guardrail_summary

        out["ai_guardrail_summary"] = (
            capo_qconnect.types.ai_guardrail_summary.redact_sensitive(
                value["ai_guardrail_summary"]
            )
        )
    return out
