"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TargetTrafficSplitEntries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.target_traffic_split_entry

TargetTrafficSplitEntries: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.target_traffic_split_entry.TargetTrafficSplitEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetTrafficSplitEntries) -> list:
    import capo_bedrock_agentcore_control.types.target_traffic_split_entry

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.target_traffic_split_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TargetTrafficSplitEntries:
    import capo_bedrock_agentcore_control.types.target_traffic_split_entry

    out: TargetTrafficSplitEntries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.target_traffic_split_entry.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: TargetTrafficSplitEntries) -> list[Any]:
    import capo_bedrock_agentcore_control.types.target_traffic_split_entry

    return [
        capo_bedrock_agentcore_control.types.target_traffic_split_entry.redact_sensitive(
            item
        )
        for item in value
    ]
