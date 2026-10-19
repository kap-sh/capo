"""Generated from Smithy shape ``com.amazonaws.bedrock#ListAutomatedReasoningPolicyBuildWorkflowsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_arn
    import capo_bedrock.types.max_results
    import capo_bedrock.types.pagination_token


class ListAutomatedReasoningPolicyBuildWorkflowsRequest(TypedDict, closed=True):
    policy_arn: (
        "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy whose build workflows you want to list.</p>"""
    next_token: NotRequired["capo_bedrock.types.pagination_token.PaginationToken"]
    """<p>A pagination token from a previous request to continue listing build workflows from where the previous request left off.</p>"""
    max_results: NotRequired["capo_bedrock.types.max_results.MaxResults"]
    """<p>The maximum number of build workflows to return in a single response. Valid range is 1-100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAutomatedReasoningPolicyBuildWorkflowsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAutomatedReasoningPolicyBuildWorkflowsRequest:
    out: ListAutomatedReasoningPolicyBuildWorkflowsRequest = {}  # type: ignore[typeddict-item]
    return out
