"""Generated from Smithy shape ``com.amazonaws.connect#CreateRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.rule_id


class CreateRuleResponse(TypedDict, closed=True):
    rule_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the rule.</p>"""
    rule_id: "capo_connect.types.rule_id.RuleId"
    """<p>A unique identifier for the rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRuleResponse) -> dict:
    out: dict = {}
    out["RuleArn"] = value["rule_arn"]
    out["RuleId"] = value["rule_id"]
    return out


def deserialize_json(data: dict) -> CreateRuleResponse:
    out: CreateRuleResponse = {}  # type: ignore[typeddict-item]
    if data.get("RuleArn") is not None:
        out["rule_arn"] = data["RuleArn"]
    else:
        out["rule_arn"] = ""
    if data.get("RuleId") is not None:
        out["rule_id"] = data["RuleId"]
    else:
        out["rule_id"] = ""
    return out
