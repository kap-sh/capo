"""Generated from Smithy shape ``com.amazonaws.backup#BackupRules``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.backup_rule

BackupRules: TypeAlias = list["capo_backup.types.backup_rule.BackupRule"]


# --- restJson1 ser/de ---
def serialize_json(value: BackupRules) -> list:
    import capo_backup.types.backup_rule

    out: list = []
    for item in value:
        out.append(capo_backup.types.backup_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> BackupRules:
    import capo_backup.types.backup_rule

    out: BackupRules = []
    for item in data:
        if item is None:
            continue
        out.append(capo_backup.types.backup_rule.deserialize_json(item))
    return out


def redact_sensitive(value: BackupRules) -> list[Any]:
    import capo_backup.types.backup_rule

    return [capo_backup.types.backup_rule.redact_sensitive(item) for item in value]
