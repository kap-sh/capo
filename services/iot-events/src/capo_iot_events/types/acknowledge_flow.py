"""Generated from Smithy shape ``com.amazonaws.iotevents#AcknowledgeFlow``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.acknowledge_flow_enabled


class AcknowledgeFlow(TypedDict, closed=True):
    enabled: "capo_iot_events.types.acknowledge_flow_enabled.AcknowledgeFlowEnabled"
    """<p>The value must be <code>TRUE</code> or <code>FALSE</code>. If <code>TRUE</code>, you receive a notification when the alarm state changes. You must choose to acknowledge the notification before the alarm state can return to <code>NORMAL</code>. If <code>FALSE</code>, you won't receive notifications. The alarm automatically changes to the <code>NORMAL</code> state when the input property value returns to the specified range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcknowledgeFlow) -> dict:
    out: dict = {}
    out["enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> AcknowledgeFlow:
    out: AcknowledgeFlow = {}  # type: ignore[typeddict-item]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    return out
