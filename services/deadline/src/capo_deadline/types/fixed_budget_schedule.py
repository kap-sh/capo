"""Generated from Smithy shape ``com.amazonaws.deadline#FixedBudgetSchedule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.ends_at
    import capo_deadline.types.starts_at


class FixedBudgetSchedule(TypedDict, closed=True):
    start_time: "capo_deadline.types.starts_at.StartsAt"
    """<p>When the budget starts.</p>"""
    end_time: "capo_deadline.types.ends_at.EndsAt"
    """<p>When the budget ends.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FixedBudgetSchedule) -> dict:
    out: dict = {}
    import capo_deadline.types.starts_at

    out["startTime"] = capo_deadline.types.starts_at.serialize_json(value["start_time"])
    import capo_deadline.types.ends_at

    out["endTime"] = capo_deadline.types.ends_at.serialize_json(value["end_time"])
    return out


def deserialize_json(data: dict) -> FixedBudgetSchedule:
    out: FixedBudgetSchedule = {}  # type: ignore[typeddict-item]
    if data.get("startTime") is not None:
        import capo_deadline.types.starts_at

        out["start_time"] = capo_deadline.types.starts_at.deserialize_json(
            data["startTime"]
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("endTime") is not None:
        import capo_deadline.types.ends_at

        out["end_time"] = capo_deadline.types.ends_at.deserialize_json(data["endTime"])
    else:
        import datetime

        out["end_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
