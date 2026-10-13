"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowTargetList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_target

MaintenanceWindowTargetList: TypeAlias = list[
    "capo_ssm.types.maintenance_window_target.MaintenanceWindowTarget"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceWindowTargetList) -> list:
    import capo_ssm.types.maintenance_window_target

    out: list = []
    for item in value:
        out.append(
            capo_ssm.types.maintenance_window_target.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MaintenanceWindowTargetList:
    import capo_ssm.types.maintenance_window_target

    out: MaintenanceWindowTargetList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ssm.types.maintenance_window_target.deserialize_aws_json_1_1(item)
        )
    return out


def redact_sensitive(value: MaintenanceWindowTargetList) -> list[Any]:
    import capo_ssm.types.maintenance_window_target

    return [
        capo_ssm.types.maintenance_window_target.redact_sensitive(item)
        for item in value
    ]
