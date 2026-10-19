"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListCollaborationPrivacyBudgetsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.collaboration_privacy_budget_summary_list
    import capo_cleanrooms.types.pagination_token


class ListCollaborationPrivacyBudgetsOutput(TypedDict, closed=True):
    collaboration_privacy_budget_summaries: "capo_cleanrooms.types.collaboration_privacy_budget_summary_list.CollaborationPrivacyBudgetSummaryList"
    """<p>Summaries of the collaboration privacy budgets.</p>"""
    next_token: NotRequired["capo_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCollaborationPrivacyBudgetsOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.collaboration_privacy_budget_summary_list

    out["collaborationPrivacyBudgetSummaries"] = (
        capo_cleanrooms.types.collaboration_privacy_budget_summary_list.serialize_json(
            value["collaboration_privacy_budget_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCollaborationPrivacyBudgetsOutput:
    out: ListCollaborationPrivacyBudgetsOutput = {}  # type: ignore[typeddict-item]
    if data.get("collaborationPrivacyBudgetSummaries") is not None:
        import capo_cleanrooms.types.collaboration_privacy_budget_summary_list

        out["collaboration_privacy_budget_summaries"] = (
            capo_cleanrooms.types.collaboration_privacy_budget_summary_list.deserialize_json(
                data["collaborationPrivacyBudgetSummaries"]
            )
        )
    else:
        out["collaboration_privacy_budget_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
