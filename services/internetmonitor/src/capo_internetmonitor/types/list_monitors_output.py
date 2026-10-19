"""Generated from Smithy shape ``com.amazonaws.internetmonitor#ListMonitorsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_internetmonitor.types.monitor_list


class ListMonitorsOutput(TypedDict, closed=True):
    monitors: "capo_internetmonitor.types.monitor_list.MonitorList"
    """<p>A list of monitors.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMonitorsOutput) -> dict:
    out: dict = {}
    import capo_internetmonitor.types.monitor_list

    out["Monitors"] = capo_internetmonitor.types.monitor_list.serialize_json(
        value["monitors"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMonitorsOutput:
    out: ListMonitorsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Monitors") is not None:
        import capo_internetmonitor.types.monitor_list

        out["monitors"] = capo_internetmonitor.types.monitor_list.deserialize_json(
            data["Monitors"]
        )
    else:
        out["monitors"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
