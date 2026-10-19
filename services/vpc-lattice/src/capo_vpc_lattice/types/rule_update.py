"""Generated from Smithy shape ``com.amazonaws.vpclattice#RuleUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.rule_action
    import capo_vpc_lattice.types.rule_identifier
    import capo_vpc_lattice.types.rule_match
    import capo_vpc_lattice.types.rule_priority


class RuleUpdate(TypedDict, closed=True):
    rule_identifier: "capo_vpc_lattice.types.rule_identifier.RuleIdentifier"
    """<p>The ID or ARN of the rule.</p>"""
    match: NotRequired["capo_vpc_lattice.types.rule_match.RuleMatch"]
    """<p>The rule match.</p>"""
    priority: NotRequired["capo_vpc_lattice.types.rule_priority.RulePriority"]
    """<p>The rule priority. A listener can't have multiple rules with the same priority.</p>"""
    action: NotRequired["capo_vpc_lattice.types.rule_action.RuleAction"]
    """<p>The rule action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleUpdate) -> dict:
    out: dict = {}
    out["ruleIdentifier"] = value["rule_identifier"]
    if "match" in value:
        import capo_vpc_lattice.types.rule_match

        out["match"] = capo_vpc_lattice.types.rule_match.serialize_json(value["match"])
    if "priority" in value:
        out["priority"] = value["priority"]
    if "action" in value:
        import capo_vpc_lattice.types.rule_action

        out["action"] = capo_vpc_lattice.types.rule_action.serialize_json(
            value["action"]
        )
    return out


def deserialize_json(data: dict) -> RuleUpdate:
    out: RuleUpdate = {}  # type: ignore[typeddict-item]
    if data.get("ruleIdentifier") is not None:
        out["rule_identifier"] = data["ruleIdentifier"]
    else:
        out["rule_identifier"] = ""
    if data.get("match") is not None:
        import capo_vpc_lattice.types.rule_match

        out["match"] = capo_vpc_lattice.types.rule_match.deserialize_json(data["match"])
    if data.get("priority") is not None:
        out["priority"] = data["priority"]
    if data.get("action") is not None:
        import capo_vpc_lattice.types.rule_action

        out["action"] = capo_vpc_lattice.types.rule_action.deserialize_json(
            data["action"]
        )
    return out
