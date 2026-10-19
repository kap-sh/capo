"""Generated from Smithy shape ``com.amazonaws.backupsearch#TimeCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_backupsearch.types.time_condition_operator


class TimeCondition(TypedDict, closed=True):
    value: "datetime.datetime"
    """<p>This is the timestamp value of the time condition.</p>"""
    operator: "capo_backupsearch.types.time_condition_operator.TimeConditionOperator"
    """<p>A string that defines what values will be returned.</p> <p>If this is included, avoid combinations of operators that will return all possible values. For example, including both <code>EQUALS_TO</code> and <code>NOT_EQUALS_TO</code> with a value of <code>4</code> will return all values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeCondition) -> dict:
    out: dict = {}
    import capo_backupsearch.types._prelude.timestamp

    out["Value"] = capo_backupsearch.types._prelude.timestamp.serialize_json(
        value["value"]
    )
    import capo_backupsearch.types.time_condition_operator

    out["Operator"] = capo_backupsearch.types.time_condition_operator.serialize_json(
        value.get("operator", "EQUALS_TO")
    )
    return out


def deserialize_json(data: dict) -> TimeCondition:
    out: TimeCondition = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        import capo_backupsearch.types._prelude.timestamp

        out["value"] = capo_backupsearch.types._prelude.timestamp.deserialize_json(
            data["Value"]
        )
    else:
        import datetime

        out["value"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("Operator") is not None:
        import capo_backupsearch.types.time_condition_operator

        out["operator"] = (
            capo_backupsearch.types.time_condition_operator.deserialize_json(
                data["Operator"]
            )
        )
    else:
        out["operator"] = "EQUALS_TO"
    return out
