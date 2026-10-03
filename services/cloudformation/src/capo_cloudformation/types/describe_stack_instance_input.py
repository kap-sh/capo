"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeStackInstanceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.account
    import capo_cloudformation.types.call_as
    import capo_cloudformation.types.region
    import capo_cloudformation.types.stack_set_name


class DescribeStackInstanceInput(TypedDict, closed=True):
    stack_set_name: NotRequired["capo_cloudformation.types.stack_set_name.StackSetName"]
    """<p>The name or the unique stack ID of the StackSet that you want to get stack instance information for.</p>"""
    stack_instance_account: NotRequired["capo_cloudformation.types.account.Account"]
    """<p>The ID of an Amazon Web Services account that's associated with this stack instance.</p>"""
    stack_instance_region: NotRequired["capo_cloudformation.types.region.Region"]
    """<p>The name of a Region that's associated with this stack instance.</p>"""
    call_as: NotRequired["capo_cloudformation.types.call_as.CallAs"]
    """<p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for StackSets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeStackInstanceInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "stack_set_name" in value:
        pairs.append((f"{key_prefix}StackSetName", str(value["stack_set_name"])))
    if "stack_instance_account" in value:
        pairs.append(
            (f"{key_prefix}StackInstanceAccount", str(value["stack_instance_account"]))
        )
    if "stack_instance_region" in value:
        pairs.append(
            (f"{key_prefix}StackInstanceRegion", str(value["stack_instance_region"]))
        )
    if "call_as" in value:
        import capo_cloudformation.types.call_as

        capo_cloudformation.types.call_as.serialize_query(
            value["call_as"], pairs, f"{key_prefix}CallAs"
        )


def deserialize_query(el: Element) -> DescribeStackInstanceInput:
    out: DescribeStackInstanceInput = {}  # type: ignore[typeddict-item]
    child_stack_set_name = el.find("StackSetName")
    if child_stack_set_name is not None:
        out["stack_set_name"] = str(child_stack_set_name.text or "")
    child_stack_instance_account = el.find("StackInstanceAccount")
    if child_stack_instance_account is not None:
        out["stack_instance_account"] = str(child_stack_instance_account.text or "")
    child_stack_instance_region = el.find("StackInstanceRegion")
    if child_stack_instance_region is not None:
        out["stack_instance_region"] = str(child_stack_instance_region.text or "")
    child_call_as = el.find("CallAs")
    if child_call_as is not None:
        import capo_cloudformation.types.call_as

        out["call_as"] = capo_cloudformation.types.call_as.deserialize_query(
            child_call_as
        )
    return out
