"""Generated from Smithy shape ``com.amazonaws.backup#BackupSelection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_backup.errors import DeserializationError

if TYPE_CHECKING:
    import capo_backup.types.backup_selection_name
    import capo_backup.types.conditions
    import capo_backup.types.iam_role_arn
    import capo_backup.types.list_of_tags
    import capo_backup.types.resource_arns


class BackupSelection(TypedDict, closed=True):
    selection_name: "capo_backup.types.backup_selection_name.BackupSelectionName"
    """<p>The display name of a resource selection document. Must contain 1 to 50 alphanumeric or '-_.' characters.</p>"""
    iam_role_arn: "capo_backup.types.iam_role_arn.IAMRoleArn"
    """<p>The ARN of the IAM role that Backup uses to authenticate when backing up the target resource; for example, <code>arn:aws:iam::123456789012:role/S3Access</code>.</p>"""
    resources: NotRequired["capo_backup.types.resource_arns.ResourceArns"]
    """<p>The Amazon Resource Names (ARNs) of the resources to assign to a backup plan. The maximum number of ARNs is 500 without wildcards, or 30 ARNs with wildcards.</p> <p>If you need to assign many resources to a backup plan, consider a different resource selection strategy, such as assigning all resources of a resource type or refining your resource selection using tags.</p> <p>If you specify multiple ARNs, the resources much match any of the ARNs (OR logic).</p> <note> <p>When using wildcards in ARN patterns for backup selections, the asterisk (*) must appear at the end of the ARN string (prefix pattern). For example, <code>arn:aws:s3:::my-bucket-*</code> is valid, but <code>arn:aws:s3:::*-logs</code> is not supported.</p> </note>"""
    list_of_tags: NotRequired["capo_backup.types.list_of_tags.ListOfTags"]
    """<p>The conditions that you define to assign resources to your backup plans using tags. For example, <code>"StringEquals": { "ConditionKey": "backup", "ConditionValue": "daily"}</code>.</p> <p> <code>ListOfTags</code> supports only <code>StringEquals</code>. Condition operators are case sensitive.</p> <p>If you specify multiple conditions, the resources much match any of the conditions (OR logic).</p>"""
    not_resources: NotRequired["capo_backup.types.resource_arns.ResourceArns"]
    """<p>The Amazon Resource Names (ARNs) of the resources to exclude from a backup plan. The maximum number of ARNs is 500 without wildcards, or 30 ARNs with wildcards.</p> <p>If you need to exclude many resources from a backup plan, consider a different resource selection strategy, such as assigning only one or a few resource types or refining your resource selection using tags.</p>"""
    conditions: NotRequired["capo_backup.types.conditions.Conditions"]
    """<p>The conditions that you define to assign resources to your backup plans using tags. For example, <code>"StringEquals": { "ConditionKey": "aws:ResourceTag/backup", "ConditionValue": "daily" }</code>.</p> <p> <code>Conditions</code> supports <code>StringEquals</code>, <code>StringLike</code>, <code>StringNotEquals</code>, and <code>StringNotLike</code>. Condition operators are case sensitive.</p> <p>If you specify multiple conditions, the resources much match all conditions (AND logic).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BackupSelection) -> dict:
    out: dict = {}
    out["SelectionName"] = value["selection_name"]
    out["IamRoleArn"] = value["iam_role_arn"]
    if "resources" in value:
        import capo_backup.types.resource_arns

        out["Resources"] = capo_backup.types.resource_arns.serialize_json(
            value["resources"]
        )
    if "list_of_tags" in value:
        import capo_backup.types.list_of_tags

        out["ListOfTags"] = capo_backup.types.list_of_tags.serialize_json(
            value["list_of_tags"]
        )
    if "not_resources" in value:
        import capo_backup.types.resource_arns

        out["NotResources"] = capo_backup.types.resource_arns.serialize_json(
            value["not_resources"]
        )
    if "conditions" in value:
        import capo_backup.types.conditions

        out["Conditions"] = capo_backup.types.conditions.serialize_json(
            value["conditions"]
        )
    return out


def deserialize_json(data: dict) -> BackupSelection:
    out: BackupSelection = {}  # type: ignore[typeddict-item]
    if data.get("SelectionName") is not None:
        out["selection_name"] = data["SelectionName"]
    else:
        raise DeserializationError("BackupSelection.selection_name required")
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
    else:
        raise DeserializationError("BackupSelection.iam_role_arn required")
    if data.get("Resources") is not None:
        import capo_backup.types.resource_arns

        out["resources"] = capo_backup.types.resource_arns.deserialize_json(
            data["Resources"]
        )
    if data.get("ListOfTags") is not None:
        import capo_backup.types.list_of_tags

        out["list_of_tags"] = capo_backup.types.list_of_tags.deserialize_json(
            data["ListOfTags"]
        )
    if data.get("NotResources") is not None:
        import capo_backup.types.resource_arns

        out["not_resources"] = capo_backup.types.resource_arns.deserialize_json(
            data["NotResources"]
        )
    if data.get("Conditions") is not None:
        import capo_backup.types.conditions

        out["conditions"] = capo_backup.types.conditions.deserialize_json(
            data["Conditions"]
        )
    return out
