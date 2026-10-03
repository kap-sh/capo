"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#AutoTuneOptionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.auto_tune_desired_state
    import capo_elasticsearch_service.types.auto_tune_maintenance_schedule_list


class AutoTuneOptionsInput(TypedDict, closed=True):
    desired_state: NotRequired[
        "capo_elasticsearch_service.types.auto_tune_desired_state.AutoTuneDesiredState"
    ]
    """<p>Specifies the Auto-Tune desired state. Valid values are ENABLED, DISABLED. </p>"""
    maintenance_schedules: NotRequired[
        "capo_elasticsearch_service.types.auto_tune_maintenance_schedule_list.AutoTuneMaintenanceScheduleList"
    ]
    """<p>Specifies list of maitenance schedules. See the <a href="https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/auto-tune.html" target="_blank">Developer Guide</a> for more information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoTuneOptionsInput) -> dict:
    out: dict = {}
    if "desired_state" in value:
        import capo_elasticsearch_service.types.auto_tune_desired_state

        out["DesiredState"] = (
            capo_elasticsearch_service.types.auto_tune_desired_state.serialize_json(
                value["desired_state"]
            )
        )
    if "maintenance_schedules" in value:
        import capo_elasticsearch_service.types.auto_tune_maintenance_schedule_list

        out["MaintenanceSchedules"] = (
            capo_elasticsearch_service.types.auto_tune_maintenance_schedule_list.serialize_json(
                value["maintenance_schedules"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutoTuneOptionsInput:
    out: AutoTuneOptionsInput = {}  # type: ignore[typeddict-item]
    if data.get("DesiredState") is not None:
        import capo_elasticsearch_service.types.auto_tune_desired_state

        out["desired_state"] = (
            capo_elasticsearch_service.types.auto_tune_desired_state.deserialize_json(
                data["DesiredState"]
            )
        )
    if data.get("MaintenanceSchedules") is not None:
        import capo_elasticsearch_service.types.auto_tune_maintenance_schedule_list

        out["maintenance_schedules"] = (
            capo_elasticsearch_service.types.auto_tune_maintenance_schedule_list.deserialize_json(
                data["MaintenanceSchedules"]
            )
        )
    return out
