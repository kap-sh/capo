"""Generated from Smithy shape ``com.amazonaws.amp#LoggingFilter``."""

from typing_extensions import TypedDict


class LoggingFilter(TypedDict, closed=True):
    qsp_threshold: "int"
    """<p>The Query Samples Processed (QSP) threshold above which queries will be logged. Queries processing more samples than this threshold will be captured in logs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoggingFilter) -> dict:
    out: dict = {}
    out["qspThreshold"] = value["qsp_threshold"]
    return out


def deserialize_json(data: dict) -> LoggingFilter:
    out: LoggingFilter = {}  # type: ignore[typeddict-item]
    if data.get("qspThreshold") is not None:
        out["qsp_threshold"] = data["qspThreshold"]
    else:
        out["qsp_threshold"] = 0
    return out
