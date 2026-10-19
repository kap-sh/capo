"""Generated from Smithy shape ``com.amazonaws.quicksight#WhatIfPointScenario``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.double
    import capo_quicksight.types.timestamp


class WhatIfPointScenario(TypedDict, closed=True):
    date: "capo_quicksight.types.timestamp.Timestamp"
    """<p>The date that you need the forecast results for.</p>"""
    value: "capo_quicksight.types.double.Double"
    """<p>The target value that you want to meet for the provided date.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WhatIfPointScenario) -> dict:
    out: dict = {}
    import capo_quicksight.types.timestamp

    out["Date"] = capo_quicksight.types.timestamp.serialize_json(value["date"])
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


def deserialize_json(data: dict) -> WhatIfPointScenario:
    out: WhatIfPointScenario = {}  # type: ignore[typeddict-item]
    if data.get("Date") is not None:
        import capo_quicksight.types.timestamp

        out["date"] = capo_quicksight.types.timestamp.deserialize_json(data["Date"])
    else:
        import datetime

        out["date"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("Value") is not None:
        out["value"] = float(data["Value"])
    else:
        out["value"] = 0
    return out
