"""Generated from Smithy shape ``com.amazonaws.devopsagent#MonthlyRecurrence``."""

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError


class MonthlyRecurrence(TypedDict, closed=True):
    day_of_month: "int"
    """<p>Day of month the window recurs on</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MonthlyRecurrence) -> dict:
    out: dict = {}
    out["dayOfMonth"] = value["day_of_month"]
    return out


def deserialize_json(data: dict) -> MonthlyRecurrence:
    out: MonthlyRecurrence = {}  # type: ignore[typeddict-item]
    if data.get("dayOfMonth") is not None:
        out["day_of_month"] = data["dayOfMonth"]
    else:
        raise DeserializationError("MonthlyRecurrence.day_of_month required")
    return out
