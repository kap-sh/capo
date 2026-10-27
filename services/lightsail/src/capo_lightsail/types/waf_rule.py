"""Generated from Smithy shape ``com.amazonaws.lightsail#WafRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.string
    import capo_lightsail.types.waf_acfp_config
    import capo_lightsail.types.waf_atp_config
    import capo_lightsail.types.waf_bot_control_config


class WafRule(TypedDict, closed=True):
    name: "capo_lightsail.types.string.string"
    """<p>The name of the WAF rule group (for example, <code>AWSManagedRulesCommonRuleSet</code>).</p> <p>For the WAF rule groups that you can specify for each bundle, see the <code>wafRules</code> parameter of the <code>CreateDistribution</code> action.</p>"""
    atp_config: NotRequired["capo_lightsail.types.waf_atp_config.WafAtpConfig"]
    """<p>An object that describes the configuration of the account takeover prevention rule group.</p> <p>Constraints:</p> <ul> <li> <p>Define this parameter only when the <code>name</code> is <code>AWSManagedRulesATPRuleSet</code>.</p> </li> <li> <p>This parameter is required when the <code>name</code> is <code>AWSManagedRulesATPRuleSet</code>.</p> </li> </ul>"""
    acfp_config: NotRequired["capo_lightsail.types.waf_acfp_config.WafAcfpConfig"]
    """<p>An object that describes the configuration of the account creation fraud prevention rule group.</p> <p>Constraints:</p> <ul> <li> <p>Define this parameter only when the <code>name</code> is <code>AWSManagedRulesACFPRuleSet</code>.</p> </li> <li> <p>This parameter is required when the <code>name</code> is <code>AWSManagedRulesACFPRuleSet</code>.</p> </li> </ul>"""
    bot_control_config: NotRequired[
        "capo_lightsail.types.waf_bot_control_config.WafBotControlConfig"
    ]
    """<p>An object that describes the configuration of the bot control rule group.</p> <p>Constraints:</p> <ul> <li> <p>Define this parameter only when the <code>name</code> is <code>AWSManagedRulesBotControlRuleSet</code>.</p> </li> <li> <p>This parameter is required when the <code>name</code> is <code>AWSManagedRulesBotControlRuleSet</code>.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WafRule) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "atp_config" in value:
        import capo_lightsail.types.waf_atp_config

        out["atpConfig"] = capo_lightsail.types.waf_atp_config.serialize_aws_json_1_1(
            value["atp_config"]
        )
    if "acfp_config" in value:
        import capo_lightsail.types.waf_acfp_config

        out["acfpConfig"] = capo_lightsail.types.waf_acfp_config.serialize_aws_json_1_1(
            value["acfp_config"]
        )
    if "bot_control_config" in value:
        import capo_lightsail.types.waf_bot_control_config

        out["botControlConfig"] = (
            capo_lightsail.types.waf_bot_control_config.serialize_aws_json_1_1(
                value["bot_control_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WafRule:
    out: WafRule = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("atpConfig") is not None:
        import capo_lightsail.types.waf_atp_config

        out["atp_config"] = (
            capo_lightsail.types.waf_atp_config.deserialize_aws_json_1_1(
                data["atpConfig"]
            )
        )
    if data.get("acfpConfig") is not None:
        import capo_lightsail.types.waf_acfp_config

        out["acfp_config"] = (
            capo_lightsail.types.waf_acfp_config.deserialize_aws_json_1_1(
                data["acfpConfig"]
            )
        )
    if data.get("botControlConfig") is not None:
        import capo_lightsail.types.waf_bot_control_config

        out["bot_control_config"] = (
            capo_lightsail.types.waf_bot_control_config.deserialize_aws_json_1_1(
                data["botControlConfig"]
            )
        )
    return out
