"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#ListResourcePoliciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.event_bus_arn
    import capo_eventbridgev2.types.max_results
    import capo_eventbridgev2.types.next_token


class ListResourcePoliciesRequest(TypedDict, closed=True):
    resource_arn: "capo_eventbridgev2.types.event_bus_arn.EventBusArn"
    next_token: NotRequired["capo_eventbridgev2.types.next_token.NextToken"]
    max_results: NotRequired["capo_eventbridgev2.types.max_results.MaxResults"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListResourcePoliciesRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> ListResourcePoliciesRequest:
    out: ListResourcePoliciesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
