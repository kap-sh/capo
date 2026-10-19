"""Generated from Smithy shape ``com.amazonaws.applicationsignals#BatchUpdateExclusionWindowsError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.exclusion_window_error_code
    import capo_application_signals.types.exclusion_window_error_message
    import capo_application_signals.types.service_level_objective_id


class BatchUpdateExclusionWindowsError(TypedDict, closed=True):
    slo_id: "capo_application_signals.types.service_level_objective_id.ServiceLevelObjectiveId"
    """<p>The SLO ID in the error.</p>"""
    error_code: "capo_application_signals.types.exclusion_window_error_code.ExclusionWindowErrorCode"
    """<p>The error code.</p>"""
    error_message: "capo_application_signals.types.exclusion_window_error_message.ExclusionWindowErrorMessage"
    """<p>The error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateExclusionWindowsError) -> dict:
    out: dict = {}
    out["SloId"] = value["slo_id"]
    out["ErrorCode"] = value["error_code"]
    out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> BatchUpdateExclusionWindowsError:
    out: BatchUpdateExclusionWindowsError = {}  # type: ignore[typeddict-item]
    if data.get("SloId") is not None:
        out["slo_id"] = data["SloId"]
    else:
        out["slo_id"] = ""
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    else:
        out["error_code"] = ""
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    else:
        out["error_message"] = ""
    return out
