"""Generated from Smithy shape ``com.amazonaws.continuum#IssueSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_continuum.types.issue_arn
    import capo_continuum.types.issue_confidence
    import capo_continuum.types.issue_id
    import capo_continuum.types.issue_name
    import capo_continuum.types.issue_phase
    import capo_continuum.types.issue_severity
    import capo_continuum.types.issue_status
    import capo_continuum.types.issue_status_message
    import capo_continuum.types.issue_status_reason


class IssueSummary(TypedDict, closed=True):
    issue_id: "capo_continuum.types.issue_id.IssueId"
    """The unique identifier of the issue."""
    issue_arn: "capo_continuum.types.issue_arn.IssueArn"
    """The ARN of the issue."""
    name: "capo_continuum.types.issue_name.IssueName"
    """The name of the issue."""
    severity: NotRequired["capo_continuum.types.issue_severity.IssueSeverity"]
    """Scanner-derived severity assigned to the issue."""
    confidence: NotRequired["capo_continuum.types.issue_confidence.IssueConfidence"]
    """The likelihood that this issue is a true positive, expressed as a percentage (0-100)."""
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


# --- restJson1 ser/de ---
def serialize_json(value: IssueSummary) -> dict:
    out: dict = {}
    out["issueId"] = value["issue_id"]
    out["issueArn"] = value["issue_arn"]
    out["name"] = value["name"]
    if "severity" in value:
        import capo_continuum.types.issue_severity

        out["severity"] = capo_continuum.types.issue_severity.serialize_json(
            value["severity"]
        )
    if "confidence" in value:
        out["confidence"] = value["confidence"]
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
    return out


def deserialize_json(data: dict) -> IssueSummary:
    out: IssueSummary = {}  # type: ignore[typeddict-item]
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
    if data.get("severity") is not None:
        import capo_continuum.types.issue_severity

        out["severity"] = capo_continuum.types.issue_severity.deserialize_json(
            data["severity"]
        )
    if data.get("confidence") is not None:
        out["confidence"] = data["confidence"]
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
    return out
