"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListStackSetAutoDeploymentTargetsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.next_token
    import capo_cloudformation.types.stack_set_auto_deployment_target_summaries


class ListStackSetAutoDeploymentTargetsOutput(TypedDict, closed=True):
    summaries: NotRequired[
        "capo_cloudformation.types.stack_set_auto_deployment_target_summaries.StackSetAutoDeploymentTargetSummaries"
    ]
    """<p>An array of summaries of the deployment targets for the StackSet.</p>"""
    next_token: NotRequired["capo_cloudformation.types.next_token.NextToken"]
    """<p>If the request doesn't return all the remaining results, <code>NextToken</code> is set to a token. To retrieve the next set of results, call <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListStackSetAutoDeploymentTargets.html">ListStackSetAutoDeploymentTargets</a> again and use that value for the <code>NextToken</code> parameter. If the request returns all results, <code>NextToken</code> is set to an empty string.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListStackSetAutoDeploymentTargetsOutput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "summaries" in value:
        import capo_cloudformation.types.stack_set_auto_deployment_target_summaries

        capo_cloudformation.types.stack_set_auto_deployment_target_summaries.serialize_query(
            value["summaries"], pairs, f"{key_prefix}Summaries"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListStackSetAutoDeploymentTargetsOutput:
    out: ListStackSetAutoDeploymentTargetsOutput = {}  # type: ignore[typeddict-item]
    child_summaries = el.find("Summaries")
    if child_summaries is not None:
        import capo_cloudformation.types.stack_set_auto_deployment_target_summaries

        out["summaries"] = (
            capo_cloudformation.types.stack_set_auto_deployment_target_summaries.deserialize_query(
                child_summaries
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
