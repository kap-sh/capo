"""Generated from Smithy shape ``com.amazonaws.backup#RestoreTestingSelectionForUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.integer
    import capo_backup.types.protected_resource_conditions
    import capo_backup.types.sensitive_string_map
    import capo_backup.types.string_list


class RestoreTestingSelectionForUpdate(TypedDict, closed=True):
    iam_role_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that Backup uses to create the target resource; for example: <code>arn:aws:iam::123456789012:role/S3Access</code>.</p>"""
    protected_resource_arns: NotRequired["capo_backup.types.string_list.stringList"]
    """<p>You can include a list of specific ARNs, such as <code>ProtectedResourceArns: ["arn:aws:...", "arn:aws:..."]</code> or you can include a wildcard: <code>ProtectedResourceArns: ["*"]</code>, but not both.</p>"""
    protected_resource_conditions: NotRequired[
        "capo_backup.types.protected_resource_conditions.ProtectedResourceConditions"
    ]
    """<p>The conditions that you define for resources in your restore testing plan using tags.</p>"""
    restore_metadata_overrides: NotRequired[
        "capo_backup.types.sensitive_string_map.SensitiveStringMap"
    ]
    """<p>You can override certain restore metadata keys by including the parameter <code>RestoreMetadataOverrides</code> in the body of <code>RestoreTestingSelection</code>. Key values are not case sensitive.</p> <p>See the complete list of <a href="https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing-inferred-metadata.html">restore testing inferred metadata</a>.</p>"""
    validation_window_hours: "capo_backup.types.integer.integer"
    """<p>This value represents the time, in hours, data is retained after a restore test so that optional validation can be completed.</p> <p>Accepted value is an integer between 0 and 168 (the hourly equivalent of seven days).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestoreTestingSelectionForUpdate) -> dict:
    out: dict = {}
    if "iam_role_arn" in value:
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
    if "restore_metadata_overrides" in value:
        import capo_backup.types.sensitive_string_map

        out["RestoreMetadataOverrides"] = (
            capo_backup.types.sensitive_string_map.serialize_json(
                value["restore_metadata_overrides"]
            )
        )
    out["ValidationWindowHours"] = value.get("validation_window_hours", 0)
    return out


def deserialize_json(data: dict) -> RestoreTestingSelectionForUpdate:
    out: RestoreTestingSelectionForUpdate = {}  # type: ignore[typeddict-item]
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
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
    if data.get("RestoreMetadataOverrides") is not None:
        import capo_backup.types.sensitive_string_map

        out["restore_metadata_overrides"] = (
            capo_backup.types.sensitive_string_map.deserialize_json(
                data["RestoreMetadataOverrides"]
            )
        )
    if data.get("ValidationWindowHours") is not None:
        out["validation_window_hours"] = data["ValidationWindowHours"]
    else:
        out["validation_window_hours"] = 0
    return out
