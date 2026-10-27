"""Generated from Smithy shape ``com.amazonaws.lightsail#WafConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.boolean
    import capo_lightsail.types.waf_rule_list


class WafConfig(TypedDict, closed=True):
    is_waf_enabled: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>Specifies whether WAF is enabled for the distribution.</p>"""
    waf_rules: NotRequired["capo_lightsail.types.waf_rule_list.WafRuleList"]
    """<p>An array of objects that describe the WAF rule groups enabled for the distribution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WafConfig) -> dict:
    out: dict = {}
    if "is_waf_enabled" in value:
        out["isWafEnabled"] = value["is_waf_enabled"]
    if "waf_rules" in value:
        import capo_lightsail.types.waf_rule_list

        out["wafRules"] = capo_lightsail.types.waf_rule_list.serialize_aws_json_1_1(
            value["waf_rules"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WafConfig:
    out: WafConfig = {}  # type: ignore[typeddict-item]
    if data.get("isWafEnabled") is not None:
        out["is_waf_enabled"] = data["isWafEnabled"]
    if data.get("wafRules") is not None:
        import capo_lightsail.types.waf_rule_list

        out["waf_rules"] = capo_lightsail.types.waf_rule_list.deserialize_aws_json_1_1(
            data["wafRules"]
        )
    return out
