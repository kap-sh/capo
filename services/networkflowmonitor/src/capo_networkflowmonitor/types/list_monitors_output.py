"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#ListMonitorsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.monitor_list


class ListMonitorsOutput(TypedDict, closed=True):
    monitors: "capo_networkflowmonitor.types.monitor_list.MonitorList"
    """<p>The monitors that are in an account.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMonitorsOutput) -> dict:
    out: dict = {}
    import capo_networkflowmonitor.types.monitor_list

    out["monitors"] = capo_networkflowmonitor.types.monitor_list.serialize_json(
        value["monitors"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMonitorsOutput:
    out: ListMonitorsOutput = {}  # type: ignore[typeddict-item]
    if data.get("monitors") is not None:
        import capo_networkflowmonitor.types.monitor_list

        out["monitors"] = capo_networkflowmonitor.types.monitor_list.deserialize_json(
            data["monitors"]
        )
    else:
        out["monitors"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
