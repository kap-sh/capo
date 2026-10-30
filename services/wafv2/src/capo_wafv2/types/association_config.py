"""Generated from Smithy shape ``com.amazonaws.wafv2#AssociationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.challenge_javascript_sdk_injection
    import capo_wafv2.types.request_body


class AssociationConfig(TypedDict, closed=True):
    request_body: NotRequired["capo_wafv2.types.request_body.RequestBody"]
    """<p>Customizes the maximum size of the request body that your protected CloudFront, API Gateway, Amazon Cognito, App Runner, and Verified Access resources forward to WAF for inspection. The default size is 16 KB (16,384 bytes). You can change the setting for any of the available resource types. </p> <note> <p>You are charged additional fees when your protected resources forward body sizes that are larger than the default. For more information, see <a href="http://aws.amazon.com/waf/pricing/">WAF Pricing</a>.</p> </note> <p>Example JSON: <code> { "API_GATEWAY": "KB_48", "APP_RUNNER_SERVICE": "KB_32" }</code> </p> <p>For Application Load Balancer and AppSync, the limit is fixed at 8 KB (8,192 bytes).</p>"""
    challenge_javascript_sdk_injection: NotRequired[
        "capo_wafv2.types.challenge_javascript_sdk_injection.ChallengeJavascriptSdkInjection"
    ]
    """<p>Specifies the CloudFront distributions that insert the WAF challenge JavaScript SDK into the HTML responses that they return. When you enable this setting for a distribution, you do not add the SDK to your web pages yourself. </p> <p>You can configure this setting only for CloudFront distributions, using the <code>CLOUDFRONT</code> map key. WAF rejects any other resource type, and the setting is not available for regional resources. To configure it, use the CloudFront scope. </p> <p>Your web ACL must also contain at least one of the following qualifying managed rule groups. WAF Bot Control qualifies only at the <code>TARGETED</code> inspection level, not at <code>COMMON</code>: </p> <ul> <li> <p>The WAF Bot Control managed rule group <code>AWSManagedRulesBotControlRuleSet</code>, with the inspection level set to <code>TARGETED</code>. </p> </li> <li> <p>The WAF Fraud Control account takeover prevention (ATP) managed rule group <code>AWSManagedRulesATPRuleSet</code>. </p> </li> <li> <p>The WAF Fraud Control account creation fraud prevention (ACFP) managed rule group <code>AWSManagedRulesACFPRuleSet</code>. </p> </li> </ul> <p>If you remove the last qualifying managed rule group from the web ACL, or lower the WAF Bot Control inspection level from <code>TARGETED</code> to <code>COMMON</code>, you must remove this setting in the same update. Otherwise, WAF rejects the update. </p> <p>Example JSON: <code> { "CLOUDFRONT": {} }</code> </p> <p>If you omit this setting, CloudFront does not insert the SDK. When you omit it from a web ACL that previously used it, cached HTML that already contains the SDK is still served until it expires, or until you invalidate the cache for that distribution. For more information, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-challenge-javascript-sdk-injection.html">Automatic SDK integration for CloudFront distributions</a> in the <i>WAF Developer Guide</i>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationConfig) -> dict:
    out: dict = {}
    if "request_body" in value:
        import capo_wafv2.types.request_body

        out["RequestBody"] = capo_wafv2.types.request_body.serialize_aws_json_1_1(
            value["request_body"]
        )
    if "challenge_javascript_sdk_injection" in value:
        import capo_wafv2.types.challenge_javascript_sdk_injection

        out["ChallengeJavascriptSdkInjection"] = (
            capo_wafv2.types.challenge_javascript_sdk_injection.serialize_aws_json_1_1(
                value["challenge_javascript_sdk_injection"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociationConfig:
    out: AssociationConfig = {}  # type: ignore[typeddict-item]
    if data.get("RequestBody") is not None:
        import capo_wafv2.types.request_body

        out["request_body"] = capo_wafv2.types.request_body.deserialize_aws_json_1_1(
            data["RequestBody"]
        )
    if data.get("ChallengeJavascriptSdkInjection") is not None:
        import capo_wafv2.types.challenge_javascript_sdk_injection

        out["challenge_javascript_sdk_injection"] = (
            capo_wafv2.types.challenge_javascript_sdk_injection.deserialize_aws_json_1_1(
                data["ChallengeJavascriptSdkInjection"]
            )
        )
    return out
