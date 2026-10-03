"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeChangeSetOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.capabilities
    import capo_cloudformation.types.change_set_id
    import capo_cloudformation.types.change_set_name
    import capo_cloudformation.types.change_set_status
    import capo_cloudformation.types.change_set_status_reason
    import capo_cloudformation.types.changes
    import capo_cloudformation.types.creation_time
    import capo_cloudformation.types.deployment_config
    import capo_cloudformation.types.deployment_mode
    import capo_cloudformation.types.description
    import capo_cloudformation.types.execution_status
    import capo_cloudformation.types.import_existing_resources
    import capo_cloudformation.types.include_nested_stacks
    import capo_cloudformation.types.next_token
    import capo_cloudformation.types.notification_ar_ns
    import capo_cloudformation.types.on_stack_failure
    import capo_cloudformation.types.parameters
    import capo_cloudformation.types.rollback_configuration
    import capo_cloudformation.types.stack_drift_status
    import capo_cloudformation.types.stack_id
    import capo_cloudformation.types.stack_name
    import capo_cloudformation.types.tags


class DescribeChangeSetOutput(TypedDict, closed=True):
    change_set_name: NotRequired[
        "capo_cloudformation.types.change_set_name.ChangeSetName"
    ]
    """<p>The name of the change set.</p>"""
    change_set_id: NotRequired["capo_cloudformation.types.change_set_id.ChangeSetId"]
    """<p>The Amazon Resource Name (ARN) of the change set.</p>"""
    stack_id: NotRequired["capo_cloudformation.types.stack_id.StackId"]
    """<p>The Amazon Resource Name (ARN) of the stack that's associated with the change set.</p>"""
    stack_name: NotRequired["capo_cloudformation.types.stack_name.StackName"]
    """<p>The name of the stack that's associated with the change set.</p>"""
    description: NotRequired["capo_cloudformation.types.description.Description"]
    """<p>Information about the change set.</p>"""
    parameters: NotRequired["capo_cloudformation.types.parameters.Parameters"]
    """<p>A list of <code>Parameter</code> structures that describes the input parameters and their values used to create the change set. For more information, see the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_Parameter.html">Parameter</a> data type.</p>"""
    creation_time: NotRequired["capo_cloudformation.types.creation_time.CreationTime"]
    """<p>The start time when the change set was created, in UTC.</p>"""
    execution_status: NotRequired[
        "capo_cloudformation.types.execution_status.ExecutionStatus"
    ]
    """<p>If the change set execution status is <code>AVAILABLE</code>, you can execute the change set. If you can't execute the change set, the status indicates why. For example, a change set might be in an <code>UNAVAILABLE</code> state because CloudFormation is still creating it or in an <code>OBSOLETE</code> state because the stack was already updated.</p>"""
    status: NotRequired["capo_cloudformation.types.change_set_status.ChangeSetStatus"]
    """<p>The current status of the change set, such as <code>CREATE_PENDING</code>, <code>CREATE_COMPLETE</code>, or <code>FAILED</code>.</p>"""
    status_reason: NotRequired[
        "capo_cloudformation.types.change_set_status_reason.ChangeSetStatusReason"
    ]
    """<p>A description of the change set's status. For example, if your attempt to create a change set failed, CloudFormation shows the error message.</p>"""
    stack_drift_status: NotRequired[
        "capo_cloudformation.types.stack_drift_status.StackDriftStatus"
    ]
    """<p>The drift status of the stack when the change set was created. Valid values:</p> <ul> <li> <p> <code>DRIFTED</code> – The stack has drifted from its last deployment.</p> </li> <li> <p> <code>IN_SYNC</code> – The stack is in sync with its last deployment.</p> </li> <li> <p> <code>NOT_CHECKED</code> – CloudFormation doesn’t currently return this value.</p> </li> <li> <p> <code>UNKNOWN</code> – The drift status could not be determined.</p> </li> </ul> <p>Only present for drift-aware change sets.</p>"""
    notification_ar_ns: NotRequired[
        "capo_cloudformation.types.notification_ar_ns.NotificationARNs"
    ]
    """<p>The ARNs of the Amazon SNS topics that will be associated with the stack if you execute the change set.</p>"""
    rollback_configuration: NotRequired[
        "capo_cloudformation.types.rollback_configuration.RollbackConfiguration"
    ]
    """<p>The rollback triggers for CloudFormation to monitor during stack creation and updating operations, and for the specified monitoring period afterwards.</p>"""
    capabilities: NotRequired["capo_cloudformation.types.capabilities.Capabilities"]
    """<p>If you execute the change set, the list of capabilities that were explicitly acknowledged when the change set was created.</p>"""
    tags: NotRequired["capo_cloudformation.types.tags.Tags"]
    """<p>If you execute the change set, the tags that will be associated with the stack.</p>"""
    changes: NotRequired["capo_cloudformation.types.changes.Changes"]
    """<p>A list of <code>Change</code> structures that describes the resources CloudFormation changes if you execute the change set.</p>"""
    next_token: NotRequired["capo_cloudformation.types.next_token.NextToken"]
    """<p>If the output exceeds 1 MB, a string that identifies the next page of changes. If there is no additional page, this value is null.</p>"""
    include_nested_stacks: NotRequired[
        "capo_cloudformation.types.include_nested_stacks.IncludeNestedStacks"
    ]
    """<p>Verifies if <code>IncludeNestedStacks</code> is set to <code>True</code>.</p>"""
    parent_change_set_id: NotRequired[
        "capo_cloudformation.types.change_set_id.ChangeSetId"
    ]
    """<p>Specifies the change set ID of the parent change set in the current nested change set hierarchy.</p>"""
    root_change_set_id: NotRequired[
        "capo_cloudformation.types.change_set_id.ChangeSetId"
    ]
    """<p>Specifies the change set ID of the root change set in the current nested change set hierarchy.</p>"""
    on_stack_failure: NotRequired[
        "capo_cloudformation.types.on_stack_failure.OnStackFailure"
    ]
    """<p>Determines what action will be taken if stack creation fails. When this parameter is specified, the <code>DisableRollback</code> parameter to the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ExecuteChangeSet.html">ExecuteChangeSet</a> API operation must not be specified. This must be one of these values:</p> <ul> <li> <p> <code>DELETE</code> - Deletes the change set if the stack creation fails. This is only valid when the <code>ChangeSetType</code> parameter is set to <code>CREATE</code>. If the deletion of the stack fails, the status of the stack is <code>DELETE_FAILED</code>.</p> </li> <li> <p> <code>DO_NOTHING</code> - if the stack creation fails, do nothing. This is equivalent to specifying <code>true</code> for the <code>DisableRollback</code> parameter to the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ExecuteChangeSet.html">ExecuteChangeSet</a> API operation.</p> </li> <li> <p> <code>ROLLBACK</code> - if the stack creation fails, roll back the stack. This is equivalent to specifying <code>false</code> for the <code>DisableRollback</code> parameter to the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ExecuteChangeSet.html">ExecuteChangeSet</a> API operation.</p> </li> </ul>"""
    import_existing_resources: NotRequired[
        "capo_cloudformation.types.import_existing_resources.ImportExistingResources"
    ]
    """<p>Indicates if the change set imports resources that already exist.</p> <note> <p>This parameter can only import resources that have <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-name.html">custom names</a> in templates. To import resources that do not accept custom names, such as EC2 instances, use the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import.html">resource import</a> feature instead.</p> </note>"""
    deployment_mode: NotRequired[
        "capo_cloudformation.types.deployment_mode.DeploymentMode"
    ]
    """<p>The deployment mode specified when the change set was created. Valid value is <code>REVERT_DRIFT</code>. Only present for drift-aware change sets.</p>"""
    deployment_config: NotRequired[
        "capo_cloudformation.types.deployment_config.DeploymentConfig"
    ]
    """<p>The deployment configuration specified when the change set was created.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeChangeSetOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "change_set_name" in value:
        pairs.append((f"{key_prefix}ChangeSetName", str(value["change_set_name"])))
    if "change_set_id" in value:
        pairs.append((f"{key_prefix}ChangeSetId", str(value["change_set_id"])))
    if "stack_id" in value:
        pairs.append((f"{key_prefix}StackId", str(value["stack_id"])))
    if "stack_name" in value:
        pairs.append((f"{key_prefix}StackName", str(value["stack_name"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "parameters" in value:
        import capo_cloudformation.types.parameters

        capo_cloudformation.types.parameters.serialize_query(
            value["parameters"], pairs, f"{key_prefix}Parameters"
        )
    if "creation_time" in value:
        import capo_cloudformation.types.creation_time

        capo_cloudformation.types.creation_time.serialize_query(
            value["creation_time"], pairs, f"{key_prefix}CreationTime"
        )
    if "execution_status" in value:
        import capo_cloudformation.types.execution_status

        capo_cloudformation.types.execution_status.serialize_query(
            value["execution_status"], pairs, f"{key_prefix}ExecutionStatus"
        )
    if "status" in value:
        import capo_cloudformation.types.change_set_status

        capo_cloudformation.types.change_set_status.serialize_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "status_reason" in value:
        pairs.append((f"{key_prefix}StatusReason", str(value["status_reason"])))
    if "stack_drift_status" in value:
        import capo_cloudformation.types.stack_drift_status

        capo_cloudformation.types.stack_drift_status.serialize_query(
            value["stack_drift_status"], pairs, f"{key_prefix}StackDriftStatus"
        )
    if "notification_ar_ns" in value:
        import capo_cloudformation.types.notification_ar_ns

        capo_cloudformation.types.notification_ar_ns.serialize_query(
            value["notification_ar_ns"], pairs, f"{key_prefix}NotificationARNs"
        )
    if "rollback_configuration" in value:
        import capo_cloudformation.types.rollback_configuration

        capo_cloudformation.types.rollback_configuration.serialize_query(
            value["rollback_configuration"], pairs, f"{key_prefix}RollbackConfiguration"
        )
    if "capabilities" in value:
        import capo_cloudformation.types.capabilities

        capo_cloudformation.types.capabilities.serialize_query(
            value["capabilities"], pairs, f"{key_prefix}Capabilities"
        )
    if "tags" in value:
        import capo_cloudformation.types.tags

        capo_cloudformation.types.tags.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )
    if "changes" in value:
        import capo_cloudformation.types.changes

        capo_cloudformation.types.changes.serialize_query(
            value["changes"], pairs, f"{key_prefix}Changes"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "include_nested_stacks" in value:
        pairs.append(
            (
                f"{key_prefix}IncludeNestedStacks",
                "true" if value["include_nested_stacks"] else "false",
            )
        )
    if "parent_change_set_id" in value:
        pairs.append(
            (f"{key_prefix}ParentChangeSetId", str(value["parent_change_set_id"]))
        )
    if "root_change_set_id" in value:
        pairs.append((f"{key_prefix}RootChangeSetId", str(value["root_change_set_id"])))
    if "on_stack_failure" in value:
        import capo_cloudformation.types.on_stack_failure

        capo_cloudformation.types.on_stack_failure.serialize_query(
            value["on_stack_failure"], pairs, f"{key_prefix}OnStackFailure"
        )
    if "import_existing_resources" in value:
        pairs.append(
            (
                f"{key_prefix}ImportExistingResources",
                "true" if value["import_existing_resources"] else "false",
            )
        )
    if "deployment_mode" in value:
        import capo_cloudformation.types.deployment_mode

        capo_cloudformation.types.deployment_mode.serialize_query(
            value["deployment_mode"], pairs, f"{key_prefix}DeploymentMode"
        )
    if "deployment_config" in value:
        import capo_cloudformation.types.deployment_config

        capo_cloudformation.types.deployment_config.serialize_query(
            value["deployment_config"], pairs, f"{key_prefix}DeploymentConfig"
        )


def deserialize_query(el: Element) -> DescribeChangeSetOutput:
    out: DescribeChangeSetOutput = {}  # type: ignore[typeddict-item]
    child_change_set_name = el.find("ChangeSetName")
    if child_change_set_name is not None:
        out["change_set_name"] = str(child_change_set_name.text or "")
    child_change_set_id = el.find("ChangeSetId")
    if child_change_set_id is not None:
        out["change_set_id"] = str(child_change_set_id.text or "")
    child_stack_id = el.find("StackId")
    if child_stack_id is not None:
        out["stack_id"] = str(child_stack_id.text or "")
    child_stack_name = el.find("StackName")
    if child_stack_name is not None:
        out["stack_name"] = str(child_stack_name.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_parameters = el.find("Parameters")
    if child_parameters is not None:
        import capo_cloudformation.types.parameters

        out["parameters"] = capo_cloudformation.types.parameters.deserialize_query(
            child_parameters
        )
    child_creation_time = el.find("CreationTime")
    if child_creation_time is not None:
        import capo_cloudformation.types.creation_time

        out["creation_time"] = (
            capo_cloudformation.types.creation_time.deserialize_query(
                child_creation_time
            )
        )
    child_execution_status = el.find("ExecutionStatus")
    if child_execution_status is not None:
        import capo_cloudformation.types.execution_status

        out["execution_status"] = (
            capo_cloudformation.types.execution_status.deserialize_query(
                child_execution_status
            )
        )
    child_status = el.find("Status")
    if child_status is not None:
        import capo_cloudformation.types.change_set_status

        out["status"] = capo_cloudformation.types.change_set_status.deserialize_query(
            child_status
        )
    child_status_reason = el.find("StatusReason")
    if child_status_reason is not None:
        out["status_reason"] = str(child_status_reason.text or "")
    child_stack_drift_status = el.find("StackDriftStatus")
    if child_stack_drift_status is not None:
        import capo_cloudformation.types.stack_drift_status

        out["stack_drift_status"] = (
            capo_cloudformation.types.stack_drift_status.deserialize_query(
                child_stack_drift_status
            )
        )
    child_notification_ar_ns = el.find("NotificationARNs")
    if child_notification_ar_ns is not None:
        import capo_cloudformation.types.notification_ar_ns

        out["notification_ar_ns"] = (
            capo_cloudformation.types.notification_ar_ns.deserialize_query(
                child_notification_ar_ns
            )
        )
    child_rollback_configuration = el.find("RollbackConfiguration")
    if child_rollback_configuration is not None:
        import capo_cloudformation.types.rollback_configuration

        out["rollback_configuration"] = (
            capo_cloudformation.types.rollback_configuration.deserialize_query(
                child_rollback_configuration
            )
        )
    child_capabilities = el.find("Capabilities")
    if child_capabilities is not None:
        import capo_cloudformation.types.capabilities

        out["capabilities"] = capo_cloudformation.types.capabilities.deserialize_query(
            child_capabilities
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_cloudformation.types.tags

        out["tags"] = capo_cloudformation.types.tags.deserialize_query(child_tags)
    child_changes = el.find("Changes")
    if child_changes is not None:
        import capo_cloudformation.types.changes

        out["changes"] = capo_cloudformation.types.changes.deserialize_query(
            child_changes
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_include_nested_stacks = el.find("IncludeNestedStacks")
    if child_include_nested_stacks is not None:
        out["include_nested_stacks"] = (
            child_include_nested_stacks.text or ""
        ).lower() == "true"
    child_parent_change_set_id = el.find("ParentChangeSetId")
    if child_parent_change_set_id is not None:
        out["parent_change_set_id"] = str(child_parent_change_set_id.text or "")
    child_root_change_set_id = el.find("RootChangeSetId")
    if child_root_change_set_id is not None:
        out["root_change_set_id"] = str(child_root_change_set_id.text or "")
    child_on_stack_failure = el.find("OnStackFailure")
    if child_on_stack_failure is not None:
        import capo_cloudformation.types.on_stack_failure

        out["on_stack_failure"] = (
            capo_cloudformation.types.on_stack_failure.deserialize_query(
                child_on_stack_failure
            )
        )
    child_import_existing_resources = el.find("ImportExistingResources")
    if child_import_existing_resources is not None:
        out["import_existing_resources"] = (
            child_import_existing_resources.text or ""
        ).lower() == "true"
    child_deployment_mode = el.find("DeploymentMode")
    if child_deployment_mode is not None:
        import capo_cloudformation.types.deployment_mode

        out["deployment_mode"] = (
            capo_cloudformation.types.deployment_mode.deserialize_query(
                child_deployment_mode
            )
        )
    child_deployment_config = el.find("DeploymentConfig")
    if child_deployment_config is not None:
        import capo_cloudformation.types.deployment_config

        out["deployment_config"] = (
            capo_cloudformation.types.deployment_config.deserialize_query(
                child_deployment_config
            )
        )
    return out
