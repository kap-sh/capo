"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListStackSetOperationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.call_as
    import capo_cloudformation.types.max_results
    import capo_cloudformation.types.next_token
    import capo_cloudformation.types.stack_set_name


class ListStackSetOperationsInput(TypedDict, closed=True):
    stack_set_name: NotRequired["capo_cloudformation.types.stack_set_name.StackSetName"]
    """<p>The name or unique ID of the StackSet that you want to get operation summaries for.</p>"""
    next_token: NotRequired["capo_cloudformation.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    max_results: NotRequired["capo_cloudformation.types.max_results.MaxResults"]
    """<p>The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.</p>"""
    call_as: NotRequired["capo_cloudformation.types.call_as.CallAs"]
    """<p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for StackSets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListStackSetOperationsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "stack_set_name" in value:
        pairs.append((f"{key_prefix}StackSetName", str(value["stack_set_name"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "call_as" in value:
        import capo_cloudformation.types.call_as

        capo_cloudformation.types.call_as.serialize_query(
            value["call_as"], pairs, f"{key_prefix}CallAs"
        )


def deserialize_query(el: Element) -> ListStackSetOperationsInput:
    out: ListStackSetOperationsInput = {}  # type: ignore[typeddict-item]
    child_stack_set_name = el.find("StackSetName")
    if child_stack_set_name is not None:
        out["stack_set_name"] = str(child_stack_set_name.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_call_as = el.find("CallAs")
    if child_call_as is not None:
        import capo_cloudformation.types.call_as

        out["call_as"] = capo_cloudformation.types.call_as.deserialize_query(
            child_call_as
        )
    return out
