"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessHookEventBridgeTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_event_bridge_bus_arn


class HarnessHookEventBridgeTarget(TypedDict, closed=True):
    arn: "capo_bedrock_agentcore_control.types.harness_event_bridge_bus_arn.HarnessEventBridgeBusArn"
    """<p>The ARN of the Amazon EventBridge event bus to send hook events to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessHookEventBridgeTarget) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> HarnessHookEventBridgeTarget:
    out: HarnessHookEventBridgeTarget = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    return out
