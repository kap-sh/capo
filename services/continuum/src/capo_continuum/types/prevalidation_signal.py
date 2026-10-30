"""Generated from Smithy shape ``com.amazonaws.continuum#PrevalidationSignal``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.artifact_citation
    import capo_continuum.types.artifact_text
    import capo_continuum.types.issue_artifact_producer_name
    import capo_continuum.types.signal_computation
    import capo_continuum.types.signal_confidence_reasoning
    import capo_continuum.types.signal_dimension
    import capo_continuum.types.signal_exploitability
    import capo_continuum.types.signal_impact_dimensions
    import capo_continuum.types.signal_preconditions
    import capo_continuum.types.signal_strength
    import capo_continuum.types.validation_confidence


class PrevalidationSignal(TypedDict, closed=True):
    subject_ref: NotRequired["capo_continuum.types.artifact_citation.ArtifactCitation"]
    """What this signal is about, such as a finding or issue reference."""
    dimension: NotRequired["capo_continuum.types.signal_dimension.SignalDimension"]
    """The axis this signal speaks to. Absent when the producer reported a dimension with no mapping yet."""
    signal_strength: NotRequired["capo_continuum.types.signal_strength.SignalStrength"]
    """The signal's own rating. This is an input to scoring and is NOT the finding's severity."""
    conclusion: NotRequired["capo_continuum.types.artifact_text.ArtifactText"]
    """The producer's conclusion."""
    producer_id: NotRequired[
        "capo_continuum.types.issue_artifact_producer_name.IssueArtifactProducerName"
    ]
    """Stable name of the producer that emitted this signal."""
    producer_version: NotRequired[
        "capo_continuum.types.artifact_citation.ArtifactCitation"
    ]
    """Version of that producer."""
    confidence: NotRequired[
        "capo_continuum.types.validation_confidence.ValidationConfidence"
    ]
    """The producer's confidence in this conclusion, on its native 0-1 scale. Absent when the stored value falls outside 0-1."""
    confidence_reasoning: NotRequired[
        "capo_continuum.types.signal_confidence_reasoning.SignalConfidenceReasoning"
    ]
    """Why the producer is or is not sure, kept structured rather than prose."""
    computed: NotRequired["capo_continuum.types.signal_computation.SignalComputation"]
    """The deterministic values the producer computed from its assessment."""
    preconditions: NotRequired[
        "capo_continuum.types.signal_preconditions.SignalPreconditions"
    ]
    """The four exploit preconditions a likelihood signal assessed, each with the basis the producer had for it."""
    impact_dimensions: NotRequired[
        "capo_continuum.types.signal_impact_dimensions.SignalImpactDimensions"
    ]
    """The three impact dimensions an impact signal assessed, each with the basis the producer had for it. These are what the computed impact band is derived from."""
    exploitability: NotRequired[
        "capo_continuum.types.signal_exploitability.SignalExploitability"
    ]
    """What validation established about exploitability, on an exploitability signal. This summarizes the verdict the signal was derived from; the proof itself is the VALIDATION_EVIDENCE artifact it cites."""


# --- restJson1 ser/de ---
def serialize_json(value: PrevalidationSignal) -> dict:
    out: dict = {}
    if "subject_ref" in value:
        out["subjectRef"] = value["subject_ref"]
    if "dimension" in value:
        import capo_continuum.types.signal_dimension

        out["dimension"] = capo_continuum.types.signal_dimension.serialize_json(
            value["dimension"]
        )
    if "signal_strength" in value:
        import capo_continuum.types.signal_strength

        out["signalStrength"] = capo_continuum.types.signal_strength.serialize_json(
            value["signal_strength"]
        )
    if "conclusion" in value:
        out["conclusion"] = value["conclusion"]
    if "producer_id" in value:
        out["producerId"] = value["producer_id"]
    if "producer_version" in value:
        out["producerVersion"] = value["producer_version"]
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
    if "confidence_reasoning" in value:
        import capo_continuum.types.signal_confidence_reasoning

        out["confidenceReasoning"] = (
            capo_continuum.types.signal_confidence_reasoning.serialize_json(
                value["confidence_reasoning"]
            )
        )
    if "computed" in value:
        import capo_continuum.types.signal_computation

        out["computed"] = capo_continuum.types.signal_computation.serialize_json(
            value["computed"]
        )
    if "preconditions" in value:
        import capo_continuum.types.signal_preconditions

        out["preconditions"] = capo_continuum.types.signal_preconditions.serialize_json(
            value["preconditions"]
        )
    if "impact_dimensions" in value:
        import capo_continuum.types.signal_impact_dimensions

        out["impactDimensions"] = (
            capo_continuum.types.signal_impact_dimensions.serialize_json(
                value["impact_dimensions"]
            )
        )
    if "exploitability" in value:
        import capo_continuum.types.signal_exploitability

        out["exploitability"] = (
            capo_continuum.types.signal_exploitability.serialize_json(
                value["exploitability"]
            )
        )
    return out


def deserialize_json(data: dict) -> PrevalidationSignal:
    out: PrevalidationSignal = {}  # type: ignore[typeddict-item]
    if data.get("subjectRef") is not None:
        out["subject_ref"] = data["subjectRef"]
    if data.get("dimension") is not None:
        import capo_continuum.types.signal_dimension

        out["dimension"] = capo_continuum.types.signal_dimension.deserialize_json(
            data["dimension"]
        )
    if data.get("signalStrength") is not None:
        import capo_continuum.types.signal_strength

        out["signal_strength"] = capo_continuum.types.signal_strength.deserialize_json(
            data["signalStrength"]
        )
    if data.get("conclusion") is not None:
        out["conclusion"] = data["conclusion"]
    if data.get("producerId") is not None:
        out["producer_id"] = data["producerId"]
    if data.get("producerVersion") is not None:
        out["producer_version"] = data["producerVersion"]
    if data.get("confidence") is not None:
        out["confidence"] = float(data["confidence"])
    if data.get("confidenceReasoning") is not None:
        import capo_continuum.types.signal_confidence_reasoning

        out["confidence_reasoning"] = (
            capo_continuum.types.signal_confidence_reasoning.deserialize_json(
                data["confidenceReasoning"]
            )
        )
    if data.get("computed") is not None:
        import capo_continuum.types.signal_computation

        out["computed"] = capo_continuum.types.signal_computation.deserialize_json(
            data["computed"]
        )
    if data.get("preconditions") is not None:
        import capo_continuum.types.signal_preconditions

        out["preconditions"] = (
            capo_continuum.types.signal_preconditions.deserialize_json(
                data["preconditions"]
            )
        )
    if data.get("impactDimensions") is not None:
        import capo_continuum.types.signal_impact_dimensions

        out["impact_dimensions"] = (
            capo_continuum.types.signal_impact_dimensions.deserialize_json(
                data["impactDimensions"]
            )
        )
    if data.get("exploitability") is not None:
        import capo_continuum.types.signal_exploitability

        out["exploitability"] = (
            capo_continuum.types.signal_exploitability.deserialize_json(
                data["exploitability"]
            )
        )
    return out
