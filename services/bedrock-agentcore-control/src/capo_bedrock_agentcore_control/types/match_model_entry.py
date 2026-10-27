"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MatchModelEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.match_operator
    import capo_bedrock_agentcore_control.types.model_pattern


class MatchModelEntry(TypedDict, closed=True):
    value: "capo_bedrock_agentcore_control.types.model_pattern.ModelPattern"
    """<p>The model ID or pattern to match. With the <code>StringLike</code> operator, you can use <code>*</code> and <code>?</code> as wildcards, for example <code>anthropic.claude-*</code>.</p>"""
    operator: "capo_bedrock_agentcore_control.types.match_operator.MatchOperator"
    """<p>The operator to use when comparing the requested model to the value:</p> <ul> <li> <p> <code>StringEquals</code> – Requires an exact match.</p> </li> <li> <p> <code>StringLike</code> – Supports wildcard patterns using <code>*</code> and <code>?</code>. This is the default.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatchModelEntry) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    import capo_bedrock_agentcore_control.types.match_operator

    out["operator"] = (
        capo_bedrock_agentcore_control.types.match_operator.serialize_json(
            value.get("operator", "StringLike")
        )
    )
    return out


def deserialize_json(data: dict) -> MatchModelEntry:
    out: MatchModelEntry = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    if data.get("operator") is not None:
        import capo_bedrock_agentcore_control.types.match_operator

        out["operator"] = (
            capo_bedrock_agentcore_control.types.match_operator.deserialize_json(
                data["operator"]
            )
        )
    else:
        out["operator"] = "StringLike"
    return out
