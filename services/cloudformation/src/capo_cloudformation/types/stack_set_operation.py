"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackSetOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.client_request_token
    import capo_cloudformation.types.deployment_targets
    import capo_cloudformation.types.execution_role_name
    import capo_cloudformation.types.retain_stacks_nullable
    import capo_cloudformation.types.role_arn
    import capo_cloudformation.types.stack_set_drift_detection_details
    import capo_cloudformation.types.stack_set_id
    import capo_cloudformation.types.stack_set_operation_action
    import capo_cloudformation.types.stack_set_operation_preferences
    import capo_cloudformation.types.stack_set_operation_status
    import capo_cloudformation.types.stack_set_operation_status_details
    import capo_cloudformation.types.stack_set_operation_status_reason
    import capo_cloudformation.types.timestamp


class StackSetOperation(TypedDict, closed=True):
    operation_id: NotRequired[
        "capo_cloudformation.types.client_request_token.ClientRequestToken"
    ]
    """<p>The unique ID of a StackSet operation.</p>"""
    stack_set_id: NotRequired["capo_cloudformation.types.stack_set_id.StackSetId"]
    """<p>The ID of the StackSet.</p>"""
    action: NotRequired[
        "capo_cloudformation.types.stack_set_operation_action.StackSetOperationAction"
    ]
    """<p>The type of StackSet operation: <code>CREATE</code>, <code>UPDATE</code>, or <code>DELETE</code>. Create and delete operations affect only the specified stack instances that are associated with the specified StackSet. Update operations affect both the StackSet itself, in addition to <i>all</i> associated stack instances.</p>"""
    status: NotRequired[
        "capo_cloudformation.types.stack_set_operation_status.StackSetOperationStatus"
    ]
    """<p>The status of the operation.</p> <ul> <li> <p> <code>FAILED</code>: The operation exceeded the specified failure tolerance. The failure tolerance value that you've set for an operation is applied for each Region during stack create and update operations. If the number of failed stacks within a Region exceeds the failure tolerance, the status of the operation in the Region is set to <code>FAILED</code>. This in turn sets the status of the operation as a whole to <code>FAILED</code>, and CloudFormation cancels the operation in any remaining Regions.</p> </li> <li> <p> <code>QUEUED</code>: [Service-managed permissions] For automatic deployments that require a sequence of operations, the operation is queued to be performed. For more information, see the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stackset-status-codes">StackSets status codes</a> in the <i>CloudFormation User Guide</i>.</p> </li> <li> <p> <code>RUNNING</code>: The operation is currently being performed.</p> </li> <li> <p> <code>STOPPED</code>: The user has canceled the operation.</p> </li> <li> <p> <code>STOPPING</code>: The operation is in the process of stopping, at user request.</p> </li> <li> <p> <code>SUCCEEDED</code>: The operation completed creating or updating all the specified stacks without exceeding the failure tolerance for the operation.</p> </li> </ul>"""
    operation_preferences: NotRequired[
        "capo_cloudformation.types.stack_set_operation_preferences.StackSetOperationPreferences"
    ]
    """<p>The preferences for how CloudFormation performs this StackSet operation.</p>"""
    retain_stacks: NotRequired[
        "capo_cloudformation.types.retain_stacks_nullable.RetainStacksNullable"
    ]
    """<p>For StackSet operations of action type <code>DELETE</code>, specifies whether to remove the stack instances from the specified StackSet, but doesn't delete the stacks. You can't re-associate a retained stack, or add an existing, saved stack to a new StackSet.</p>"""
    administration_role_arn: NotRequired["capo_cloudformation.types.role_arn.RoleARN"]
    """<p>The Amazon Resource Name (ARN) of the IAM role used to perform this StackSet operation.</p> <p>Use customized administrator roles to control which users or groups can manage specific StackSets within the same administrator account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html">Grant self-managed permissions</a> in the <i>CloudFormation User Guide</i>.</p>"""
    execution_role_name: NotRequired[
        "capo_cloudformation.types.execution_role_name.ExecutionRoleName"
    ]
    """<p>The name of the IAM execution role used to create or update the StackSet.</p> <p>Use customized execution roles to control which stack resources users and groups can include in their StackSets.</p>"""
    creation_timestamp: NotRequired["capo_cloudformation.types.timestamp.Timestamp"]
    """<p>The time at which the operation was initiated. Note that the creation times for the stack set operation might differ from the creation time of the individual stacks themselves. This is because CloudFormation needs to perform preparatory work for the operation, such as dispatching the work to the requested Regions, before actually creating the first stacks.</p>"""
    end_timestamp: NotRequired["capo_cloudformation.types.timestamp.Timestamp"]
    """<p>The time at which the StackSet operation ended, across all accounts and Regions specified. Note that this doesn't necessarily mean that the StackSet operation was successful, or even attempted, in each account or Region.</p>"""
    deployment_targets: NotRequired[
        "capo_cloudformation.types.deployment_targets.DeploymentTargets"
    ]
    """<p>The Organizations accounts affected by the stack operation. Valid only if the StackSet uses service-managed permissions.</p>"""
    stack_set_drift_detection_details: NotRequired[
        "capo_cloudformation.types.stack_set_drift_detection_details.StackSetDriftDetectionDetails"
    ]
    """<p>Detailed information about the drift status of the StackSet. This includes information about drift operations currently being performed on the StackSet.</p> <p>This information will only be present for StackSet operations whose <code>Action</code> type is <code>DETECT_DRIFT</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html">Performing drift detection on CloudFormation StackSets</a> in the <i>CloudFormation User Guide</i>.</p>"""
    status_reason: NotRequired[
        "capo_cloudformation.types.stack_set_operation_status_reason.StackSetOperationStatusReason"
    ]
    """<p>The status of the operation in details.</p>"""
    status_details: NotRequired[
        "capo_cloudformation.types.stack_set_operation_status_details.StackSetOperationStatusDetails"
    ]
    """<p>Detailed information about the StackSet operation.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StackSetOperation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "operation_id" in value:
        pairs.append((f"{key_prefix}OperationId", str(value["operation_id"])))
    if "stack_set_id" in value:
        pairs.append((f"{key_prefix}StackSetId", str(value["stack_set_id"])))
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
    if "operation_preferences" in value:
        import capo_cloudformation.types.stack_set_operation_preferences

        capo_cloudformation.types.stack_set_operation_preferences.serialize_query(
            value["operation_preferences"], pairs, f"{key_prefix}OperationPreferences"
        )
    if "retain_stacks" in value:
        pairs.append(
            (f"{key_prefix}RetainStacks", "true" if value["retain_stacks"] else "false")
        )
    if "administration_role_arn" in value:
        pairs.append(
            (
                f"{key_prefix}AdministrationRoleARN",
                str(value["administration_role_arn"]),
            )
        )
    if "execution_role_name" in value:
        pairs.append(
            (f"{key_prefix}ExecutionRoleName", str(value["execution_role_name"]))
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
    if "deployment_targets" in value:
        import capo_cloudformation.types.deployment_targets

        capo_cloudformation.types.deployment_targets.serialize_query(
            value["deployment_targets"], pairs, f"{key_prefix}DeploymentTargets"
        )
    if "stack_set_drift_detection_details" in value:
        import capo_cloudformation.types.stack_set_drift_detection_details

        capo_cloudformation.types.stack_set_drift_detection_details.serialize_query(
            value["stack_set_drift_detection_details"],
            pairs,
            f"{key_prefix}StackSetDriftDetectionDetails",
        )
    if "status_reason" in value:
        pairs.append((f"{key_prefix}StatusReason", str(value["status_reason"])))
    if "status_details" in value:
        import capo_cloudformation.types.stack_set_operation_status_details

        capo_cloudformation.types.stack_set_operation_status_details.serialize_query(
            value["status_details"], pairs, f"{key_prefix}StatusDetails"
        )


def deserialize_query(el: Element) -> StackSetOperation:
    out: StackSetOperation = {}  # type: ignore[typeddict-item]
    child_operation_id = el.find("OperationId")
    if child_operation_id is not None:
        out["operation_id"] = str(child_operation_id.text or "")
    child_stack_set_id = el.find("StackSetId")
    if child_stack_set_id is not None:
        out["stack_set_id"] = str(child_stack_set_id.text or "")
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
    child_operation_preferences = el.find("OperationPreferences")
    if child_operation_preferences is not None:
        import capo_cloudformation.types.stack_set_operation_preferences

        out["operation_preferences"] = (
            capo_cloudformation.types.stack_set_operation_preferences.deserialize_query(
                child_operation_preferences
            )
        )
    child_retain_stacks = el.find("RetainStacks")
    if child_retain_stacks is not None:
        out["retain_stacks"] = (child_retain_stacks.text or "").lower() == "true"
    child_administration_role_arn = el.find("AdministrationRoleARN")
    if child_administration_role_arn is not None:
        out["administration_role_arn"] = str(child_administration_role_arn.text or "")
    child_execution_role_name = el.find("ExecutionRoleName")
    if child_execution_role_name is not None:
        out["execution_role_name"] = str(child_execution_role_name.text or "")
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
    child_deployment_targets = el.find("DeploymentTargets")
    if child_deployment_targets is not None:
        import capo_cloudformation.types.deployment_targets

        out["deployment_targets"] = (
            capo_cloudformation.types.deployment_targets.deserialize_query(
                child_deployment_targets
            )
        )
    child_stack_set_drift_detection_details = el.find("StackSetDriftDetectionDetails")
    if child_stack_set_drift_detection_details is not None:
        import capo_cloudformation.types.stack_set_drift_detection_details

        out["stack_set_drift_detection_details"] = (
            capo_cloudformation.types.stack_set_drift_detection_details.deserialize_query(
                child_stack_set_drift_detection_details
            )
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
    return out
