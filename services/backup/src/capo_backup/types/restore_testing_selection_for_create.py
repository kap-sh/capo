"""Generated from Smithy shape ``com.amazonaws.backup#RestoreTestingSelectionForCreate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_backup.errors import DeserializationError

if TYPE_CHECKING:
    import capo_backup.types.integer
    import capo_backup.types.protected_resource_conditions
    import capo_backup.types.sensitive_string_map
    import capo_backup.types.string_list


class RestoreTestingSelectionForCreate(TypedDict, closed=True):
    iam_role_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the IAM role that Backup uses to create the target resource; for example: <code>arn:aws:iam::123456789012:role/S3Access</code>. </p>"""
    protected_resource_arns: NotRequired["capo_backup.types.string_list.stringList"]
    """<p>Each protected resource can be filtered by its specific ARNs, such as <code>ProtectedResourceArns: ["arn:aws:...", "arn:aws:..."]</code> or by a wildcard: <code>ProtectedResourceArns: ["*"]</code>, but not both.</p>"""
    protected_resource_conditions: NotRequired[
        "capo_backup.types.protected_resource_conditions.ProtectedResourceConditions"
    ]
    """<p>If you have included the wildcard in ProtectedResourceArns, you can include resource conditions, such as <code>ProtectedResourceConditions: { StringEquals: [{ key: "XXXX", value: "YYYY" }]</code>.</p>"""
    protected_resource_type: "str"
    """<p>The type of Amazon Web Services resource included in a restore testing selection; for example, an Amazon EBS volume or an Amazon RDS database.</p> <p>Supported resource types accepted include:</p> <ul> <li> <p> <code>Aurora</code> for Amazon Aurora</p> </li> <li> <p> <code>DocumentDB</code> for Amazon DocumentDB (with MongoDB compatibility)</p> </li> <li> <p> <code>DynamoDB</code> for Amazon DynamoDB</p> </li> <li> <p> <code>EBS</code> for Amazon Elastic Block Store</p> </li> <li> <p> <code>EC2</code> for Amazon Elastic Compute Cloud</p> </li> <li> <p> <code>EFS</code> for Amazon Elastic File System</p> </li> <li> <p> <code>FSx</code> for Amazon FSx</p> </li> <li> <p> <code>Neptune</code> for Amazon Neptune</p> </li> <li> <p> <code>RDS</code> for Amazon Relational Database Service</p> </li> <li> <p> <code>S3</code> for Amazon S3</p> </li> </ul>"""
    restore_metadata_overrides: NotRequired[
        "capo_backup.types.sensitive_string_map.SensitiveStringMap"
    ]
    """<p>You can override certain restore metadata keys by including the parameter <code>RestoreMetadataOverrides</code> in the body of <code>RestoreTestingSelection</code>. Key values are not case sensitive.</p> <p>See the complete list of <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing-inferred-metadata.html">restore testing inferred metadata</a>.</p>"""
    restore_testing_selection_name: "str"
    """<p>The unique name of the restore testing selection that belongs to the related restore testing plan.</p> <p>The name consists of only alphanumeric characters and underscores. Maximum length is 50.</p>"""
    validation_window_hours: "capo_backup.types.integer.integer"
    """<p>This is amount of hours (0 to 168) available to run a validation script on the data. The data will be deleted upon the completion of the validation script or the end of the specified retention period, whichever comes first.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestoreTestingSelectionForCreate) -> dict:
    out: dict = {}
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
    out["RestoreTestingSelectionName"] = value["restore_testing_selection_name"]
    out["ValidationWindowHours"] = value.get("validation_window_hours", 0)
    return out


def deserialize_json(data: dict) -> RestoreTestingSelectionForCreate:
    out: RestoreTestingSelectionForCreate = {}  # type: ignore[typeddict-item]
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
    else:
        raise DeserializationError(
            "RestoreTestingSelectionForCreate.iam_role_arn required"
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
            "RestoreTestingSelectionForCreate.protected_resource_type required"
        )
    if data.get("RestoreMetadataOverrides") is not None:
        import capo_backup.types.sensitive_string_map

        out["restore_metadata_overrides"] = (
            capo_backup.types.sensitive_string_map.deserialize_json(
                data["RestoreMetadataOverrides"]
            )
        )
    if data.get("RestoreTestingSelectionName") is not None:
        out["restore_testing_selection_name"] = data["RestoreTestingSelectionName"]
    else:
        raise DeserializationError(
            "RestoreTestingSelectionForCreate.restore_testing_selection_name required"
        )
    if data.get("ValidationWindowHours") is not None:
        out["validation_window_hours"] = data["ValidationWindowHours"]
    else:
        out["validation_window_hours"] = 0
    return out
