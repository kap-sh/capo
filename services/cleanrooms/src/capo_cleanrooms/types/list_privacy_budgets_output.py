"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListPrivacyBudgetsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.pagination_token
    import capo_cleanrooms.types.privacy_budget_summary_list


class ListPrivacyBudgetsOutput(TypedDict, closed=True):
    privacy_budget_summaries: (
        "capo_cleanrooms.types.privacy_budget_summary_list.PrivacyBudgetSummaryList"
    )
    """<p>An array that summarizes the privacy budgets. The summary includes collaboration information, membership information, privacy budget template information, and privacy budget details.</p>"""
    next_token: NotRequired["capo_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPrivacyBudgetsOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.privacy_budget_summary_list

    out["privacyBudgetSummaries"] = (
        capo_cleanrooms.types.privacy_budget_summary_list.serialize_json(
            value["privacy_budget_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPrivacyBudgetsOutput:
    out: ListPrivacyBudgetsOutput = {}  # type: ignore[typeddict-item]
    if data.get("privacyBudgetSummaries") is not None:
        import capo_cleanrooms.types.privacy_budget_summary_list

        out["privacy_budget_summaries"] = (
            capo_cleanrooms.types.privacy_budget_summary_list.deserialize_json(
                data["privacyBudgetSummaries"]
            )
        )
    else:
        out["privacy_budget_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
