"""Generated from Smithy shape ``com.amazonaws.wafv2#GetRateBasedStatementManagedKeysRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.entity_id
    import capo_wafv2.types.entity_name
    import capo_wafv2.types.scope


class GetRateBasedStatementManagedKeysRequest(TypedDict, closed=True):
    scope: "capo_wafv2.types.scope.Scope"
    """<p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>"""
    web_acl_name: "capo_wafv2.types.entity_name.EntityName"
    """<p>The name of the web ACL. You cannot change the name of a web ACL after you create it.</p>"""
    web_acl_id: "capo_wafv2.types.entity_id.EntityId"
    """<p>The unique identifier for the web ACL. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.</p>"""
    rule_group_rule_name: NotRequired["capo_wafv2.types.entity_name.EntityName"]
    """<p>The name of the rule group reference statement in your web ACL. This is required only when you have the rate-based rule nested inside a rule group. </p>"""
    rule_name: "capo_wafv2.types.entity_name.EntityName"
    """<p>The name of the rate-based rule to get the keys for. If you have the rule defined inside a rule group that you're using in your web ACL, also provide the name of the rule group reference statement in the request parameter <code>RuleGroupRuleName</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRateBasedStatementManagedKeysRequest) -> dict:
    out: dict = {}
    import capo_wafv2.types.scope

    out["Scope"] = capo_wafv2.types.scope.serialize_aws_json_1_1(value["scope"])
    out["WebACLName"] = value["web_acl_name"]
    out["WebACLId"] = value["web_acl_id"]
    if "rule_group_rule_name" in value:
        out["RuleGroupRuleName"] = value["rule_group_rule_name"]
    out["RuleName"] = value["rule_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRateBasedStatementManagedKeysRequest:
    out: GetRateBasedStatementManagedKeysRequest = {}  # type: ignore[typeddict-item]
    if data.get("Scope") is not None:
        import capo_wafv2.types.scope

        out["scope"] = capo_wafv2.types.scope.deserialize_aws_json_1_1(data["Scope"])
    else:
        import typing

        out["scope"] = typing.cast("capo_wafv2.types.scope.Scope", "")
    if data.get("WebACLName") is not None:
        out["web_acl_name"] = data["WebACLName"]
    else:
        out["web_acl_name"] = ""
    if data.get("WebACLId") is not None:
        out["web_acl_id"] = data["WebACLId"]
    else:
        out["web_acl_id"] = ""
    if data.get("RuleGroupRuleName") is not None:
        out["rule_group_rule_name"] = data["RuleGroupRuleName"]
    if data.get("RuleName") is not None:
        out["rule_name"] = data["RuleName"]
    else:
        out["rule_name"] = ""
    return out
