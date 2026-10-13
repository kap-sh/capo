"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowTaskList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_task

MaintenanceWindowTaskList: TypeAlias = list[
    "capo_ssm.types.maintenance_window_task.MaintenanceWindowTask"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceWindowTaskList) -> list:
    import capo_ssm.types.maintenance_window_task

    out: list = []
    for item in value:
        out.append(capo_ssm.types.maintenance_window_task.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MaintenanceWindowTaskList:
    import capo_ssm.types.maintenance_window_task

    out: MaintenanceWindowTaskList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ssm.types.maintenance_window_task.deserialize_aws_json_1_1(item)
        )
    return out


def redact_sensitive(value: MaintenanceWindowTaskList) -> list[Any]:
    import capo_ssm.types.maintenance_window_task

    return [
        capo_ssm.types.maintenance_window_task.redact_sensitive(item) for item in value
    ]
