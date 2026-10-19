"""Generated from Smithy shape ``com.amazonaws.iotwireless#ListEventConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.event_notification_resource_type
    import capo_iot_wireless.types.max_results
    import capo_iot_wireless.types.next_token


class ListEventConfigurationsRequest(TypedDict, closed=True):
    resource_type: "capo_iot_wireless.types.event_notification_resource_type.EventNotificationResourceType"
    """<p>Resource type to filter event configurations.</p>"""
    max_results: NotRequired["capo_iot_wireless.types.max_results.MaxResults"]
    next_token: NotRequired["capo_iot_wireless.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventConfigurationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListEventConfigurationsRequest:
    out: ListEventConfigurationsRequest = {}  # type: ignore[typeddict-item]
    return out
