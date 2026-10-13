"""Generated from Smithy shape ``com.amazonaws.bedrock#ListAutomatedReasoningPoliciesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_summaries
    import capo_bedrock.types.pagination_token


class ListAutomatedReasoningPoliciesResponse(TypedDict, closed=True):
    automated_reasoning_policy_summaries: "capo_bedrock.types.automated_reasoning_policy_summaries.AutomatedReasoningPolicySummaries"
    """<p>A list of Automated Reasoning policy summaries.</p>"""
    next_token: NotRequired["capo_bedrock.types.pagination_token.PaginationToken"]
    """<p>The pagination token to use in a subsequent request to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAutomatedReasoningPoliciesResponse) -> dict:
    out: dict = {}
    import capo_bedrock.types.automated_reasoning_policy_summaries

    out["automatedReasoningPolicySummaries"] = (
        capo_bedrock.types.automated_reasoning_policy_summaries.serialize_json(
            value["automated_reasoning_policy_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAutomatedReasoningPoliciesResponse:
    out: ListAutomatedReasoningPoliciesResponse = {}  # type: ignore[typeddict-item]
    if data.get("automatedReasoningPolicySummaries") is not None:
        import capo_bedrock.types.automated_reasoning_policy_summaries

        out["automated_reasoning_policy_summaries"] = (
            capo_bedrock.types.automated_reasoning_policy_summaries.deserialize_json(
                data["automatedReasoningPolicySummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListAutomatedReasoningPoliciesResponse.automated_reasoning_policy_summaries required"
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListAutomatedReasoningPoliciesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "automated_reasoning_policy_summaries" in value:
        import capo_bedrock.types.automated_reasoning_policy_summaries

        out["automated_reasoning_policy_summaries"] = (
            capo_bedrock.types.automated_reasoning_policy_summaries.redact_sensitive(
                value["automated_reasoning_policy_summaries"]
            )
        )
    return out
