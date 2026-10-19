"""Generated from Smithy shape ``com.amazonaws.budgets#DescribeBudgetPerformanceHistoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_budgets.types.account_id
    import capo_budgets.types.budget_name
    import capo_budgets.types.generic_string
    import capo_budgets.types.max_results
    import capo_budgets.types.time_period


class DescribeBudgetPerformanceHistoryRequest(TypedDict, closed=True):
    account_id: "capo_budgets.types.account_id.AccountId"
    budget_name: "capo_budgets.types.budget_name.BudgetName"
    time_period: NotRequired["capo_budgets.types.time_period.TimePeriod"]
    """<p>Retrieves how often the budget went into an <code>ALARM</code> state for the specified time period.</p>"""
    max_results: NotRequired["capo_budgets.types.max_results.MaxResults"]
    next_token: NotRequired["capo_budgets.types.generic_string.GenericString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBudgetPerformanceHistoryRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["BudgetName"] = value["budget_name"]
    if "time_period" in value:
        import capo_budgets.types.time_period

        out["TimePeriod"] = capo_budgets.types.time_period.serialize_aws_json_1_1(
            value["time_period"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBudgetPerformanceHistoryRequest:
    out: DescribeBudgetPerformanceHistoryRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    else:
        out["account_id"] = ""
    if data.get("BudgetName") is not None:
        out["budget_name"] = data["BudgetName"]
    else:
        out["budget_name"] = ""
    if data.get("TimePeriod") is not None:
        import capo_budgets.types.time_period

        out["time_period"] = capo_budgets.types.time_period.deserialize_aws_json_1_1(
            data["TimePeriod"]
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
