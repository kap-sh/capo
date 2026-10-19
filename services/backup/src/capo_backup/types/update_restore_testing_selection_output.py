"""Generated from Smithy shape ``com.amazonaws.backup#UpdateRestoreTestingSelectionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime


class UpdateRestoreTestingSelectionOutput(TypedDict, closed=True):
    creation_time: "datetime.datetime"
    """<p>The time the resource testing selection was updated successfully.</p>"""
    restore_testing_plan_arn: "str"
    """<p>Unique string that is the name of the restore testing plan.</p>"""
    restore_testing_plan_name: "str"
    """<p>The restore testing plan with which the updated restore testing selection is associated.</p>"""
    restore_testing_selection_name: "str"
    """<p>The returned restore testing selection name.</p>"""
    update_time: "datetime.datetime"
    """<p>The time the update completed for the restore testing selection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRestoreTestingSelectionOutput) -> dict:
    out: dict = {}
    import capo_backup.types._prelude.timestamp

    out["CreationTime"] = capo_backup.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    out["RestoreTestingPlanArn"] = value["restore_testing_plan_arn"]
    out["RestoreTestingPlanName"] = value["restore_testing_plan_name"]
    out["RestoreTestingSelectionName"] = value["restore_testing_selection_name"]
    import capo_backup.types._prelude.timestamp

    out["UpdateTime"] = capo_backup.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> UpdateRestoreTestingSelectionOutput:
    out: UpdateRestoreTestingSelectionOutput = {}  # type: ignore[typeddict-item]
    if data.get("CreationTime") is not None:
        import capo_backup.types._prelude.timestamp

        out["creation_time"] = capo_backup.types._prelude.timestamp.deserialize_json(
            data["CreationTime"]
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("RestoreTestingPlanArn") is not None:
        out["restore_testing_plan_arn"] = data["RestoreTestingPlanArn"]
    else:
        out["restore_testing_plan_arn"] = ""
    if data.get("RestoreTestingPlanName") is not None:
        out["restore_testing_plan_name"] = data["RestoreTestingPlanName"]
    else:
        out["restore_testing_plan_name"] = ""
    if data.get("RestoreTestingSelectionName") is not None:
        out["restore_testing_selection_name"] = data["RestoreTestingSelectionName"]
    else:
        out["restore_testing_selection_name"] = ""
    if data.get("UpdateTime") is not None:
        import capo_backup.types._prelude.timestamp

        out["update_time"] = capo_backup.types._prelude.timestamp.deserialize_json(
            data["UpdateTime"]
        )
    else:
        import datetime

        out["update_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
