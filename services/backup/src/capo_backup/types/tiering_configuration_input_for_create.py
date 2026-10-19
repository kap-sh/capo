"""Generated from Smithy shape ``com.amazonaws.backup#TieringConfigurationInputForCreate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_backup.types.backup_vault_name_or_wildcard
    import capo_backup.types.resource_selections
    import capo_backup.types.tiering_configuration_name


class TieringConfigurationInputForCreate(TypedDict, closed=True):
    tiering_configuration_name: (
        "capo_backup.types.tiering_configuration_name.TieringConfigurationName"
    )
    """<p>The unique name of the tiering configuration. This cannot be changed after creation, and it must consist of only alphanumeric characters and underscores.</p>"""
    backup_vault_name: (
        "capo_backup.types.backup_vault_name_or_wildcard.BackupVaultNameOrWildcard"
    )
    """<p>The name of the backup vault where the tiering configuration applies. Use <code>*</code> to apply to all backup vaults.</p>"""
    resource_selection: "capo_backup.types.resource_selections.ResourceSelections"
    """<p>An array of resource selection objects that specify which resources are included in the tiering configuration and their tiering settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TieringConfigurationInputForCreate) -> dict:
    out: dict = {}
    out["TieringConfigurationName"] = value["tiering_configuration_name"]
    out["BackupVaultName"] = value["backup_vault_name"]
    import capo_backup.types.resource_selections

    out["ResourceSelection"] = capo_backup.types.resource_selections.serialize_json(
        value["resource_selection"]
    )
    return out


def deserialize_json(data: dict) -> TieringConfigurationInputForCreate:
    out: TieringConfigurationInputForCreate = {}  # type: ignore[typeddict-item]
    if data.get("TieringConfigurationName") is not None:
        out["tiering_configuration_name"] = data["TieringConfigurationName"]
    else:
        out["tiering_configuration_name"] = ""
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
    return out
