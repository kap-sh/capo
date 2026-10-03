"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FirewallPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_firewall.types.custom_actions
    import capo_network_firewall.types.enable_tls_session_holding
    import capo_network_firewall.types.policy_variables
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.stateful_actions
    import capo_network_firewall.types.stateful_engine_options
    import capo_network_firewall.types.stateful_rule_group_references
    import capo_network_firewall.types.stateless_actions
    import capo_network_firewall.types.stateless_rule_group_references


class FirewallPolicy(TypedDict, closed=True):
    stateless_rule_group_references: NotRequired[
        "capo_network_firewall.types.stateless_rule_group_references.StatelessRuleGroupReferences"
    ]
    """<p>References to the stateless rule groups that are used in the policy. These define the matching criteria in stateless rules. </p>"""
    stateless_default_actions: (
        "capo_network_firewall.types.stateless_actions.StatelessActions"
    )
    """<p>The actions to take on a packet if it doesn't match any of the stateless rules in the policy. If you want non-matching packets to be forwarded for stateful inspection, specify <code>aws:forward_to_sfe</code>. </p> <p>You must specify one of the standard actions: <code>aws:pass</code>, <code>aws:drop</code>, or <code>aws:forward_to_sfe</code>. In addition, you can specify custom actions that are compatible with your standard section choice.</p> <p>For example, you could specify <code>["aws:pass"]</code> or you could specify <code>["aws:pass", “customActionName”]</code>. For information about compatibility, see the custom action descriptions under <a>CustomAction</a>.</p>"""
    stateless_fragment_default_actions: (
        "capo_network_firewall.types.stateless_actions.StatelessActions"
    )
    """<p>The actions to take on a fragmented UDP packet if it doesn't match any of the stateless rules in the policy. Network Firewall only manages UDP packet fragments and silently drops packet fragments for other protocols. If you want non-matching fragmented UDP packets to be forwarded for stateful inspection, specify <code>aws:forward_to_sfe</code>. </p> <p>You must specify one of the standard actions: <code>aws:pass</code>, <code>aws:drop</code>, or <code>aws:forward_to_sfe</code>. In addition, you can specify custom actions that are compatible with your standard section choice.</p> <p>For example, you could specify <code>["aws:pass"]</code> or you could specify <code>["aws:pass", “customActionName”]</code>. For information about compatibility, see the custom action descriptions under <a>CustomAction</a>.</p>"""
    stateless_custom_actions: NotRequired[
        "capo_network_firewall.types.custom_actions.CustomActions"
    ]
    """<p>The custom action definitions that are available for use in the firewall policy's <code>StatelessDefaultActions</code> setting. You name each custom action that you define, and then you can use it by name in your default actions specifications.</p>"""
    stateful_rule_group_references: NotRequired[
        "capo_network_firewall.types.stateful_rule_group_references.StatefulRuleGroupReferences"
    ]
    """<p>References to the stateful rule groups that are used in the policy. These define the inspection criteria in stateful rules. </p>"""
    stateful_default_actions: NotRequired[
        "capo_network_firewall.types.stateful_actions.StatefulActions"
    ]
    """<p>The default actions to take on a packet that doesn't match any stateful rules. The stateful default action is optional, and is only valid when using the strict rule order.</p> <p>Valid values of the stateful default action:</p> <ul> <li> <p>aws:drop_strict</p> </li> <li> <p>aws:drop_established</p> </li> <li> <p>aws:alert_strict</p> </li> <li> <p>aws:alert_established</p> </li> <li> <p>aws:drop_established_app_layer</p> </li> <li> <p>aws:alert_established_app_layer</p> </li> <li> <p>aws:drop_established_app_layer_to_server</p> </li> <li> <p>aws:alert_established_app_layer_to_server</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-rule-evaluation-order.html#suricata-strict-rule-evaluation-order.html">Strict evaluation order</a> in the <i>Network Firewall Developer Guide</i>. </p>"""
    stateful_engine_options: NotRequired[
        "capo_network_firewall.types.stateful_engine_options.StatefulEngineOptions"
    ]
    """<p>Additional options governing how Network Firewall handles stateful rules. The stateful rule groups that you use in your policy must have stateful rule options settings that are compatible with these settings.</p>"""
    tls_inspection_configuration_arn: NotRequired[
        "capo_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the TLS inspection configuration.</p>"""
    policy_variables: NotRequired[
        "capo_network_firewall.types.policy_variables.PolicyVariables"
    ]
    """<p>Contains variables that you can use to override default Suricata settings in your firewall policy.</p>"""
    enable_tls_session_holding: NotRequired[
        "capo_network_firewall.types.enable_tls_session_holding.EnableTLSSessionHolding"
    ]
    """<p>When true, prevents TCP and TLS packets from reaching destination servers until TLS Inspection has evaluated Server Name Indication (SNI) rules. Requires an associated TLS Inspection configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FirewallPolicy) -> dict:
    out: dict = {}
    if "stateless_rule_group_references" in value:
        import capo_network_firewall.types.stateless_rule_group_references

        out["StatelessRuleGroupReferences"] = (
            capo_network_firewall.types.stateless_rule_group_references.serialize_aws_json_1_0(
                value["stateless_rule_group_references"]
            )
        )
    import capo_network_firewall.types.stateless_actions

    out["StatelessDefaultActions"] = (
        capo_network_firewall.types.stateless_actions.serialize_aws_json_1_0(
            value["stateless_default_actions"]
        )
    )
    import capo_network_firewall.types.stateless_actions

    out["StatelessFragmentDefaultActions"] = (
        capo_network_firewall.types.stateless_actions.serialize_aws_json_1_0(
            value["stateless_fragment_default_actions"]
        )
    )
    if "stateless_custom_actions" in value:
        import capo_network_firewall.types.custom_actions

        out["StatelessCustomActions"] = (
            capo_network_firewall.types.custom_actions.serialize_aws_json_1_0(
                value["stateless_custom_actions"]
            )
        )
    if "stateful_rule_group_references" in value:
        import capo_network_firewall.types.stateful_rule_group_references

        out["StatefulRuleGroupReferences"] = (
            capo_network_firewall.types.stateful_rule_group_references.serialize_aws_json_1_0(
                value["stateful_rule_group_references"]
            )
        )
    if "stateful_default_actions" in value:
        import capo_network_firewall.types.stateful_actions

        out["StatefulDefaultActions"] = (
            capo_network_firewall.types.stateful_actions.serialize_aws_json_1_0(
                value["stateful_default_actions"]
            )
        )
    if "stateful_engine_options" in value:
        import capo_network_firewall.types.stateful_engine_options

        out["StatefulEngineOptions"] = (
            capo_network_firewall.types.stateful_engine_options.serialize_aws_json_1_0(
                value["stateful_engine_options"]
            )
        )
    if "tls_inspection_configuration_arn" in value:
        out["TLSInspectionConfigurationArn"] = value["tls_inspection_configuration_arn"]
    if "policy_variables" in value:
        import capo_network_firewall.types.policy_variables

        out["PolicyVariables"] = (
            capo_network_firewall.types.policy_variables.serialize_aws_json_1_0(
                value["policy_variables"]
            )
        )
    if "enable_tls_session_holding" in value:
        out["EnableTLSSessionHolding"] = value["enable_tls_session_holding"]
    return out


def deserialize_aws_json_1_0(data: dict) -> FirewallPolicy:
    out: FirewallPolicy = {}  # type: ignore[typeddict-item]
    if data.get("StatelessRuleGroupReferences") is not None:
        import capo_network_firewall.types.stateless_rule_group_references

        out["stateless_rule_group_references"] = (
            capo_network_firewall.types.stateless_rule_group_references.deserialize_aws_json_1_0(
                data["StatelessRuleGroupReferences"]
            )
        )
    if data.get("StatelessDefaultActions") is not None:
        import capo_network_firewall.types.stateless_actions

        out["stateless_default_actions"] = (
            capo_network_firewall.types.stateless_actions.deserialize_aws_json_1_0(
                data["StatelessDefaultActions"]
            )
        )
    else:
        raise DeserializationError("FirewallPolicy.stateless_default_actions required")
    if data.get("StatelessFragmentDefaultActions") is not None:
        import capo_network_firewall.types.stateless_actions

        out["stateless_fragment_default_actions"] = (
            capo_network_firewall.types.stateless_actions.deserialize_aws_json_1_0(
                data["StatelessFragmentDefaultActions"]
            )
        )
    else:
        raise DeserializationError(
            "FirewallPolicy.stateless_fragment_default_actions required"
        )
    if data.get("StatelessCustomActions") is not None:
        import capo_network_firewall.types.custom_actions

        out["stateless_custom_actions"] = (
            capo_network_firewall.types.custom_actions.deserialize_aws_json_1_0(
                data["StatelessCustomActions"]
            )
        )
    if data.get("StatefulRuleGroupReferences") is not None:
        import capo_network_firewall.types.stateful_rule_group_references

        out["stateful_rule_group_references"] = (
            capo_network_firewall.types.stateful_rule_group_references.deserialize_aws_json_1_0(
                data["StatefulRuleGroupReferences"]
            )
        )
    if data.get("StatefulDefaultActions") is not None:
        import capo_network_firewall.types.stateful_actions

        out["stateful_default_actions"] = (
            capo_network_firewall.types.stateful_actions.deserialize_aws_json_1_0(
                data["StatefulDefaultActions"]
            )
        )
    if data.get("StatefulEngineOptions") is not None:
        import capo_network_firewall.types.stateful_engine_options

        out["stateful_engine_options"] = (
            capo_network_firewall.types.stateful_engine_options.deserialize_aws_json_1_0(
                data["StatefulEngineOptions"]
            )
        )
    if data.get("TLSInspectionConfigurationArn") is not None:
        out["tls_inspection_configuration_arn"] = data["TLSInspectionConfigurationArn"]
    if data.get("PolicyVariables") is not None:
        import capo_network_firewall.types.policy_variables

        out["policy_variables"] = (
            capo_network_firewall.types.policy_variables.deserialize_aws_json_1_0(
                data["PolicyVariables"]
            )
        )
    if data.get("EnableTLSSessionHolding") is not None:
        out["enable_tls_session_holding"] = data["EnableTLSSessionHolding"]
    return out
