"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#DescribeEventBusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.event_bus_arn


class DescribeEventBusRequest(TypedDict, closed=True):
    event_bus_arn: "capo_eventbridgev2.types.event_bus_arn.EventBusArn"


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeEventBusRequest) -> dict:
    out: dict = {}
    out["EventBusArn"] = value["event_bus_arn"]
    return out


def deserialize_cbor(data: dict) -> DescribeEventBusRequest:
    out: DescribeEventBusRequest = {}  # type: ignore[typeddict-item]
    if data.get("EventBusArn") is not None:
        out["event_bus_arn"] = data["EventBusArn"]
    else:
        out["event_bus_arn"] = ""
    return out
