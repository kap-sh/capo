"""Generated from Smithy shape ``com.amazonaws.backup#GetBackupPlanFromTemplateOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.backup_plan


class GetBackupPlanFromTemplateOutput(TypedDict, closed=True):
    backup_plan_document: NotRequired["capo_backup.types.backup_plan.BackupPlan"]
    """<p>Returns the body of a backup plan based on the target template, including the name, rules, and backup vault of the plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBackupPlanFromTemplateOutput) -> dict:
    out: dict = {}
    if "backup_plan_document" in value:
        import capo_backup.types.backup_plan

        out["BackupPlanDocument"] = capo_backup.types.backup_plan.serialize_json(
            value["backup_plan_document"]
        )
    return out


def deserialize_json(data: dict) -> GetBackupPlanFromTemplateOutput:
    out: GetBackupPlanFromTemplateOutput = {}  # type: ignore[typeddict-item]
    if data.get("BackupPlanDocument") is not None:
        import capo_backup.types.backup_plan

        out["backup_plan_document"] = capo_backup.types.backup_plan.deserialize_json(
            data["BackupPlanDocument"]
        )
    return out


def redact_sensitive(value: GetBackupPlanFromTemplateOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "backup_plan_document" in value:
        import capo_backup.types.backup_plan

        out["backup_plan_document"] = capo_backup.types.backup_plan.redact_sensitive(
            value["backup_plan_document"]
        )
    return out
