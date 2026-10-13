"""Generated from Smithy shape ``com.amazonaws.backup#UpdateBackupPlanInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_backup.errors import DeserializationError

if TYPE_CHECKING:
    import capo_backup.types.backup_plan_input
    import capo_backup.types.string


class UpdateBackupPlanInput(TypedDict, closed=True):
    backup_plan_id: "capo_backup.types.string.string"
    """<p>The ID of the backup plan.</p>"""
    backup_plan: "capo_backup.types.backup_plan_input.BackupPlanInput"
    """<p>The body of a backup plan. Includes a <code>BackupPlanName</code> and one or more sets of <code>Rules</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBackupPlanInput) -> dict:
    out: dict = {}
    import capo_backup.types.backup_plan_input

    out["BackupPlan"] = capo_backup.types.backup_plan_input.serialize_json(
        value["backup_plan"]
    )
    return out


def deserialize_json(data: dict) -> UpdateBackupPlanInput:
    out: UpdateBackupPlanInput = {}  # type: ignore[typeddict-item]
    if data.get("BackupPlan") is not None:
        import capo_backup.types.backup_plan_input

        out["backup_plan"] = capo_backup.types.backup_plan_input.deserialize_json(
            data["BackupPlan"]
        )
    else:
        raise DeserializationError("UpdateBackupPlanInput.backup_plan required")
    return out


def redact_sensitive(value: UpdateBackupPlanInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "backup_plan" in value:
        import capo_backup.types.backup_plan_input

        out["backup_plan"] = capo_backup.types.backup_plan_input.redact_sensitive(
            value["backup_plan"]
        )
    return out
