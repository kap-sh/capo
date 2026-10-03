"""Generated from Smithy shape ``com.amazonaws.wafv2#GetWebACLResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.lock_token
    import capo_wafv2.types.output_url
    import capo_wafv2.types.web_acl


class GetWebACLResponse(TypedDict, closed=True):
    web_acl: NotRequired["capo_wafv2.types.web_acl.WebACL"]
    """<p>The web ACL specification. You can modify the settings in this web ACL and use it to update this web ACL or create a new one.</p>"""
    lock_token: NotRequired["capo_wafv2.types.lock_token.LockToken"]
    """<p>A token used for optimistic locking. WAF returns a token to your <code>get</code> and <code>list</code> requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like <code>update</code> and <code>delete</code>. WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a <code>WAFOptimisticLockException</code>. If this happens, perform another <code>get</code>, and use the new token returned by that operation. </p>"""
    application_integration_url: NotRequired["capo_wafv2.types.output_url.OutputUrl"]
    """<p>The URL to use in SDK integrations with Amazon Web Services managed rule groups. For example, you can use the integration SDKs with the account takeover prevention managed rule group <code>AWSManagedRulesATPRuleSet</code> and the account creation fraud prevention managed rule group <code>AWSManagedRulesACFPRuleSet</code>. This is only populated if you are using a rule group in your web ACL that integrates with your applications in this way. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-application-integration.html">WAF client application integration</a> in the <i>WAF Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetWebACLResponse) -> dict:
    out: dict = {}
    if "web_acl" in value:
        import capo_wafv2.types.web_acl

        out["WebACL"] = capo_wafv2.types.web_acl.serialize_aws_json_1_1(
            value["web_acl"]
        )
    if "lock_token" in value:
        out["LockToken"] = value["lock_token"]
    if "application_integration_url" in value:
        out["ApplicationIntegrationURL"] = value["application_integration_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetWebACLResponse:
    out: GetWebACLResponse = {}  # type: ignore[typeddict-item]
    if data.get("WebACL") is not None:
        import capo_wafv2.types.web_acl

        out["web_acl"] = capo_wafv2.types.web_acl.deserialize_aws_json_1_1(
            data["WebACL"]
        )
    if data.get("LockToken") is not None:
        out["lock_token"] = data["LockToken"]
    if data.get("ApplicationIntegrationURL") is not None:
        out["application_integration_url"] = data["ApplicationIntegrationURL"]
    return out
