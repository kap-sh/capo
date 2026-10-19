"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AggregatedValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.aggregates
    import capo_iotsitewise.types.quality
    import capo_iotsitewise.types.timestamp


class AggregatedValue(TypedDict, closed=True):
    timestamp: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the aggregating computations occurred, in Unix epoch time.</p>"""
    quality: NotRequired["capo_iotsitewise.types.quality.Quality"]
    """<p>The quality of the aggregated data.</p>"""
    value: "capo_iotsitewise.types.aggregates.Aggregates"
    """<p>The value of the aggregates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AggregatedValue) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.timestamp

    out["timestamp"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["timestamp"]
    )
    if "quality" in value:
        import capo_iotsitewise.types.quality

        out["quality"] = capo_iotsitewise.types.quality.serialize_json(value["quality"])
    import capo_iotsitewise.types.aggregates

    out["value"] = capo_iotsitewise.types.aggregates.serialize_json(value["value"])
    return out


def deserialize_json(data: dict) -> AggregatedValue:
    out: AggregatedValue = {}  # type: ignore[typeddict-item]
    if data.get("timestamp") is not None:
        import capo_iotsitewise.types.timestamp

        out["timestamp"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["timestamp"]
        )
    else:
        import datetime

        out["timestamp"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("quality") is not None:
        import capo_iotsitewise.types.quality

        out["quality"] = capo_iotsitewise.types.quality.deserialize_json(
            data["quality"]
        )
    if data.get("value") is not None:
        import capo_iotsitewise.types.aggregates

        out["value"] = capo_iotsitewise.types.aggregates.deserialize_json(data["value"])
    else:
        raise DeserializationError("AggregatedValue.value required")
    return out
