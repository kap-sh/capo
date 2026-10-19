"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MatchPrincipals``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.match_principal_entries


class MatchPrincipals(TypedDict, closed=True):
    any_of: "capo_bedrock_agentcore_control.types.match_principal_entries.MatchPrincipalEntries"
    """<p>A list of principal entries. The condition is met if any of the entries match the caller's identity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatchPrincipals) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.match_principal_entries

    out["anyOf"] = (
        capo_bedrock_agentcore_control.types.match_principal_entries.serialize_json(
            value["any_of"]
        )
    )
    return out


def deserialize_json(data: dict) -> MatchPrincipals:
    out: MatchPrincipals = {}  # type: ignore[typeddict-item]
    if data.get("anyOf") is not None:
        import capo_bedrock_agentcore_control.types.match_principal_entries

        out["any_of"] = (
            capo_bedrock_agentcore_control.types.match_principal_entries.deserialize_json(
                data["anyOf"]
            )
        )
    else:
        out["any_of"] = []
    return out
