"""Generated from Smithy shape ``com.amazonaws.quicksight#TimeRangeDrillDownFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.column_identifier
    import capo_quicksight.types.time_granularity
    import capo_quicksight.types.timestamp


class TimeRangeDrillDownFilter(TypedDict, closed=True):
    column: "capo_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that the filter is applied to.</p>"""
    range_minimum: "capo_quicksight.types.timestamp.Timestamp"
    """<p>The minimum value for the filter value range.</p>"""
    range_maximum: "capo_quicksight.types.timestamp.Timestamp"
    """<p>The maximum value for the filter value range.</p>"""
    time_granularity: "capo_quicksight.types.time_granularity.TimeGranularity"
    """<p>The level of time precision that is used to aggregate <code>DateTime</code> values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeRangeDrillDownFilter) -> dict:
    out: dict = {}
    import capo_quicksight.types.column_identifier

    out["Column"] = capo_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    import capo_quicksight.types.timestamp

    out["RangeMinimum"] = capo_quicksight.types.timestamp.serialize_json(
        value["range_minimum"]
    )
    import capo_quicksight.types.timestamp

    out["RangeMaximum"] = capo_quicksight.types.timestamp.serialize_json(
        value["range_maximum"]
    )
    import capo_quicksight.types.time_granularity

    out["TimeGranularity"] = capo_quicksight.types.time_granularity.serialize_json(
        value["time_granularity"]
    )
    return out


def deserialize_json(data: dict) -> TimeRangeDrillDownFilter:
    out: TimeRangeDrillDownFilter = {}  # type: ignore[typeddict-item]
    if data.get("Column") is not None:
        import capo_quicksight.types.column_identifier

        out["column"] = capo_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError("TimeRangeDrillDownFilter.column required")
    if data.get("RangeMinimum") is not None:
        import capo_quicksight.types.timestamp

        out["range_minimum"] = capo_quicksight.types.timestamp.deserialize_json(
            data["RangeMinimum"]
        )
    else:
        import datetime

        out["range_minimum"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("RangeMaximum") is not None:
        import capo_quicksight.types.timestamp

        out["range_maximum"] = capo_quicksight.types.timestamp.deserialize_json(
            data["RangeMaximum"]
        )
    else:
        import datetime

        out["range_maximum"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("TimeGranularity") is not None:
        import capo_quicksight.types.time_granularity

        out["time_granularity"] = (
            capo_quicksight.types.time_granularity.deserialize_json(
                data["TimeGranularity"]
            )
        )
    else:
        import typing

        out["time_granularity"] = typing.cast(
            "capo_quicksight.types.time_granularity.TimeGranularity", ""
        )
    return out
