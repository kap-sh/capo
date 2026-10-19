"""Generated from Smithy shape ``com.amazonaws.backup#GetBackupPlanInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.max_scheduled_runs_preview
    import capo_backup.types.string


class GetBackupPlanInput(TypedDict, closed=True):
    backup_plan_id: "capo_backup.types.string.string"
    """<p>Uniquely identifies a backup plan.</p>"""
    version_id: NotRequired["capo_backup.types.string.string"]
    """<p>Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. Version IDs cannot be edited.</p>"""
    max_scheduled_runs_preview: NotRequired[
        "capo_backup.types.max_scheduled_runs_preview.MaxScheduledRunsPreview"
    ]
    """<p>Number of future scheduled backup runs to preview. When set to 0 (default), no scheduled runs preview is included in the response. Valid range is 0-10.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBackupPlanInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBackupPlanInput:
    out: GetBackupPlanInput = {}  # type: ignore[typeddict-item]
    return out
