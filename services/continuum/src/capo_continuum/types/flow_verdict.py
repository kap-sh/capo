"""Generated from Smithy shape ``com.amazonaws.continuum#FlowVerdict``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.artifact_citations
    import capo_continuum.types.attack_flow_id
    import capo_continuum.types.flow_verdict_value
    import capo_continuum.types.validation_confidence


class FlowVerdict(TypedDict, closed=True):
    flow_id: "capo_continuum.types.attack_flow_id.AttackFlowId"
    """Identifier of the attack flow assessed."""
    verdict: "capo_continuum.types.flow_verdict_value.FlowVerdictValue"
    """Outcome for this flow."""
    confidence: NotRequired[
        "capo_continuum.types.validation_confidence.ValidationConfidence"
    ]
    """Confidence in this flow's verdict. Absent when out of range."""
    evidence: NotRequired["capo_continuum.types.artifact_citations.ArtifactCitations"]
    """Citations supporting the verdict."""


# --- restJson1 ser/de ---
def serialize_json(value: FlowVerdict) -> dict:
    out: dict = {}
    out["flowId"] = value["flow_id"]
    import capo_continuum.types.flow_verdict_value

    out["verdict"] = capo_continuum.types.flow_verdict_value.serialize_json(
        value["verdict"]
    )
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
    if "evidence" in value:
        import capo_continuum.types.artifact_citations

        out["evidence"] = capo_continuum.types.artifact_citations.serialize_json(
            value["evidence"]
        )
    return out


def deserialize_json(data: dict) -> FlowVerdict:
    out: FlowVerdict = {}  # type: ignore[typeddict-item]
    if data.get("flowId") is not None:
        out["flow_id"] = data["flowId"]
    else:
        out["flow_id"] = ""
    if data.get("verdict") is not None:
        import capo_continuum.types.flow_verdict_value

        out["verdict"] = capo_continuum.types.flow_verdict_value.deserialize_json(
            data["verdict"]
        )
    else:
        import typing

        out["verdict"] = typing.cast(
            "capo_continuum.types.flow_verdict_value.FlowVerdictValue", ""
        )
    if data.get("confidence") is not None:
        out["confidence"] = float(data["confidence"])
    if data.get("evidence") is not None:
        import capo_continuum.types.artifact_citations

        out["evidence"] = capo_continuum.types.artifact_citations.deserialize_json(
            data["evidence"]
        )
    return out
