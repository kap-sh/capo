"""Generated from Smithy shape ``com.amazonaws.applicationsignals#BatchUpdateExclusionWindowsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.batch_update_exclusion_windows_errors
    import capo_application_signals.types.service_level_objective_ids


class BatchUpdateExclusionWindowsOutput(TypedDict, closed=True):
    slo_ids: "capo_application_signals.types.service_level_objective_ids.ServiceLevelObjectiveIds"
    """<p>The list of SLO IDs that were successfully processed.</p>"""
    errors: "capo_application_signals.types.batch_update_exclusion_windows_errors.BatchUpdateExclusionWindowsErrors"
    """<p>A list of errors that occurred while processing the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateExclusionWindowsOutput) -> dict:
    out: dict = {}
    import capo_application_signals.types.service_level_objective_ids

    out["SloIds"] = (
        capo_application_signals.types.service_level_objective_ids.serialize_json(
            value["slo_ids"]
        )
    )
    import capo_application_signals.types.batch_update_exclusion_windows_errors

    out["Errors"] = (
        capo_application_signals.types.batch_update_exclusion_windows_errors.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateExclusionWindowsOutput:
    out: BatchUpdateExclusionWindowsOutput = {}  # type: ignore[typeddict-item]
    if data.get("SloIds") is not None:
        import capo_application_signals.types.service_level_objective_ids

        out["slo_ids"] = (
            capo_application_signals.types.service_level_objective_ids.deserialize_json(
                data["SloIds"]
            )
        )
    else:
        out["slo_ids"] = []
    if data.get("Errors") is not None:
        import capo_application_signals.types.batch_update_exclusion_windows_errors

        out["errors"] = (
            capo_application_signals.types.batch_update_exclusion_windows_errors.deserialize_json(
                data["Errors"]
            )
        )
    else:
        out["errors"] = []
    return out
