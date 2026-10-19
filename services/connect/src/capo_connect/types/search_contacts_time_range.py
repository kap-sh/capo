"""Generated from Smithy shape ``com.amazonaws.connect#SearchContactsTimeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.search_contacts_time_range_type
    import capo_connect.types.timestamp


class SearchContactsTimeRange(TypedDict, closed=True):
    type: (
        "capo_connect.types.search_contacts_time_range_type.SearchContactsTimeRangeType"
    )
    """<p>The type of timestamp to search.</p>"""
    start_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The start time of the time range.</p>"""
    end_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The end time of the time range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchContactsTimeRange) -> dict:
    out: dict = {}
    import capo_connect.types.search_contacts_time_range_type

    out["Type"] = capo_connect.types.search_contacts_time_range_type.serialize_json(
        value["type"]
    )
    import capo_connect.types.timestamp

    out["StartTime"] = capo_connect.types.timestamp.serialize_json(value["start_time"])
    import capo_connect.types.timestamp

    out["EndTime"] = capo_connect.types.timestamp.serialize_json(value["end_time"])
    return out


def deserialize_json(data: dict) -> SearchContactsTimeRange:
    out: SearchContactsTimeRange = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_connect.types.search_contacts_time_range_type

        out["type"] = (
            capo_connect.types.search_contacts_time_range_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_connect.types.search_contacts_time_range_type.SearchContactsTimeRangeType",
            "",
        )
    if data.get("StartTime") is not None:
        import capo_connect.types.timestamp

        out["start_time"] = capo_connect.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("EndTime") is not None:
        import capo_connect.types.timestamp

        out["end_time"] = capo_connect.types.timestamp.deserialize_json(data["EndTime"])
    else:
        import datetime

        out["end_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
