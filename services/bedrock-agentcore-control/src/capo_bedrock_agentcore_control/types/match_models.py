"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MatchModels``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.match_model_entries


class MatchModels(TypedDict, closed=True):
    any_of: "capo_bedrock_agentcore_control.types.match_model_entries.MatchModelEntries"
    """<p>A list of model entries. The condition is met if the requested model matches any of the entries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatchModels) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.match_model_entries

    out["anyOf"] = (
        capo_bedrock_agentcore_control.types.match_model_entries.serialize_json(
            value["any_of"]
        )
    )
    return out


def deserialize_json(data: dict) -> MatchModels:
    out: MatchModels = {}  # type: ignore[typeddict-item]
    if data.get("anyOf") is not None:
        import capo_bedrock_agentcore_control.types.match_model_entries

        out["any_of"] = (
            capo_bedrock_agentcore_control.types.match_model_entries.deserialize_json(
                data["anyOf"]
            )
        )
    else:
        out["any_of"] = []
    return out
