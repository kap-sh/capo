"""Generated from Smithy shape ``com.amazonaws.ssm#CreateOpsItemRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.date_time
    import capo_ssm.types.ops_item_account_id
    import capo_ssm.types.ops_item_category
    import capo_ssm.types.ops_item_description
    import capo_ssm.types.ops_item_notifications
    import capo_ssm.types.ops_item_operational_data
    import capo_ssm.types.ops_item_priority
    import capo_ssm.types.ops_item_severity
    import capo_ssm.types.ops_item_source
    import capo_ssm.types.ops_item_title
    import capo_ssm.types.ops_item_type
    import capo_ssm.types.related_ops_items
    import capo_ssm.types.tag_list


class CreateOpsItemRequest(TypedDict, closed=True):
    description: "capo_ssm.types.ops_item_description.OpsItemDescription"
    """<p>User-defined text that contains information about the OpsItem, in Markdown format. </p> <note> <p>Provide enough information so that users viewing this OpsItem for the first time understand the issue. </p> </note>"""
    ops_item_type: NotRequired["capo_ssm.types.ops_item_type.OpsItemType"]
    """<p>The type of OpsItem to create. Systems Manager supports the following types of OpsItems:</p> <ul> <li> <p> <code>/aws/issue</code> </p> <p>This type of OpsItem is used for default OpsItems created by OpsCenter. </p> </li> <li> <p> <code>/aws/insight</code> </p> <p>This type of OpsItem is used by OpsCenter for aggregating and reporting on duplicate OpsItems. </p> </li> <li> <p> <code>/aws/changerequest</code> </p> <p>This type of OpsItem is used by Change Manager for reviewing and approving or rejecting change requests. </p> <important> <p>Amazon Web Services Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager-availability-change.html">Amazon Web Services Systems Manager Change Manager availability change</a>.</p> </important> </li> </ul>"""
    operational_data: NotRequired[
        "capo_ssm.types.ops_item_operational_data.OpsItemOperationalData"
    ]
    """<p>Operational data is custom data that provides useful reference details about the OpsItem. For example, you can specify log files, error strings, license keys, troubleshooting tips, or other relevant data. You enter operational data as key-value pairs. The key has a maximum length of 128 characters. The value has a maximum size of 20 KB.</p> <important> <p>Operational data keys <i>can't</i> begin with the following: <code>amazon</code>, <code>aws</code>, <code>amzn</code>, <code>ssm</code>, <code>/amazon</code>, <code>/aws</code>, <code>/amzn</code>, <code>/ssm</code>.</p> </important> <p>You can choose to make the data searchable by other users in the account or you can restrict search access. Searchable data means that all users with access to the OpsItem Overview page (as provided by the <a>DescribeOpsItems</a> API operation) can view and search on the specified data. Operational data that isn't searchable is only viewable by users who have access to the OpsItem (as provided by the <a>GetOpsItem</a> API operation).</p> <p>Use the <code>/aws/resources</code> key in OperationalData to specify a related resource in the request. Use the <code>/aws/automations</code> key in OperationalData to associate an Automation runbook with the OpsItem. To view Amazon Web Services CLI example commands that use these keys, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-manually-create-OpsItems.html">Create OpsItems manually</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    notifications: NotRequired[
        "capo_ssm.types.ops_item_notifications.OpsItemNotifications"
    ]
    """<p>The Amazon Resource Name (ARN) of an SNS topic where notifications are sent when this OpsItem is edited or changed.</p>"""
    priority: NotRequired["capo_ssm.types.ops_item_priority.OpsItemPriority"]
    """<p>The importance of this OpsItem in relation to other OpsItems in the system.</p>"""
    related_ops_items: NotRequired["capo_ssm.types.related_ops_items.RelatedOpsItems"]
    """<p>One or more OpsItems that share something in common with the current OpsItems. For example, related OpsItems can include OpsItems with similar error messages, impacted resources, or statuses for the impacted resource.</p>"""
    source: "capo_ssm.types.ops_item_source.OpsItemSource"
    """<p>The origin of the OpsItem, such as Amazon EC2 or Systems Manager.</p> <note> <p>The source name can't contain the following strings: <code>aws</code>, <code>amazon</code>, and <code>amzn</code>. </p> </note>"""
    title: "capo_ssm.types.ops_item_title.OpsItemTitle"
    """<p>A short heading that describes the nature of the OpsItem and the impacted resource.</p>"""
    tags: NotRequired["capo_ssm.types.tag_list.TagList"]
    """<p>Optional metadata that you assign to a resource.</p> <p>Tags use a key-value pair. For example:</p> <p> <code>Key=Department,Value=Finance</code> </p> <important> <p>To add tags to a new OpsItem, a user must have IAM permissions for both the <code>ssm:CreateOpsItems</code> operation and the <code>ssm:AddTagsToResource</code> operation. To add tags to an existing OpsItem, use the <a>AddTagsToResource</a> operation.</p> </important>"""
    category: NotRequired["capo_ssm.types.ops_item_category.OpsItemCategory"]
    """<p>Specify a category to assign to an OpsItem. </p>"""
    severity: NotRequired["capo_ssm.types.ops_item_severity.OpsItemSeverity"]
    """<p>Specify a severity to assign to an OpsItem.</p>"""
    actual_start_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The time a runbook workflow started. Currently reported only for the OpsItem type <code>/aws/changerequest</code>.</p>"""
    actual_end_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The time a runbook workflow ended. Currently reported only for the OpsItem type <code>/aws/changerequest</code>.</p>"""
    planned_start_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The time specified in a change request for a runbook workflow to start. Currently supported only for the OpsItem type <code>/aws/changerequest</code>.</p>"""
    planned_end_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The time specified in a change request for a runbook workflow to end. Currently supported only for the OpsItem type <code>/aws/changerequest</code>.</p>"""
    account_id: NotRequired["capo_ssm.types.ops_item_account_id.OpsItemAccountId"]
    """<p>The target Amazon Web Services account where you want to create an OpsItem. To make this call, your account must be configured to work with OpsItems across accounts. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-setup.html">Set up OpsCenter</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateOpsItemRequest) -> dict:
    out: dict = {}
    out["Description"] = value["description"]
    if "ops_item_type" in value:
        out["OpsItemType"] = value["ops_item_type"]
    if "operational_data" in value:
        import capo_ssm.types.ops_item_operational_data

        out["OperationalData"] = (
            capo_ssm.types.ops_item_operational_data.serialize_aws_json_1_1(
                value["operational_data"]
            )
        )
    if "notifications" in value:
        import capo_ssm.types.ops_item_notifications

        out["Notifications"] = (
            capo_ssm.types.ops_item_notifications.serialize_aws_json_1_1(
                value["notifications"]
            )
        )
    if "priority" in value:
        out["Priority"] = value["priority"]
    if "related_ops_items" in value:
        import capo_ssm.types.related_ops_items

        out["RelatedOpsItems"] = (
            capo_ssm.types.related_ops_items.serialize_aws_json_1_1(
                value["related_ops_items"]
            )
        )
    out["Source"] = value["source"]
    out["Title"] = value["title"]
    if "tags" in value:
        import capo_ssm.types.tag_list

        out["Tags"] = capo_ssm.types.tag_list.serialize_aws_json_1_1(value["tags"])
    if "category" in value:
        out["Category"] = value["category"]
    if "severity" in value:
        out["Severity"] = value["severity"]
    if "actual_start_time" in value:
        import capo_ssm.types.date_time

        out["ActualStartTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["actual_start_time"]
        )
    if "actual_end_time" in value:
        import capo_ssm.types.date_time

        out["ActualEndTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["actual_end_time"]
        )
    if "planned_start_time" in value:
        import capo_ssm.types.date_time

        out["PlannedStartTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["planned_start_time"]
        )
    if "planned_end_time" in value:
        import capo_ssm.types.date_time

        out["PlannedEndTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["planned_end_time"]
        )
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateOpsItemRequest:
    out: CreateOpsItemRequest = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("CreateOpsItemRequest.description required")
    if data.get("OpsItemType") is not None:
        out["ops_item_type"] = data["OpsItemType"]
    if data.get("OperationalData") is not None:
        import capo_ssm.types.ops_item_operational_data

        out["operational_data"] = (
            capo_ssm.types.ops_item_operational_data.deserialize_aws_json_1_1(
                data["OperationalData"]
            )
        )
    if data.get("Notifications") is not None:
        import capo_ssm.types.ops_item_notifications

        out["notifications"] = (
            capo_ssm.types.ops_item_notifications.deserialize_aws_json_1_1(
                data["Notifications"]
            )
        )
    if data.get("Priority") is not None:
        out["priority"] = data["Priority"]
    if data.get("RelatedOpsItems") is not None:
        import capo_ssm.types.related_ops_items

        out["related_ops_items"] = (
            capo_ssm.types.related_ops_items.deserialize_aws_json_1_1(
                data["RelatedOpsItems"]
            )
        )
    if data.get("Source") is not None:
        out["source"] = data["Source"]
    else:
        raise DeserializationError("CreateOpsItemRequest.source required")
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    else:
        raise DeserializationError("CreateOpsItemRequest.title required")
    if data.get("Tags") is not None:
        import capo_ssm.types.tag_list

        out["tags"] = capo_ssm.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    if data.get("Category") is not None:
        out["category"] = data["Category"]
    if data.get("Severity") is not None:
        out["severity"] = data["Severity"]
    if data.get("ActualStartTime") is not None:
        import capo_ssm.types.date_time

        out["actual_start_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["ActualStartTime"]
        )
    if data.get("ActualEndTime") is not None:
        import capo_ssm.types.date_time

        out["actual_end_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["ActualEndTime"]
        )
    if data.get("PlannedStartTime") is not None:
        import capo_ssm.types.date_time

        out["planned_start_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["PlannedStartTime"]
        )
    if data.get("PlannedEndTime") is not None:
        import capo_ssm.types.date_time

        out["planned_end_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["PlannedEndTime"]
        )
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    return out
