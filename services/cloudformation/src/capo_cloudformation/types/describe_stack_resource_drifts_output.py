"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribeStackResourceDriftsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.next_token
    import capo_cloudformation.types.stack_resource_drifts


class DescribeStackResourceDriftsOutput(TypedDict, closed=True):
    stack_resource_drifts: NotRequired[
        "capo_cloudformation.types.stack_resource_drifts.StackResourceDrifts"
    ]
    """<p>Drift information for the resources that have been checked for drift in the specified stack. This includes actual and expected configuration values for resources where CloudFormation detects drift.</p> <p>For a given stack, there will be one <code>StackResourceDrift</code> for each stack resource that has been checked for drift. Resources that haven't yet been checked for drift aren't included. Resources that do not currently support drift detection aren't checked, and so not included. For a list of resources that support drift detection, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-supported-resources.html">Resource type support for imports and drift detection</a>.</p>"""
    next_token: NotRequired["capo_cloudformation.types.next_token.NextToken"]
    """<p>If the request doesn't return all the remaining results, <code>NextToken</code> is set to a token. To retrieve the next set of results, call <code>DescribeStackResourceDrifts</code> again and assign that token to the request object's <code>NextToken</code> parameter. If the request returns all results, <code>NextToken</code> is set to <code>null</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeStackResourceDriftsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "stack_resource_drifts" in value:
        import capo_cloudformation.types.stack_resource_drifts

        capo_cloudformation.types.stack_resource_drifts.serialize_query(
            value["stack_resource_drifts"], pairs, f"{key_prefix}StackResourceDrifts"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> DescribeStackResourceDriftsOutput:
    out: DescribeStackResourceDriftsOutput = {}  # type: ignore[typeddict-item]
    child_stack_resource_drifts = el.find("StackResourceDrifts")
    if child_stack_resource_drifts is not None:
        import capo_cloudformation.types.stack_resource_drifts

        out["stack_resource_drifts"] = (
            capo_cloudformation.types.stack_resource_drifts.deserialize_query(
                child_stack_resource_drifts
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
