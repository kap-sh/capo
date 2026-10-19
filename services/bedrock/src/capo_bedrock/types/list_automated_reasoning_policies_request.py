"""Generated from Smithy shape ``com.amazonaws.bedrock#ListAutomatedReasoningPoliciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_arn
    import capo_bedrock.types.max_results
    import capo_bedrock.types.pagination_token


class ListAutomatedReasoningPoliciesRequest(TypedDict, closed=True):
    policy_arn: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    ]
    """<p>Optional filter to list only the policy versions with the specified Amazon Resource Name (ARN). If not provided, the DRAFT versions for all policies are listed.</p>"""
    next_token: NotRequired["capo_bedrock.types.pagination_token.PaginationToken"]
    """<p>The pagination token from a previous request to retrieve the next page of results.</p>"""
    max_results: NotRequired["capo_bedrock.types.max_results.MaxResults"]
    """<p>The maximum number of policies to return in a single call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAutomatedReasoningPoliciesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAutomatedReasoningPoliciesRequest:
    out: ListAutomatedReasoningPoliciesRequest = {}  # type: ignore[typeddict-item]
    return out
