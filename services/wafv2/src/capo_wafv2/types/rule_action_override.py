"""Generated from Smithy shape ``com.amazonaws.wafv2#RuleActionOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.entity_name
    import capo_wafv2.types.rule_action


class RuleActionOverride(TypedDict, closed=True):
    name: "capo_wafv2.types.entity_name.EntityName"
    """<p>The name of the rule to override.</p> <note> <p>Verify the rule names in your overrides carefully. With managed rule groups, WAF silently ignores any override that uses an invalid rule name. With customer-owned rule groups, invalid rule names in your overrides will cause web ACL updates to fail. An invalid rule name is any name that doesn't exactly match the case-sensitive name of an existing rule in the rule group.</p> </note>"""
    action_to_use: "capo_wafv2.types.rule_action.RuleAction"
    """<p>The override action to use, in place of the configured action of the rule in the rule group. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleActionOverride) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_wafv2.types.rule_action

    out["ActionToUse"] = capo_wafv2.types.rule_action.serialize_aws_json_1_1(
        value["action_to_use"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RuleActionOverride:
    out: RuleActionOverride = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("ActionToUse") is not None:
        import capo_wafv2.types.rule_action

        out["action_to_use"] = capo_wafv2.types.rule_action.deserialize_aws_json_1_1(
            data["ActionToUse"]
        )
    else:
        raise DeserializationError("RuleActionOverride.action_to_use required")
    return out
