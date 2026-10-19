"""Generated from Smithy shape ``com.amazonaws.sustainability#TimePeriod``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sustainability.types.timestamp


class TimePeriod(TypedDict, closed=True):
    start: "capo_sustainability.types.timestamp.Timestamp"
    """<p>The start (inclusive) of the time period. ISO-8601 formatted timestamp, for example: <code>YYYY-MM-DDThh:mm:ss.sssZ</code> </p>"""
    end: "capo_sustainability.types.timestamp.Timestamp"
    """<p>The end (exclusive) of the time period. ISO-8601 formatted timestamp, for example: <code>YYYY-MM-DDThh:mm:ss.sssZ</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimePeriod) -> dict:
    out: dict = {}
    import capo_sustainability.types.timestamp

    out["Start"] = capo_sustainability.types.timestamp.serialize_json(value["start"])
    import capo_sustainability.types.timestamp

    out["End"] = capo_sustainability.types.timestamp.serialize_json(value["end"])
    return out


def deserialize_json(data: dict) -> TimePeriod:
    out: TimePeriod = {}  # type: ignore[typeddict-item]
    if data.get("Start") is not None:
        import capo_sustainability.types.timestamp

        out["start"] = capo_sustainability.types.timestamp.deserialize_json(
            data["Start"]
        )
    else:
        import datetime

        out["start"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("End") is not None:
        import capo_sustainability.types.timestamp

        out["end"] = capo_sustainability.types.timestamp.deserialize_json(data["End"])
    else:
        import datetime

        out["end"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
