"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#GetMonitorScopeSuggestionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.max_results
    import capo_networkflowmonitor.types.monitor_arn


class GetMonitorScopeSuggestionsInput(TypedDict, closed=True):
    monitor_arn: "capo_networkflowmonitor.types.monitor_arn.MonitorArn"
    """<p>The Amazon Resource Name (ARN) of the monitor that you want to return scope suggestions for.</p>"""
    max_results: NotRequired["capo_networkflowmonitor.types.max_results.MaxResults"]
    """<p>The number of query results that you want to return with this call.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMonitorScopeSuggestionsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMonitorScopeSuggestionsInput:
    out: GetMonitorScopeSuggestionsInput = {}  # type: ignore[typeddict-item]
    return out
