"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#GenerateRuleConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.idempotency_token
    import capo_network_security_manager.types.rule_firewall_type
    import capo_network_security_manager.types.rule_type
    import capo_network_security_manager.types.sensitive_string
    import capo_network_security_manager.types.waf_config_data_type


class GenerateRuleConfigurationRequest(TypedDict, closed=True):
    prompt: "capo_network_security_manager.types.sensitive_string.SensitiveString"
    """<p>A natural-language description of the configuration that you want to generate.</p>"""
    rule_firewall_type: (
        "capo_network_security_manager.types.rule_firewall_type.RuleFirewallType"
    )
    """<p>The firewall type of the rule.</p>"""
    rule_type: "capo_network_security_manager.types.rule_type.RuleType"
    """<p>The type of the rule. <code>CONFIGURATION</code> rules contain firewall settings, and <code>INSPECTION</code> rules contain rule groups.</p>"""
    waf_config_data_type: NotRequired[
        "capo_network_security_manager.types.waf_config_data_type.WAFConfigDataType"
    ]
    """<p>For AWS WAF configuration rules, the specific AWS WAF configuration variant to generate. This is optional; if you omit it, the service selects the variant.</p>"""
    current_configuration: NotRequired["str"]
    """<p>An existing configuration to edit, as a JSON string. When you provide this value, the operation edits the configuration. When you omit it, the operation generates a new configuration.</p>"""
    client_token: NotRequired[
        "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerateRuleConfigurationRequest) -> dict:
    out: dict = {}
    out["prompt"] = value["prompt"]
    import capo_network_security_manager.types.rule_firewall_type

    out["ruleFirewallType"] = (
        capo_network_security_manager.types.rule_firewall_type.serialize_json(
            value["rule_firewall_type"]
        )
    )
    import capo_network_security_manager.types.rule_type

    out["ruleType"] = capo_network_security_manager.types.rule_type.serialize_json(
        value["rule_type"]
    )
    if "waf_config_data_type" in value:
        import capo_network_security_manager.types.waf_config_data_type

        out["wafConfigDataType"] = (
            capo_network_security_manager.types.waf_config_data_type.serialize_json(
                value["waf_config_data_type"]
            )
        )
    if "current_configuration" in value:
        out["currentConfiguration"] = value["current_configuration"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> GenerateRuleConfigurationRequest:
    out: GenerateRuleConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("prompt") is not None:
        out["prompt"] = data["prompt"]
    else:
        raise DeserializationError("GenerateRuleConfigurationRequest.prompt required")
    if data.get("ruleFirewallType") is not None:
        import capo_network_security_manager.types.rule_firewall_type

        out["rule_firewall_type"] = (
            capo_network_security_manager.types.rule_firewall_type.deserialize_json(
                data["ruleFirewallType"]
            )
        )
    else:
        raise DeserializationError(
            "GenerateRuleConfigurationRequest.rule_firewall_type required"
        )
    if data.get("ruleType") is not None:
        import capo_network_security_manager.types.rule_type

        out["rule_type"] = (
            capo_network_security_manager.types.rule_type.deserialize_json(
                data["ruleType"]
            )
        )
    else:
        raise DeserializationError(
            "GenerateRuleConfigurationRequest.rule_type required"
        )
    if data.get("wafConfigDataType") is not None:
        import capo_network_security_manager.types.waf_config_data_type

        out["waf_config_data_type"] = (
            capo_network_security_manager.types.waf_config_data_type.deserialize_json(
                data["wafConfigDataType"]
            )
        )
    if data.get("currentConfiguration") is not None:
        out["current_configuration"] = data["currentConfiguration"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
