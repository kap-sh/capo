"""Generated from Smithy shape ``com.amazonaws.continuum#ReasoningStep``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.artifact_citation
    import capo_continuum.types.artifact_text
    import capo_continuum.types.validation_confidence


class ReasoningStep(TypedDict, closed=True):
    step: "int"
    """Position of this step in the chain."""
    claim: "capo_continuum.types.artifact_text.ArtifactText"
    """The claim or conclusion reached at this step."""
    source: "capo_continuum.types.artifact_citation.ArtifactCitation"
    """Citation supporting the claim."""
    confidence: NotRequired[
        "capo_continuum.types.validation_confidence.ValidationConfidence"
    ]
    """Confidence in this individual claim, on the producer's native 0-1 scale."""


# --- restJson1 ser/de ---
def serialize_json(value: ReasoningStep) -> dict:
    out: dict = {}
    out["step"] = value["step"]
    out["claim"] = value["claim"]
    out["source"] = value["source"]
    if "confidence" in value:
        out["confidence"] = (
            "NaN"
            if value["confidence"] != value["confidence"]
            else "Infinity"
            if value["confidence"] == float("inf")
            else "-Infinity"
            if value["confidence"] == float("-inf")
            else value["confidence"]
        )
    return out


def deserialize_json(data: dict) -> ReasoningStep:
    out: ReasoningStep = {}  # type: ignore[typeddict-item]
    if data.get("step") is not None:
        out["step"] = data["step"]
    else:
        out["step"] = 0
    if data.get("claim") is not None:
        out["claim"] = data["claim"]
    else:
        out["claim"] = ""
    if data.get("source") is not None:
        out["source"] = data["source"]
    else:
        out["source"] = ""
    if data.get("confidence") is not None:
        out["confidence"] = float(data["confidence"])
    return out
