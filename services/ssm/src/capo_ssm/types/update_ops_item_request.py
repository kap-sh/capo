"""Generated from Smithy shape ``com.amazonaws.ssm#UpdateOpsItemRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.date_time
    import capo_ssm.types.ops_item_arn
    import capo_ssm.types.ops_item_category
    import capo_ssm.types.ops_item_description
    import capo_ssm.types.ops_item_id
    import capo_ssm.types.ops_item_notifications
    import capo_ssm.types.ops_item_operational_data
    import capo_ssm.types.ops_item_ops_data_keys_list
    import capo_ssm.types.ops_item_priority
    import capo_ssm.types.ops_item_severity
    import capo_ssm.types.ops_item_status
    import capo_ssm.types.ops_item_title
    import capo_ssm.types.related_ops_items


class UpdateOpsItemRequest(TypedDict, closed=True):
    description: NotRequired["capo_ssm.types.ops_item_description.OpsItemDescription"]
    """<p>User-defined text that contains information about the OpsItem, in Markdown format. </p>"""
    operational_data: NotRequired[
        "capo_ssm.types.ops_item_operational_data.OpsItemOperationalData"
    ]
    """<p>Add new keys or edit existing key-value pairs of the OperationalData map in the OpsItem object.</p> <p>Operational data is custom data that provides useful reference details about the OpsItem. For example, you can specify log files, error strings, license keys, troubleshooting tips, or other relevant data. You enter operational data as key-value pairs. The key has a maximum length of 128 characters. The value has a maximum size of 20 KB.</p> <important> <p>Operational data keys <i>can't</i> begin with the following: <code>amazon</code>, <code>aws</code>, <code>amzn</code>, <code>ssm</code>, <code>/amazon</code>, <code>/aws</code>, <code>/amzn</code>, <code>/ssm</code>.</p> </important> <p>You can choose to make the data searchable by other users in the account or you can restrict search access. Searchable data means that all users with access to the OpsItem Overview page (as provided by the <a>DescribeOpsItems</a> API operation) can view and search on the specified data. Operational data that isn't searchable is only viewable by users who have access to the OpsItem (as provided by the <a>GetOpsItem</a> API operation).</p> <p>Use the <code>/aws/resources</code> key in OperationalData to specify a related resource in the request. Use the <code>/aws/automations</code> key in OperationalData to associate an Automation runbook with the OpsItem. To view Amazon Web Services CLI example commands that use these keys, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-manually-create-OpsItems.html">Creating OpsItems manually</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    operational_data_to_delete: NotRequired[
        "capo_ssm.types.ops_item_ops_data_keys_list.OpsItemOpsDataKeysList"
    ]
    """<p>Keys that you want to remove from the OperationalData map.</p>"""
    notifications: NotRequired[
        "capo_ssm.types.ops_item_notifications.OpsItemNotifications"
    ]
    """<p>The Amazon Resource Name (ARN) of an SNS topic where notifications are sent when this OpsItem is edited or changed.</p>"""
    priority: NotRequired["capo_ssm.types.ops_item_priority.OpsItemPriority"]
    """<p>The importance of this OpsItem in relation to other OpsItems in the system.</p>"""
    related_ops_items: NotRequired["capo_ssm.types.related_ops_items.RelatedOpsItems"]
    """<p>One or more OpsItems that share something in common with the current OpsItems. For example, related OpsItems can include OpsItems with similar error messages, impacted resources, or statuses for the impacted resource.</p>"""
    status: NotRequired["capo_ssm.types.ops_item_status.OpsItemStatus"]
    """<p>The OpsItem status. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-working-with-OpsItems-editing-details.html">Editing OpsItem details</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    ops_item_id: "capo_ssm.types.ops_item_id.OpsItemId"
    """<p>The ID of the OpsItem.</p>"""
    title: NotRequired["capo_ssm.types.ops_item_title.OpsItemTitle"]
    """<p>A short heading that describes the nature of the OpsItem and the impacted resource.</p>"""
    category: NotRequired["capo_ssm.types.ops_item_category.OpsItemCategory"]
    """<p>Specify a new category for an OpsItem.</p>"""
    severity: NotRequired["capo_ssm.types.ops_item_severity.OpsItemSeverity"]
    """<p>Specify a new severity for an OpsItem.</p>"""
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
def serialize_aws_json_1_1(value: UpdateOpsItemRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "operational_data" in value:
        import capo_ssm.types.ops_item_operational_data

        out["OperationalData"] = (
            capo_ssm.types.ops_item_operational_data.serialize_aws_json_1_1(
                value["operational_data"]
            )
        )
    if "operational_data_to_delete" in value:
        import capo_ssm.types.ops_item_ops_data_keys_list

        out["OperationalDataToDelete"] = (
            capo_ssm.types.ops_item_ops_data_keys_list.serialize_aws_json_1_1(
                value["operational_data_to_delete"]
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
    if "status" in value:
        import capo_ssm.types.ops_item_status

        out["Status"] = capo_ssm.types.ops_item_status.serialize_aws_json_1_1(
            value["status"]
        )
    out["OpsItemId"] = value["ops_item_id"]
    if "title" in value:
        out["Title"] = value["title"]
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


def deserialize_aws_json_1_1(data: dict) -> UpdateOpsItemRequest:
    out: UpdateOpsItemRequest = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("OperationalData") is not None:
        import capo_ssm.types.ops_item_operational_data

        out["operational_data"] = (
            capo_ssm.types.ops_item_operational_data.deserialize_aws_json_1_1(
                data["OperationalData"]
            )
        )
    if data.get("OperationalDataToDelete") is not None:
        import capo_ssm.types.ops_item_ops_data_keys_list

        out["operational_data_to_delete"] = (
            capo_ssm.types.ops_item_ops_data_keys_list.deserialize_aws_json_1_1(
                data["OperationalDataToDelete"]
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
    if data.get("Status") is not None:
        import capo_ssm.types.ops_item_status

        out["status"] = capo_ssm.types.ops_item_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("OpsItemId") is not None:
        out["ops_item_id"] = data["OpsItemId"]
    else:
        raise DeserializationError("UpdateOpsItemRequest.ops_item_id required")
    if data.get("Title") is not None:
        out["title"] = data["Title"]
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
