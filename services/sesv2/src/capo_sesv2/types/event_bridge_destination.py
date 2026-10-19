"""Generated from Smithy shape ``com.amazonaws.sesv2#EventBridgeDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.amazon_resource_name


class EventBridgeDestination(TypedDict, closed=True):
    event_bus_arn: "capo_sesv2.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the Amazon EventBridge bus to publish email events to. Only the default bus is supported. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventBridgeDestination) -> dict:
    out: dict = {}
    out["EventBusArn"] = value["event_bus_arn"]
    return out


def deserialize_json(data: dict) -> EventBridgeDestination:
    out: EventBridgeDestination = {}  # type: ignore[typeddict-item]
    if data.get("EventBusArn") is not None:
        out["event_bus_arn"] = data["EventBusArn"]
    else:
        out["event_bus_arn"] = ""
    return out
