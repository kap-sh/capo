"""Generated from Smithy shape ``com.amazonaws.wafv2#CreateWebACLRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.application_config
    import capo_wafv2.types.association_config
    import capo_wafv2.types.captcha_config
    import capo_wafv2.types.challenge_config
    import capo_wafv2.types.custom_response_bodies
    import capo_wafv2.types.data_protection_config
    import capo_wafv2.types.default_action
    import capo_wafv2.types.entity_description
    import capo_wafv2.types.entity_name
    import capo_wafv2.types.monetization_config
    import capo_wafv2.types.on_source_d_do_s_protection_config
    import capo_wafv2.types.rules
    import capo_wafv2.types.scope
    import capo_wafv2.types.tag_list
    import capo_wafv2.types.token_domains
    import capo_wafv2.types.visibility_config


class CreateWebACLRequest(TypedDict, closed=True):
    name: "capo_wafv2.types.entity_name.EntityName"
    """<p>The name of the web ACL. You cannot change the name of a web ACL after you create it.</p>"""
    scope: "capo_wafv2.types.scope.Scope"
    """<p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>"""
    default_action: "capo_wafv2.types.default_action.DefaultAction"
    """<p>The action to perform if none of the <code>Rules</code> contained in the <code>WebACL</code> match. </p>"""
    description: NotRequired["capo_wafv2.types.entity_description.EntityDescription"]
    """<p>A description of the web ACL that helps with identification. </p>"""
    rules: NotRequired["capo_wafv2.types.rules.Rules"]
    """<p>The <a>Rule</a> statements used to identify the web requests that you want to manage. Each rule includes one top-level statement that WAF uses to identify matching web requests, and parameters that govern how WAF handles them. </p>"""
    visibility_config: "capo_wafv2.types.visibility_config.VisibilityConfig"
    """<p>Defines and enables Amazon CloudWatch metrics and web request sample collection. </p>"""
    data_protection_config: NotRequired[
        "capo_wafv2.types.data_protection_config.DataProtectionConfig"
    ]
    """<p>Specifies data protection to apply to the web request data for the web ACL. This is a web ACL level data protection option. </p> <p>The data protection that you configure for the web ACL alters the data that's available for any other data collection activity, including your WAF logging destinations, web ACL request sampling, and Amazon Security Lake data collection and management. Your other option for data protection is in the logging configuration, which only affects logging. </p>"""
    tags: NotRequired["capo_wafv2.types.tag_list.TagList"]
    """<p>An array of key:value pairs to associate with the resource.</p>"""
    custom_response_bodies: NotRequired[
        "capo_wafv2.types.custom_response_bodies.CustomResponseBodies"
    ]
    """<p>A map of custom response keys and content bodies. When you create a rule with a block action, you can send a custom response to the web request. You define these for the web ACL, and then use them in the rules and default actions that you define in the web ACL. </p> <p>For information about customizing web requests and responses, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html">Customizing web requests and responses in WAF</a> in the <i>WAF Developer Guide</i>. </p> <p>For information about the limits on count and size for custom request and response settings, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">WAF quotas</a> in the <i>WAF Developer Guide</i>. </p>"""
    captcha_config: NotRequired["capo_wafv2.types.captcha_config.CaptchaConfig"]
    """<p>Specifies how WAF should handle <code>CAPTCHA</code> evaluations for rules that don't have their own <code>CaptchaConfig</code> settings. If you don't specify this, WAF uses its default settings for <code>CaptchaConfig</code>. </p>"""
    challenge_config: NotRequired["capo_wafv2.types.challenge_config.ChallengeConfig"]
    """<p>Specifies how WAF should handle challenge evaluations for rules that don't have their own <code>ChallengeConfig</code> settings. If you don't specify this, WAF uses its default settings for <code>ChallengeConfig</code>. </p>"""
    token_domains: NotRequired["capo_wafv2.types.token_domains.TokenDomains"]
    """<p>Specifies the domains that WAF should accept in a web request token. This enables the use of tokens across multiple protected websites. When WAF provides a token, it uses the domain of the Amazon Web Services resource that the web ACL is protecting. If you don't specify a list of token domains, WAF accepts tokens only for the domain of the protected resource. With a token domain list, WAF accepts the resource's host domain plus all domains in the token domain list, including their prefixed subdomains.</p> <p>Example JSON: <code>"TokenDomains": { "mywebsite.com", "myotherwebsite.com" }</code> </p> <p>Public suffixes aren't allowed. For example, you can't use <code>gov.au</code> or <code>co.uk</code> as token domains.</p>"""
    association_config: NotRequired[
        "capo_wafv2.types.association_config.AssociationConfig"
    ]
    """<p>Specifies custom configurations for the associations between the web ACL and protected resources. </p> <p>Use this to customize the maximum size of the request body that your protected resources forward to WAF for inspection. You can customize this setting for CloudFront, API Gateway, Amazon Cognito, App Runner, or Verified Access resources. The default setting is 16 KB (16,384 bytes). </p> <note> <p>You are charged additional fees when your protected resources forward body sizes that are larger than the default. For more information, see <a href="http://aws.amazon.com/waf/pricing/">WAF Pricing</a>.</p> </note> <p>For Application Load Balancer and AppSync, the limit is fixed at 8 KB (8,192 bytes).</p>"""
    on_source_d_do_s_protection_config: NotRequired[
        "capo_wafv2.types.on_source_d_do_s_protection_config.OnSourceDDoSProtectionConfig"
    ]
    """<p>Specifies the type of DDoS protection to apply to web request data for a web ACL. For most scenarios, it is recommended to use the default protection level, <code>ACTIVE_UNDER_DDOS</code>. If a web ACL is associated with multiple Application Load Balancers, the changes you make to DDoS protection in that web ACL will apply to all associated Application Load Balancers.</p>"""
    application_config: NotRequired[
        "capo_wafv2.types.application_config.ApplicationConfig"
    ]
    """<p>Configures the ability for the WAF console to store and retrieve application attributes during the web ACL creation process. Application attributes help WAF give recommendations for protection packs.</p>"""
    monetization_config: NotRequired[
        "capo_wafv2.types.monetization_config.MonetizationConfig"
    ]
    """<p>The monetization configuration for the web ACL. Provide this when any rule in the web ACL uses the <code>Monetize</code> action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWebACLRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_wafv2.types.scope

    out["Scope"] = capo_wafv2.types.scope.serialize_aws_json_1_1(value["scope"])
    import capo_wafv2.types.default_action

    out["DefaultAction"] = capo_wafv2.types.default_action.serialize_aws_json_1_1(
        value["default_action"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "rules" in value:
        import capo_wafv2.types.rules

        out["Rules"] = capo_wafv2.types.rules.serialize_aws_json_1_1(value["rules"])
    import capo_wafv2.types.visibility_config

    out["VisibilityConfig"] = capo_wafv2.types.visibility_config.serialize_aws_json_1_1(
        value["visibility_config"]
    )
    if "data_protection_config" in value:
        import capo_wafv2.types.data_protection_config

        out["DataProtectionConfig"] = (
            capo_wafv2.types.data_protection_config.serialize_aws_json_1_1(
                value["data_protection_config"]
            )
        )
    if "tags" in value:
        import capo_wafv2.types.tag_list

        out["Tags"] = capo_wafv2.types.tag_list.serialize_aws_json_1_1(value["tags"])
    if "custom_response_bodies" in value:
        import capo_wafv2.types.custom_response_bodies

        out["CustomResponseBodies"] = (
            capo_wafv2.types.custom_response_bodies.serialize_aws_json_1_1(
                value["custom_response_bodies"]
            )
        )
    if "captcha_config" in value:
        import capo_wafv2.types.captcha_config

        out["CaptchaConfig"] = capo_wafv2.types.captcha_config.serialize_aws_json_1_1(
            value["captcha_config"]
        )
    if "challenge_config" in value:
        import capo_wafv2.types.challenge_config

        out["ChallengeConfig"] = (
            capo_wafv2.types.challenge_config.serialize_aws_json_1_1(
                value["challenge_config"]
            )
        )
    if "token_domains" in value:
        import capo_wafv2.types.token_domains

        out["TokenDomains"] = capo_wafv2.types.token_domains.serialize_aws_json_1_1(
            value["token_domains"]
        )
    if "association_config" in value:
        import capo_wafv2.types.association_config

        out["AssociationConfig"] = (
            capo_wafv2.types.association_config.serialize_aws_json_1_1(
                value["association_config"]
            )
        )
    if "on_source_d_do_s_protection_config" in value:
        import capo_wafv2.types.on_source_d_do_s_protection_config

        out["OnSourceDDoSProtectionConfig"] = (
            capo_wafv2.types.on_source_d_do_s_protection_config.serialize_aws_json_1_1(
                value["on_source_d_do_s_protection_config"]
            )
        )
    if "application_config" in value:
        import capo_wafv2.types.application_config

        out["ApplicationConfig"] = (
            capo_wafv2.types.application_config.serialize_aws_json_1_1(
                value["application_config"]
            )
        )
    if "monetization_config" in value:
        import capo_wafv2.types.monetization_config

        out["MonetizationConfig"] = (
            capo_wafv2.types.monetization_config.serialize_aws_json_1_1(
                value["monetization_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWebACLRequest:
    out: CreateWebACLRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateWebACLRequest.name required")
    if data.get("Scope") is not None:
        import capo_wafv2.types.scope

        out["scope"] = capo_wafv2.types.scope.deserialize_aws_json_1_1(data["Scope"])
    else:
        raise DeserializationError("CreateWebACLRequest.scope required")
    if data.get("DefaultAction") is not None:
        import capo_wafv2.types.default_action

        out["default_action"] = (
            capo_wafv2.types.default_action.deserialize_aws_json_1_1(
                data["DefaultAction"]
            )
        )
    else:
        raise DeserializationError("CreateWebACLRequest.default_action required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Rules") is not None:
        import capo_wafv2.types.rules

        out["rules"] = capo_wafv2.types.rules.deserialize_aws_json_1_1(data["Rules"])
    if data.get("VisibilityConfig") is not None:
        import capo_wafv2.types.visibility_config

        out["visibility_config"] = (
            capo_wafv2.types.visibility_config.deserialize_aws_json_1_1(
                data["VisibilityConfig"]
            )
        )
    else:
        raise DeserializationError("CreateWebACLRequest.visibility_config required")
    if data.get("DataProtectionConfig") is not None:
        import capo_wafv2.types.data_protection_config

        out["data_protection_config"] = (
            capo_wafv2.types.data_protection_config.deserialize_aws_json_1_1(
                data["DataProtectionConfig"]
            )
        )
    if data.get("Tags") is not None:
        import capo_wafv2.types.tag_list

        out["tags"] = capo_wafv2.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    if data.get("CustomResponseBodies") is not None:
        import capo_wafv2.types.custom_response_bodies

        out["custom_response_bodies"] = (
            capo_wafv2.types.custom_response_bodies.deserialize_aws_json_1_1(
                data["CustomResponseBodies"]
            )
        )
    if data.get("CaptchaConfig") is not None:
        import capo_wafv2.types.captcha_config

        out["captcha_config"] = (
            capo_wafv2.types.captcha_config.deserialize_aws_json_1_1(
                data["CaptchaConfig"]
            )
        )
    if data.get("ChallengeConfig") is not None:
        import capo_wafv2.types.challenge_config

        out["challenge_config"] = (
            capo_wafv2.types.challenge_config.deserialize_aws_json_1_1(
                data["ChallengeConfig"]
            )
        )
    if data.get("TokenDomains") is not None:
        import capo_wafv2.types.token_domains

        out["token_domains"] = capo_wafv2.types.token_domains.deserialize_aws_json_1_1(
            data["TokenDomains"]
        )
    if data.get("AssociationConfig") is not None:
        import capo_wafv2.types.association_config

        out["association_config"] = (
            capo_wafv2.types.association_config.deserialize_aws_json_1_1(
                data["AssociationConfig"]
            )
        )
    if data.get("OnSourceDDoSProtectionConfig") is not None:
        import capo_wafv2.types.on_source_d_do_s_protection_config

        out["on_source_d_do_s_protection_config"] = (
            capo_wafv2.types.on_source_d_do_s_protection_config.deserialize_aws_json_1_1(
                data["OnSourceDDoSProtectionConfig"]
            )
        )
    if data.get("ApplicationConfig") is not None:
        import capo_wafv2.types.application_config

        out["application_config"] = (
            capo_wafv2.types.application_config.deserialize_aws_json_1_1(
                data["ApplicationConfig"]
            )
        )
    if data.get("MonetizationConfig") is not None:
        import capo_wafv2.types.monetization_config

        out["monetization_config"] = (
            capo_wafv2.types.monetization_config.deserialize_aws_json_1_1(
                data["MonetizationConfig"]
            )
        )
    return out
