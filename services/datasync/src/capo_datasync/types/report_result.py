"""Generated from Smithy shape ``com.amazonaws.datasync#ReportResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.phase_status
    import capo_datasync.types.string


class ReportResult(TypedDict, closed=True):
    status: NotRequired["capo_datasync.types.phase_status.PhaseStatus"]
    """<p>Indicates whether DataSync is still working on your report, created a report, or can't create a complete report.</p>"""
    error_code: NotRequired["capo_datasync.types.string.string"]
    """<p>Indicates the code associated with the error if DataSync can't create a complete report.</p>"""
    error_detail: NotRequired["capo_datasync.types.string.string"]
    """<p>Provides details about issues creating a report.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportResult) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_datasync.types.phase_status

        out["Status"] = capo_datasync.types.phase_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_detail" in value:
        out["ErrorDetail"] = value["error_detail"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReportResult:
    out: ReportResult = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_datasync.types.phase_status

        out["status"] = capo_datasync.types.phase_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("ErrorDetail") is not None:
        out["error_detail"] = data["ErrorDetail"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReportResult) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_datasync.types.phase_status

        out["Status"] = capo_datasync.types.phase_status.serialize_cbor(value["status"])
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_detail" in value:
        out["ErrorDetail"] = value["error_detail"]
    return out


def deserialize_cbor(data: dict) -> ReportResult:
    out: ReportResult = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_datasync.types.phase_status

        out["status"] = capo_datasync.types.phase_status.deserialize_cbor(
            data["Status"]
        )
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("ErrorDetail") is not None:
        out["error_detail"] = data["ErrorDetail"]
    return out
