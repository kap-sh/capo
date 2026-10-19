"""Generated from Smithy shape ``com.amazonaws.backup#RestoreTestingSelectionForList``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_backup.types.integer


class RestoreTestingSelectionForList(TypedDict, closed=True):
    creation_time: "datetime.datetime"
    """<p>The date and time that a restore testing selection was created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationTime</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26,2018 12:11:30.087 AM.</p>"""
    iam_role_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the IAM role that Backup uses to create the target resource; for example: <code>arn:aws:iam::123456789012:role/S3Access</code>.</p>"""
    protected_resource_type: "str"
    """<p>The type of Amazon Web Services resource included in a restore testing selection; for example, an Amazon EBS volume or an Amazon RDS database.</p>"""
    restore_testing_plan_name: "str"
    """<p>Unique string that is the name of the restore testing plan.</p> <p>The name cannot be changed after creation. The name must consist of only alphanumeric characters and underscores. Maximum length is 50.</p>"""
    restore_testing_selection_name: "str"
    """<p>Unique name of a restore testing selection.</p> <p>The name consists of only alphanumeric characters and underscores. Maximum length is 50.</p>"""
    validation_window_hours: "capo_backup.types.integer.integer"
    """<p>This value represents the time, in hours, data is retained after a restore test so that optional validation can be completed.</p> <p>Accepted value is an integer between 0 and 168 (the hourly equivalent of seven days).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestoreTestingSelectionForList) -> dict:
    out: dict = {}
    import capo_backup.types._prelude.timestamp

    out["CreationTime"] = capo_backup.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    out["IamRoleArn"] = value["iam_role_arn"]
    out["ProtectedResourceType"] = value["protected_resource_type"]
    out["RestoreTestingPlanName"] = value["restore_testing_plan_name"]
    out["RestoreTestingSelectionName"] = value["restore_testing_selection_name"]
    out["ValidationWindowHours"] = value.get("validation_window_hours", 0)
    return out


def deserialize_json(data: dict) -> RestoreTestingSelectionForList:
    out: RestoreTestingSelectionForList = {}  # type: ignore[typeddict-item]
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
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
    else:
        out["iam_role_arn"] = ""
    if data.get("ProtectedResourceType") is not None:
        out["protected_resource_type"] = data["ProtectedResourceType"]
    else:
        out["protected_resource_type"] = ""
    if data.get("RestoreTestingPlanName") is not None:
        out["restore_testing_plan_name"] = data["RestoreTestingPlanName"]
    else:
        out["restore_testing_plan_name"] = ""
    if data.get("RestoreTestingSelectionName") is not None:
        out["restore_testing_selection_name"] = data["RestoreTestingSelectionName"]
    else:
        out["restore_testing_selection_name"] = ""
    if data.get("ValidationWindowHours") is not None:
        out["validation_window_hours"] = data["ValidationWindowHours"]
    else:
        out["validation_window_hours"] = 0
    return out
