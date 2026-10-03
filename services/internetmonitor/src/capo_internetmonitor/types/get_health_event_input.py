"""Generated from Smithy shape ``com.amazonaws.internetmonitor#GetHealthEventInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_internetmonitor.types.account_id
    import capo_internetmonitor.types.health_event_name
    import capo_internetmonitor.types.resource_name


class GetHealthEventInput(TypedDict, closed=True):
    monitor_name: "capo_internetmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor.</p>"""
    event_id: "capo_internetmonitor.types.health_event_name.HealthEventName"
    """<p>The internally-generated identifier of a health event. Because <code>EventID</code> contains the forward slash (“/”) character, you must URL-encode the <code>EventID</code> field in the request URL.</p>"""
    linked_account_id: NotRequired["capo_internetmonitor.types.account_id.AccountId"]
    """<p>The account ID for an account that you've set up cross-account sharing for in Amazon CloudWatch Internet Monitor. You configure cross-account sharing by using Amazon CloudWatch Observability Access Manager. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cwim-cross-account.html">Internet Monitor cross-account observability</a> in the Amazon CloudWatch Internet Monitor User Guide.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetHealthEventInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetHealthEventInput:
    out: GetHealthEventInput = {}  # type: ignore[typeddict-item]
    return out
