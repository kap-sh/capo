"""Generated from Smithy shape ``com.amazonaws.bedrock#ListAutomatedReasoningPolicyTestCasesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_arn
    import capo_bedrock.types.max_results
    import capo_bedrock.types.pagination_token


class ListAutomatedReasoningPolicyTestCasesRequest(TypedDict, closed=True):
    policy_arn: (
        "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy for which to list tests.</p>"""
    next_token: NotRequired["capo_bedrock.types.pagination_token.PaginationToken"]
    """<p>The pagination token from a previous request to retrieve the next page of results.</p>"""
    max_results: NotRequired["capo_bedrock.types.max_results.MaxResults"]
    """<p>The maximum number of tests to return in a single call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAutomatedReasoningPolicyTestCasesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAutomatedReasoningPolicyTestCasesRequest:
    out: ListAutomatedReasoningPolicyTestCasesRequest = {}  # type: ignore[typeddict-item]
    return out
