"""Generated from Smithy shape ``com.amazonaws.backup#UpdateRestoreTestingSelectionInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_backup.errors import DeserializationError

if TYPE_CHECKING:
    import capo_backup.types.restore_testing_selection_for_update


class UpdateRestoreTestingSelectionInput(TypedDict, closed=True):
    restore_testing_plan_name: "str"
    """<p>The restore testing plan name is required to update the indicated testing plan.</p>"""
    restore_testing_selection: "capo_backup.types.restore_testing_selection_for_update.RestoreTestingSelectionForUpdate"
    """<p>To update your restore testing selection, you can use either protected resource ARNs or conditions, but not both. That is, if your selection has <code>ProtectedResourceArns</code>, requesting an update with the parameter <code>ProtectedResourceConditions</code> will be unsuccessful.</p>"""
    restore_testing_selection_name: "str"
    """<p>The required restore testing selection name of the restore testing selection you wish to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRestoreTestingSelectionInput) -> dict:
    out: dict = {}
    import capo_backup.types.restore_testing_selection_for_update

    out["RestoreTestingSelection"] = (
        capo_backup.types.restore_testing_selection_for_update.serialize_json(
            value["restore_testing_selection"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateRestoreTestingSelectionInput:
    out: UpdateRestoreTestingSelectionInput = {}  # type: ignore[typeddict-item]
    if data.get("RestoreTestingSelection") is not None:
        import capo_backup.types.restore_testing_selection_for_update

        out["restore_testing_selection"] = (
            capo_backup.types.restore_testing_selection_for_update.deserialize_json(
                data["RestoreTestingSelection"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateRestoreTestingSelectionInput.restore_testing_selection required"
        )
    return out


def redact_sensitive(value: UpdateRestoreTestingSelectionInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "restore_testing_selection" in value:
        import capo_backup.types.restore_testing_selection_for_update

        out["restore_testing_selection"] = (
            capo_backup.types.restore_testing_selection_for_update.redact_sensitive(
                value["restore_testing_selection"]
            )
        )
    return out
