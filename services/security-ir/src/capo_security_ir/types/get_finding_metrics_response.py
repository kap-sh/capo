"""Generated from Smithy shape ``com.amazonaws.securityir#GetFindingMetricsResponse``."""

from typing_extensions import TypedDict

from capo_security_ir.errors import DeserializationError


class GetFindingMetricsResponse(TypedDict, closed=True):
    findings_ingested_security_hub: "int"
    """The number of findings ingested from AWS Security Hub during the requested date range."""
    findings_ingested_guard_duty: "int"
    """The number of findings ingested from Amazon GuardDuty during the requested date range."""
    findings_triaged: "int"
    """The number of findings triaged during the requested date range."""
    findings_triaged_false_positive: "int"
    """The number of triaged findings that were closed as false positives during the requested date range."""
    findings_investigated: "int"
    """The number of findings investigated during the requested date range."""
    findings_investigated_false_positive: "int"
    """The number of investigated findings that were closed as false positives during the requested date range."""
    findings_escalated: "int"
    """The number of findings escalated during the requested date range."""
    findings_escalated_false_positive: "int"
    """The number of escalated findings that were closed as false positives during the requested date range."""
    findings_true_positive: "int"
    """The number of findings confirmed as true positives during the requested date range."""
    findings_investigated_in_progress: "int"
    """The number of findings whose investigation was in progress during the requested date range."""
    findings_escalated_in_progress: "int"
    """The number of findings whose escalation was in progress during the requested date range."""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingMetricsResponse) -> dict:
    out: dict = {}
    out["findingsIngestedSecurityHub"] = value["findings_ingested_security_hub"]
    out["findingsIngestedGuardDuty"] = value["findings_ingested_guard_duty"]
    out["findingsTriaged"] = value["findings_triaged"]
    out["findingsTriagedFalsePositive"] = value["findings_triaged_false_positive"]
    out["findingsInvestigated"] = value["findings_investigated"]
    out["findingsInvestigatedFalsePositive"] = value[
        "findings_investigated_false_positive"
    ]
    out["findingsEscalated"] = value["findings_escalated"]
    out["findingsEscalatedFalsePositive"] = value["findings_escalated_false_positive"]
    out["findingsTruePositive"] = value["findings_true_positive"]
    out["findingsInvestigatedInProgress"] = value["findings_investigated_in_progress"]
    out["findingsEscalatedInProgress"] = value["findings_escalated_in_progress"]
    return out


def deserialize_json(data: dict) -> GetFindingMetricsResponse:
    out: GetFindingMetricsResponse = {}  # type: ignore[typeddict-item]
    if data.get("findingsIngestedSecurityHub") is not None:
        out["findings_ingested_security_hub"] = data["findingsIngestedSecurityHub"]
    else:
        raise DeserializationError(
            "GetFindingMetricsResponse.findings_ingested_security_hub required"
        )
    if data.get("findingsIngestedGuardDuty") is not None:
        out["findings_ingested_guard_duty"] = data["findingsIngestedGuardDuty"]
    else:
        raise DeserializationError(
            "GetFindingMetricsResponse.findings_ingested_guard_duty required"
        )
    if data.get("findingsTriaged") is not None:
        out["findings_triaged"] = data["findingsTriaged"]
    else:
        raise DeserializationError(
            "GetFindingMetricsResponse.findings_triaged required"
        )
    if data.get("findingsTriagedFalsePositive") is not None:
        out["findings_triaged_false_positive"] = data["findingsTriagedFalsePositive"]
    else:
        raise DeserializationError(
            "GetFindingMetricsResponse.findings_triaged_false_positive required"
        )
    if data.get("findingsInvestigated") is not None:
        out["findings_investigated"] = data["findingsInvestigated"]
    else:
        raise DeserializationError(
            "GetFindingMetricsResponse.findings_investigated required"
        )
    if data.get("findingsInvestigatedFalsePositive") is not None:
        out["findings_investigated_false_positive"] = data[
            "findingsInvestigatedFalsePositive"
        ]
    else:
        raise DeserializationError(
            "GetFindingMetricsResponse.findings_investigated_false_positive required"
        )
    if data.get("findingsEscalated") is not None:
        out["findings_escalated"] = data["findingsEscalated"]
    else:
        raise DeserializationError(
            "GetFindingMetricsResponse.findings_escalated required"
        )
    if data.get("findingsEscalatedFalsePositive") is not None:
        out["findings_escalated_false_positive"] = data[
            "findingsEscalatedFalsePositive"
        ]
    else:
        raise DeserializationError(
            "GetFindingMetricsResponse.findings_escalated_false_positive required"
        )
    if data.get("findingsTruePositive") is not None:
        out["findings_true_positive"] = data["findingsTruePositive"]
    else:
        raise DeserializationError(
            "GetFindingMetricsResponse.findings_true_positive required"
        )
    if data.get("findingsInvestigatedInProgress") is not None:
        out["findings_investigated_in_progress"] = data[
            "findingsInvestigatedInProgress"
        ]
    else:
        raise DeserializationError(
            "GetFindingMetricsResponse.findings_investigated_in_progress required"
        )
    if data.get("findingsEscalatedInProgress") is not None:
        out["findings_escalated_in_progress"] = data["findingsEscalatedInProgress"]
    else:
        raise DeserializationError(
            "GetFindingMetricsResponse.findings_escalated_in_progress required"
        )
    return out
