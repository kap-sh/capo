"""Generated from Smithy shape ``com.amazonaws.costexplorer#DateInterval``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.year_month_day


class DateInterval(TypedDict, closed=True):
    start: "capo_cost_explorer.types.year_month_day.YearMonthDay"
    """<p>The beginning of the time period. The start date is inclusive. For example, if <code>start</code> is <code>2017-01-01</code>, Amazon Web Services retrieves cost and usage data starting at <code>2017-01-01</code> up to the end date. The start date must be equal to or no later than the current date to avoid a validation error.</p>"""
    end: "capo_cost_explorer.types.year_month_day.YearMonthDay"
    """<p>The end of the time period. The end date is exclusive. For example, if <code>end</code> is <code>2017-05-01</code>, Amazon Web Services retrieves cost and usage data from the start date up to, but not including, <code>2017-05-01</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DateInterval) -> dict:
    out: dict = {}
    out["Start"] = value["start"]
    out["End"] = value["end"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DateInterval:
    out: DateInterval = {}  # type: ignore[typeddict-item]
    if data.get("Start") is not None:
        out["start"] = data["Start"]
    else:
        out["start"] = ""
    if data.get("End") is not None:
        out["end"] = data["End"]
    else:
        out["end"] = ""
    return out
