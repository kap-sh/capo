"""Generated from Smithy shape ``com.amazonaws.internetmonitor#ListHealthEventsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_internetmonitor.types.account_id
    import capo_internetmonitor.types.health_event_status
    import capo_internetmonitor.types.max_results
    import capo_internetmonitor.types.resource_name


class ListHealthEventsInput(TypedDict, closed=True):
    monitor_name: "capo_internetmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor.</p>"""
    start_time: NotRequired["datetime.datetime"]
    """<p>The time when a health event started.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The time when a health event ended. If the health event is still ongoing, then the end time is not set.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""
    max_results: NotRequired["capo_internetmonitor.types.max_results.MaxResults"]
    """<p>The number of health event objects that you want to return with this call. </p>"""
    event_status: NotRequired[
        "capo_internetmonitor.types.health_event_status.HealthEventStatus"
    ]
    """<p>The status of a health event.</p>"""
    linked_account_id: NotRequired["capo_internetmonitor.types.account_id.AccountId"]
    """<p>The account ID for an account that you've set up cross-account sharing for in Amazon CloudWatch Internet Monitor. You configure cross-account sharing by using Amazon CloudWatch Observability Access Manager. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cwim-cross-account.html">Internet Monitor cross-account observability</a> in the Amazon CloudWatch Internet Monitor User Guide.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListHealthEventsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListHealthEventsInput:
    out: ListHealthEventsInput = {}  # type: ignore[typeddict-item]
    return out
