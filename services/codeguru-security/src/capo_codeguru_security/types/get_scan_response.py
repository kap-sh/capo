"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#GetScanResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_codeguru_security.types.analysis_type
    import capo_codeguru_security.types.error_message
    import capo_codeguru_security.types.scan_name
    import capo_codeguru_security.types.scan_name_arn
    import capo_codeguru_security.types.scan_state
    import capo_codeguru_security.types.uuid


class GetScanResponse(TypedDict, closed=True):
    scan_name: "capo_codeguru_security.types.scan_name.ScanName"
    """<p>The name of the scan.</p>"""
    run_id: "capo_codeguru_security.types.uuid.Uuid"
    """<p>UUID that identifies the individual scan run.</p>"""
    scan_state: "capo_codeguru_security.types.scan_state.ScanState"
    """<p>The current state of the scan. Returns either <code>InProgress</code>, <code>Successful</code>, or <code>Failed</code>.</p>"""
    created_at: "datetime.datetime"
    """<p>The time the scan was created.</p>"""
    analysis_type: "capo_codeguru_security.types.analysis_type.AnalysisType"
    """<p>The type of analysis CodeGuru Security performed in the scan, either <code>Security</code> or <code>All</code>. The <code>Security</code> type only generates findings related to security. The <code>All</code> type generates both security findings and quality findings.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The time when the scan was last updated. Only available for <code>STANDARD</code> scan types.</p>"""
    number_of_revisions: NotRequired["int"]
    """<p>The number of times a scan has been re-run on a revised resource.</p>"""
    scan_name_arn: NotRequired["capo_codeguru_security.types.scan_name_arn.ScanNameArn"]
    """<p>The ARN for the scan name.</p>"""
    error_message: NotRequired[
        "capo_codeguru_security.types.error_message.ErrorMessage"
    ]
    """<p>Details about the error that causes a scan to fail to be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetScanResponse) -> dict:
    out: dict = {}
    out["scanName"] = value["scan_name"]
    out["runId"] = value["run_id"]
    import capo_codeguru_security.types.scan_state

    out["scanState"] = capo_codeguru_security.types.scan_state.serialize_json(
        value["scan_state"]
    )
    import capo_codeguru_security.types._prelude.timestamp

    out["createdAt"] = capo_codeguru_security.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_codeguru_security.types.analysis_type

    out["analysisType"] = capo_codeguru_security.types.analysis_type.serialize_json(
        value["analysis_type"]
    )
    if "updated_at" in value:
        import capo_codeguru_security.types._prelude.timestamp

        out["updatedAt"] = (
            capo_codeguru_security.types._prelude.timestamp.serialize_json(
                value["updated_at"]
            )
        )
    if "number_of_revisions" in value:
        out["numberOfRevisions"] = value["number_of_revisions"]
    if "scan_name_arn" in value:
        out["scanNameArn"] = value["scan_name_arn"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> GetScanResponse:
    out: GetScanResponse = {}  # type: ignore[typeddict-item]
    if data.get("scanName") is not None:
        out["scan_name"] = data["scanName"]
    else:
        out["scan_name"] = ""
    if data.get("runId") is not None:
        out["run_id"] = data["runId"]
    else:
        out["run_id"] = ""
    if data.get("scanState") is not None:
        import capo_codeguru_security.types.scan_state

        out["scan_state"] = capo_codeguru_security.types.scan_state.deserialize_json(
            data["scanState"]
        )
    else:
        import typing

        out["scan_state"] = typing.cast(
            "capo_codeguru_security.types.scan_state.ScanState", ""
        )
    if data.get("createdAt") is not None:
        import capo_codeguru_security.types._prelude.timestamp

        out["created_at"] = (
            capo_codeguru_security.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("analysisType") is not None:
        import capo_codeguru_security.types.analysis_type

        out["analysis_type"] = (
            capo_codeguru_security.types.analysis_type.deserialize_json(
                data["analysisType"]
            )
        )
    else:
        import typing

        out["analysis_type"] = typing.cast(
            "capo_codeguru_security.types.analysis_type.AnalysisType", ""
        )
    if data.get("updatedAt") is not None:
        import capo_codeguru_security.types._prelude.timestamp

        out["updated_at"] = (
            capo_codeguru_security.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    if data.get("numberOfRevisions") is not None:
        out["number_of_revisions"] = data["numberOfRevisions"]
    if data.get("scanNameArn") is not None:
        out["scan_name_arn"] = data["scanNameArn"]
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    return out
