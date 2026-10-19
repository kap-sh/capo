"""Generated from Smithy shape ``com.amazonaws.applicationsignals#RecurrenceRule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.expression


class RecurrenceRule(TypedDict, closed=True):
    expression: "capo_application_signals.types.expression.Expression"
    """<p>A cron or rate expression that specifies the schedule for the exclusion window.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecurrenceRule) -> dict:
    out: dict = {}
    out["Expression"] = value["expression"]
    return out


def deserialize_json(data: dict) -> RecurrenceRule:
    out: RecurrenceRule = {}  # type: ignore[typeddict-item]
    if data.get("Expression") is not None:
        out["expression"] = data["Expression"]
    else:
        out["expression"] = ""
    return out
