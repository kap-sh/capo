"""Generated from Smithy shape ``com.amazonaws.bedrock#ListAutomatedReasoningPolicyTestResultsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_arn
    import capo_bedrock.types.automated_reasoning_policy_build_workflow_id
    import capo_bedrock.types.max_results
    import capo_bedrock.types.pagination_token


class ListAutomatedReasoningPolicyTestResultsRequest(TypedDict, closed=True):
    policy_arn: (
        "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy whose test results you want to list.</p>"""
    build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId"
    """<p>The unique identifier of the build workflow whose test results you want to list.</p>"""
    next_token: NotRequired["capo_bedrock.types.pagination_token.PaginationToken"]
    """<p>A pagination token from a previous request to continue listing test results from where the previous request left off.</p>"""
    max_results: NotRequired["capo_bedrock.types.max_results.MaxResults"]
    """<p>The maximum number of test results to return in a single response. Valid range is 1-100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAutomatedReasoningPolicyTestResultsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAutomatedReasoningPolicyTestResultsRequest:
    out: ListAutomatedReasoningPolicyTestResultsRequest = {}  # type: ignore[typeddict-item]
    return out
