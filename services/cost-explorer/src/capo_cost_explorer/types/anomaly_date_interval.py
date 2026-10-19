"""Generated from Smithy shape ``com.amazonaws.costexplorer#AnomalyDateInterval``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.year_month_day


class AnomalyDateInterval(TypedDict, closed=True):
    start_date: "capo_cost_explorer.types.year_month_day.YearMonthDay"
    """<p>The first date an anomaly was observed. </p>"""
    end_date: NotRequired["capo_cost_explorer.types.year_month_day.YearMonthDay"]
    """<p>The last date an anomaly was observed. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnomalyDateInterval) -> dict:
    out: dict = {}
    out["StartDate"] = value["start_date"]
    if "end_date" in value:
        out["EndDate"] = value["end_date"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AnomalyDateInterval:
    out: AnomalyDateInterval = {}  # type: ignore[typeddict-item]
    if data.get("StartDate") is not None:
        out["start_date"] = data["StartDate"]
    else:
        out["start_date"] = ""
    if data.get("EndDate") is not None:
        out["end_date"] = data["EndDate"]
    return out
