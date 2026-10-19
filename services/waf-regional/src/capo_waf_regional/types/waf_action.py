"""Generated from Smithy shape ``com.amazonaws.wafregional#WafAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.waf_action_type


class WafAction(TypedDict, closed=True):
    type: "capo_waf_regional.types.waf_action_type.WafActionType"
    """<p>Specifies how you want AWS WAF to respond to requests that match the settings in a <code>Rule</code>. Valid settings include the following:</p> <ul> <li> <p> <code>ALLOW</code>: AWS WAF allows requests</p> </li> <li> <p> <code>BLOCK</code>: AWS WAF blocks requests</p> </li> <li> <p> <code>COUNT</code>: AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can't specify <code>COUNT</code> for the default action for a <code>WebACL</code>.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WafAction) -> dict:
    out: dict = {}
    import capo_waf_regional.types.waf_action_type

    out["Type"] = capo_waf_regional.types.waf_action_type.serialize_aws_json_1_1(
        value["type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> WafAction:
    out: WafAction = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_waf_regional.types.waf_action_type

        out["type"] = capo_waf_regional.types.waf_action_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_waf_regional.types.waf_action_type.WafActionType", ""
        )
    return out
