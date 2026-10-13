"""Generated from Smithy shape ``com.amazonaws.backup#GetRestoreTestingSelectionOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_backup.errors import DeserializationError

if TYPE_CHECKING:
    import capo_backup.types.restore_testing_selection_for_get


class GetRestoreTestingSelectionOutput(TypedDict, closed=True):
    restore_testing_selection: "capo_backup.types.restore_testing_selection_for_get.RestoreTestingSelectionForGet"
    """<p>Unique name of the restore testing selection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRestoreTestingSelectionOutput) -> dict:
    out: dict = {}
    import capo_backup.types.restore_testing_selection_for_get

    out["RestoreTestingSelection"] = (
        capo_backup.types.restore_testing_selection_for_get.serialize_json(
            value["restore_testing_selection"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetRestoreTestingSelectionOutput:
    out: GetRestoreTestingSelectionOutput = {}  # type: ignore[typeddict-item]
    if data.get("RestoreTestingSelection") is not None:
        import capo_backup.types.restore_testing_selection_for_get

        out["restore_testing_selection"] = (
            capo_backup.types.restore_testing_selection_for_get.deserialize_json(
                data["RestoreTestingSelection"]
            )
        )
    else:
        raise DeserializationError(
            "GetRestoreTestingSelectionOutput.restore_testing_selection required"
        )
    return out


def redact_sensitive(value: GetRestoreTestingSelectionOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "restore_testing_selection" in value:
        import capo_backup.types.restore_testing_selection_for_get

        out["restore_testing_selection"] = (
            capo_backup.types.restore_testing_selection_for_get.redact_sensitive(
                value["restore_testing_selection"]
            )
        )
    return out
