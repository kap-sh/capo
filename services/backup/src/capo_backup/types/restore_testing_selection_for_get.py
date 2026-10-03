"""Generated from Smithy shape ``com.amazonaws.backup#RestoreTestingSelectionForGet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_backup.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_backup.types.integer
    import capo_backup.types.protected_resource_conditions
    import capo_backup.types.sensitive_string_map
    import capo_backup.types.string_list


class RestoreTestingSelectionForGet(TypedDict, closed=True):
    creation_time: "datetime.datetime"
    """<p>The date and time that a restore testing selection was created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationTime</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 201812:11:30.087 AM.</p>"""
    creator_request_id: NotRequired["str"]
    """<p>This identifies the request and allows failed requests to be retried without the risk of running the operation twice. If the request includes a <code>CreatorRequestId</code> that matches an existing backup plan, that plan is returned. This parameter is optional.</p> <p>If used, this parameter must contain 1 to 50 alphanumeric or '-_.' characters.</p>"""
    iam_role_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the IAM role that Backup uses to create the target resource; for example:<code>arn:aws:iam::123456789012:role/S3Access</code>.</p>"""
    protected_resource_arns: NotRequired["capo_backup.types.string_list.stringList"]
    """<p>You can include specific ARNs, such as <code>ProtectedResourceArns: ["arn:aws:...", "arn:aws:..."]</code> or you can include a wildcard: <code>ProtectedResourceArns: ["*"]</code>, but not both.</p>"""
    protected_resource_conditions: NotRequired[
        "capo_backup.types.protected_resource_conditions.ProtectedResourceConditions"
    ]
    """<p>In a resource testing selection, this parameter filters by specific conditions such as <code>StringEquals</code> or <code>StringNotEquals</code>.</p>"""
    protected_resource_type: "str"
    """<p>The type of Amazon Web Services resource included in a resource testing selection; for example, an Amazon EBS volume or an Amazon RDS database.</p>"""
    restore_metadata_overrides: NotRequired[
        "capo_backup.types.sensitive_string_map.SensitiveStringMap"
    ]
    """<p>You can override certain restore metadata keys by including the parameter <code>RestoreMetadataOverrides</code> in the body of <code>RestoreTestingSelection</code>. Key values are not case sensitive.</p> <p>See the complete list of <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing-inferred-metadata.html">restore testing inferred metadata</a>.</p>"""
    restore_testing_plan_name: "str"
    """<p>The RestoreTestingPlanName is a unique string that is the name of the restore testing plan.</p>"""
    restore_testing_selection_name: "str"
    """<p>The unique name of the restore testing selection that belongs to the related restore testing plan.</p> <p>The name consists of only alphanumeric characters and underscores. Maximum length is 50.</p>"""
    validation_window_hours: "capo_backup.types.integer.integer"
    """<p>This is amount of hours (1 to 168) available to run a validation script on the data. The data will be deleted upon the completion of the validation script or the end of the specified retention period, whichever comes first.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestoreTestingSelectionForGet) -> dict:
    out: dict = {}
    import capo_backup.types._prelude.timestamp

    out["CreationTime"] = capo_backup.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    out["IamRoleArn"] = value["iam_role_arn"]
    if "protected_resource_arns" in value:
        import capo_backup.types.string_list

        out["ProtectedResourceArns"] = capo_backup.types.string_list.serialize_json(
            value["protected_resource_arns"]
        )
    if "protected_resource_conditions" in value:
        import capo_backup.types.protected_resource_conditions

        out["ProtectedResourceConditions"] = (
            capo_backup.types.protected_resource_conditions.serialize_json(
                value["protected_resource_conditions"]
            )
        )
    out["ProtectedResourceType"] = value["protected_resource_type"]
    if "restore_metadata_overrides" in value:
        import capo_backup.types.sensitive_string_map

        out["RestoreMetadataOverrides"] = (
            capo_backup.types.sensitive_string_map.serialize_json(
                value["restore_metadata_overrides"]
            )
        )
    out["RestoreTestingPlanName"] = value["restore_testing_plan_name"]
    out["RestoreTestingSelectionName"] = value["restore_testing_selection_name"]
    out["ValidationWindowHours"] = value.get("validation_window_hours", 0)
    return out


def deserialize_json(data: dict) -> RestoreTestingSelectionForGet:
    out: RestoreTestingSelectionForGet = {}  # type: ignore[typeddict-item]
    if data.get("CreationTime") is not None:
        import capo_backup.types._prelude.timestamp

        out["creation_time"] = capo_backup.types._prelude.timestamp.deserialize_json(
            data["CreationTime"]
        )
    else:
        raise DeserializationError(
            "RestoreTestingSelectionForGet.creation_time required"
        )
    if data.get("CreatorRequestId") is not None:
        out["creator_request_id"] = data["CreatorRequestId"]
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
    else:
        raise DeserializationError(
            "RestoreTestingSelectionForGet.iam_role_arn required"
        )
    if data.get("ProtectedResourceArns") is not None:
        import capo_backup.types.string_list

        out["protected_resource_arns"] = capo_backup.types.string_list.deserialize_json(
            data["ProtectedResourceArns"]
        )
    if data.get("ProtectedResourceConditions") is not None:
        import capo_backup.types.protected_resource_conditions

        out["protected_resource_conditions"] = (
            capo_backup.types.protected_resource_conditions.deserialize_json(
                data["ProtectedResourceConditions"]
            )
        )
    if data.get("ProtectedResourceType") is not None:
        out["protected_resource_type"] = data["ProtectedResourceType"]
    else:
        raise DeserializationError(
            "RestoreTestingSelectionForGet.protected_resource_type required"
        )
    if data.get("RestoreMetadataOverrides") is not None:
        import capo_backup.types.sensitive_string_map

        out["restore_metadata_overrides"] = (
            capo_backup.types.sensitive_string_map.deserialize_json(
                data["RestoreMetadataOverrides"]
            )
        )
    if data.get("RestoreTestingPlanName") is not None:
        out["restore_testing_plan_name"] = data["RestoreTestingPlanName"]
    else:
        raise DeserializationError(
            "RestoreTestingSelectionForGet.restore_testing_plan_name required"
        )
    if data.get("RestoreTestingSelectionName") is not None:
        out["restore_testing_selection_name"] = data["RestoreTestingSelectionName"]
    else:
        raise DeserializationError(
            "RestoreTestingSelectionForGet.restore_testing_selection_name required"
        )
    if data.get("ValidationWindowHours") is not None:
        out["validation_window_hours"] = data["ValidationWindowHours"]
    else:
        out["validation_window_hours"] = 0
    return out
