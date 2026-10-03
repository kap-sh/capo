"""Generated from Smithy shape ``com.amazonaws.waf#WebACL``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_waf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_waf.types.activated_rules
    import capo_waf.types.metric_name
    import capo_waf.types.resource_arn
    import capo_waf.types.resource_id
    import capo_waf.types.resource_name
    import capo_waf.types.waf_action


class WebACL(TypedDict, closed=True):
    web_acl_id: "capo_waf.types.resource_id.ResourceId"
    """<p>A unique identifier for a <code>WebACL</code>. You use <code>WebACLId</code> to get information about a <code>WebACL</code> (see <a>GetWebACL</a>), update a <code>WebACL</code> (see <a>UpdateWebACL</a>), and delete a <code>WebACL</code> from AWS WAF (see <a>DeleteWebACL</a>).</p> <p> <code>WebACLId</code> is returned by <a>CreateWebACL</a> and by <a>ListWebACLs</a>.</p>"""
    name: NotRequired["capo_waf.types.resource_name.ResourceName"]
    """<p>A friendly name or description of the <code>WebACL</code>. You can't change the name of a <code>WebACL</code> after you create it.</p>"""
    metric_name: NotRequired["capo_waf.types.metric_name.MetricName"]
    """<p>A friendly name or description for the metrics for this <code>WebACL</code>. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and "Default_Action." You can't change <code>MetricName</code> after you create the <code>WebACL</code>.</p>"""
    default_action: "capo_waf.types.waf_action.WafAction"
    """<p>The action to perform if none of the <code>Rules</code> contained in the <code>WebACL</code> match. The action is specified by the <a>WafAction</a> object.</p>"""
    rules: "capo_waf.types.activated_rules.ActivatedRules"
    """<p>An array that contains the action for each <code>Rule</code> in a <code>WebACL</code>, the priority of the <code>Rule</code>, and the ID of the <code>Rule</code>.</p>"""
    web_acl_arn: NotRequired["capo_waf.types.resource_arn.ResourceArn"]
    """<p>Tha Amazon Resource Name (ARN) of the web ACL.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebACL) -> dict:
    out: dict = {}
    out["WebACLId"] = value["web_acl_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    import capo_waf.types.waf_action

    out["DefaultAction"] = capo_waf.types.waf_action.serialize_aws_json_1_1(
        value["default_action"]
    )
    import capo_waf.types.activated_rules

    out["Rules"] = capo_waf.types.activated_rules.serialize_aws_json_1_1(value["rules"])
    if "web_acl_arn" in value:
        out["WebACLArn"] = value["web_acl_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WebACL:
    out: WebACL = {}  # type: ignore[typeddict-item]
    if data.get("WebACLId") is not None:
        out["web_acl_id"] = data["WebACLId"]
    else:
        raise DeserializationError("WebACL.web_acl_id required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    if data.get("DefaultAction") is not None:
        import capo_waf.types.waf_action

        out["default_action"] = capo_waf.types.waf_action.deserialize_aws_json_1_1(
            data["DefaultAction"]
        )
    else:
        raise DeserializationError("WebACL.default_action required")
    if data.get("Rules") is not None:
        import capo_waf.types.activated_rules

        out["rules"] = capo_waf.types.activated_rules.deserialize_aws_json_1_1(
            data["Rules"]
        )
    else:
        raise DeserializationError("WebACL.rules required")
    if data.get("WebACLArn") is not None:
        out["web_acl_arn"] = data["WebACLArn"]
    return out
