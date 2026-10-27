"""Generated from Smithy shape ``com.amazonaws.deadline#DateTimeFilterExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.comparison_operator
    import capo_deadline.types.string
    import capo_deadline.types.timestamp


class DateTimeFilterExpression(TypedDict, closed=True):
    name: "capo_deadline.types.string.String"
    """The name of the date-time field to filter on."""
    operator: "capo_deadline.types.comparison_operator.ComparisonOperator"
    """The type of comparison to use to filter the results."""
    date_time: "capo_deadline.types.timestamp.Timestamp"
    """The date and time."""


# --- restJson1 ser/de ---
def serialize_json(value: DateTimeFilterExpression) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_deadline.types.comparison_operator

    out["operator"] = capo_deadline.types.comparison_operator.serialize_json(
        value["operator"]
    )
    import capo_deadline._protocol.serialize

    out["dateTime"] = capo_deadline._protocol.serialize.fmt_date_time(
        value["date_time"]
    )
    return out


def deserialize_json(data: dict) -> DateTimeFilterExpression:
    out: DateTimeFilterExpression = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("operator") is not None:
        import capo_deadline.types.comparison_operator

        out["operator"] = capo_deadline.types.comparison_operator.deserialize_json(
            data["operator"]
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_deadline.types.comparison_operator.ComparisonOperator", ""
        )
    if data.get("dateTime") is not None:
        import datetime

        out["date_time"] = datetime.datetime.fromisoformat(
            data["dateTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["date_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
