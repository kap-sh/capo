"""Generated from Smithy shape ``com.amazonaws.m2#LogGroupSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_m2.types.log_group_identifier
    import capo_m2.types.string20


class LogGroupSummary(TypedDict, closed=True):
    log_type: "capo_m2.types.string20.String20"
    """<p>The type of log.</p>"""
    log_group_name: "capo_m2.types.log_group_identifier.LogGroupIdentifier"
    """<p>The name of the log group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogGroupSummary) -> dict:
    out: dict = {}
    out["logType"] = value["log_type"]
    out["logGroupName"] = value["log_group_name"]
    return out


def deserialize_json(data: dict) -> LogGroupSummary:
    out: LogGroupSummary = {}  # type: ignore[typeddict-item]
    if data.get("logType") is not None:
        out["log_type"] = data["logType"]
    else:
        out["log_type"] = ""
    if data.get("logGroupName") is not None:
        out["log_group_name"] = data["logGroupName"]
    else:
        out["log_group_name"] = ""
    return out
