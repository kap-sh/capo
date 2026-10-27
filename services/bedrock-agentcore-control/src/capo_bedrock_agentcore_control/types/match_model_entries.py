"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MatchModelEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.match_model_entry

MatchModelEntries: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.match_model_entry.MatchModelEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: MatchModelEntries) -> list:
    import capo_bedrock_agentcore_control.types.match_model_entry

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.match_model_entry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MatchModelEntries:
    import capo_bedrock_agentcore_control.types.match_model_entry

    out: MatchModelEntries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.match_model_entry.deserialize_json(
                item
            )
        )
    return out
