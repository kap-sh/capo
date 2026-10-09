"""Generated from Smithy shape ``com.amazonaws.cloudformation#ContinueUpdateRollbackInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.client_request_token
    import capo_cloudformation.types.force_rollback
    import capo_cloudformation.types.resources_to_skip
    import capo_cloudformation.types.role_arn
    import capo_cloudformation.types.stack_name_or_id


class ContinueUpdateRollbackInput(TypedDict, closed=True):
    stack_name: NotRequired["capo_cloudformation.types.stack_name_or_id.StackNameOrId"]
    """<p>The name or the unique ID of the stack that you want to continue rolling back.</p> <note> <p>Don't specify the name of a nested stack (a stack that was created by using the <code>AWS::CloudFormation::Stack</code> resource). Instead, use this operation on the parent stack (the stack that contains the <code>AWS::CloudFormation::Stack</code> resource).</p> </note>"""
    role_arn: NotRequired["capo_cloudformation.types.role_arn.RoleARN"]
    """<p>The Amazon Resource Name (ARN) of an IAM role that CloudFormation assumes to roll back the stack. CloudFormation uses the role's credentials to make calls on your behalf. CloudFormation always uses this role for all future operations on the stack. Provided that users have permission to operate on the stack, CloudFormation uses this role even if the users don't have permission to pass it. Ensure that the role grants least permission.</p> <p>If you don't specify a value, CloudFormation uses the role that was previously associated with the stack. If no role is available, CloudFormation uses a temporary session that's generated from your user credentials.</p>"""
    resources_to_skip: NotRequired[
        "capo_cloudformation.types.resources_to_skip.ResourcesToSkip"
    ]
    """<p>A list of the logical IDs of the resources that CloudFormation skips during the continue update rollback operation. You can specify only resources that are in the <code>UPDATE_FAILED</code> state because a rollback failed. You can't specify resources that are in the <code>UPDATE_FAILED</code> state for other reasons, for example, because an update was canceled. To check why a resource update failed, use the <a>DescribeStackResources</a> action, and view the resource status reason.</p> <important> <p>Specify this property to skip rolling back resources that CloudFormation can't successfully roll back. We recommend that you <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html#troubleshooting-errors-update-rollback-failed"> troubleshoot</a> resources before skipping them. CloudFormation sets the status of the specified resources to <code>UPDATE_COMPLETE</code> and continues to roll back the stack. After the rollback is complete, the state of the skipped resources will be inconsistent with the state of the resources in the stack template. Before performing another stack update, you must update the stack or resources to be consistent with each other. If you don't, subsequent stack updates might fail, and the stack will become unrecoverable.</p> </important> <p>Specify the minimum number of resources required to successfully roll back your stack. For example, a failed resource update might cause dependent resources to fail. In this case, it might not be necessary to skip the dependent resources.</p> <p>To skip resources that are part of nested stacks, use the following format: <code>NestedStackName.ResourceLogicalID</code>. If you want to specify the logical ID of a stack resource (<code>Type: AWS::CloudFormation::Stack</code>) in the <code>ResourcesToSkip</code> list, then its corresponding embedded stack must be in one of the following states: <code>DELETE_IN_PROGRESS</code>, <code>DELETE_COMPLETE</code>, or <code>DELETE_FAILED</code>.</p> <note> <p>Don't confuse a child stack's name with its corresponding logical ID defined in the parent stack. For an example of a continue update rollback operation with nested stacks, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-continueupdaterollback.html#nested-stacks">Continue rolling back from failed nested stack updates</a>.</p> </note>"""
    client_request_token: NotRequired[
        "capo_cloudformation.types.client_request_token.ClientRequestToken"
    ]
    """<p>A unique identifier for this <code>ContinueUpdateRollback</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to continue the rollback to a stack with the same name. You might retry <code>ContinueUpdateRollback</code> requests to ensure that CloudFormation successfully received them.</p>"""
    force_rollback: NotRequired[
        "capo_cloudformation.types.force_rollback.ForceRollback"
    ]
    """<p>Specifies whether CloudFormation forces the rollback to continue by skipping resources currently in the <code>UPDATE_FAILED</code> state. Use this instead of listing each resource individually in <code>ResourcesToSkip</code>. Only resources that entered the <code>UPDATE_FAILED</code> state because a rollback failed are skipped. If you don't specify a value, the default is <code>false</code> and CloudFormation doesn't skip any resources.</p> <p> <code>ForceRollback</code> and <code>ResourcesToSkip</code> are mutually exclusive. Specifying both in the same request returns a validation error.</p> <important> <p>We recommend that you <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html#troubleshooting-errors-update-rollback-failed">troubleshoot</a> resources before skipping them. CloudFormation sets the status of the skipped resources to <code>UPDATE_COMPLETE</code> and continues to roll back the stack, including resources in nested stacks. After the rollback completes, the skipped resources no longer match the resources in the stack template. Before performing another stack update, you must update the stack or resources to be consistent with each other. If you don't, subsequent stack updates might fail, and the stack will become unrecoverable.</p> <p>Drift detection reports skipped resources as <code>NOT_CHECKED</code>. For guidance, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-continueupdaterollback.html">Continue rolling back an update</a> in the <i>CloudFormation User Guide</i>.</p> </important>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ContinueUpdateRollbackInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "stack_name" in value:
        pairs.append((f"{key_prefix}StackName", str(value["stack_name"])))
    if "role_arn" in value:
        pairs.append((f"{key_prefix}RoleARN", str(value["role_arn"])))
    if "resources_to_skip" in value:
        import capo_cloudformation.types.resources_to_skip

        capo_cloudformation.types.resources_to_skip.serialize_query(
            value["resources_to_skip"], pairs, f"{key_prefix}ResourcesToSkip"
        )
    if "client_request_token" in value:
        pairs.append(
            (f"{key_prefix}ClientRequestToken", str(value["client_request_token"]))
        )
    if "force_rollback" in value:
        pairs.append(
            (
                f"{key_prefix}ForceRollback",
                "true" if value["force_rollback"] else "false",
            )
        )


def deserialize_query(el: Element) -> ContinueUpdateRollbackInput:
    out: ContinueUpdateRollbackInput = {}  # type: ignore[typeddict-item]
    child_stack_name = el.find("StackName")
    if child_stack_name is not None:
        out["stack_name"] = str(child_stack_name.text or "")
    child_role_arn = el.find("RoleARN")
    if child_role_arn is not None:
        out["role_arn"] = str(child_role_arn.text or "")
    child_resources_to_skip = el.find("ResourcesToSkip")
    if child_resources_to_skip is not None:
        import capo_cloudformation.types.resources_to_skip

        out["resources_to_skip"] = (
            capo_cloudformation.types.resources_to_skip.deserialize_query(
                child_resources_to_skip
            )
        )
    child_client_request_token = el.find("ClientRequestToken")
    if child_client_request_token is not None:
        out["client_request_token"] = str(child_client_request_token.text or "")
    child_force_rollback = el.find("ForceRollback")
    if child_force_rollback is not None:
        out["force_rollback"] = (child_force_rollback.text or "").lower() == "true"
    return out
