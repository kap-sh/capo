"""Generated from Smithy shape ``com.amazonaws.supplychain#ListDataIntegrationEventsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.data_integration_event_list
    import capo_supplychain.types.data_integration_event_next_token


class ListDataIntegrationEventsResponse(TypedDict, closed=True):
    events: (
        "capo_supplychain.types.data_integration_event_list.DataIntegrationEventList"
    )
    """<p>The list of data integration events.</p>"""
    next_token: NotRequired[
        "capo_supplychain.types.data_integration_event_next_token.DataIntegrationEventNextToken"
    ]
    """<p>The pagination token to fetch the next page of the ListDataIntegrationEvents.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataIntegrationEventsResponse) -> dict:
    out: dict = {}
    import capo_supplychain.types.data_integration_event_list

    out["events"] = capo_supplychain.types.data_integration_event_list.serialize_json(
        value["events"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataIntegrationEventsResponse:
    out: ListDataIntegrationEventsResponse = {}  # type: ignore[typeddict-item]
    if data.get("events") is not None:
        import capo_supplychain.types.data_integration_event_list

        out["events"] = (
            capo_supplychain.types.data_integration_event_list.deserialize_json(
                data["events"]
            )
        )
    else:
        out["events"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
