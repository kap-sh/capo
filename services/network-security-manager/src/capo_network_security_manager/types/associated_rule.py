"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#AssociatedRule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.rule_arn


class AssociatedRule(TypedDict, closed=True):
    rule_arn: "capo_network_security_manager.types.rule_arn.RuleArn"
    """<p>The ARN of the associated rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedRule) -> dict:
    out: dict = {}
    out["ruleArn"] = value["rule_arn"]
    return out


def deserialize_json(data: dict) -> AssociatedRule:
    out: AssociatedRule = {}  # type: ignore[typeddict-item]
    if data.get("ruleArn") is not None:
        out["rule_arn"] = data["ruleArn"]
    else:
        raise DeserializationError("AssociatedRule.rule_arn required")
    return out
