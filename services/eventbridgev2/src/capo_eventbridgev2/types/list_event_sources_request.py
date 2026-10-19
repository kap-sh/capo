"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#ListEventSourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.event_bus_arn
    import capo_eventbridgev2.types.event_source_name
    import capo_eventbridgev2.types.max_results
    import capo_eventbridgev2.types.next_token


class ListEventSourcesRequest(TypedDict, closed=True):
    event_bus_arn: NotRequired["capo_eventbridgev2.types.event_bus_arn.EventBusArn"]
    name_prefix: NotRequired[
        "capo_eventbridgev2.types.event_source_name.EventSourceName"
    ]
    next_token: NotRequired["capo_eventbridgev2.types.next_token.NextToken"]
    max_results: NotRequired["capo_eventbridgev2.types.max_results.MaxResults"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListEventSourcesRequest) -> dict:
    out: dict = {}
    if "event_bus_arn" in value:
        out["EventBusArn"] = value["event_bus_arn"]
    if "name_prefix" in value:
        out["NamePrefix"] = value["name_prefix"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> ListEventSourcesRequest:
    out: ListEventSourcesRequest = {}  # type: ignore[typeddict-item]
    if data.get("EventBusArn") is not None:
        out["event_bus_arn"] = data["EventBusArn"]
    if data.get("NamePrefix") is not None:
        out["name_prefix"] = data["NamePrefix"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
