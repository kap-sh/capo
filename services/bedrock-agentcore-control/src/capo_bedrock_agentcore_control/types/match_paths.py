"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MatchPaths``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.match_path_patterns


class MatchPaths(TypedDict, closed=True):
    any_of: "capo_bedrock_agentcore_control.types.match_path_patterns.MatchPathPatterns"
    """<p>A list of path patterns. The condition is met if the request path matches any of the patterns.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatchPaths) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.match_path_patterns

    out["anyOf"] = (
        capo_bedrock_agentcore_control.types.match_path_patterns.serialize_json(
            value["any_of"]
        )
    )
    return out


def deserialize_json(data: dict) -> MatchPaths:
    out: MatchPaths = {}  # type: ignore[typeddict-item]
    if data.get("anyOf") is not None:
        import capo_bedrock_agentcore_control.types.match_path_patterns

        out["any_of"] = (
            capo_bedrock_agentcore_control.types.match_path_patterns.deserialize_json(
                data["anyOf"]
            )
        )
    else:
        out["any_of"] = []
    return out
