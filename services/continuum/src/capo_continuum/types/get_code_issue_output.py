"""Generated from Smithy shape ``com.amazonaws.continuum#GetCodeIssueOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_continuum.types.issue_arn
    import capo_continuum.types.issue_confidence
    import capo_continuum.types.issue_evidence_availability
    import capo_continuum.types.issue_finding_ids
    import capo_continuum.types.issue_id
    import capo_continuum.types.issue_name
    import capo_continuum.types.issue_patch_delivery
    import capo_continuum.types.issue_phase
    import capo_continuum.types.issue_remediation_summary
    import capo_continuum.types.issue_severity
    import capo_continuum.types.issue_severity_reasoning
    import capo_continuum.types.issue_status
    import capo_continuum.types.issue_status_message
    import capo_continuum.types.issue_status_reason
    import capo_continuum.types.issue_synopsis


class GetCodeIssueOutput(TypedDict, closed=True):
    issue_id: "capo_continuum.types.issue_id.IssueId"
    """The unique identifier of the issue."""
    issue_arn: "capo_continuum.types.issue_arn.IssueArn"
    """The ARN of the issue."""
    name: "capo_continuum.types.issue_name.IssueName"
    """The name of the issue."""
    synopsis: "capo_continuum.types.issue_synopsis.IssueSynopsis"
    """A free-form synopsis of the issue."""
    severity: NotRequired["capo_continuum.types.issue_severity.IssueSeverity"]
    """Current severity: the FindingSeverity seed at create, overwritten by the authoritative severity that prioritization assigns after validation."""
    confidence: NotRequired["capo_continuum.types.issue_confidence.IssueConfidence"]
    """The likelihood that this issue is a true positive, expressed as a percentage (0-100)."""
    severity_reasoning: NotRequired[
        "capo_continuum.types.issue_severity_reasoning.IssueSeverityReasoning"
    ]
    """The justification for the current severity. Always leads with a customer-facing basis clause synthesized from how the severity was determined (e.g. "Severity from finding.", "Severity from Continuum system."); when prioritization has run, its own reasoning follows. Issues created before the basis clause was introduced return their original reasoning without it."""
    summary: NotRequired[
        "capo_continuum.types.issue_remediation_summary.IssueRemediationSummary"
    ]
    """The remediation completion summary, when the green stage has run."""
    finding_ids: "capo_continuum.types.issue_finding_ids.IssueFindingIds"
    """The findings that motivated this issue. Bare identifiers only -- a caller authorized for GetCodeIssue is not necessarily authorized to read finding detail; call GetCodeFinding for that. Every referenced finding is included regardless of origin (both CustomerUploaded and ContinuumScanner)."""
    status: "capo_continuum.types.issue_status.IssueStatus"
    """The current lifecycle status of the issue."""
    phase: NotRequired["capo_continuum.types.issue_phase.IssuePhase"]
    """The part of the workflow the issue is in. Present when status is IN_PROGRESS, and when status is FAILED and the failing phase is known."""
    status_reason: NotRequired[
        "capo_continuum.types.issue_status_reason.IssueStatusReason"
    ]
    """Why the issue failed. Present only when status is FAILED."""
    status_message: NotRequired[
        "capo_continuum.types.issue_status_message.IssueStatusMessage"
    ]
    """Customer-facing explanation of statusReason. Present only when status is FAILED."""
    status_updated_at: "datetime.datetime"
    """The timestamp when the status or phase last changed."""
    created_at: "datetime.datetime"
    """The timestamp when the issue was created."""
    updated_at: NotRequired["datetime.datetime"]
    """The timestamp when any field of the issue last changed. Advances on every mutation (including score-only updates that do not transition status), so it is greater than or equal to statusUpdatedAt."""
    evidence_availability: NotRequired[
        "capo_continuum.types.issue_evidence_availability.IssueEvidenceAvailability"
    ]
    """Whether the issue has any attached evidence (formerly 'artifacts': tool output, remediation proposals, patches). NONE = no evidence; AVAILABLE = at least one evidence item exists. Computed at read time."""
    patch_delivery: NotRequired[
        "capo_continuum.types.issue_patch_delivery.IssuePatchDelivery"
    ]
    """Customer delivery of the issue's patches, summarized from its PATCH artifacts at read time. Absent when no patch has a destination delivery."""


# --- restJson1 ser/de ---
def serialize_json(value: GetCodeIssueOutput) -> dict:
    out: dict = {}
    out["issueId"] = value["issue_id"]
    out["issueArn"] = value["issue_arn"]
    out["name"] = value["name"]
    out["synopsis"] = value["synopsis"]
    if "severity" in value:
        import capo_continuum.types.issue_severity

        out["severity"] = capo_continuum.types.issue_severity.serialize_json(
            value["severity"]
        )
    if "confidence" in value:
        out["confidence"] = value["confidence"]
    if "severity_reasoning" in value:
        out["severityReasoning"] = value["severity_reasoning"]
    if "summary" in value:
        out["summary"] = value["summary"]
    import capo_continuum.types.issue_finding_ids

    out["findingIds"] = capo_continuum.types.issue_finding_ids.serialize_json(
        value["finding_ids"]
    )
    import capo_continuum.types.issue_status

    out["status"] = capo_continuum.types.issue_status.serialize_json(value["status"])
    if "phase" in value:
        import capo_continuum.types.issue_phase

        out["phase"] = capo_continuum.types.issue_phase.serialize_json(value["phase"])
    if "status_reason" in value:
        import capo_continuum.types.issue_status_reason

        out["statusReason"] = capo_continuum.types.issue_status_reason.serialize_json(
            value["status_reason"]
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    import capo_continuum._protocol.serialize

    out["statusUpdatedAt"] = capo_continuum._protocol.serialize.fmt_date_time(
        value["status_updated_at"]
    )
    import capo_continuum._protocol.serialize

    out["createdAt"] = capo_continuum._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    if "updated_at" in value:
        import capo_continuum._protocol.serialize

        out["updatedAt"] = capo_continuum._protocol.serialize.fmt_date_time(
            value["updated_at"]
        )
    if "evidence_availability" in value:
        import capo_continuum.types.issue_evidence_availability

        out["evidenceAvailability"] = (
            capo_continuum.types.issue_evidence_availability.serialize_json(
                value["evidence_availability"]
            )
        )
    if "patch_delivery" in value:
        import capo_continuum.types.issue_patch_delivery

        out["patchDelivery"] = capo_continuum.types.issue_patch_delivery.serialize_json(
            value["patch_delivery"]
        )
    return out


def deserialize_json(data: dict) -> GetCodeIssueOutput:
    out: GetCodeIssueOutput = {}  # type: ignore[typeddict-item]
    if data.get("issueId") is not None:
        out["issue_id"] = data["issueId"]
    else:
        out["issue_id"] = ""
    if data.get("issueArn") is not None:
        out["issue_arn"] = data["issueArn"]
    else:
        out["issue_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("synopsis") is not None:
        out["synopsis"] = data["synopsis"]
    else:
        out["synopsis"] = ""
    if data.get("severity") is not None:
        import capo_continuum.types.issue_severity

        out["severity"] = capo_continuum.types.issue_severity.deserialize_json(
            data["severity"]
        )
    if data.get("confidence") is not None:
        out["confidence"] = data["confidence"]
    if data.get("severityReasoning") is not None:
        out["severity_reasoning"] = data["severityReasoning"]
    if data.get("summary") is not None:
        out["summary"] = data["summary"]
    if data.get("findingIds") is not None:
        import capo_continuum.types.issue_finding_ids

        out["finding_ids"] = capo_continuum.types.issue_finding_ids.deserialize_json(
            data["findingIds"]
        )
    else:
        out["finding_ids"] = []
    if data.get("status") is not None:
        import capo_continuum.types.issue_status

        out["status"] = capo_continuum.types.issue_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast("capo_continuum.types.issue_status.IssueStatus", "")
    if data.get("phase") is not None:
        import capo_continuum.types.issue_phase

        out["phase"] = capo_continuum.types.issue_phase.deserialize_json(data["phase"])
    if data.get("statusReason") is not None:
        import capo_continuum.types.issue_status_reason

        out["status_reason"] = (
            capo_continuum.types.issue_status_reason.deserialize_json(
                data["statusReason"]
            )
        )
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    if data.get("statusUpdatedAt") is not None:
        import datetime

        out["status_updated_at"] = datetime.datetime.fromisoformat(
            data["statusUpdatedAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["status_updated_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    if data.get("evidenceAvailability") is not None:
        import capo_continuum.types.issue_evidence_availability

        out["evidence_availability"] = (
            capo_continuum.types.issue_evidence_availability.deserialize_json(
                data["evidenceAvailability"]
            )
        )
    if data.get("patchDelivery") is not None:
        import capo_continuum.types.issue_patch_delivery

        out["patch_delivery"] = (
            capo_continuum.types.issue_patch_delivery.deserialize_json(
                data["patchDelivery"]
            )
        )
    return out
