"""Generated from Smithy shape ``com.amazonaws.backup#BackupPlan``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_backup.errors import DeserializationError

if TYPE_CHECKING:
    import capo_backup.types.advanced_backup_settings
    import capo_backup.types.backup_plan_name
    import capo_backup.types.backup_rules
    import capo_backup.types.scan_settings


class BackupPlan(TypedDict, closed=True):
    backup_plan_name: "capo_backup.types.backup_plan_name.BackupPlanName"
    """<p>The display name of a backup plan. Must contain only alphanumeric or '-_.' special characters.</p> <p>If this is set in the console, it can contain 1 to 50 characters; if this is set through CLI or API, it can contain 1 to 200 characters.</p>"""
    rules: "capo_backup.types.backup_rules.BackupRules"
    """<p>An array of <code>BackupRule</code> objects, each of which specifies a scheduled task that is used to back up a selection of resources. </p>"""
    advanced_backup_settings: NotRequired[
        "capo_backup.types.advanced_backup_settings.AdvancedBackupSettings"
    ]
    """<p>Contains a list of <code>BackupOptions</code> for each resource type.</p>"""
    scan_settings: NotRequired["capo_backup.types.scan_settings.ScanSettings"]
    """<p>Contains your scanning configuration for the backup plan and includes the Malware scanner, your selected resources, and scanner role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BackupPlan) -> dict:
    out: dict = {}
    out["BackupPlanName"] = value["backup_plan_name"]
    import capo_backup.types.backup_rules

    out["Rules"] = capo_backup.types.backup_rules.serialize_json(value["rules"])
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


def deserialize_json(data: dict) -> BackupPlan:
    out: BackupPlan = {}  # type: ignore[typeddict-item]
    if data.get("BackupPlanName") is not None:
        out["backup_plan_name"] = data["BackupPlanName"]
    else:
        raise DeserializationError("BackupPlan.backup_plan_name required")
    if data.get("Rules") is not None:
        import capo_backup.types.backup_rules

        out["rules"] = capo_backup.types.backup_rules.deserialize_json(data["Rules"])
    else:
        raise DeserializationError("BackupPlan.rules required")
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


def redact_sensitive(value: BackupPlan) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "rules" in value:
        import capo_backup.types.backup_rules

        out["rules"] = capo_backup.types.backup_rules.redact_sensitive(value["rules"])
    return out
