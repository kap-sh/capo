"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DateRangeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.timestamp


class DateRangeFilter(TypedDict, closed=True):
    start_date_time: "capo_lex_models_v2.types.timestamp.Timestamp"
    """<p>A timestamp indicating the start date for the date range filter.</p>"""
    end_date_time: "capo_lex_models_v2.types.timestamp.Timestamp"
    """<p>A timestamp indicating the end date for the date range filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DateRangeFilter) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.timestamp

    out["startDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
        value["start_date_time"]
    )
    import capo_lex_models_v2.types.timestamp

    out["endDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
        value["end_date_time"]
    )
    return out


def deserialize_json(data: dict) -> DateRangeFilter:
    out: DateRangeFilter = {}  # type: ignore[typeddict-item]
    if data.get("startDateTime") is not None:
        import capo_lex_models_v2.types.timestamp

        out["start_date_time"] = capo_lex_models_v2.types.timestamp.deserialize_json(
            data["startDateTime"]
        )
    else:
        import datetime

        out["start_date_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("endDateTime") is not None:
        import capo_lex_models_v2.types.timestamp

        out["end_date_time"] = capo_lex_models_v2.types.timestamp.deserialize_json(
            data["endDateTime"]
        )
    else:
        import datetime

        out["end_date_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
