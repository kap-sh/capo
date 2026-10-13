"""Generated from Smithy shape ``com.amazonaws.qconnect#CreateAIGuardrailVersionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.ai_guardrail_data
    import capo_qconnect.types.version


class CreateAIGuardrailVersionResponse(TypedDict, closed=True):
    ai_guardrail: NotRequired["capo_qconnect.types.ai_guardrail_data.AIGuardrailData"]
    """<p>The data of the AI Guardrail version.</p>"""
    version_number: NotRequired["capo_qconnect.types.version.Version"]
    """<p>The version number of the AI Guardrail version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAIGuardrailVersionResponse) -> dict:
    out: dict = {}
    if "ai_guardrail" in value:
        import capo_qconnect.types.ai_guardrail_data

        out["aiGuardrail"] = capo_qconnect.types.ai_guardrail_data.serialize_json(
            value["ai_guardrail"]
        )
    if "version_number" in value:
        out["versionNumber"] = value["version_number"]
    return out


def deserialize_json(data: dict) -> CreateAIGuardrailVersionResponse:
    out: CreateAIGuardrailVersionResponse = {}  # type: ignore[typeddict-item]
    if data.get("aiGuardrail") is not None:
        import capo_qconnect.types.ai_guardrail_data

        out["ai_guardrail"] = capo_qconnect.types.ai_guardrail_data.deserialize_json(
            data["aiGuardrail"]
        )
    if data.get("versionNumber") is not None:
        out["version_number"] = data["versionNumber"]
    return out


def redact_sensitive(value: CreateAIGuardrailVersionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ai_guardrail" in value:
        import capo_qconnect.types.ai_guardrail_data

        out["ai_guardrail"] = capo_qconnect.types.ai_guardrail_data.redact_sensitive(
            value["ai_guardrail"]
        )
    return out
