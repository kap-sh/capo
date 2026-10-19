"""Generated from Smithy shape ``com.amazonaws.networkfirewall#StatelessRulesAndCustomActions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.custom_actions
    import capo_network_firewall.types.stateless_rules


class StatelessRulesAndCustomActions(TypedDict, closed=True):
    stateless_rules: "capo_network_firewall.types.stateless_rules.StatelessRules"
    """<p>Defines the set of stateless rules for use in a stateless rule group. </p>"""
    custom_actions: NotRequired[
        "capo_network_firewall.types.custom_actions.CustomActions"
    ]
    """<p>Defines an array of individual custom action definitions that are available for use by the stateless rules in this <code>StatelessRulesAndCustomActions</code> specification. You name each custom action that you define, and then you can use it by name in your <a>StatelessRule</a> <a>RuleDefinition</a> <code>Actions</code> specification.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StatelessRulesAndCustomActions) -> dict:
    out: dict = {}
    import capo_network_firewall.types.stateless_rules

    out["StatelessRules"] = (
        capo_network_firewall.types.stateless_rules.serialize_aws_json_1_0(
            value["stateless_rules"]
        )
    )
    if "custom_actions" in value:
        import capo_network_firewall.types.custom_actions

        out["CustomActions"] = (
            capo_network_firewall.types.custom_actions.serialize_aws_json_1_0(
                value["custom_actions"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StatelessRulesAndCustomActions:
    out: StatelessRulesAndCustomActions = {}  # type: ignore[typeddict-item]
    if data.get("StatelessRules") is not None:
        import capo_network_firewall.types.stateless_rules

        out["stateless_rules"] = (
            capo_network_firewall.types.stateless_rules.deserialize_aws_json_1_0(
                data["StatelessRules"]
            )
        )
    else:
        out["stateless_rules"] = []
    if data.get("CustomActions") is not None:
        import capo_network_firewall.types.custom_actions

        out["custom_actions"] = (
            capo_network_firewall.types.custom_actions.deserialize_aws_json_1_0(
                data["CustomActions"]
            )
        )
    return out
