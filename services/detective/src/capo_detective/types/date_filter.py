"""Generated from Smithy shape ``com.amazonaws.detective#DateFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_detective.types.timestamp


class DateFilter(TypedDict, closed=True):
    start_inclusive: "capo_detective.types.timestamp.Timestamp"
    """<p>A timestamp representing the start of the time period from when data is filtered, including the start date.</p>"""
    end_inclusive: "capo_detective.types.timestamp.Timestamp"
    """<p>A timestamp representing the end date of the time period until when data is filtered, including the end date.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DateFilter) -> dict:
    out: dict = {}
    import capo_detective.types.timestamp

    out["StartInclusive"] = capo_detective.types.timestamp.serialize_json(
        value["start_inclusive"]
    )
    import capo_detective.types.timestamp

    out["EndInclusive"] = capo_detective.types.timestamp.serialize_json(
        value["end_inclusive"]
    )
    return out


def deserialize_json(data: dict) -> DateFilter:
    out: DateFilter = {}  # type: ignore[typeddict-item]
    if data.get("StartInclusive") is not None:
        import capo_detective.types.timestamp

        out["start_inclusive"] = capo_detective.types.timestamp.deserialize_json(
            data["StartInclusive"]
        )
    else:
        import datetime

        out["start_inclusive"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("EndInclusive") is not None:
        import capo_detective.types.timestamp

        out["end_inclusive"] = capo_detective.types.timestamp.deserialize_json(
            data["EndInclusive"]
        )
    else:
        import datetime

        out["end_inclusive"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
