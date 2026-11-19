"""Generated from Smithy shape ``com.amazonaws.elementalinference#EventBridgeDeliveryMode``."""

from typing import Literal, TypeAlias, cast

"""<p>Whether Elemental Inference sends a function's marked results to Amazon EventBridge.</p> <ul> <li> <p>ENABLED – Elemental Inference sends each result that is a JSON object with a top-level <code>eventBridge</code> field set to <code>true</code> as an event. </p> </li> <li> <p>DISABLED – Elemental Inference doesn't send events.</p> </li> </ul>"""
EventBridgeDeliveryMode: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EventBridgeDeliveryMode) -> str:
    return value


def deserialize_json(data: str) -> EventBridgeDeliveryMode:
    return cast(EventBridgeDeliveryMode, data)
