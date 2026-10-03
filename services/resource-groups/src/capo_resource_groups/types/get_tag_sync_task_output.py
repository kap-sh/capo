"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GetTagSyncTaskOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups.types.error_message
    import capo_resource_groups.types.group_arn_v2
    import capo_resource_groups.types.group_name
    import capo_resource_groups.types.resource_query
    import capo_resource_groups.types.role_arn
    import capo_resource_groups.types.tag_key
    import capo_resource_groups.types.tag_sync_task_arn
    import capo_resource_groups.types.tag_sync_task_status
    import capo_resource_groups.types.tag_value
    import capo_resource_groups.types.timestamp


class GetTagSyncTaskOutput(TypedDict, closed=True):
    group_arn: NotRequired["capo_resource_groups.types.group_arn_v2.GroupArnV2"]
    """<p>The Amazon resource name (ARN) of the application group. </p>"""
    group_name: NotRequired["capo_resource_groups.types.group_name.GroupName"]
    """<p>The name of the application group. </p>"""
    task_arn: NotRequired["capo_resource_groups.types.tag_sync_task_arn.TagSyncTaskArn"]
    """<p>The Amazon resource name (ARN) of the tag-sync task. </p>"""
    tag_key: NotRequired["capo_resource_groups.types.tag_key.TagKey"]
    """<p>The tag key. </p>"""
    tag_value: NotRequired["capo_resource_groups.types.tag_value.TagValue"]
    """<p>The tag value. </p>"""
    resource_query: NotRequired[
        "capo_resource_groups.types.resource_query.ResourceQuery"
    ]
    role_arn: NotRequired["capo_resource_groups.types.role_arn.RoleArn"]
    """<p>The Amazon resource name (ARN) of the role assumed by Resource Groups to tag and untag resources on your behalf. </p> <p>For more information about this role, review <a href="https://docs.aws.amazon.com/servicecatalog/latest/arguide/app-tag-sync.html#tag-sync-role">Tag-sync required permissions</a>. </p>"""
    status: NotRequired[
        "capo_resource_groups.types.tag_sync_task_status.TagSyncTaskStatus"
    ]
    """<p>The status of the tag-sync task. </p> <p>Valid values include:</p> <ul> <li> <p> <code>ACTIVE</code> - The tag-sync task is actively managing resources in the application by adding or removing the <code>awsApplication</code> tag from resources when they are tagged or untagged with the specified tag key-value pair. </p> </li> <li> <p> <code>ERROR</code> - The tag-sync task is not actively managing resources in the application. Review the <code>ErrorMessage</code> for more information about resolving the error. </p> </li> </ul>"""
    error_message: NotRequired["capo_resource_groups.types.error_message.ErrorMessage"]
    """<p>The specific error message in cases where the tag-sync task status is <code>ERROR</code>. </p>"""
    created_at: NotRequired["capo_resource_groups.types.timestamp.timestamp"]
    """<p>The timestamp of when the tag-sync task was created. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTagSyncTaskOutput) -> dict:
    out: dict = {}
    if "group_arn" in value:
        out["GroupArn"] = value["group_arn"]
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    if "task_arn" in value:
        out["TaskArn"] = value["task_arn"]
    if "tag_key" in value:
        out["TagKey"] = value["tag_key"]
    if "tag_value" in value:
        out["TagValue"] = value["tag_value"]
    if "resource_query" in value:
        import capo_resource_groups.types.resource_query

        out["ResourceQuery"] = capo_resource_groups.types.resource_query.serialize_json(
            value["resource_query"]
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "status" in value:
        import capo_resource_groups.types.tag_sync_task_status

        out["Status"] = capo_resource_groups.types.tag_sync_task_status.serialize_json(
            value["status"]
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "created_at" in value:
        import capo_resource_groups.types.timestamp

        out["CreatedAt"] = capo_resource_groups.types.timestamp.serialize_json(
            value["created_at"]
        )
    return out


def deserialize_json(data: dict) -> GetTagSyncTaskOutput:
    out: GetTagSyncTaskOutput = {}  # type: ignore[typeddict-item]
    if data.get("GroupArn") is not None:
        out["group_arn"] = data["GroupArn"]
    if data.get("GroupName") is not None:
        out["group_name"] = data["GroupName"]
    if data.get("TaskArn") is not None:
        out["task_arn"] = data["TaskArn"]
    if data.get("TagKey") is not None:
        out["tag_key"] = data["TagKey"]
    if data.get("TagValue") is not None:
        out["tag_value"] = data["TagValue"]
    if data.get("ResourceQuery") is not None:
        import capo_resource_groups.types.resource_query

        out["resource_query"] = (
            capo_resource_groups.types.resource_query.deserialize_json(
                data["ResourceQuery"]
            )
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("Status") is not None:
        import capo_resource_groups.types.tag_sync_task_status

        out["status"] = (
            capo_resource_groups.types.tag_sync_task_status.deserialize_json(
                data["Status"]
            )
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    if data.get("CreatedAt") is not None:
        import capo_resource_groups.types.timestamp

        out["created_at"] = capo_resource_groups.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    return out
