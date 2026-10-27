"""Generated from Smithy shape ``com.amazonaws.lightsail#WafRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.waf_rule

WafRuleList: TypeAlias = list["capo_lightsail.types.waf_rule.WafRule"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WafRuleList) -> list:
    import capo_lightsail.types.waf_rule

    out: list = []
    for item in value:
        out.append(capo_lightsail.types.waf_rule.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> WafRuleList:
    import capo_lightsail.types.waf_rule

    out: WafRuleList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lightsail.types.waf_rule.deserialize_aws_json_1_1(item))
    return out
