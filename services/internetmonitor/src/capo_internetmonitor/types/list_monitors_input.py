"""Generated from Smithy shape ``com.amazonaws.internetmonitor#ListMonitorsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_internetmonitor.types.max_results


class ListMonitorsInput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""
    max_results: NotRequired["capo_internetmonitor.types.max_results.MaxResults"]
    """<p>The number of monitor objects that you want to return with this call.</p>"""
    monitor_status: NotRequired["str"]
    """<p>The status of a monitor. This includes the status of the data processing for the monitor and the status of the monitor itself.</p> <p>For information about the statuses for a monitor, see <a href="https://docs.aws.amazon.com/internet-monitor/latest/api/API_Monitor.html"> Monitor</a>.</p>"""
    include_linked_accounts: NotRequired["bool"]
    """<p>A boolean option that you can set to <code>TRUE</code> to include monitors for linked accounts in a list of monitors, when you've set up cross-account sharing in Amazon CloudWatch Internet Monitor. You configure cross-account sharing by using Amazon CloudWatch Observability Access Manager. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cwim-cross-account.html">Internet Monitor cross-account observability</a> in the Amazon CloudWatch Internet Monitor User Guide.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMonitorsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMonitorsInput:
    out: ListMonitorsInput = {}  # type: ignore[typeddict-item]
    return out
