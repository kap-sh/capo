"""Generated from Smithy shape ``com.amazonaws.opensearch#AutoTuneOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.auto_tune_desired_state
    import capo_opensearch.types.auto_tune_maintenance_schedule_list
    import capo_opensearch.types.boolean
    import capo_opensearch.types.rollback_on_disable


class AutoTuneOptions(TypedDict, closed=True):
    desired_state: NotRequired[
        "capo_opensearch.types.auto_tune_desired_state.AutoTuneDesiredState"
    ]
    """<p>Whether Auto-Tune is enabled or disabled.</p>"""
    rollback_on_disable: NotRequired[
        "capo_opensearch.types.rollback_on_disable.RollbackOnDisable"
    ]
    """<p>When disabling Auto-Tune, specify <code>NO_ROLLBACK</code> to retain all prior Auto-Tune settings or <code>DEFAULT_ROLLBACK</code> to revert to the OpenSearch Service defaults. If you specify <code>DEFAULT_ROLLBACK</code>, you must include a <code>MaintenanceSchedule</code> in the request. Otherwise, OpenSearch Service is unable to perform the rollback.</p>"""
    maintenance_schedules: NotRequired[
        "capo_opensearch.types.auto_tune_maintenance_schedule_list.AutoTuneMaintenanceScheduleList"
    ]
    """<p>DEPRECATED. Use <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/off-peak.html">off-peak window</a> instead.</p> <p>A list of maintenance schedules during which Auto-Tune can deploy changes.</p>"""
    use_off_peak_window: NotRequired["capo_opensearch.types.boolean.Boolean"]
    """<p>Whether to use the domain's <a href="https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_OffPeakWindow.html">off-peak window</a> to deploy configuration changes on the domain rather than a maintenance schedule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoTuneOptions) -> dict:
    out: dict = {}
    if "desired_state" in value:
        import capo_opensearch.types.auto_tune_desired_state

        out["DesiredState"] = (
            capo_opensearch.types.auto_tune_desired_state.serialize_json(
                value["desired_state"]
            )
        )
    if "rollback_on_disable" in value:
        import capo_opensearch.types.rollback_on_disable

        out["RollbackOnDisable"] = (
            capo_opensearch.types.rollback_on_disable.serialize_json(
                value["rollback_on_disable"]
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


def deserialize_json(data: dict) -> AutoTuneOptions:
    out: AutoTuneOptions = {}  # type: ignore[typeddict-item]
    if data.get("DesiredState") is not None:
        import capo_opensearch.types.auto_tune_desired_state

        out["desired_state"] = (
            capo_opensearch.types.auto_tune_desired_state.deserialize_json(
                data["DesiredState"]
            )
        )
    if data.get("RollbackOnDisable") is not None:
        import capo_opensearch.types.rollback_on_disable

        out["rollback_on_disable"] = (
            capo_opensearch.types.rollback_on_disable.deserialize_json(
                data["RollbackOnDisable"]
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
