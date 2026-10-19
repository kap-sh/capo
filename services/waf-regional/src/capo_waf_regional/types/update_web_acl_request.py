"""Generated from Smithy shape ``com.amazonaws.wafregional#UpdateWebACLRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.change_token
    import capo_waf_regional.types.resource_id
    import capo_waf_regional.types.waf_action
    import capo_waf_regional.types.web_acl_updates


class UpdateWebACLRequest(TypedDict, closed=True):
    web_acl_id: "capo_waf_regional.types.resource_id.ResourceId"
    """<p>The <code>WebACLId</code> of the <a>WebACL</a> that you want to update. <code>WebACLId</code> is returned by <a>CreateWebACL</a> and by <a>ListWebACLs</a>.</p>"""
    change_token: "capo_waf_regional.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""
    updates: NotRequired["capo_waf_regional.types.web_acl_updates.WebACLUpdates"]
    """<p>An array of updates to make to the <a>WebACL</a>.</p> <p>An array of <code>WebACLUpdate</code> objects that you want to insert into or delete from a <a>WebACL</a>. For more information, see the applicable data types:</p> <ul> <li> <p> <a>WebACLUpdate</a>: Contains <code>Action</code> and <code>ActivatedRule</code> </p> </li> <li> <p> <a>ActivatedRule</a>: Contains <code>Action</code>, <code>OverrideAction</code>, <code>Priority</code>, <code>RuleId</code>, and <code>Type</code>. <code>ActivatedRule|OverrideAction</code> applies only when updating or adding a <code>RuleGroup</code> to a <code>WebACL</code>. In this case, you do not use <code>ActivatedRule|Action</code>. For all other update requests, <code>ActivatedRule|Action</code> is used instead of <code>ActivatedRule|OverrideAction</code>. </p> </li> <li> <p> <a>WafAction</a>: Contains <code>Type</code> </p> </li> </ul>"""
    default_action: NotRequired["capo_waf_regional.types.waf_action.WafAction"]
    """<p>A default action for the web ACL, either ALLOW or BLOCK. AWS WAF performs the default action if a request doesn't match the criteria in any of the rules in a web ACL.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateWebACLRequest) -> dict:
    out: dict = {}
    out["WebACLId"] = value["web_acl_id"]
    out["ChangeToken"] = value["change_token"]
    if "updates" in value:
        import capo_waf_regional.types.web_acl_updates

        out["Updates"] = capo_waf_regional.types.web_acl_updates.serialize_aws_json_1_1(
            value["updates"]
        )
    if "default_action" in value:
        import capo_waf_regional.types.waf_action

        out["DefaultAction"] = (
            capo_waf_regional.types.waf_action.serialize_aws_json_1_1(
                value["default_action"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateWebACLRequest:
    out: UpdateWebACLRequest = {}  # type: ignore[typeddict-item]
    if data.get("WebACLId") is not None:
        out["web_acl_id"] = data["WebACLId"]
    else:
        out["web_acl_id"] = ""
    if data.get("ChangeToken") is not None:
        out["change_token"] = data["ChangeToken"]
    else:
        out["change_token"] = ""
    if data.get("Updates") is not None:
        import capo_waf_regional.types.web_acl_updates

        out["updates"] = (
            capo_waf_regional.types.web_acl_updates.deserialize_aws_json_1_1(
                data["Updates"]
            )
        )
    if data.get("DefaultAction") is not None:
        import capo_waf_regional.types.waf_action

        out["default_action"] = (
            capo_waf_regional.types.waf_action.deserialize_aws_json_1_1(
                data["DefaultAction"]
            )
        )
    return out
