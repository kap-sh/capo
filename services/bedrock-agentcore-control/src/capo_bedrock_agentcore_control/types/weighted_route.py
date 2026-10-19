"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#WeightedRoute``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.target_traffic_split_entries


class WeightedRoute(TypedDict, closed=True):
    traffic_split: "capo_bedrock_agentcore_control.types.target_traffic_split_entries.TargetTrafficSplitEntries"
    """<p>The traffic split entries defining how traffic is distributed between targets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WeightedRoute) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.target_traffic_split_entries

    out["trafficSplit"] = (
        capo_bedrock_agentcore_control.types.target_traffic_split_entries.serialize_json(
            value["traffic_split"]
        )
    )
    return out


def deserialize_json(data: dict) -> WeightedRoute:
    out: WeightedRoute = {}  # type: ignore[typeddict-item]
    if data.get("trafficSplit") is not None:
        import capo_bedrock_agentcore_control.types.target_traffic_split_entries

        out["traffic_split"] = (
            capo_bedrock_agentcore_control.types.target_traffic_split_entries.deserialize_json(
                data["trafficSplit"]
            )
        )
    else:
        out["traffic_split"] = []
    return out


def redact_sensitive(value: WeightedRoute) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "traffic_split" in value:
        import capo_bedrock_agentcore_control.types.target_traffic_split_entries

        out["traffic_split"] = (
            capo_bedrock_agentcore_control.types.target_traffic_split_entries.redact_sensitive(
                value["traffic_split"]
            )
        )
    return out
