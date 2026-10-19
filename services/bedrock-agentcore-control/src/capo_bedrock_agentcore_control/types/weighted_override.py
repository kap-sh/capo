"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#WeightedOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.traffic_split_entries


class WeightedOverride(TypedDict, closed=True):
    traffic_split: (
        "capo_bedrock_agentcore_control.types.traffic_split_entries.TrafficSplitEntries"
    )
    """<p>The traffic split entries defining how traffic is distributed between configuration bundle versions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WeightedOverride) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.traffic_split_entries

    out["trafficSplit"] = (
        capo_bedrock_agentcore_control.types.traffic_split_entries.serialize_json(
            value["traffic_split"]
        )
    )
    return out


def deserialize_json(data: dict) -> WeightedOverride:
    out: WeightedOverride = {}  # type: ignore[typeddict-item]
    if data.get("trafficSplit") is not None:
        import capo_bedrock_agentcore_control.types.traffic_split_entries

        out["traffic_split"] = (
            capo_bedrock_agentcore_control.types.traffic_split_entries.deserialize_json(
                data["trafficSplit"]
            )
        )
    else:
        out["traffic_split"] = []
    return out
