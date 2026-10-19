"""Generated from Smithy shape ``com.amazonaws.backup#CreateRestoreTestingSelectionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime


class CreateRestoreTestingSelectionOutput(TypedDict, closed=True):
    creation_time: "datetime.datetime"
    """<p>The time that the resource testing selection was created.</p>"""
    restore_testing_plan_arn: "str"
    """<p>The ARN of the restore testing plan with which the restore testing selection is associated.</p>"""
    restore_testing_plan_name: "str"
    """<p>The name of the restore testing plan.</p> <p>The name cannot be changed after creation. The name consists of only alphanumeric characters and underscores. Maximum length is 50.</p>"""
    restore_testing_selection_name: "str"
    """<p>The name of the restore testing selection for the related restore testing plan.</p> <p>The name cannot be changed after creation. The name consists of only alphanumeric characters and underscores. Maximum length is 50.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRestoreTestingSelectionOutput) -> dict:
    out: dict = {}
    import capo_backup.types._prelude.timestamp

    out["CreationTime"] = capo_backup.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    out["RestoreTestingPlanArn"] = value["restore_testing_plan_arn"]
    out["RestoreTestingPlanName"] = value["restore_testing_plan_name"]
    out["RestoreTestingSelectionName"] = value["restore_testing_selection_name"]
    return out


def deserialize_json(data: dict) -> CreateRestoreTestingSelectionOutput:
    out: CreateRestoreTestingSelectionOutput = {}  # type: ignore[typeddict-item]
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
    return out
