"""Generated from Smithy shape ``com.amazonaws.continuum#SignalConfidenceReasoning``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.artifact_citations
    import capo_continuum.types.artifact_text


class SignalConfidenceReasoning(TypedDict, closed=True):
    summary: "capo_continuum.types.artifact_text.ArtifactText"
    """One-line rationale."""
    factors: NotRequired["capo_continuum.types.artifact_citations.ArtifactCitations"]
    """The individual factors behind it."""


# --- restJson1 ser/de ---
def serialize_json(value: SignalConfidenceReasoning) -> dict:
    out: dict = {}
    out["summary"] = value["summary"]
    if "factors" in value:
        import capo_continuum.types.artifact_citations

        out["factors"] = capo_continuum.types.artifact_citations.serialize_json(
            value["factors"]
        )
    return out


def deserialize_json(data: dict) -> SignalConfidenceReasoning:
    out: SignalConfidenceReasoning = {}  # type: ignore[typeddict-item]
    if data.get("summary") is not None:
        out["summary"] = data["summary"]
    else:
        out["summary"] = ""
    if data.get("factors") is not None:
        import capo_continuum.types.artifact_citations

        out["factors"] = capo_continuum.types.artifact_citations.deserialize_json(
            data["factors"]
        )
    return out
