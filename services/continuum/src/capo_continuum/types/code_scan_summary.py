"""Generated from Smithy shape ``com.amazonaws.continuum#CodeScanSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_continuum.types.scan_failure_stage
    import capo_continuum.types.scan_origin
    import capo_continuum.types.scan_run_failure_message
    import capo_continuum.types.scan_run_id
    import capo_continuum.types.scan_status


class CodeScanSummary(TypedDict, closed=True):
    scan_run_id: "capo_continuum.types.scan_run_id.ScanRunId"
    """The unique scan identifier."""
    status: "capo_continuum.types.scan_status.ScanStatus"
    """Current customer-visible status."""
    origin: "capo_continuum.types.scan_origin.ScanOrigin"
    """Why the scan was created. Always present."""
    created_at: "datetime.datetime"
    """Time at which Continuum accepted the scan request."""
    completed_at: NotRequired["datetime.datetime"]
    """Time at which a terminal result was recorded."""
    failure_message: NotRequired[
        "capo_continuum.types.scan_run_failure_message.ScanRunFailureMessage"
    ]
    """Failure detail present for unsuccessful scans."""
    failure_stage: NotRequired[
        "capo_continuum.types.scan_failure_stage.ScanFailureStage"
    ]
    """Phase this scan failed in. Present only when `status` is FAILED, and absent for a scan that failed before this field existed."""


# --- restJson1 ser/de ---
def serialize_json(value: CodeScanSummary) -> dict:
    out: dict = {}
    out["scanRunId"] = value["scan_run_id"]
    import capo_continuum.types.scan_status

    out["status"] = capo_continuum.types.scan_status.serialize_json(value["status"])
    import capo_continuum.types.scan_origin

    out["origin"] = capo_continuum.types.scan_origin.serialize_json(value["origin"])
    import capo_continuum._protocol.serialize

    out["createdAt"] = capo_continuum._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    if "completed_at" in value:
        import capo_continuum._protocol.serialize

        out["completedAt"] = capo_continuum._protocol.serialize.fmt_date_time(
            value["completed_at"]
        )
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    if "failure_stage" in value:
        import capo_continuum.types.scan_failure_stage

        out["failureStage"] = capo_continuum.types.scan_failure_stage.serialize_json(
            value["failure_stage"]
        )
    return out


def deserialize_json(data: dict) -> CodeScanSummary:
    out: CodeScanSummary = {}  # type: ignore[typeddict-item]
    if data.get("scanRunId") is not None:
        out["scan_run_id"] = data["scanRunId"]
    else:
        out["scan_run_id"] = ""
    if data.get("status") is not None:
        import capo_continuum.types.scan_status

        out["status"] = capo_continuum.types.scan_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast("capo_continuum.types.scan_status.ScanStatus", "")
    if data.get("origin") is not None:
        import capo_continuum.types.scan_origin

        out["origin"] = capo_continuum.types.scan_origin.deserialize_json(
            data["origin"]
        )
    else:
        import typing

        out["origin"] = typing.cast("capo_continuum.types.scan_origin.ScanOrigin", "")
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("completedAt") is not None:
        import datetime

        out["completed_at"] = datetime.datetime.fromisoformat(
            data["completedAt"].replace("Z", "+00:00")
        )
    if data.get("failureMessage") is not None:
        out["failure_message"] = data["failureMessage"]
    if data.get("failureStage") is not None:
        import capo_continuum.types.scan_failure_stage

        out["failure_stage"] = capo_continuum.types.scan_failure_stage.deserialize_json(
            data["failureStage"]
        )
    return out
