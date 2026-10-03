"""Generated from Smithy shape ``com.amazonaws.internetmonitor#GetMonitorInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_internetmonitor.types.account_id
    import capo_internetmonitor.types.resource_name


class GetMonitorInput(TypedDict, closed=True):
    monitor_name: "capo_internetmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor.</p>"""
    linked_account_id: NotRequired["capo_internetmonitor.types.account_id.AccountId"]
    """<p>The account ID for an account that you've set up cross-account sharing for in Amazon CloudWatch Internet Monitor. You configure cross-account sharing by using Amazon CloudWatch Observability Access Manager. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cwim-cross-account.html">Internet Monitor cross-account observability</a> in the Amazon CloudWatch Internet Monitor User Guide.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMonitorInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMonitorInput:
    out: GetMonitorInput = {}  # type: ignore[typeddict-item]
    return out
