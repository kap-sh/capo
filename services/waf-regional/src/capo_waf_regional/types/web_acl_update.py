"""Generated from Smithy shape ``com.amazonaws.wafregional#WebACLUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import capo_waf_regional.types.activated_rule
    import capo_waf_regional.types.change_action


class WebACLUpdate(TypedDict, closed=True):
    action: "capo_waf_regional.types.change_action.ChangeAction"
    """<p>Specifies whether to insert a <code>Rule</code> into or delete a <code>Rule</code> from a <code>WebACL</code>.</p>"""
    activated_rule: "capo_waf_regional.types.activated_rule.ActivatedRule"
    """<p>The <code>ActivatedRule</code> object in an <a>UpdateWebACL</a> request specifies a <code>Rule</code> that you want to insert or delete, the priority of the <code>Rule</code> in the <code>WebACL</code>, and the action that you want AWS WAF to take when a web request matches the <code>Rule</code> (<code>ALLOW</code>, <code>BLOCK</code>, or <code>COUNT</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebACLUpdate) -> dict:
    out: dict = {}
    import capo_waf_regional.types.change_action

    out["Action"] = capo_waf_regional.types.change_action.serialize_aws_json_1_1(
        value["action"]
    )
    import capo_waf_regional.types.activated_rule

    out["ActivatedRule"] = (
        capo_waf_regional.types.activated_rule.serialize_aws_json_1_1(
            value["activated_rule"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> WebACLUpdate:
    out: WebACLUpdate = {}  # type: ignore[typeddict-item]
    if data.get("Action") is not None:
        import capo_waf_regional.types.change_action

        out["action"] = capo_waf_regional.types.change_action.deserialize_aws_json_1_1(
            data["Action"]
        )
    else:
        import typing

        out["action"] = typing.cast(
            "capo_waf_regional.types.change_action.ChangeAction", ""
        )
    if data.get("ActivatedRule") is not None:
        import capo_waf_regional.types.activated_rule

        out["activated_rule"] = (
            capo_waf_regional.types.activated_rule.deserialize_aws_json_1_1(
                data["ActivatedRule"]
            )
        )
    else:
        raise DeserializationError("WebACLUpdate.activated_rule required")
    return out
