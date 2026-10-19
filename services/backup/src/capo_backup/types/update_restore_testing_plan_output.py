"""Generated from Smithy shape ``com.amazonaws.backup#UpdateRestoreTestingPlanOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime


class UpdateRestoreTestingPlanOutput(TypedDict, closed=True):
    creation_time: "datetime.datetime"
    """<p>The time the resource testing plan was created.</p>"""
    restore_testing_plan_arn: "str"
    """<p>Unique ARN (Amazon Resource Name) of the restore testing plan.</p>"""
    restore_testing_plan_name: "str"
    """<p>The name cannot be changed after creation. The name consists of only alphanumeric characters and underscores. Maximum length is 50.</p>"""
    update_time: "datetime.datetime"
    """<p>The time the update completed for the restore testing plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRestoreTestingPlanOutput) -> dict:
    out: dict = {}
    import capo_backup.types._prelude.timestamp

    out["CreationTime"] = capo_backup.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    out["RestoreTestingPlanArn"] = value["restore_testing_plan_arn"]
    out["RestoreTestingPlanName"] = value["restore_testing_plan_name"]
    import capo_backup.types._prelude.timestamp

    out["UpdateTime"] = capo_backup.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> UpdateRestoreTestingPlanOutput:
    out: UpdateRestoreTestingPlanOutput = {}  # type: ignore[typeddict-item]
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
