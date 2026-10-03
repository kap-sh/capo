"""Generated from Smithy shape ``com.amazonaws.cloudformation#Stack``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.capabilities
    import capo_cloudformation.types.change_set_id
    import capo_cloudformation.types.creation_time
    import capo_cloudformation.types.deletion_mode
    import capo_cloudformation.types.deletion_time
    import capo_cloudformation.types.deployment_config
    import capo_cloudformation.types.description
    import capo_cloudformation.types.detailed_status
    import capo_cloudformation.types.disable_rollback
    import capo_cloudformation.types.enable_termination_protection
    import capo_cloudformation.types.last_operations
    import capo_cloudformation.types.last_updated_time
    import capo_cloudformation.types.notification_ar_ns
    import capo_cloudformation.types.outputs
    import capo_cloudformation.types.parameters
    import capo_cloudformation.types.retain_except_on_create
    import capo_cloudformation.types.role_arn
    import capo_cloudformation.types.rollback_configuration
    import capo_cloudformation.types.stack_drift_information
    import capo_cloudformation.types.stack_id
    import capo_cloudformation.types.stack_name
    import capo_cloudformation.types.stack_status
    import capo_cloudformation.types.stack_status_reason
    import capo_cloudformation.types.tags
    import capo_cloudformation.types.timeout_minutes


class Stack(TypedDict, closed=True):
    stack_id: NotRequired["capo_cloudformation.types.stack_id.StackId"]
    """<p>Unique identifier of the stack.</p>"""
    stack_name: NotRequired["capo_cloudformation.types.stack_name.StackName"]
    """<p>The name associated with the stack.</p>"""
    change_set_id: NotRequired["capo_cloudformation.types.change_set_id.ChangeSetId"]
    """<p>The unique ID of the change set.</p>"""
    description: NotRequired["capo_cloudformation.types.description.Description"]
    """<p>A user-defined description associated with the stack.</p>"""
    parameters: NotRequired["capo_cloudformation.types.parameters.Parameters"]
    """<p>A list of <code>Parameter</code> structures.</p>"""
    creation_time: NotRequired["capo_cloudformation.types.creation_time.CreationTime"]
    """<p>The time at which the stack was created.</p>"""
    deletion_time: NotRequired["capo_cloudformation.types.deletion_time.DeletionTime"]
    """<p>The time the stack was deleted.</p>"""
    last_updated_time: NotRequired[
        "capo_cloudformation.types.last_updated_time.LastUpdatedTime"
    ]
    """<p>The time the stack was last updated. This field will only be returned if the stack has been updated at least once.</p>"""
    rollback_configuration: NotRequired[
        "capo_cloudformation.types.rollback_configuration.RollbackConfiguration"
    ]
    """<p>The rollback triggers for CloudFormation to monitor during stack creation and updating operations, and for the specified monitoring period afterwards.</p>"""
    stack_status: NotRequired["capo_cloudformation.types.stack_status.StackStatus"]
    """<p>Current status of the stack.</p>"""
    stack_status_reason: NotRequired[
        "capo_cloudformation.types.stack_status_reason.StackStatusReason"
    ]
    """<p>Success/failure message associated with the stack status.</p>"""
    disable_rollback: NotRequired[
        "capo_cloudformation.types.disable_rollback.DisableRollback"
    ]
    """<p>Boolean to enable or disable rollback on stack creation failures:</p> <ul> <li> <p> <code>true</code>: disable rollback.</p> </li> <li> <p> <code>false</code>: enable rollback.</p> </li> </ul>"""
    deployment_config: NotRequired[
        "capo_cloudformation.types.deployment_config.DeploymentConfig"
    ]
    """<p>The deployment configuration for the stack, including the deployment mode used for stack operations.</p>"""
    notification_ar_ns: NotRequired[
        "capo_cloudformation.types.notification_ar_ns.NotificationARNs"
    ]
    """<p>Amazon SNS topic Amazon Resource Names (ARNs) to which stack related events are published.</p>"""
    timeout_in_minutes: NotRequired[
        "capo_cloudformation.types.timeout_minutes.TimeoutMinutes"
    ]
    """<p>The amount of time within which stack creation should complete.</p>"""
    capabilities: NotRequired["capo_cloudformation.types.capabilities.Capabilities"]
    """<p>The capabilities allowed in the stack.</p>"""
    outputs: NotRequired["capo_cloudformation.types.outputs.Outputs"]
    """<p>A list of output structures.</p>"""
    role_arn: NotRequired["capo_cloudformation.types.role_arn.RoleARN"]
    """<p>The Amazon Resource Name (ARN) of an IAM role that's associated with the stack. During a stack operation, CloudFormation uses this role's credentials to make calls on your behalf.</p>"""
    tags: NotRequired["capo_cloudformation.types.tags.Tags"]
    """<p>A list of <code>Tag</code>s that specify information about the stack.</p>"""
    enable_termination_protection: NotRequired[
        "capo_cloudformation.types.enable_termination_protection.EnableTerminationProtection"
    ]
    """<p>Whether termination protection is enabled for the stack.</p> <p>For <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html">nested stacks</a>, termination protection is set on the root stack and can't be changed directly on the nested stack. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.html">Protect a CloudFormation stack from being deleted</a> in the <i>CloudFormation User Guide</i>.</p>"""
    parent_id: NotRequired["capo_cloudformation.types.stack_id.StackId"]
    """<p>For nested stacks, the stack ID of the direct parent of this stack. For the first level of nested stacks, the root stack is also the parent stack.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html">Nested stacks</a> in the <i>CloudFormation User Guide</i>.</p>"""
    root_id: NotRequired["capo_cloudformation.types.stack_id.StackId"]
    """<p>For nested stacks, the stack ID of the top-level stack to which the nested stack ultimately belongs.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html">Nested stacks</a> in the <i>CloudFormation User Guide</i>.</p>"""
    drift_information: NotRequired[
        "capo_cloudformation.types.stack_drift_information.StackDriftInformation"
    ]
    """<p>Information about whether a stack's actual configuration differs, or has <i>drifted</i>, from its expected configuration, as defined in the stack template and any values specified as template parameters. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html">Detect unmanaged configuration changes to stacks and resources with drift detection</a>.</p>"""
    retain_except_on_create: NotRequired[
        "capo_cloudformation.types.retain_except_on_create.RetainExceptOnCreate"
    ]
    """<p>When set to <code>true</code>, newly created resources are deleted when the operation rolls back. This includes newly created resources marked with a deletion policy of <code>Retain</code>.</p> <p>Default: <code>false</code> </p>"""
    deletion_mode: NotRequired["capo_cloudformation.types.deletion_mode.DeletionMode"]
    """<p>Specifies the deletion mode for the stack. Possible values are:</p> <ul> <li> <p> <code>STANDARD</code> - Use the standard behavior. Specifying this value is the same as not specifying this parameter.</p> </li> <li> <p> <code>FORCE_DELETE_STACK</code> - Delete the stack if it's stuck in a <code>DELETE_FAILED</code> state due to resource deletion failure.</p> </li> </ul>"""
    detailed_status: NotRequired[
        "capo_cloudformation.types.detailed_status.DetailedStatus"
    ]
    """<p>The detailed status of the resource or stack. If <code>CONFIGURATION_COMPLETE</code> is present, the resource or resource configuration phase has completed and the stabilization of the resources is in progress. The StackSets <code>CONFIGURATION_COMPLETE</code> when all of the resources in the stack have reached that event. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stack-resource-configuration-complete.html">Understand CloudFormation stack creation events</a> in the <i>CloudFormation User Guide</i>.</p>"""
    last_operations: NotRequired[
        "capo_cloudformation.types.last_operations.LastOperations"
    ]
    """<p>Information about the most recent operations performed on this stack.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Stack, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "stack_id" in value:
        pairs.append((f"{key_prefix}StackId", str(value["stack_id"])))
    if "stack_name" in value:
        pairs.append((f"{key_prefix}StackName", str(value["stack_name"])))
    if "change_set_id" in value:
        pairs.append((f"{key_prefix}ChangeSetId", str(value["change_set_id"])))
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
    if "deletion_time" in value:
        import capo_cloudformation.types.deletion_time

        capo_cloudformation.types.deletion_time.serialize_query(
            value["deletion_time"], pairs, f"{key_prefix}DeletionTime"
        )
    if "last_updated_time" in value:
        import capo_cloudformation.types.last_updated_time

        capo_cloudformation.types.last_updated_time.serialize_query(
            value["last_updated_time"], pairs, f"{key_prefix}LastUpdatedTime"
        )
    if "rollback_configuration" in value:
        import capo_cloudformation.types.rollback_configuration

        capo_cloudformation.types.rollback_configuration.serialize_query(
            value["rollback_configuration"], pairs, f"{key_prefix}RollbackConfiguration"
        )
    if "stack_status" in value:
        import capo_cloudformation.types.stack_status

        capo_cloudformation.types.stack_status.serialize_query(
            value["stack_status"], pairs, f"{key_prefix}StackStatus"
        )
    if "stack_status_reason" in value:
        pairs.append(
            (f"{key_prefix}StackStatusReason", str(value["stack_status_reason"]))
        )
    if "disable_rollback" in value:
        pairs.append(
            (
                f"{key_prefix}DisableRollback",
                "true" if value["disable_rollback"] else "false",
            )
        )
    if "deployment_config" in value:
        import capo_cloudformation.types.deployment_config

        capo_cloudformation.types.deployment_config.serialize_query(
            value["deployment_config"], pairs, f"{key_prefix}DeploymentConfig"
        )
    if "notification_ar_ns" in value:
        import capo_cloudformation.types.notification_ar_ns

        capo_cloudformation.types.notification_ar_ns.serialize_query(
            value["notification_ar_ns"], pairs, f"{key_prefix}NotificationARNs"
        )
    if "timeout_in_minutes" in value:
        pairs.append(
            (f"{key_prefix}TimeoutInMinutes", str(value["timeout_in_minutes"]))
        )
    if "capabilities" in value:
        import capo_cloudformation.types.capabilities

        capo_cloudformation.types.capabilities.serialize_query(
            value["capabilities"], pairs, f"{key_prefix}Capabilities"
        )
    if "outputs" in value:
        import capo_cloudformation.types.outputs

        capo_cloudformation.types.outputs.serialize_query(
            value["outputs"], pairs, f"{key_prefix}Outputs"
        )
    if "role_arn" in value:
        pairs.append((f"{key_prefix}RoleARN", str(value["role_arn"])))
    if "tags" in value:
        import capo_cloudformation.types.tags

        capo_cloudformation.types.tags.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )
    if "enable_termination_protection" in value:
        pairs.append(
            (
                f"{key_prefix}EnableTerminationProtection",
                "true" if value["enable_termination_protection"] else "false",
            )
        )
    if "parent_id" in value:
        pairs.append((f"{key_prefix}ParentId", str(value["parent_id"])))
    if "root_id" in value:
        pairs.append((f"{key_prefix}RootId", str(value["root_id"])))
    if "drift_information" in value:
        import capo_cloudformation.types.stack_drift_information

        capo_cloudformation.types.stack_drift_information.serialize_query(
            value["drift_information"], pairs, f"{key_prefix}DriftInformation"
        )
    if "retain_except_on_create" in value:
        pairs.append(
            (
                f"{key_prefix}RetainExceptOnCreate",
                "true" if value["retain_except_on_create"] else "false",
            )
        )
    if "deletion_mode" in value:
        import capo_cloudformation.types.deletion_mode

        capo_cloudformation.types.deletion_mode.serialize_query(
            value["deletion_mode"], pairs, f"{key_prefix}DeletionMode"
        )
    if "detailed_status" in value:
        import capo_cloudformation.types.detailed_status

        capo_cloudformation.types.detailed_status.serialize_query(
            value["detailed_status"], pairs, f"{key_prefix}DetailedStatus"
        )
    if "last_operations" in value:
        import capo_cloudformation.types.last_operations

        capo_cloudformation.types.last_operations.serialize_query(
            value["last_operations"], pairs, f"{key_prefix}LastOperations"
        )


def deserialize_query(el: Element) -> Stack:
    out: Stack = {}  # type: ignore[typeddict-item]
    child_stack_id = el.find("StackId")
    if child_stack_id is not None:
        out["stack_id"] = str(child_stack_id.text or "")
    child_stack_name = el.find("StackName")
    if child_stack_name is not None:
        out["stack_name"] = str(child_stack_name.text or "")
    child_change_set_id = el.find("ChangeSetId")
    if child_change_set_id is not None:
        out["change_set_id"] = str(child_change_set_id.text or "")
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
    child_deletion_time = el.find("DeletionTime")
    if child_deletion_time is not None:
        import capo_cloudformation.types.deletion_time

        out["deletion_time"] = (
            capo_cloudformation.types.deletion_time.deserialize_query(
                child_deletion_time
            )
        )
    child_last_updated_time = el.find("LastUpdatedTime")
    if child_last_updated_time is not None:
        import capo_cloudformation.types.last_updated_time

        out["last_updated_time"] = (
            capo_cloudformation.types.last_updated_time.deserialize_query(
                child_last_updated_time
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
    child_stack_status = el.find("StackStatus")
    if child_stack_status is not None:
        import capo_cloudformation.types.stack_status

        out["stack_status"] = capo_cloudformation.types.stack_status.deserialize_query(
            child_stack_status
        )
    child_stack_status_reason = el.find("StackStatusReason")
    if child_stack_status_reason is not None:
        out["stack_status_reason"] = str(child_stack_status_reason.text or "")
    child_disable_rollback = el.find("DisableRollback")
    if child_disable_rollback is not None:
        out["disable_rollback"] = (child_disable_rollback.text or "").lower() == "true"
    child_deployment_config = el.find("DeploymentConfig")
    if child_deployment_config is not None:
        import capo_cloudformation.types.deployment_config

        out["deployment_config"] = (
            capo_cloudformation.types.deployment_config.deserialize_query(
                child_deployment_config
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
    child_timeout_in_minutes = el.find("TimeoutInMinutes")
    if child_timeout_in_minutes is not None:
        out["timeout_in_minutes"] = int(child_timeout_in_minutes.text or "")
    child_capabilities = el.find("Capabilities")
    if child_capabilities is not None:
        import capo_cloudformation.types.capabilities

        out["capabilities"] = capo_cloudformation.types.capabilities.deserialize_query(
            child_capabilities
        )
    child_outputs = el.find("Outputs")
    if child_outputs is not None:
        import capo_cloudformation.types.outputs

        out["outputs"] = capo_cloudformation.types.outputs.deserialize_query(
            child_outputs
        )
    child_role_arn = el.find("RoleARN")
    if child_role_arn is not None:
        out["role_arn"] = str(child_role_arn.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_cloudformation.types.tags

        out["tags"] = capo_cloudformation.types.tags.deserialize_query(child_tags)
    child_enable_termination_protection = el.find("EnableTerminationProtection")
    if child_enable_termination_protection is not None:
        out["enable_termination_protection"] = (
            child_enable_termination_protection.text or ""
        ).lower() == "true"
    child_parent_id = el.find("ParentId")
    if child_parent_id is not None:
        out["parent_id"] = str(child_parent_id.text or "")
    child_root_id = el.find("RootId")
    if child_root_id is not None:
        out["root_id"] = str(child_root_id.text or "")
    child_drift_information = el.find("DriftInformation")
    if child_drift_information is not None:
        import capo_cloudformation.types.stack_drift_information

        out["drift_information"] = (
            capo_cloudformation.types.stack_drift_information.deserialize_query(
                child_drift_information
            )
        )
    child_retain_except_on_create = el.find("RetainExceptOnCreate")
    if child_retain_except_on_create is not None:
        out["retain_except_on_create"] = (
            child_retain_except_on_create.text or ""
        ).lower() == "true"
    child_deletion_mode = el.find("DeletionMode")
    if child_deletion_mode is not None:
        import capo_cloudformation.types.deletion_mode

        out["deletion_mode"] = (
            capo_cloudformation.types.deletion_mode.deserialize_query(
                child_deletion_mode
            )
        )
    child_detailed_status = el.find("DetailedStatus")
    if child_detailed_status is not None:
        import capo_cloudformation.types.detailed_status

        out["detailed_status"] = (
            capo_cloudformation.types.detailed_status.deserialize_query(
                child_detailed_status
            )
        )
    child_last_operations = el.find("LastOperations")
    if child_last_operations is not None:
        import capo_cloudformation.types.last_operations

        out["last_operations"] = (
            capo_cloudformation.types.last_operations.deserialize_query(
                child_last_operations
            )
        )
    return out
