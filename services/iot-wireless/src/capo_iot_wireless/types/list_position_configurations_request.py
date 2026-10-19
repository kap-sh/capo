"""Generated from Smithy shape ``com.amazonaws.iotwireless#ListPositionConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.max_results
    import capo_iot_wireless.types.next_token
    import capo_iot_wireless.types.position_resource_type


class ListPositionConfigurationsRequest(TypedDict, closed=True):
    resource_type: NotRequired[
        "capo_iot_wireless.types.position_resource_type.PositionResourceType"
    ]
    """<p>Resource type for which position configurations are listed.</p>"""
    max_results: NotRequired["capo_iot_wireless.types.max_results.MaxResults"]
    next_token: NotRequired["capo_iot_wireless.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPositionConfigurationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPositionConfigurationsRequest:
    out: ListPositionConfigurationsRequest = {}  # type: ignore[typeddict-item]
    return out
