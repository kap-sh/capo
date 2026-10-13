"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowIdentityList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_identity

MaintenanceWindowIdentityList: TypeAlias = list[
    "capo_ssm.types.maintenance_window_identity.MaintenanceWindowIdentity"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceWindowIdentityList) -> list:
    import capo_ssm.types.maintenance_window_identity

    out: list = []
    for item in value:
        out.append(
            capo_ssm.types.maintenance_window_identity.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MaintenanceWindowIdentityList:
    import capo_ssm.types.maintenance_window_identity

    out: MaintenanceWindowIdentityList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ssm.types.maintenance_window_identity.deserialize_aws_json_1_1(item)
        )
    return out


def redact_sensitive(value: MaintenanceWindowIdentityList) -> list[Any]:
    import capo_ssm.types.maintenance_window_identity

    return [
        capo_ssm.types.maintenance_window_identity.redact_sensitive(item)
        for item in value
    ]
