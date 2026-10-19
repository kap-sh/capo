"""Generated from Smithy shape ``com.amazonaws.backup#TieringConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.arn
    import capo_backup.types.backup_vault_name_or_wildcard
    import capo_backup.types.creator_request_id
    import capo_backup.types.resource_selections
    import capo_backup.types.tiering_configuration_name
    import capo_backup.types.timestamp


class TieringConfiguration(TypedDict, closed=True):
    tiering_configuration_name: (
        "capo_backup.types.tiering_configuration_name.TieringConfigurationName"
    )
    """<p>The unique name of the tiering configuration. This cannot be changed after creation, and it must consist of only alphanumeric characters and underscores.</p>"""
    tiering_configuration_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies the tiering configuration.</p>"""
    backup_vault_name: (
        "capo_backup.types.backup_vault_name_or_wildcard.BackupVaultNameOrWildcard"
    )
    """<p>The name of the backup vault where the tiering configuration applies. Use <code>*</code> to apply to all backup vaults.</p>"""
    resource_selection: "capo_backup.types.resource_selections.ResourceSelections"
    """<p>An array of resource selection objects that specify which resources are included in the tiering configuration and their tiering settings.</p>"""
    creator_request_id: NotRequired[
        "capo_backup.types.creator_request_id.CreatorRequestId"
    ]
    """<p>This is a unique string that identifies the request and allows failed requests to be retried without the risk of running the operation twice.</p>"""
    creation_time: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The date and time a tiering configuration was created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationTime</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087AM.</p>"""
    last_updated_time: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The date and time a tiering configuration was updated, in Unix format and Coordinated Universal Time (UTC). The value of <code>LastUpdatedTime</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087AM.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TieringConfiguration) -> dict:
    out: dict = {}
    out["TieringConfigurationName"] = value["tiering_configuration_name"]
    if "tiering_configuration_arn" in value:
        out["TieringConfigurationArn"] = value["tiering_configuration_arn"]
    out["BackupVaultName"] = value["backup_vault_name"]
    import capo_backup.types.resource_selections

    out["ResourceSelection"] = capo_backup.types.resource_selections.serialize_json(
        value["resource_selection"]
    )
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    if "creation_time" in value:
        import capo_backup.types.timestamp

        out["CreationTime"] = capo_backup.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "last_updated_time" in value:
        import capo_backup.types.timestamp

        out["LastUpdatedTime"] = capo_backup.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    return out


def deserialize_json(data: dict) -> TieringConfiguration:
    out: TieringConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("TieringConfigurationName") is not None:
        out["tiering_configuration_name"] = data["TieringConfigurationName"]
    else:
        out["tiering_configuration_name"] = ""
    if data.get("TieringConfigurationArn") is not None:
        out["tiering_configuration_arn"] = data["TieringConfigurationArn"]
    if data.get("BackupVaultName") is not None:
        out["backup_vault_name"] = data["BackupVaultName"]
    else:
        out["backup_vault_name"] = ""
    if data.get("ResourceSelection") is not None:
        import capo_backup.types.resource_selections

        out["resource_selection"] = (
            capo_backup.types.resource_selections.deserialize_json(
                data["ResourceSelection"]
            )
        )
    else:
        out["resource_selection"] = []
    if data.get("CreatorRequestId") is not None:
        out["creator_request_id"] = data["CreatorRequestId"]
    if data.get("CreationTime") is not None:
        import capo_backup.types.timestamp

        out["creation_time"] = capo_backup.types.timestamp.deserialize_json(
            data["CreationTime"]
        )
    if data.get("LastUpdatedTime") is not None:
        import capo_backup.types.timestamp

        out["last_updated_time"] = capo_backup.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    return out
