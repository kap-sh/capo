"""Generated from Smithy shape ``com.amazonaws.budgets#HistoricalOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_budgets.types.adjustment_period


class HistoricalOptions(TypedDict, closed=True):
    budget_adjustment_period: "capo_budgets.types.adjustment_period.AdjustmentPeriod"
    """<p>The number of budget periods included in the moving-average calculation that determines your auto-adjusted budget amount. The maximum value depends on the <code>TimeUnit</code> granularity of the budget:</p> <ul> <li> <p>For the <code>DAILY</code> granularity, the maximum value is <code>60</code>.</p> </li> <li> <p>For the <code>MONTHLY</code> granularity, the maximum value is <code>12</code>.</p> </li> <li> <p>For the <code>QUARTERLY</code> granularity, the maximum value is <code>4</code>.</p> </li> <li> <p>For the <code>ANNUALLY</code> granularity, the maximum value is <code>1</code>.</p> </li> </ul>"""
    look_back_available_periods: NotRequired[
        "capo_budgets.types.adjustment_period.AdjustmentPeriod"
    ]
    """<p>The integer that describes how many budget periods in your <code>BudgetAdjustmentPeriod</code> are included in the calculation of your current <code>BudgetLimit</code>. If the first budget period in your <code>BudgetAdjustmentPeriod</code> has no cost data, then that budget period isn’t included in the average that determines your budget limit. </p> <p>For example, if you set <code>BudgetAdjustmentPeriod</code> as <code>4</code> quarters, but your account had no cost data in the first quarter, then only the last three quarters are included in the calculation. In this scenario, <code>LookBackAvailablePeriods</code> returns <code>3</code>. </p> <p>You can’t set your own <code>LookBackAvailablePeriods</code>. The value is automatically calculated from the <code>BudgetAdjustmentPeriod</code> and your historical cost data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HistoricalOptions) -> dict:
    out: dict = {}
    out["BudgetAdjustmentPeriod"] = value["budget_adjustment_period"]
    if "look_back_available_periods" in value:
        out["LookBackAvailablePeriods"] = value["look_back_available_periods"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HistoricalOptions:
    out: HistoricalOptions = {}  # type: ignore[typeddict-item]
    if data.get("BudgetAdjustmentPeriod") is not None:
        out["budget_adjustment_period"] = data["BudgetAdjustmentPeriod"]
    else:
        out["budget_adjustment_period"] = 0
    if data.get("LookBackAvailablePeriods") is not None:
        out["look_back_available_periods"] = data["LookBackAvailablePeriods"]
    return out
