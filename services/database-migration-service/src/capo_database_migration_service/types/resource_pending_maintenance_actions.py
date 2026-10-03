"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ResourcePendingMaintenanceActions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.pending_maintenance_action_details
    import capo_database_migration_service.types.string


class ResourcePendingMaintenanceActions(TypedDict, closed=True):
    resource_identifier: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) of the DMS resource that the pending maintenance action applies to. For information about creating an ARN, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.AWS.ARN.html"> Constructing an Amazon Resource Name (ARN) for DMS</a> in the DMS documentation.</p>"""
    pending_maintenance_action_details: NotRequired[
        "capo_database_migration_service.types.pending_maintenance_action_details.PendingMaintenanceActionDetails"
    ]
    """<p>Detailed information about the pending maintenance action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourcePendingMaintenanceActions) -> dict:
    out: dict = {}
    if "resource_identifier" in value:
        out["ResourceIdentifier"] = value["resource_identifier"]
    if "pending_maintenance_action_details" in value:
        import capo_database_migration_service.types.pending_maintenance_action_details

        out["PendingMaintenanceActionDetails"] = (
            capo_database_migration_service.types.pending_maintenance_action_details.serialize_aws_json_1_1(
                value["pending_maintenance_action_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourcePendingMaintenanceActions:
    out: ResourcePendingMaintenanceActions = {}  # type: ignore[typeddict-item]
    if data.get("ResourceIdentifier") is not None:
        out["resource_identifier"] = data["ResourceIdentifier"]
    if data.get("PendingMaintenanceActionDetails") is not None:
        import capo_database_migration_service.types.pending_maintenance_action_details

        out["pending_maintenance_action_details"] = (
            capo_database_migration_service.types.pending_maintenance_action_details.deserialize_aws_json_1_1(
                data["PendingMaintenanceActionDetails"]
            )
        )
    return out
