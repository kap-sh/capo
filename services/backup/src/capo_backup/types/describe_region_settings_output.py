"""Generated from Smithy shape ``com.amazonaws.backup#DescribeRegionSettingsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.resource_type_management_preference
    import capo_backup.types.resource_type_opt_in_preference


class DescribeRegionSettingsOutput(TypedDict, closed=True):
    resource_type_opt_in_preference: NotRequired[
        "capo_backup.types.resource_type_opt_in_preference.ResourceTypeOptInPreference"
    ]
    """<p>The services along with the opt-in preferences in the Region.</p>"""
    resource_type_management_preference: NotRequired[
        "capo_backup.types.resource_type_management_preference.ResourceTypeManagementPreference"
    ]
    """<p>Returns whether Backup fully manages the backups for a resource type.</p> <p>For the benefits of full Backup management, see <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html#full-management">Full Backup management</a>.</p> <p>For a list of resource types and whether each supports full Backup management, see the <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-feature-availability.html#features-by-resource">Feature availability by resource</a> table.</p> <p>If <code>"DynamoDB":false</code>, you can enable full Backup management for DynamoDB backup by enabling <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/advanced-ddb-backup.html#advanced-ddb-backup-enable-cli"> Backup's advanced DynamoDB backup features</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRegionSettingsOutput) -> dict:
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


def deserialize_json(data: dict) -> DescribeRegionSettingsOutput:
    out: DescribeRegionSettingsOutput = {}  # type: ignore[typeddict-item]
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
