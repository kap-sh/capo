"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.date_time
    import capo_ssm.types.ops_item_arn
    import capo_ssm.types.ops_item_category
    import capo_ssm.types.ops_item_description
    import capo_ssm.types.ops_item_id
    import capo_ssm.types.ops_item_notifications
    import capo_ssm.types.ops_item_operational_data
    import capo_ssm.types.ops_item_priority
    import capo_ssm.types.ops_item_severity
    import capo_ssm.types.ops_item_source
    import capo_ssm.types.ops_item_status
    import capo_ssm.types.ops_item_title
    import capo_ssm.types.ops_item_type
    import capo_ssm.types.related_ops_items
    import capo_ssm.types.string


class OpsItem(TypedDict, closed=True):
    created_by: NotRequired["capo_ssm.types.string.String"]
    """<p>The ARN of the Amazon Web Services account that created the OpsItem.</p>"""
    ops_item_type: NotRequired["capo_ssm.types.ops_item_type.OpsItemType"]
    """<p>The type of OpsItem. Systems Manager supports the following types of OpsItems:</p> <ul> <li> <p> <code>/aws/issue</code> </p> <p>This type of OpsItem is used for default OpsItems created by OpsCenter. </p> </li> <li> <p> <code>/aws/changerequest</code> </p> <p>This type of OpsItem is used by Change Manager for reviewing and approving or rejecting change requests. </p> </li> <li> <p> <code>/aws/insight</code> </p> <p>This type of OpsItem is used by OpsCenter for aggregating and reporting on duplicate OpsItems. </p> </li> </ul>"""
    created_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date and time the OpsItem was created.</p>"""
    description: NotRequired["capo_ssm.types.ops_item_description.OpsItemDescription"]
    """<p>The OpsItem description.</p>"""
    last_modified_by: NotRequired["capo_ssm.types.string.String"]
    """<p>The ARN of the Amazon Web Services account that last updated the OpsItem.</p>"""
    last_modified_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date and time the OpsItem was last updated.</p>"""
    notifications: NotRequired[
        "capo_ssm.types.ops_item_notifications.OpsItemNotifications"
    ]
    """<p>The Amazon Resource Name (ARN) of an Amazon Simple Notification Service (Amazon SNS) topic where notifications are sent when this OpsItem is edited or changed.</p>"""
    priority: NotRequired["capo_ssm.types.ops_item_priority.OpsItemPriority"]
    """<p>The importance of this OpsItem in relation to other OpsItems in the system.</p>"""
    related_ops_items: NotRequired["capo_ssm.types.related_ops_items.RelatedOpsItems"]
    """<p>One or more OpsItems that share something in common with the current OpsItem. For example, related OpsItems can include OpsItems with similar error messages, impacted resources, or statuses for the impacted resource.</p>"""
    status: NotRequired["capo_ssm.types.ops_item_status.OpsItemStatus"]
    """<p>The OpsItem status. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-working-with-OpsItems-editing-details.html">Editing OpsItem details</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    ops_item_id: NotRequired["capo_ssm.types.ops_item_id.OpsItemId"]
    """<p>The ID of the OpsItem.</p>"""
    version: NotRequired["capo_ssm.types.string.String"]
    """<p>The version of this OpsItem. Each time the OpsItem is edited the version number increments by one.</p>"""
    title: NotRequired["capo_ssm.types.ops_item_title.OpsItemTitle"]
    """<p>A short heading that describes the nature of the OpsItem and the impacted resource.</p>"""
    source: NotRequired["capo_ssm.types.ops_item_source.OpsItemSource"]
    """<p>The origin of the OpsItem, such as Amazon EC2 or Systems Manager. The impacted resource is a subset of source.</p>"""
    operational_data: NotRequired[
        "capo_ssm.types.ops_item_operational_data.OpsItemOperationalData"
    ]
    """<p>Operational data is custom data that provides useful reference details about the OpsItem. For example, you can specify log files, error strings, license keys, troubleshooting tips, or other relevant data. You enter operational data as key-value pairs. The key has a maximum length of 128 characters. The value has a maximum size of 20 KB.</p> <important> <p>Operational data keys <i>can't</i> begin with the following: <code>amazon</code>, <code>aws</code>, <code>amzn</code>, <code>ssm</code>, <code>/amazon</code>, <code>/aws</code>, <code>/amzn</code>, <code>/ssm</code>.</p> </important> <p>You can choose to make the data searchable by other users in the account or you can restrict search access. Searchable data means that all users with access to the OpsItem Overview page (as provided by the <a>DescribeOpsItems</a> API operation) can view and search on the specified data. Operational data that isn't searchable is only viewable by users who have access to the OpsItem (as provided by the <a>GetOpsItem</a> API operation).</p> <p>Use the <code>/aws/resources</code> key in OperationalData to specify a related resource in the request. Use the <code>/aws/automations</code> key in OperationalData to associate an Automation runbook with the OpsItem. To view Amazon Web Services CLI example commands that use these keys, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-manually-create-OpsItems.html">Creating OpsItems manually</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    category: NotRequired["capo_ssm.types.ops_item_category.OpsItemCategory"]
    """<p>An OpsItem category. Category options include: Availability, Cost, Performance, Recovery, Security.</p>"""
    severity: NotRequired["capo_ssm.types.ops_item_severity.OpsItemSeverity"]
    """<p>The severity of the OpsItem. Severity options range from 1 to 4.</p>"""
    actual_start_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The time a runbook workflow started. Currently reported only for the OpsItem type <code>/aws/changerequest</code>.</p>"""
    actual_end_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The time a runbook workflow ended. Currently reported only for the OpsItem type <code>/aws/changerequest</code>.</p>"""
    planned_start_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The time specified in a change request for a runbook workflow to start. Currently supported only for the OpsItem type <code>/aws/changerequest</code>.</p>"""
    planned_end_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The time specified in a change request for a runbook workflow to end. Currently supported only for the OpsItem type <code>/aws/changerequest</code>.</p>"""
    ops_item_arn: NotRequired["capo_ssm.types.ops_item_arn.OpsItemArn"]
    """<p>The OpsItem Amazon Resource Name (ARN).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItem) -> dict:
    out: dict = {}
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "ops_item_type" in value:
        out["OpsItemType"] = value["ops_item_type"]
    if "created_time" in value:
        import capo_ssm.types.date_time

        out["CreatedTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["created_time"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "last_modified_by" in value:
        out["LastModifiedBy"] = value["last_modified_by"]
    if "last_modified_time" in value:
        import capo_ssm.types.date_time

        out["LastModifiedTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["last_modified_time"]
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
    if "status" in value:
        import capo_ssm.types.ops_item_status

        out["Status"] = capo_ssm.types.ops_item_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "ops_item_id" in value:
        out["OpsItemId"] = value["ops_item_id"]
    if "version" in value:
        out["Version"] = value["version"]
    if "title" in value:
        out["Title"] = value["title"]
    if "source" in value:
        out["Source"] = value["source"]
    if "operational_data" in value:
        import capo_ssm.types.ops_item_operational_data

        out["OperationalData"] = (
            capo_ssm.types.ops_item_operational_data.serialize_aws_json_1_1(
                value["operational_data"]
            )
        )
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
    if "ops_item_arn" in value:
        out["OpsItemArn"] = value["ops_item_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsItem:
    out: OpsItem = {}  # type: ignore[typeddict-item]
    if data.get("CreatedBy") is not None:
        out["created_by"] = data["CreatedBy"]
    if data.get("OpsItemType") is not None:
        out["ops_item_type"] = data["OpsItemType"]
    if data.get("CreatedTime") is not None:
        import capo_ssm.types.date_time

        out["created_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["CreatedTime"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("LastModifiedBy") is not None:
        out["last_modified_by"] = data["LastModifiedBy"]
    if data.get("LastModifiedTime") is not None:
        import capo_ssm.types.date_time

        out["last_modified_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["LastModifiedTime"]
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
    if data.get("Status") is not None:
        import capo_ssm.types.ops_item_status

        out["status"] = capo_ssm.types.ops_item_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("OpsItemId") is not None:
        out["ops_item_id"] = data["OpsItemId"]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    if data.get("Source") is not None:
        out["source"] = data["Source"]
    if data.get("OperationalData") is not None:
        import capo_ssm.types.ops_item_operational_data

        out["operational_data"] = (
            capo_ssm.types.ops_item_operational_data.deserialize_aws_json_1_1(
                data["OperationalData"]
            )
        )
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
    if data.get("OpsItemArn") is not None:
        out["ops_item_arn"] = data["OpsItemArn"]
    return out
