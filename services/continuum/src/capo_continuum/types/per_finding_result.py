"""Generated from Smithy shape ``com.amazonaws.continuum#PerFindingResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.exploitability_verdict
    import capo_continuum.types.finding_id
    import capo_continuum.types.flow_verdicts
    import capo_continuum.types.reasoning_steps
    import capo_continuum.types.validation_confidence
    import capo_continuum.types.validation_exploit_artifact


class PerFindingResult(TypedDict, closed=True):
    finding_id: "capo_continuum.types.finding_id.FindingId"
    """The finding assessed."""
    exploitable: "capo_continuum.types.exploitability_verdict.ExploitabilityVerdict"
    """Exploitability verdict for this finding."""
    confidence: NotRequired[
        "capo_continuum.types.validation_confidence.ValidationConfidence"
    ]
    """Confidence in this finding's verdict. Absent when out of range."""
    flow_verdicts: NotRequired["capo_continuum.types.flow_verdicts.FlowVerdicts"]
    """Per-flow verdicts recorded for this finding."""
    reasoning_chain: NotRequired["capo_continuum.types.reasoning_steps.ReasoningSteps"]
    """Reasoning chain recorded for this finding."""
    exploit_artifact: NotRequired[
        "capo_continuum.types.validation_exploit_artifact.ValidationExploitArtifact"
    ]
    """Exploit artifact produced for this finding, when there was one."""


# --- restJson1 ser/de ---
def serialize_json(value: PerFindingResult) -> dict:
    out: dict = {}
    out["findingId"] = value["finding_id"]
    import capo_continuum.types.exploitability_verdict

    out["exploitable"] = capo_continuum.types.exploitability_verdict.serialize_json(
        value["exploitable"]
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
    if "flow_verdicts" in value:
        import capo_continuum.types.flow_verdicts

        out["flowVerdicts"] = capo_continuum.types.flow_verdicts.serialize_json(
            value["flow_verdicts"]
        )
    if "reasoning_chain" in value:
        import capo_continuum.types.reasoning_steps

        out["reasoningChain"] = capo_continuum.types.reasoning_steps.serialize_json(
            value["reasoning_chain"]
        )
    if "exploit_artifact" in value:
        import capo_continuum.types.validation_exploit_artifact

        out["exploitArtifact"] = (
            capo_continuum.types.validation_exploit_artifact.serialize_json(
                value["exploit_artifact"]
            )
        )
    return out


def deserialize_json(data: dict) -> PerFindingResult:
    out: PerFindingResult = {}  # type: ignore[typeddict-item]
    if data.get("findingId") is not None:
        out["finding_id"] = data["findingId"]
    else:
        out["finding_id"] = ""
    if data.get("exploitable") is not None:
        import capo_continuum.types.exploitability_verdict

        out["exploitable"] = (
            capo_continuum.types.exploitability_verdict.deserialize_json(
                data["exploitable"]
            )
        )
    else:
        import typing

        out["exploitable"] = typing.cast(
            "capo_continuum.types.exploitability_verdict.ExploitabilityVerdict", ""
        )
    if data.get("confidence") is not None:
        out["confidence"] = float(data["confidence"])
    if data.get("flowVerdicts") is not None:
        import capo_continuum.types.flow_verdicts

        out["flow_verdicts"] = capo_continuum.types.flow_verdicts.deserialize_json(
            data["flowVerdicts"]
        )
    if data.get("reasoningChain") is not None:
        import capo_continuum.types.reasoning_steps

        out["reasoning_chain"] = capo_continuum.types.reasoning_steps.deserialize_json(
            data["reasoningChain"]
        )
    if data.get("exploitArtifact") is not None:
        import capo_continuum.types.validation_exploit_artifact

        out["exploit_artifact"] = (
            capo_continuum.types.validation_exploit_artifact.deserialize_json(
                data["exploitArtifact"]
            )
        )
    return out
