"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AccessBudgetDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.access_budget_type
    import capo_cleanrooms.types.auto_refresh_mode
    import capo_cleanrooms.types.budget
    import capo_cleanrooms.types.remaining_budget


class AccessBudgetDetails(TypedDict, closed=True):
    start_time: "datetime.datetime"
    """<p>The start time for the access budget period.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The end time for the access budget period.</p>"""
    remaining_budget: "capo_cleanrooms.types.remaining_budget.RemainingBudget"
    """<p>The remaining budget amount available for use within this access budget.</p>"""
    budget: "capo_cleanrooms.types.budget.Budget"
    """<p>The total budget allocation amount for this access budget.</p>"""
    budget_type: "capo_cleanrooms.types.access_budget_type.AccessBudgetType"
    """<p>Specifies the time period for limiting table usage in queries and jobs. For calendar-based periods, the budget can renew if auto refresh is enabled. For lifetime budgets, the limit applies to the total usage throughout the collaboration. Valid values are:</p> <p> <code>CALENDAR_DAY</code> - Limit table usage per day.</p> <p> <code>CALENDAR_WEEK</code> - Limit table usage per week.</p> <p> <code>CALENDAR_MONTH</code> - Limit table usage per month.</p> <p> <code>LIFETIME</code> - Limit total table usage for the collaboration duration.</p>"""
    auto_refresh: NotRequired["capo_cleanrooms.types.auto_refresh_mode.AutoRefreshMode"]
    """<p>Indicates whether the budget automatically refreshes for each time period specified in <code>budgetType</code>. Valid values are:</p> <p> <code>ENABLED</code> - The budget refreshes automatically at the start of each period.</p> <p> <code>DISABLED</code> - The budget must be refreshed manually.</p> <p> <code>NULL</code> - The value is null when <code>budgetType</code> is set to <code>LIFETIME</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessBudgetDetails) -> dict:
    out: dict = {}
    import capo_cleanrooms.types._prelude.timestamp

    out["startTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["start_time"]
    )
    if "end_time" in value:
        import capo_cleanrooms.types._prelude.timestamp

        out["endTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
            value["end_time"]
        )
    out["remainingBudget"] = value["remaining_budget"]
    out["budget"] = value["budget"]
    import capo_cleanrooms.types.access_budget_type

    out["budgetType"] = capo_cleanrooms.types.access_budget_type.serialize_json(
        value["budget_type"]
    )
    if "auto_refresh" in value:
        import capo_cleanrooms.types.auto_refresh_mode

        out["autoRefresh"] = capo_cleanrooms.types.auto_refresh_mode.serialize_json(
            value["auto_refresh"]
        )
    return out


def deserialize_json(data: dict) -> AccessBudgetDetails:
    out: AccessBudgetDetails = {}  # type: ignore[typeddict-item]
    if data.get("startTime") is not None:
        import capo_cleanrooms.types._prelude.timestamp

        out["start_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["startTime"]
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("endTime") is not None:
        import capo_cleanrooms.types._prelude.timestamp

        out["end_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["endTime"]
        )
    if data.get("remainingBudget") is not None:
        out["remaining_budget"] = data["remainingBudget"]
    else:
        out["remaining_budget"] = 0
    if data.get("budget") is not None:
        out["budget"] = data["budget"]
    else:
        out["budget"] = 0
    if data.get("budgetType") is not None:
        import capo_cleanrooms.types.access_budget_type

        out["budget_type"] = capo_cleanrooms.types.access_budget_type.deserialize_json(
            data["budgetType"]
        )
    else:
        import typing

        out["budget_type"] = typing.cast(
            "capo_cleanrooms.types.access_budget_type.AccessBudgetType", ""
        )
    if data.get("autoRefresh") is not None:
        import capo_cleanrooms.types.auto_refresh_mode

        out["auto_refresh"] = capo_cleanrooms.types.auto_refresh_mode.deserialize_json(
            data["autoRefresh"]
        )
    return out
