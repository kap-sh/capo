"""Generated from Smithy shape ``com.amazonaws.opensearch#AutoTuneOptionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.auto_tune_desired_state
    import capo_opensearch.types.auto_tune_maintenance_schedule_list
    import capo_opensearch.types.boolean


class AutoTuneOptionsInput(TypedDict, closed=True):
    desired_state: NotRequired[
        "capo_opensearch.types.auto_tune_desired_state.AutoTuneDesiredState"
    ]
    """<p>Whether Auto-Tune is enabled or disabled.</p>"""
    maintenance_schedules: NotRequired[
        "capo_opensearch.types.auto_tune_maintenance_schedule_list.AutoTuneMaintenanceScheduleList"
    ]
    """<p>A list of maintenance schedules during which Auto-Tune can deploy changes. Maintenance windows are deprecated and have been replaced with <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/off-peak.html">off-peak windows</a>.</p>"""
    use_off_peak_window: NotRequired["capo_opensearch.types.boolean.Boolean"]
    """<p>Whether to schedule Auto-Tune optimizations that require blue/green deployments during the domain's configured daily off-peak window.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoTuneOptionsInput) -> dict:
    out: dict = {}
    if "desired_state" in value:
        import capo_opensearch.types.auto_tune_desired_state

        out["DesiredState"] = (
            capo_opensearch.types.auto_tune_desired_state.serialize_json(
                value["desired_state"]
            )
        )
    if "maintenance_schedules" in value:
        import capo_opensearch.types.auto_tune_maintenance_schedule_list

        out["MaintenanceSchedules"] = (
            capo_opensearch.types.auto_tune_maintenance_schedule_list.serialize_json(
                value["maintenance_schedules"]
            )
        )
    if "use_off_peak_window" in value:
        out["UseOffPeakWindow"] = value["use_off_peak_window"]
    return out


def deserialize_json(data: dict) -> AutoTuneOptionsInput:
    out: AutoTuneOptionsInput = {}  # type: ignore[typeddict-item]
    if data.get("DesiredState") is not None:
        import capo_opensearch.types.auto_tune_desired_state

        out["desired_state"] = (
            capo_opensearch.types.auto_tune_desired_state.deserialize_json(
                data["DesiredState"]
            )
        )
    if data.get("MaintenanceSchedules") is not None:
        import capo_opensearch.types.auto_tune_maintenance_schedule_list

        out["maintenance_schedules"] = (
            capo_opensearch.types.auto_tune_maintenance_schedule_list.deserialize_json(
                data["MaintenanceSchedules"]
            )
        )
    if data.get("UseOffPeakWindow") is not None:
        out["use_off_peak_window"] = data["UseOffPeakWindow"]
    return out
