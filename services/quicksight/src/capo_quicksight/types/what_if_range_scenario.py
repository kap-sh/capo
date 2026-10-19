"""Generated from Smithy shape ``com.amazonaws.quicksight#WhatIfRangeScenario``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.double
    import capo_quicksight.types.timestamp


class WhatIfRangeScenario(TypedDict, closed=True):
    start_date: "capo_quicksight.types.timestamp.Timestamp"
    """<p>The start date in the date range that you need the forecast results for.</p>"""
    end_date: "capo_quicksight.types.timestamp.Timestamp"
    """<p>The end date in the date range that you need the forecast results for.</p>"""
    value: "capo_quicksight.types.double.Double"
    """<p>The target value that you want to meet for the provided date range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WhatIfRangeScenario) -> dict:
    out: dict = {}
    import capo_quicksight.types.timestamp

    out["StartDate"] = capo_quicksight.types.timestamp.serialize_json(
        value["start_date"]
    )
    import capo_quicksight.types.timestamp

    out["EndDate"] = capo_quicksight.types.timestamp.serialize_json(value["end_date"])
    out["Value"] = (
        "NaN"
        if value.get("value", 0) != value.get("value", 0)
        else "Infinity"
        if value.get("value", 0) == float("inf")
        else "-Infinity"
        if value.get("value", 0) == float("-inf")
        else value.get("value", 0)
    )
    return out


def deserialize_json(data: dict) -> WhatIfRangeScenario:
    out: WhatIfRangeScenario = {}  # type: ignore[typeddict-item]
    if data.get("StartDate") is not None:
        import capo_quicksight.types.timestamp

        out["start_date"] = capo_quicksight.types.timestamp.deserialize_json(
            data["StartDate"]
        )
    else:
        import datetime

        out["start_date"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("EndDate") is not None:
        import capo_quicksight.types.timestamp

        out["end_date"] = capo_quicksight.types.timestamp.deserialize_json(
            data["EndDate"]
        )
    else:
        import datetime

        out["end_date"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("Value") is not None:
        out["value"] = float(data["Value"])
    else:
        out["value"] = 0
    return out
