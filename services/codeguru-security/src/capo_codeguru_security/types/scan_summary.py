"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#ScanSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_codeguru_security.types.scan_name
    import capo_codeguru_security.types.scan_name_arn
    import capo_codeguru_security.types.scan_state
    import capo_codeguru_security.types.uuid


class ScanSummary(TypedDict, closed=True):
    scan_state: "capo_codeguru_security.types.scan_state.ScanState"
    """<p>The state of the scan. A scan can be <code>In Progress</code>, <code>Complete</code>, or <code>Failed</code>. </p>"""
    created_at: "datetime.datetime"
    """<p> The time when the scan was created. </p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The time the scan was last updated. A scan is updated when it is re-run.</p>"""
    scan_name: "capo_codeguru_security.types.scan_name.ScanName"
    """<p>The name of the scan. </p>"""
    run_id: "capo_codeguru_security.types.uuid.Uuid"
    """<p>The identifier for the scan run. </p>"""
    scan_name_arn: NotRequired["capo_codeguru_security.types.scan_name_arn.ScanNameArn"]
    """<p>The ARN for the scan name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScanSummary) -> dict:
    out: dict = {}
    import capo_codeguru_security.types.scan_state

    out["scanState"] = capo_codeguru_security.types.scan_state.serialize_json(
        value["scan_state"]
    )
    import capo_codeguru_security.types._prelude.timestamp

    out["createdAt"] = capo_codeguru_security.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    if "updated_at" in value:
        import capo_codeguru_security.types._prelude.timestamp

        out["updatedAt"] = (
            capo_codeguru_security.types._prelude.timestamp.serialize_json(
                value["updated_at"]
            )
        )
    out["scanName"] = value["scan_name"]
    out["runId"] = value["run_id"]
    if "scan_name_arn" in value:
        out["scanNameArn"] = value["scan_name_arn"]
    return out


def deserialize_json(data: dict) -> ScanSummary:
    out: ScanSummary = {}  # type: ignore[typeddict-item]
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
    if data.get("updatedAt") is not None:
        import capo_codeguru_security.types._prelude.timestamp

        out["updated_at"] = (
            capo_codeguru_security.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    if data.get("scanName") is not None:
        out["scan_name"] = data["scanName"]
    else:
        out["scan_name"] = ""
    if data.get("runId") is not None:
        out["run_id"] = data["runId"]
    else:
        out["run_id"] = ""
    if data.get("scanNameArn") is not None:
        out["scan_name_arn"] = data["scanNameArn"]
    return out
