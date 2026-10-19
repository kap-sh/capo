"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListPrivacyBudgetTemplatesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.pagination_token
    import capo_cleanrooms.types.privacy_budget_template_summary_list


class ListPrivacyBudgetTemplatesOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    privacy_budget_template_summaries: "capo_cleanrooms.types.privacy_budget_template_summary_list.PrivacyBudgetTemplateSummaryList"
    """<p>An array that summarizes the privacy budget templates. The summary includes collaboration information, creation information, and privacy budget type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPrivacyBudgetTemplatesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_cleanrooms.types.privacy_budget_template_summary_list

    out["privacyBudgetTemplateSummaries"] = (
        capo_cleanrooms.types.privacy_budget_template_summary_list.serialize_json(
            value["privacy_budget_template_summaries"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListPrivacyBudgetTemplatesOutput:
    out: ListPrivacyBudgetTemplatesOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("privacyBudgetTemplateSummaries") is not None:
        import capo_cleanrooms.types.privacy_budget_template_summary_list

        out["privacy_budget_template_summaries"] = (
            capo_cleanrooms.types.privacy_budget_template_summary_list.deserialize_json(
                data["privacyBudgetTemplateSummaries"]
            )
        )
    else:
        out["privacy_budget_template_summaries"] = []
    return out
