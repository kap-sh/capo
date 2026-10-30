"""Generated from Smithy shape ``com.amazonaws.continuum#ValidationSourceAnalysis``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.exploit_effect
    import capo_continuum.types.validation_proof_summary


class ValidationSourceAnalysis(TypedDict, closed=True):
    summary: "capo_continuum.types.validation_proof_summary.ValidationProofSummary"
    """The non-blank analysis as Markdown: the annotated entry-to-sink walk, its citations, and why the checked guards are absent or bypassed."""
    inferred_effect: NotRequired["capo_continuum.types.exploit_effect.ExploitEffect"]
    """Effect the agent concluded WOULD occur. Deliberately not `effect`: nothing was executed, so this is reasoned from the source and must not be read as an observation. See `ValidationExecutedProof.observedEffect`."""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationSourceAnalysis) -> dict:
    out: dict = {}
    out["summary"] = value["summary"]
    if "inferred_effect" in value:
        import capo_continuum.types.exploit_effect

        out["inferredEffect"] = capo_continuum.types.exploit_effect.serialize_json(
            value["inferred_effect"]
        )
    return out


def deserialize_json(data: dict) -> ValidationSourceAnalysis:
    out: ValidationSourceAnalysis = {}  # type: ignore[typeddict-item]
    if data.get("summary") is not None:
        out["summary"] = data["summary"]
    else:
        out["summary"] = ""
    if data.get("inferredEffect") is not None:
        import capo_continuum.types.exploit_effect

        out["inferred_effect"] = capo_continuum.types.exploit_effect.deserialize_json(
            data["inferredEffect"]
        )
    return out
