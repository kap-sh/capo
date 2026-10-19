"""Generated from Smithy shape ``com.amazonaws.backup#BackupPlanInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.advanced_backup_settings
    import capo_backup.types.backup_plan_name
    import capo_backup.types.backup_rules_input
    import capo_backup.types.scan_settings


class BackupPlanInput(TypedDict, closed=True):
    backup_plan_name: "capo_backup.types.backup_plan_name.BackupPlanName"
    """<p>The display name of a backup plan. Must contain 1 to 50 alphanumeric or '-_.' characters.</p>"""
    rules: "capo_backup.types.backup_rules_input.BackupRulesInput"
    """<p>An array of <code>BackupRule</code> objects, each of which specifies a scheduled task that is used to back up a selection of resources.</p>"""
    advanced_backup_settings: NotRequired[
        "capo_backup.types.advanced_backup_settings.AdvancedBackupSettings"
    ]
    """<p>Specifies a list of <code>BackupOptions</code> for each resource type. These settings are only available for Windows Volume Shadow Copy Service (VSS) backup jobs.</p>"""
    scan_settings: NotRequired["capo_backup.types.scan_settings.ScanSettings"]
    """<p>Contains your scanning configuration for the backup rule and includes the malware scanner, and scan mode of either full or incremental.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BackupPlanInput) -> dict:
    out: dict = {}
    out["BackupPlanName"] = value["backup_plan_name"]
    import capo_backup.types.backup_rules_input

    out["Rules"] = capo_backup.types.backup_rules_input.serialize_json(value["rules"])
    if "advanced_backup_settings" in value:
        import capo_backup.types.advanced_backup_settings

        out["AdvancedBackupSettings"] = (
            capo_backup.types.advanced_backup_settings.serialize_json(
                value["advanced_backup_settings"]
            )
        )
    if "scan_settings" in value:
        import capo_backup.types.scan_settings

        out["ScanSettings"] = capo_backup.types.scan_settings.serialize_json(
            value["scan_settings"]
        )
    return out


def deserialize_json(data: dict) -> BackupPlanInput:
    out: BackupPlanInput = {}  # type: ignore[typeddict-item]
    if data.get("BackupPlanName") is not None:
        out["backup_plan_name"] = data["BackupPlanName"]
    else:
        out["backup_plan_name"] = ""
    if data.get("Rules") is not None:
        import capo_backup.types.backup_rules_input

        out["rules"] = capo_backup.types.backup_rules_input.deserialize_json(
            data["Rules"]
        )
    else:
        out["rules"] = []
    if data.get("AdvancedBackupSettings") is not None:
        import capo_backup.types.advanced_backup_settings

        out["advanced_backup_settings"] = (
            capo_backup.types.advanced_backup_settings.deserialize_json(
                data["AdvancedBackupSettings"]
            )
        )
    if data.get("ScanSettings") is not None:
        import capo_backup.types.scan_settings

        out["scan_settings"] = capo_backup.types.scan_settings.deserialize_json(
            data["ScanSettings"]
        )
    return out


def redact_sensitive(value: BackupPlanInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "rules" in value:
        import capo_backup.types.backup_rules_input

        out["rules"] = capo_backup.types.backup_rules_input.redact_sensitive(
            value["rules"]
        )
    return out
