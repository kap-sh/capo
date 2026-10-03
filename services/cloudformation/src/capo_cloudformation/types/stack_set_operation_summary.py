"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackSetOperationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.client_request_token
    import capo_cloudformation.types.stack_set_operation_action
    import capo_cloudformation.types.stack_set_operation_preferences
    import capo_cloudformation.types.stack_set_operation_status
    import capo_cloudformation.types.stack_set_operation_status_details
    import capo_cloudformation.types.stack_set_operation_status_reason
    import capo_cloudformation.types.timestamp


class StackSetOperationSummary(TypedDict, closed=True):
    operation_id: NotRequired[
        "capo_cloudformation.types.client_request_token.ClientRequestToken"
    ]
    """<p>The unique ID of the StackSet operation.</p>"""
    action: NotRequired[
        "capo_cloudformation.types.stack_set_operation_action.StackSetOperationAction"
    ]
    """<p>The type of operation: <code>CREATE</code>, <code>UPDATE</code>, or <code>DELETE</code>. Create and delete operations affect only the specified stack instances that are associated with the specified StackSet. Update operations affect both the StackSet itself and <i>all</i> associated StackSet instances.</p>"""
    status: NotRequired[
        "capo_cloudformation.types.stack_set_operation_status.StackSetOperationStatus"
    ]
    """<p>The overall status of the operation.</p> <ul> <li> <p> <code>FAILED</code>: The operation exceeded the specified failure tolerance. The failure tolerance value that you've set for an operation is applied for each Region during stack create and update operations. If the number of failed stacks within a Region exceeds the failure tolerance, the status of the operation in the Region is set to <code>FAILED</code>. This in turn sets the status of the operation as a whole to <code>FAILED</code>, and CloudFormation cancels the operation in any remaining Regions.</p> </li> <li> <p> <code>QUEUED</code>: [Service-managed permissions] For automatic deployments that require a sequence of operations, the operation is queued to be performed. For more information, see the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stackset-status-codes">StackSet status codes</a> in the <i>CloudFormation User Guide</i>.</p> </li> <li> <p> <code>RUNNING</code>: The operation is currently being performed.</p> </li> <li> <p> <code>STOPPED</code>: The user has canceled the operation.</p> </li> <li> <p> <code>STOPPING</code>: The operation is in the process of stopping, at user request.</p> </li> <li> <p> <code>SUCCEEDED</code>: The operation completed creating or updating all the specified stacks without exceeding the failure tolerance for the operation.</p> </li> </ul>"""
    creation_timestamp: NotRequired["capo_cloudformation.types.timestamp.Timestamp"]
    """<p>The time at which the operation was initiated. Note that the creation times for the StackSet operation might differ from the creation time of the individual stacks themselves. This is because CloudFormation needs to perform preparatory work for the operation, such as dispatching the work to the requested Regions, before actually creating the first stacks.</p>"""
    end_timestamp: NotRequired["capo_cloudformation.types.timestamp.Timestamp"]
    """<p>The time at which the StackSet operation ended, across all accounts and Regions specified. Note that this doesn't necessarily mean that the StackSet operation was successful, or even attempted, in each account or Region.</p>"""
    status_reason: NotRequired[
        "capo_cloudformation.types.stack_set_operation_status_reason.StackSetOperationStatusReason"
    ]
    """<p>The status of the operation in details.</p>"""
    status_details: NotRequired[
        "capo_cloudformation.types.stack_set_operation_status_details.StackSetOperationStatusDetails"
    ]
    """<p>Detailed information about the StackSet operation.</p>"""
    operation_preferences: NotRequired[
        "capo_cloudformation.types.stack_set_operation_preferences.StackSetOperationPreferences"
    ]
    """<p>The user-specified preferences for how CloudFormation performs a StackSet operation.</p> <p>For more information about maximum concurrent accounts and failure tolerance, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stackset-ops-options">StackSet operation options</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StackSetOperationSummary, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "operation_id" in value:
        pairs.append((f"{key_prefix}OperationId", str(value["operation_id"])))
    if "action" in value:
        import capo_cloudformation.types.stack_set_operation_action

        capo_cloudformation.types.stack_set_operation_action.serialize_query(
            value["action"], pairs, f"{key_prefix}Action"
        )
    if "status" in value:
        import capo_cloudformation.types.stack_set_operation_status

        capo_cloudformation.types.stack_set_operation_status.serialize_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "creation_timestamp" in value:
        import capo_cloudformation.types.timestamp

        capo_cloudformation.types.timestamp.serialize_query(
            value["creation_timestamp"], pairs, f"{key_prefix}CreationTimestamp"
        )
    if "end_timestamp" in value:
        import capo_cloudformation.types.timestamp

        capo_cloudformation.types.timestamp.serialize_query(
            value["end_timestamp"], pairs, f"{key_prefix}EndTimestamp"
        )
    if "status_reason" in value:
        pairs.append((f"{key_prefix}StatusReason", str(value["status_reason"])))
    if "status_details" in value:
        import capo_cloudformation.types.stack_set_operation_status_details

        capo_cloudformation.types.stack_set_operation_status_details.serialize_query(
            value["status_details"], pairs, f"{key_prefix}StatusDetails"
        )
    if "operation_preferences" in value:
        import capo_cloudformation.types.stack_set_operation_preferences

        capo_cloudformation.types.stack_set_operation_preferences.serialize_query(
            value["operation_preferences"], pairs, f"{key_prefix}OperationPreferences"
        )


def deserialize_query(el: Element) -> StackSetOperationSummary:
    out: StackSetOperationSummary = {}  # type: ignore[typeddict-item]
    child_operation_id = el.find("OperationId")
    if child_operation_id is not None:
        out["operation_id"] = str(child_operation_id.text or "")
    child_action = el.find("Action")
    if child_action is not None:
        import capo_cloudformation.types.stack_set_operation_action

        out["action"] = (
            capo_cloudformation.types.stack_set_operation_action.deserialize_query(
                child_action
            )
        )
    child_status = el.find("Status")
    if child_status is not None:
        import capo_cloudformation.types.stack_set_operation_status

        out["status"] = (
            capo_cloudformation.types.stack_set_operation_status.deserialize_query(
                child_status
            )
        )
    child_creation_timestamp = el.find("CreationTimestamp")
    if child_creation_timestamp is not None:
        import capo_cloudformation.types.timestamp

        out["creation_timestamp"] = (
            capo_cloudformation.types.timestamp.deserialize_query(
                child_creation_timestamp
            )
        )
    child_end_timestamp = el.find("EndTimestamp")
    if child_end_timestamp is not None:
        import capo_cloudformation.types.timestamp

        out["end_timestamp"] = capo_cloudformation.types.timestamp.deserialize_query(
            child_end_timestamp
        )
    child_status_reason = el.find("StatusReason")
    if child_status_reason is not None:
        out["status_reason"] = str(child_status_reason.text or "")
    child_status_details = el.find("StatusDetails")
    if child_status_details is not None:
        import capo_cloudformation.types.stack_set_operation_status_details

        out["status_details"] = (
            capo_cloudformation.types.stack_set_operation_status_details.deserialize_query(
                child_status_details
            )
        )
    child_operation_preferences = el.find("OperationPreferences")
    if child_operation_preferences is not None:
        import capo_cloudformation.types.stack_set_operation_preferences

        out["operation_preferences"] = (
            capo_cloudformation.types.stack_set_operation_preferences.deserialize_query(
                child_operation_preferences
            )
        )
    return out
