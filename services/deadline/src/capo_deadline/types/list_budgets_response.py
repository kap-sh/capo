"""Generated from Smithy shape ``com.amazonaws.deadline#ListBudgetsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.budget_summaries
    import capo_deadline.types.next_token


class ListBudgetsResponse(TypedDict, closed=True):
    budgets: "capo_deadline.types.budget_summaries.BudgetSummaries"
    """<p>The budgets to include on the list.</p>"""
    next_token: NotRequired["capo_deadline.types.next_token.NextToken"]
    """<p>If Deadline Cloud returns <code>nextToken</code>, then there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page, call the operation again using the returned token. Keep all other arguments unchanged. If no results remain, then <code>nextToken</code> is set to <code>null</code>. Each pagination token expires after 24 hours. If you provide a token that isn't valid, then you receive an HTTP 400 <code>ValidationException</code> error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBudgetsResponse) -> dict:
    out: dict = {}
    import capo_deadline.types.budget_summaries

    out["budgets"] = capo_deadline.types.budget_summaries.serialize_json(
        value["budgets"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBudgetsResponse:
    out: ListBudgetsResponse = {}  # type: ignore[typeddict-item]
    if data.get("budgets") is not None:
        import capo_deadline.types.budget_summaries

        out["budgets"] = capo_deadline.types.budget_summaries.deserialize_json(
            data["budgets"]
        )
    else:
        raise DeserializationError("ListBudgetsResponse.budgets required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListBudgetsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "budgets" in value:
        import capo_deadline.types.budget_summaries

        out["budgets"] = capo_deadline.types.budget_summaries.redact_sensitive(
            value["budgets"]
        )
    return out
