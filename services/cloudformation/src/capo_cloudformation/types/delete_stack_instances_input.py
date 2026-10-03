"""Generated from Smithy shape ``com.amazonaws.cloudformation#DeleteStackInstancesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.account_list
    import capo_cloudformation.types.call_as
    import capo_cloudformation.types.client_request_token
    import capo_cloudformation.types.deployment_targets
    import capo_cloudformation.types.region_list
    import capo_cloudformation.types.retain_stacks
    import capo_cloudformation.types.stack_set_name
    import capo_cloudformation.types.stack_set_operation_preferences


class DeleteStackInstancesInput(TypedDict, closed=True):
    stack_set_name: NotRequired["capo_cloudformation.types.stack_set_name.StackSetName"]
    """<p>The name or unique ID of the StackSet that you want to delete stack instances for.</p>"""
    accounts: NotRequired["capo_cloudformation.types.account_list.AccountList"]
    """<p>[Self-managed permissions] The account IDs of the Amazon Web Services accounts that you want to delete stack instances for.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>"""
    deployment_targets: NotRequired[
        "capo_cloudformation.types.deployment_targets.DeploymentTargets"
    ]
    """<p>[Service-managed permissions] The Organizations accounts from which to delete stack instances.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>"""
    regions: NotRequired["capo_cloudformation.types.region_list.RegionList"]
    """<p>The Amazon Web Services Regions where you want to delete StackSet instances.</p>"""
    operation_preferences: NotRequired[
        "capo_cloudformation.types.stack_set_operation_preferences.StackSetOperationPreferences"
    ]
    """<p>Preferences for how CloudFormation performs this StackSet operation.</p>"""
    retain_stacks: NotRequired["capo_cloudformation.types.retain_stacks.RetainStacks"]
    """<p>Removes the stack instances from the specified StackSet, but doesn't delete the stacks. You can't reassociate a retained stack or add an existing, saved stack to a new stack set.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stackset-ops-options">StackSet operation options</a>.</p>"""
    operation_id: NotRequired[
        "capo_cloudformation.types.client_request_token.ClientRequestToken"
    ]
    """<p>The unique identifier for this StackSet operation.</p> <p>If you don't specify an operation ID, the SDK generates one automatically.</p> <p>The operation ID also functions as an idempotency token, to ensure that CloudFormation performs the StackSet operation only once, even if you retry the request multiple times. You can retry StackSet operation requests to ensure that CloudFormation successfully received them.</p> <p>Repeating this StackSet operation with a new operation ID retries all stack instances whose status is <code>OUTDATED</code>.</p>"""
    call_as: NotRequired["capo_cloudformation.types.call_as.CallAs"]
    """<p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for StackSets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteStackInstancesInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "stack_set_name" in value:
        pairs.append((f"{key_prefix}StackSetName", str(value["stack_set_name"])))
    if "accounts" in value:
        import capo_cloudformation.types.account_list

        capo_cloudformation.types.account_list.serialize_query(
            value["accounts"], pairs, f"{key_prefix}Accounts"
        )
    if "deployment_targets" in value:
        import capo_cloudformation.types.deployment_targets

        capo_cloudformation.types.deployment_targets.serialize_query(
            value["deployment_targets"], pairs, f"{key_prefix}DeploymentTargets"
        )
    if "regions" in value:
        import capo_cloudformation.types.region_list

        capo_cloudformation.types.region_list.serialize_query(
            value["regions"], pairs, f"{key_prefix}Regions"
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
    if "operation_id" in value:
        pairs.append((f"{key_prefix}OperationId", str(value["operation_id"])))
    if "call_as" in value:
        import capo_cloudformation.types.call_as

        capo_cloudformation.types.call_as.serialize_query(
            value["call_as"], pairs, f"{key_prefix}CallAs"
        )


def deserialize_query(el: Element) -> DeleteStackInstancesInput:
    out: DeleteStackInstancesInput = {}  # type: ignore[typeddict-item]
    child_stack_set_name = el.find("StackSetName")
    if child_stack_set_name is not None:
        out["stack_set_name"] = str(child_stack_set_name.text or "")
    child_accounts = el.find("Accounts")
    if child_accounts is not None:
        import capo_cloudformation.types.account_list

        out["accounts"] = capo_cloudformation.types.account_list.deserialize_query(
            child_accounts
        )
    child_deployment_targets = el.find("DeploymentTargets")
    if child_deployment_targets is not None:
        import capo_cloudformation.types.deployment_targets

        out["deployment_targets"] = (
            capo_cloudformation.types.deployment_targets.deserialize_query(
                child_deployment_targets
            )
        )
    child_regions = el.find("Regions")
    if child_regions is not None:
        import capo_cloudformation.types.region_list

        out["regions"] = capo_cloudformation.types.region_list.deserialize_query(
            child_regions
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
    child_operation_id = el.find("OperationId")
    if child_operation_id is not None:
        out["operation_id"] = str(child_operation_id.text or "")
    child_call_as = el.find("CallAs")
    if child_call_as is not None:
        import capo_cloudformation.types.call_as

        out["call_as"] = capo_cloudformation.types.call_as.deserialize_query(
            child_call_as
        )
    return out
