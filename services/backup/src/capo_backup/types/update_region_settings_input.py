"""Generated from Smithy shape ``com.amazonaws.backup#UpdateRegionSettingsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.resource_type_management_preference
    import capo_backup.types.resource_type_opt_in_preference


class UpdateRegionSettingsInput(TypedDict, closed=True):
    resource_type_opt_in_preference: NotRequired[
        "capo_backup.types.resource_type_opt_in_preference.ResourceTypeOptInPreference"
    ]
    """<p>Updates the list of services along with the opt-in preferences for the Region.</p> <p>If resource assignments are only based on tags, then service opt-in settings are applied. If a resource type is explicitly assigned to a backup plan, such as Amazon S3, Amazon EC2, or Amazon RDS, it will be included in the backup even if the opt-in is not enabled for that particular service. If both a resource type and tags are specified in a resource assignment, the resource type specified in the backup plan takes priority over the tag condition. Service opt-in settings are disregarded in this situation.</p>"""
    resource_type_management_preference: NotRequired[
        "capo_backup.types.resource_type_management_preference.ResourceTypeManagementPreference"
    ]
    """<p>Enables or disables full Backup management of backups for a resource type. To enable full Backup management for DynamoDB along with <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/advanced-ddb-backup.html"> Backup's advanced DynamoDB backup features</a>, follow the procedure to <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/advanced-ddb-backup.html#advanced-ddb-backup-enable-cli"> enable advanced DynamoDB backup programmatically</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRegionSettingsInput) -> dict:
    out: dict = {}
    if "resource_type_opt_in_preference" in value:
        import capo_backup.types.resource_type_opt_in_preference

        out["ResourceTypeOptInPreference"] = (
            capo_backup.types.resource_type_opt_in_preference.serialize_json(
                value["resource_type_opt_in_preference"]
            )
        )
    if "resource_type_management_preference" in value:
        import capo_backup.types.resource_type_management_preference

        out["ResourceTypeManagementPreference"] = (
            capo_backup.types.resource_type_management_preference.serialize_json(
                value["resource_type_management_preference"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateRegionSettingsInput:
    out: UpdateRegionSettingsInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceTypeOptInPreference") is not None:
        import capo_backup.types.resource_type_opt_in_preference

        out["resource_type_opt_in_preference"] = (
            capo_backup.types.resource_type_opt_in_preference.deserialize_json(
                data["ResourceTypeOptInPreference"]
            )
        )
    if data.get("ResourceTypeManagementPreference") is not None:
        import capo_backup.types.resource_type_management_preference

        out["resource_type_management_preference"] = (
            capo_backup.types.resource_type_management_preference.deserialize_json(
                data["ResourceTypeManagementPreference"]
            )
        )
    return out
