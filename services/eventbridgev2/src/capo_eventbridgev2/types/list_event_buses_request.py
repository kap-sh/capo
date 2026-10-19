"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#ListEventBusesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.account_id
    import capo_eventbridgev2.types.event_bus_name
    import capo_eventbridgev2.types.max_results
    import capo_eventbridgev2.types.next_token


class ListEventBusesRequest(TypedDict, closed=True):
    name_prefix: NotRequired["capo_eventbridgev2.types.event_bus_name.EventBusName"]
    event_bus_account_id: NotRequired["capo_eventbridgev2.types.account_id.AccountId"]
    next_token: NotRequired["capo_eventbridgev2.types.next_token.NextToken"]
    max_results: NotRequired["capo_eventbridgev2.types.max_results.MaxResults"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListEventBusesRequest) -> dict:
    out: dict = {}
    if "name_prefix" in value:
        out["NamePrefix"] = value["name_prefix"]
    if "event_bus_account_id" in value:
        out["EventBusAccountId"] = value["event_bus_account_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> ListEventBusesRequest:
    out: ListEventBusesRequest = {}  # type: ignore[typeddict-item]
    if data.get("NamePrefix") is not None:
        out["name_prefix"] = data["NamePrefix"]
    if data.get("EventBusAccountId") is not None:
        out["event_bus_account_id"] = data["EventBusAccountId"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
