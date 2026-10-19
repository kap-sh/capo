"""Generated from Smithy shape ``com.amazonaws.rtbfabric#LinkApplicationLogSampling``."""

from typing_extensions import TypedDict


class LinkApplicationLogSampling(TypedDict, closed=True):
    error_log: "float"
    """<p>An error log entry.</p>"""
    filter_log: "float"
    """<p>A filter log entry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LinkApplicationLogSampling) -> dict:
    out: dict = {}
    out["errorLog"] = (
        "NaN"
        if value["error_log"] != value["error_log"]
        else "Infinity"
        if value["error_log"] == float("inf")
        else "-Infinity"
        if value["error_log"] == float("-inf")
        else value["error_log"]
    )
    out["filterLog"] = (
        "NaN"
        if value["filter_log"] != value["filter_log"]
        else "Infinity"
        if value["filter_log"] == float("inf")
        else "-Infinity"
        if value["filter_log"] == float("-inf")
        else value["filter_log"]
    )
    return out


def deserialize_json(data: dict) -> LinkApplicationLogSampling:
    out: LinkApplicationLogSampling = {}  # type: ignore[typeddict-item]
    if data.get("errorLog") is not None:
        out["error_log"] = float(data["errorLog"])
    else:
        out["error_log"] = 0.0
    if data.get("filterLog") is not None:
        out["filter_log"] = float(data["filterLog"])
    else:
        out["filter_log"] = 0.0
    return out
