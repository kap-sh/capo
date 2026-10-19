"""Generated from Smithy shape ``com.amazonaws.bedrock#ListAutomatedReasoningPolicyBuildWorkflowsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_build_workflow_summaries
    import capo_bedrock.types.pagination_token


class ListAutomatedReasoningPolicyBuildWorkflowsResponse(TypedDict, closed=True):
    automated_reasoning_policy_build_workflow_summaries: "capo_bedrock.types.automated_reasoning_policy_build_workflow_summaries.AutomatedReasoningPolicyBuildWorkflowSummaries"
    """<p>A list of build workflow summaries, each containing key information about a build workflow including its status and timestamps.</p>"""
    next_token: NotRequired["capo_bedrock.types.pagination_token.PaginationToken"]
    """<p>A pagination token to use in subsequent requests to retrieve additional build workflows.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAutomatedReasoningPolicyBuildWorkflowsResponse) -> dict:
    out: dict = {}
    import capo_bedrock.types.automated_reasoning_policy_build_workflow_summaries

    out["automatedReasoningPolicyBuildWorkflowSummaries"] = (
        capo_bedrock.types.automated_reasoning_policy_build_workflow_summaries.serialize_json(
            value["automated_reasoning_policy_build_workflow_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAutomatedReasoningPolicyBuildWorkflowsResponse:
    out: ListAutomatedReasoningPolicyBuildWorkflowsResponse = {}  # type: ignore[typeddict-item]
    if data.get("automatedReasoningPolicyBuildWorkflowSummaries") is not None:
        import capo_bedrock.types.automated_reasoning_policy_build_workflow_summaries

        out["automated_reasoning_policy_build_workflow_summaries"] = (
            capo_bedrock.types.automated_reasoning_policy_build_workflow_summaries.deserialize_json(
                data["automatedReasoningPolicyBuildWorkflowSummaries"]
            )
        )
    else:
        out["automated_reasoning_policy_build_workflow_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
