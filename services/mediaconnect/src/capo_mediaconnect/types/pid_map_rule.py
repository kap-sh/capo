"""Generated from Smithy shape ``com.amazonaws.mediaconnect#PidMapRule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.action_string


class PidMapRule(TypedDict, closed=True):
    match_expression: "str"
    """<p>An expression that selects the elementary streams that this rule applies to.</p>"""
    action: "capo_mediaconnect.types.action_string.ActionString"
    """<p>The action to apply to the elementary streams that match this rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PidMapRule) -> dict:
    out: dict = {}
    out["matchExpression"] = value["match_expression"]
    out["action"] = value["action"]
    return out


def deserialize_json(data: dict) -> PidMapRule:
    out: PidMapRule = {}  # type: ignore[typeddict-item]
    if data.get("matchExpression") is not None:
        out["match_expression"] = data["matchExpression"]
    else:
        out["match_expression"] = ""
    if data.get("action") is not None:
        out["action"] = data["action"]
    else:
        out["action"] = ""
    return out
