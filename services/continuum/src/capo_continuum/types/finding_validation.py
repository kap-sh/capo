"""Generated from Smithy shape ``com.amazonaws.continuum#FindingValidation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.finding_blocking_reason
    import capo_continuum.types.finding_description
    import capo_continuum.types.finding_evidence_list
    import capo_continuum.types.finding_severity_adjustment
    import capo_continuum.types.finding_string_list
    import capo_continuum.types.finding_verdict


class FindingValidation(TypedDict, closed=True):
    verdict: "capo_continuum.types.finding_verdict.FindingVerdict"
    """The validator's conclusion."""
    blocking_reason: NotRequired[
        "capo_continuum.types.finding_blocking_reason.FindingBlockingReason"
    ]
    """Why the validator reached that verdict."""
    confidence: NotRequired["float"]
    """The validator's confidence, from 0.0 to 1.0 inclusive. Advisory: it does not drive Continuum's own routing decisions. The range is enforced server-side, not by a @range trait -- the smithy-rs server SDK does not support range constraints on double shapes (smithy-rs#2007)."""
    rationale: NotRequired[
        "capo_continuum.types.finding_description.FindingDescription"
    ]
    """The validator's reasoning."""
    severity_adjustment: NotRequired[
        "capo_continuum.types.finding_severity_adjustment.FindingSeverityAdjustment"
    ]
    """The validator's severity conclusion."""
    mitigating_controls: NotRequired[
        "capo_continuum.types.finding_string_list.FindingStringList"
    ]
    """Controls the validator found that reduce exploitability."""
    preconditions: NotRequired[
        "capo_continuum.types.finding_string_list.FindingStringList"
    ]
    """Conditions exploitation depends on, which bound the severity."""
    evidence: NotRequired[
        "capo_continuum.types.finding_evidence_list.FindingEvidenceList"
    ]
    """Code citations supporting the verdict."""


# --- restJson1 ser/de ---
def serialize_json(value: FindingValidation) -> dict:
    out: dict = {}
    import capo_continuum.types.finding_verdict

    out["verdict"] = capo_continuum.types.finding_verdict.serialize_json(
        value["verdict"]
    )
    if "blocking_reason" in value:
        import capo_continuum.types.finding_blocking_reason

        out["blockingReason"] = (
            capo_continuum.types.finding_blocking_reason.serialize_json(
                value["blocking_reason"]
            )
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
    if "rationale" in value:
        out["rationale"] = value["rationale"]
    if "severity_adjustment" in value:
        import capo_continuum.types.finding_severity_adjustment

        out["severityAdjustment"] = (
            capo_continuum.types.finding_severity_adjustment.serialize_json(
                value["severity_adjustment"]
            )
        )
    if "mitigating_controls" in value:
        import capo_continuum.types.finding_string_list

        out["mitigatingControls"] = (
            capo_continuum.types.finding_string_list.serialize_json(
                value["mitigating_controls"]
            )
        )
    if "preconditions" in value:
        import capo_continuum.types.finding_string_list

        out["preconditions"] = capo_continuum.types.finding_string_list.serialize_json(
            value["preconditions"]
        )
    if "evidence" in value:
        import capo_continuum.types.finding_evidence_list

        out["evidence"] = capo_continuum.types.finding_evidence_list.serialize_json(
            value["evidence"]
        )
    return out


def deserialize_json(data: dict) -> FindingValidation:
    out: FindingValidation = {}  # type: ignore[typeddict-item]
    if data.get("verdict") is not None:
        import capo_continuum.types.finding_verdict

        out["verdict"] = capo_continuum.types.finding_verdict.deserialize_json(
            data["verdict"]
        )
    else:
        import typing

        out["verdict"] = typing.cast(
            "capo_continuum.types.finding_verdict.FindingVerdict", ""
        )
    if data.get("blockingReason") is not None:
        import capo_continuum.types.finding_blocking_reason

        out["blocking_reason"] = (
            capo_continuum.types.finding_blocking_reason.deserialize_json(
                data["blockingReason"]
            )
        )
    if data.get("confidence") is not None:
        out["confidence"] = float(data["confidence"])
    if data.get("rationale") is not None:
        out["rationale"] = data["rationale"]
    if data.get("severityAdjustment") is not None:
        import capo_continuum.types.finding_severity_adjustment

        out["severity_adjustment"] = (
            capo_continuum.types.finding_severity_adjustment.deserialize_json(
                data["severityAdjustment"]
            )
        )
    if data.get("mitigatingControls") is not None:
        import capo_continuum.types.finding_string_list

        out["mitigating_controls"] = (
            capo_continuum.types.finding_string_list.deserialize_json(
                data["mitigatingControls"]
            )
        )
    if data.get("preconditions") is not None:
        import capo_continuum.types.finding_string_list

        out["preconditions"] = (
            capo_continuum.types.finding_string_list.deserialize_json(
                data["preconditions"]
            )
        )
    if data.get("evidence") is not None:
        import capo_continuum.types.finding_evidence_list

        out["evidence"] = capo_continuum.types.finding_evidence_list.deserialize_json(
            data["evidence"]
        )
    return out
