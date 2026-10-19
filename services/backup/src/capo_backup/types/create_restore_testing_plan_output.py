"""Generated from Smithy shape ``com.amazonaws.backup#CreateRestoreTestingPlanOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime


class CreateRestoreTestingPlanOutput(TypedDict, closed=True):
    creation_time: "datetime.datetime"
    """<p>The date and time a restore testing plan was created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationTime</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087AM.</p>"""
    restore_testing_plan_arn: "str"
    """<p>An Amazon Resource Name (ARN) that uniquely identifies the created restore testing plan.</p>"""
    restore_testing_plan_name: "str"
    """<p>This unique string is the name of the restore testing plan.</p> <p>The name cannot be changed after creation. The name consists of only alphanumeric characters and underscores. Maximum length is 50.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRestoreTestingPlanOutput) -> dict:
    out: dict = {}
    import capo_backup.types._prelude.timestamp

    out["CreationTime"] = capo_backup.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    out["RestoreTestingPlanArn"] = value["restore_testing_plan_arn"]
    out["RestoreTestingPlanName"] = value["restore_testing_plan_name"]
    return out


def deserialize_json(data: dict) -> CreateRestoreTestingPlanOutput:
    out: CreateRestoreTestingPlanOutput = {}  # type: ignore[typeddict-item]
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
    return out
