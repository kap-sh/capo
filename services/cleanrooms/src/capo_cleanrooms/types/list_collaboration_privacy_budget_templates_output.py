"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListCollaborationPrivacyBudgetTemplatesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.collaboration_privacy_budget_template_summary_list
    import capo_cleanrooms.types.pagination_token


class ListCollaborationPrivacyBudgetTemplatesOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    collaboration_privacy_budget_template_summaries: "capo_cleanrooms.types.collaboration_privacy_budget_template_summary_list.CollaborationPrivacyBudgetTemplateSummaryList"
    """<p>An array that summarizes the collaboration privacy budget templates. The summary includes collaboration information, creation information, the privacy budget type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCollaborationPrivacyBudgetTemplatesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_cleanrooms.types.collaboration_privacy_budget_template_summary_list

    out["collaborationPrivacyBudgetTemplateSummaries"] = (
        capo_cleanrooms.types.collaboration_privacy_budget_template_summary_list.serialize_json(
            value["collaboration_privacy_budget_template_summaries"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListCollaborationPrivacyBudgetTemplatesOutput:
    out: ListCollaborationPrivacyBudgetTemplatesOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("collaborationPrivacyBudgetTemplateSummaries") is not None:
        import capo_cleanrooms.types.collaboration_privacy_budget_template_summary_list

        out["collaboration_privacy_budget_template_summaries"] = (
            capo_cleanrooms.types.collaboration_privacy_budget_template_summary_list.deserialize_json(
                data["collaborationPrivacyBudgetTemplateSummaries"]
            )
        )
    else:
        out["collaboration_privacy_budget_template_summaries"] = []
    return out
