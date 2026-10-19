"""Generated from Smithy shape ``com.amazonaws.backup#DateRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_backup.types.timestamp


class DateRange(TypedDict, closed=True):
    from_date: "capo_backup.types.timestamp.timestamp"
    """<p>This value is the beginning date, inclusive.</p> <p>The date and time are in Unix format and Coordinated Universal Time (UTC), and it is accurate to milliseconds (milliseconds are optional).</p>"""
    to_date: "capo_backup.types.timestamp.timestamp"
    """<p>This value is the end date, inclusive.</p> <p>The date and time are in Unix format and Coordinated Universal Time (UTC), and it is accurate to milliseconds (milliseconds are optional).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DateRange) -> dict:
    out: dict = {}
    import capo_backup.types.timestamp

    out["FromDate"] = capo_backup.types.timestamp.serialize_json(value["from_date"])
    import capo_backup.types.timestamp

    out["ToDate"] = capo_backup.types.timestamp.serialize_json(value["to_date"])
    return out


def deserialize_json(data: dict) -> DateRange:
    out: DateRange = {}  # type: ignore[typeddict-item]
    if data.get("FromDate") is not None:
        import capo_backup.types.timestamp

        out["from_date"] = capo_backup.types.timestamp.deserialize_json(
            data["FromDate"]
        )
    else:
        import datetime

        out["from_date"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("ToDate") is not None:
        import capo_backup.types.timestamp

        out["to_date"] = capo_backup.types.timestamp.deserialize_json(data["ToDate"])
    else:
        import datetime

        out["to_date"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
