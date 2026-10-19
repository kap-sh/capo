"""Generated from Smithy shape ``com.amazonaws.networkfirewall#StatelessRule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_firewall.types.priority
    import capo_network_firewall.types.rule_definition


class StatelessRule(TypedDict, closed=True):
    rule_definition: "capo_network_firewall.types.rule_definition.RuleDefinition"
    """<p>Defines the stateless 5-tuple packet inspection criteria and the action to take on a packet that matches the criteria. </p>"""
    priority: "capo_network_firewall.types.priority.Priority"
    """<p>Indicates the order in which to run this rule relative to all of the rules that are defined for a stateless rule group. Network Firewall evaluates the rules in a rule group starting with the lowest priority setting. You must ensure that the priority settings are unique for the rule group. </p> <p>Each stateless rule group uses exactly one <code>StatelessRulesAndCustomActions</code> object, and each <code>StatelessRulesAndCustomActions</code> contains exactly one <code>StatelessRules</code> object. To ensure unique priority settings for your rule groups, set unique priorities for the stateless rules that you define inside any single <code>StatelessRules</code> object.</p> <p>You can change the priority settings of your rules at any time. To make it easier to insert rules later, number them so there's a wide range in between, for example use 100, 200, and so on. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StatelessRule) -> dict:
    out: dict = {}
    import capo_network_firewall.types.rule_definition

    out["RuleDefinition"] = (
        capo_network_firewall.types.rule_definition.serialize_aws_json_1_0(
            value["rule_definition"]
        )
    )
    out["Priority"] = value["priority"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StatelessRule:
    out: StatelessRule = {}  # type: ignore[typeddict-item]
    if data.get("RuleDefinition") is not None:
        import capo_network_firewall.types.rule_definition

        out["rule_definition"] = (
            capo_network_firewall.types.rule_definition.deserialize_aws_json_1_0(
                data["RuleDefinition"]
            )
        )
    else:
        raise DeserializationError("StatelessRule.rule_definition required")
    if data.get("Priority") is not None:
        out["priority"] = data["Priority"]
    else:
        out["priority"] = 0
    return out
