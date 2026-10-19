"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#QueryDataPoint``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime


class QueryDataPoint(TypedDict, closed=True):
    timestamp: "datetime.datetime"
    """<p>The timestamp of the data point.</p>"""
    query_count: "int"
    """<p>The number of queries at this data point.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryDataPoint) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types._prelude.timestamp

    out["timestamp"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
        value["timestamp"]
    )
    out["queryCount"] = value["query_count"]
    return out


def deserialize_json(data: dict) -> QueryDataPoint:
    out: QueryDataPoint = {}  # type: ignore[typeddict-item]
    if data.get("timestamp") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["timestamp"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["timestamp"]
            )
        )
    else:
        import datetime

        out["timestamp"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("queryCount") is not None:
        out["query_count"] = data["queryCount"]
    else:
        out["query_count"] = 0
    return out
