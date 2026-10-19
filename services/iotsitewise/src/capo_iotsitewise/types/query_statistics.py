"""Generated from Smithy shape ``com.amazonaws.iotsitewise#QueryStatistics``."""

from typing_extensions import TypedDict


class QueryStatistics(TypedDict, closed=True):
    row_count: "int"
    """<p>The total number of rows returned by the query.</p>"""
    bytes_scanned: "int"
    """<p>The total number of bytes scanned during query execution.</p>"""
    execution_time_in_millis: "int"
    """<p>The total query execution time, in milliseconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryStatistics) -> dict:
    out: dict = {}
    out["rowCount"] = value["row_count"]
    out["bytesScanned"] = value["bytes_scanned"]
    out["executionTimeInMillis"] = value["execution_time_in_millis"]
    return out


def deserialize_json(data: dict) -> QueryStatistics:
    out: QueryStatistics = {}  # type: ignore[typeddict-item]
    if data.get("rowCount") is not None:
        out["row_count"] = data["rowCount"]
    else:
        out["row_count"] = 0
    if data.get("bytesScanned") is not None:
        out["bytes_scanned"] = data["bytesScanned"]
    else:
        out["bytes_scanned"] = 0
    if data.get("executionTimeInMillis") is not None:
        out["execution_time_in_millis"] = data["executionTimeInMillis"]
    else:
        out["execution_time_in_millis"] = 0
    return out
