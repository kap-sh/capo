"""Generated from Smithy shape ``com.amazonaws.backup#CreateBackupPlanInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_backup.errors import DeserializationError

if TYPE_CHECKING:
    import capo_backup.types.backup_plan_input
    import capo_backup.types.string
    import capo_backup.types.tags


class CreateBackupPlanInput(TypedDict, closed=True):
    backup_plan: "capo_backup.types.backup_plan_input.BackupPlanInput"
    """<p>The body of a backup plan. Includes a <code>BackupPlanName</code> and one or more sets of <code>Rules</code>.</p>"""
    backup_plan_tags: NotRequired["capo_backup.types.tags.Tags"]
    """<p>The tags to assign to the backup plan.</p>"""
    creator_request_id: NotRequired["capo_backup.types.string.string"]
    """<p>Identifies the request and allows failed requests to be retried without the risk of running the operation twice. If the request includes a <code>CreatorRequestId</code> that matches an existing backup plan, that plan is returned. This parameter is optional.</p> <p>If used, this parameter must contain 1 to 50 alphanumeric or '-_.' characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBackupPlanInput) -> dict:
    out: dict = {}
    import capo_backup.types.backup_plan_input

    out["BackupPlan"] = capo_backup.types.backup_plan_input.serialize_json(
        value["backup_plan"]
    )
    if "backup_plan_tags" in value:
        import capo_backup.types.tags

        out["BackupPlanTags"] = capo_backup.types.tags.serialize_json(
            value["backup_plan_tags"]
        )
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    return out


def deserialize_json(data: dict) -> CreateBackupPlanInput:
    out: CreateBackupPlanInput = {}  # type: ignore[typeddict-item]
    if data.get("BackupPlan") is not None:
        import capo_backup.types.backup_plan_input

        out["backup_plan"] = capo_backup.types.backup_plan_input.deserialize_json(
            data["BackupPlan"]
        )
    else:
        raise DeserializationError("CreateBackupPlanInput.backup_plan required")
    if data.get("BackupPlanTags") is not None:
        import capo_backup.types.tags

        out["backup_plan_tags"] = capo_backup.types.tags.deserialize_json(
            data["BackupPlanTags"]
        )
    if data.get("CreatorRequestId") is not None:
        out["creator_request_id"] = data["CreatorRequestId"]
    return out


def redact_sensitive(value: CreateBackupPlanInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "backup_plan" in value:
        import capo_backup.types.backup_plan_input

        out["backup_plan"] = capo_backup.types.backup_plan_input.redact_sensitive(
            value["backup_plan"]
        )
    if "backup_plan_tags" in value:
        out["backup_plan_tags"] = "*** Sensitive Data Redacted ***"
    return out
