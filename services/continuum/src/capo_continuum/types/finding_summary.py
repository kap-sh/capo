"""Generated from Smithy shape ``com.amazonaws.continuum#FindingSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_continuum.types.environment_id
    import capo_continuum.types.finding_arn
    import capo_continuum.types.finding_category
    import capo_continuum.types.finding_discard_reason
    import capo_continuum.types.finding_file_path
    import capo_continuum.types.finding_id
    import capo_continuum.types.finding_severity_id
    import capo_continuum.types.finding_source
    import capo_continuum.types.finding_status
    import capo_continuum.types.finding_status_message
    import capo_continuum.types.finding_title
    import capo_continuum.types.finding_type
    import capo_continuum.types.issue_id
    import capo_continuum.types.scan_run_id
    import capo_continuum.types.source_finding_id


class FindingSummary(TypedDict, closed=True):
    finding_id: "capo_continuum.types.finding_id.FindingId"
    """The unique identifier of the finding."""
    finding_arn: "capo_continuum.types.finding_arn.FindingArn"
    """The ARN of the finding."""
    environment_id: "capo_continuum.types.environment_id.EnvironmentId"
    """The environment that owns the finding."""
    source: "capo_continuum.types.finding_source.FindingSource"
    """The system that produced the finding."""
    source_finding_id: "capo_continuum.types.source_finding_id.SourceFindingId"
    """The producer's own identifier for the finding."""
    reported_at: "datetime.datetime"
    """When the producer reported the finding -- its own clock, which is not Continuum's ingestion time. `createdAt` is when Continuum accepted it; these are genuinely different instants and a reader usually wants this one. For CreateCodeFinding, this is the submitted OCSF document's own top-level `time`. For findings Continuum's scanner produces, it is the finding's own creation time. Continuum does not validate it for plausibility: a producer's value is echoed as given, so a `timestamp` here asserts the unit and format, not that the instant is genuine."""
    status: "capo_continuum.types.finding_status.FindingStatus"
    """The current lifecycle status of the finding."""
    status_updated_at: "datetime.datetime"
    """The timestamp when the status last transitioned."""
    created_at: "datetime.datetime"
    """The timestamp when the finding was ingested."""
    scan_run_id: NotRequired["capo_continuum.types.scan_run_id.ScanRunId"]
    """The scan that produced the finding, when it came from one. For a finding Continuum's scanner produced, this is the Continuum scan run (see GetCodeScan). For a finding submitted with CreateCodeFinding, it is the OCSF document's `metadata.correlation_uid`, when that value is a valid ScanRunId. Absent when the finding did not come from a scan."""
    status_message: NotRequired[
        "capo_continuum.types.finding_status_message.FindingStatusMessage"
    ]
    """Human-readable context about the current status."""
    discard_reason: NotRequired[
        "capo_continuum.types.finding_discard_reason.FindingDiscardReason"
    ]
    """Why the finding was not escalated. Present only when status is DISCARDED."""
    discard_reasoning: NotRequired[
        "capo_continuum.types.finding_status_message.FindingStatusMessage"
    ]
    """Customer-facing explanation accompanying `discardReason`."""
    duplicate_of_issue_id: NotRequired["capo_continuum.types.issue_id.IssueId"]
    """The existing issue this finding duplicates. Present only for the DUPLICATE_OF_* discard reasons."""
    created_issue_id: NotRequired["capo_continuum.types.issue_id.IssueId"]
    """The issue Continuum created from this finding."""
    completed_at: NotRequired["datetime.datetime"]
    """When processing finished, whether by creating an issue or discarding. Absent while the finding is still in flight."""
    type: "capo_continuum.types.finding_type.FindingType"
    """What kind of finding this is."""
    title: "capo_continuum.types.finding_title.FindingTitle"
    """The producer's title for the finding."""
    severity: "capo_continuum.types.finding_severity_id.FindingSeverityId"
    """The finding's severity."""
    category: NotRequired["capo_continuum.types.finding_category.FindingCategory"]
    """The producer's vulnerability category."""
    file_path: NotRequired["capo_continuum.types.finding_file_path.FindingFilePath"]
    """The file the finding is about, when it has a code location."""


# --- restJson1 ser/de ---
def serialize_json(value: FindingSummary) -> dict:
    out: dict = {}
    out["findingId"] = value["finding_id"]
    out["findingArn"] = value["finding_arn"]
    out["environmentId"] = value["environment_id"]
    out["source"] = value["source"]
    out["sourceFindingId"] = value["source_finding_id"]
    import capo_continuum._protocol.serialize

    out["reportedAt"] = capo_continuum._protocol.serialize.fmt_date_time(
        value["reported_at"]
    )
    import capo_continuum.types.finding_status

    out["status"] = capo_continuum.types.finding_status.serialize_json(value["status"])
    import capo_continuum._protocol.serialize

    out["statusUpdatedAt"] = capo_continuum._protocol.serialize.fmt_date_time(
        value["status_updated_at"]
    )
    import capo_continuum._protocol.serialize

    out["createdAt"] = capo_continuum._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    if "scan_run_id" in value:
        out["scanRunId"] = value["scan_run_id"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "discard_reason" in value:
        import capo_continuum.types.finding_discard_reason

        out["discardReason"] = (
            capo_continuum.types.finding_discard_reason.serialize_json(
                value["discard_reason"]
            )
        )
    if "discard_reasoning" in value:
        out["discardReasoning"] = value["discard_reasoning"]
    if "duplicate_of_issue_id" in value:
        out["duplicateOfIssueId"] = value["duplicate_of_issue_id"]
    if "created_issue_id" in value:
        out["createdIssueId"] = value["created_issue_id"]
    if "completed_at" in value:
        import capo_continuum._protocol.serialize

        out["completedAt"] = capo_continuum._protocol.serialize.fmt_date_time(
            value["completed_at"]
        )
    import capo_continuum.types.finding_type

    out["type"] = capo_continuum.types.finding_type.serialize_json(value["type"])
    out["title"] = value["title"]
    import capo_continuum.types.finding_severity_id

    out["severity"] = capo_continuum.types.finding_severity_id.serialize_json(
        value["severity"]
    )
    if "category" in value:
        out["category"] = value["category"]
    if "file_path" in value:
        out["filePath"] = value["file_path"]
    return out


def deserialize_json(data: dict) -> FindingSummary:
    out: FindingSummary = {}  # type: ignore[typeddict-item]
    if data.get("findingId") is not None:
        out["finding_id"] = data["findingId"]
    else:
        out["finding_id"] = ""
    if data.get("findingArn") is not None:
        out["finding_arn"] = data["findingArn"]
    else:
        out["finding_arn"] = ""
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        out["environment_id"] = ""
    if data.get("source") is not None:
        out["source"] = data["source"]
    else:
        out["source"] = ""
    if data.get("sourceFindingId") is not None:
        out["source_finding_id"] = data["sourceFindingId"]
    else:
        out["source_finding_id"] = ""
    if data.get("reportedAt") is not None:
        import datetime

        out["reported_at"] = datetime.datetime.fromisoformat(
            data["reportedAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["reported_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("status") is not None:
        import capo_continuum.types.finding_status

        out["status"] = capo_continuum.types.finding_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_continuum.types.finding_status.FindingStatus", ""
        )
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
    if data.get("scanRunId") is not None:
        out["scan_run_id"] = data["scanRunId"]
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    if data.get("discardReason") is not None:
        import capo_continuum.types.finding_discard_reason

        out["discard_reason"] = (
            capo_continuum.types.finding_discard_reason.deserialize_json(
                data["discardReason"]
            )
        )
    if data.get("discardReasoning") is not None:
        out["discard_reasoning"] = data["discardReasoning"]
    if data.get("duplicateOfIssueId") is not None:
        out["duplicate_of_issue_id"] = data["duplicateOfIssueId"]
    if data.get("createdIssueId") is not None:
        out["created_issue_id"] = data["createdIssueId"]
    if data.get("completedAt") is not None:
        import datetime

        out["completed_at"] = datetime.datetime.fromisoformat(
            data["completedAt"].replace("Z", "+00:00")
        )
    if data.get("type") is not None:
        import capo_continuum.types.finding_type

        out["type"] = capo_continuum.types.finding_type.deserialize_json(data["type"])
    else:
        import typing

        out["type"] = typing.cast("capo_continuum.types.finding_type.FindingType", "")
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    if data.get("severity") is not None:
        import capo_continuum.types.finding_severity_id

        out["severity"] = capo_continuum.types.finding_severity_id.deserialize_json(
            data["severity"]
        )
    else:
        import typing

        out["severity"] = typing.cast(
            "capo_continuum.types.finding_severity_id.FindingSeverityId", ""
        )
    if data.get("category") is not None:
        out["category"] = data["category"]
    if data.get("filePath") is not None:
        out["file_path"] = data["filePath"]
    return out
