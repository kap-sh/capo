"""Generated from Smithy shape ``com.amazonaws.supplychain#ListDataIntegrationEventsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.data_integration_event_max_results
    import capo_supplychain.types.data_integration_event_next_token
    import capo_supplychain.types.data_integration_event_type
    import capo_supplychain.types.uuid


class ListDataIntegrationEventsRequest(TypedDict, closed=True):
    instance_id: "capo_supplychain.types.uuid.UUID"
    """<p>The Amazon Web Services Supply Chain instance identifier.</p>"""
    event_type: NotRequired[
        "capo_supplychain.types.data_integration_event_type.DataIntegrationEventType"
    ]
    """<p>List data integration events for the specified eventType.</p>"""
    next_token: NotRequired[
        "capo_supplychain.types.data_integration_event_next_token.DataIntegrationEventNextToken"
    ]
    """<p>The pagination token to fetch the next page of the data integration events.</p>"""
    max_results: NotRequired[
        "capo_supplychain.types.data_integration_event_max_results.DataIntegrationEventMaxResults"
    ]
    """<p>Specify the maximum number of data integration events to fetch in one paginated request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataIntegrationEventsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDataIntegrationEventsRequest:
    out: ListDataIntegrationEventsRequest = {}  # type: ignore[typeddict-item]
    return out
