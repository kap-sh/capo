"""Generated from Smithy shape ``com.amazonaws.backup#BackupRulesInput``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.backup_rule_input

BackupRulesInput: TypeAlias = list[
    "capo_backup.types.backup_rule_input.BackupRuleInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: BackupRulesInput) -> list:
    import capo_backup.types.backup_rule_input

    out: list = []
    for item in value:
        out.append(capo_backup.types.backup_rule_input.serialize_json(item))
    return out


def deserialize_json(data: list) -> BackupRulesInput:
    import capo_backup.types.backup_rule_input

    out: BackupRulesInput = []
    for item in data:
        if item is None:
            continue
        out.append(capo_backup.types.backup_rule_input.deserialize_json(item))
    return out


def redact_sensitive(value: BackupRulesInput) -> list[Any]:
    import capo_backup.types.backup_rule_input

    return [
        capo_backup.types.backup_rule_input.redact_sensitive(item) for item in value
    ]
