"""Generated from Smithy shape ``com.amazonaws.backup#PutRestoreValidationResultInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.restore_job_id
    import capo_backup.types.restore_validation_status
    import capo_backup.types.string


class PutRestoreValidationResultInput(TypedDict, closed=True):
    restore_job_id: "capo_backup.types.restore_job_id.RestoreJobId"
    """<p>This is a unique identifier of a restore job within Backup.</p>"""
    validation_status: (
        "capo_backup.types.restore_validation_status.RestoreValidationStatus"
    )
    """<p>The status of your restore validation.</p>"""
    validation_status_message: NotRequired["capo_backup.types.string.string"]
    """<p>This is an optional message string you can input to describe the validation status for the restore test validation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutRestoreValidationResultInput) -> dict:
    out: dict = {}
    import capo_backup.types.restore_validation_status

    out["ValidationStatus"] = (
        capo_backup.types.restore_validation_status.serialize_json(
            value["validation_status"]
        )
    )
    if "validation_status_message" in value:
        out["ValidationStatusMessage"] = value["validation_status_message"]
    return out


def deserialize_json(data: dict) -> PutRestoreValidationResultInput:
    out: PutRestoreValidationResultInput = {}  # type: ignore[typeddict-item]
    if data.get("ValidationStatus") is not None:
        import capo_backup.types.restore_validation_status

        out["validation_status"] = (
            capo_backup.types.restore_validation_status.deserialize_json(
                data["ValidationStatus"]
            )
        )
    else:
        import typing

        out["validation_status"] = typing.cast(
            "capo_backup.types.restore_validation_status.RestoreValidationStatus", ""
        )
    if data.get("ValidationStatusMessage") is not None:
        out["validation_status_message"] = data["ValidationStatusMessage"]
    return out
