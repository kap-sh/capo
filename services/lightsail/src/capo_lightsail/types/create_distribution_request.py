"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateDistributionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lightsail.types.boolean
    import capo_lightsail.types.cache_behavior
    import capo_lightsail.types.cache_behavior_list
    import capo_lightsail.types.cache_settings
    import capo_lightsail.types.distribution_custom_error_response_list
    import capo_lightsail.types.input_origin
    import capo_lightsail.types.ip_address_type
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.string
    import capo_lightsail.types.tag_list
    import capo_lightsail.types.viewer_minimum_tls_protocol_version_enum
    import capo_lightsail.types.waf_rule_list


class CreateDistributionRequest(TypedDict, closed=True):
    distribution_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name for the distribution.</p>"""
    origin: "capo_lightsail.types.input_origin.InputOrigin"
    """<p>An object that describes the origin resource for the distribution, such as a Lightsail instance, bucket, or load balancer.</p> <p>The distribution pulls, caches, and serves content from the origin.</p>"""
    default_cache_behavior: "capo_lightsail.types.cache_behavior.CacheBehavior"
    """<p>An object that describes the default cache behavior for the distribution.</p>"""
    cache_behavior_settings: NotRequired[
        "capo_lightsail.types.cache_settings.CacheSettings"
    ]
    """<p>An object that describes the cache behavior settings for the distribution.</p>"""
    cache_behaviors: NotRequired[
        "capo_lightsail.types.cache_behavior_list.CacheBehaviorList"
    ]
    """<p>An array of objects that describe the per-path cache behavior for the distribution.</p>"""
    bundle_id: "capo_lightsail.types.string.string"
    """<p>The bundle ID to use for the distribution.</p> <p>A distribution bundle describes the specifications of your distribution, such as the monthly cost and monthly network transfer quota.</p> <p>Use the <code>GetDistributionBundles</code> action to get a list of distribution bundle IDs that you can specify.</p>"""
    ip_address_type: NotRequired["capo_lightsail.types.ip_address_type.IpAddressType"]
    """<p>The IP address type for the distribution.</p> <p>The possible values are <code>ipv4</code> for IPv4 only, and <code>dualstack</code> for IPv4 and IPv6.</p> <p>The default value is <code>dualstack</code>.</p>"""
    tags: NotRequired["capo_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values to add to the distribution during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>"""
    certificate_name: NotRequired["capo_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the SSL/TLS certificate that you want to attach to the distribution.</p> <p>Use the <a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetCertificates.html">GetCertificates</a> action to get a list of certificate names that you can specify.</p>"""
    viewer_minimum_tls_protocol_version: NotRequired[
        "capo_lightsail.types.viewer_minimum_tls_protocol_version_enum.ViewerMinimumTlsProtocolVersionEnum"
    ]
    """<p>The minimum TLS protocol version for the SSL/TLS certificate.</p>"""
    enable_private_origin_access: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>Specifies whether to enable private origin access for the distribution. With private origin access, the distribution can serve objects that aren't publicly accessible from a Lightsail bucket.</p> <p>Lightsail grants the distribution permission to read the bucket's objects. Enabling private origin access doesn't change the bucket's access settings, and you can still retrieve publicly accessible objects directly from the bucket's endpoint.</p> <note> <p>You can enable private origin access only when the distribution's origin is a Lightsail bucket. If the origin is another resource type, the request fails.</p> </note>"""
    default_root_object: NotRequired["capo_lightsail.types.string.string"]
    """<p>The object (for example, <code>index.html</code>) that the distribution returns when a viewer requests the root URL of the distribution (<code>/</code>) instead of a specific object. The object that you specify must be available from the origin.</p>"""
    custom_error_responses: NotRequired[
        "capo_lightsail.types.distribution_custom_error_response_list.DistributionCustomErrorResponseList"
    ]
    """<p>An array of objects that describe the custom error responses for the distribution. With a custom error response, you can specify the page to return when the origin responds with a given HTTP error code. You can also specify the HTTP status code to send to the viewer.</p>"""
    enable_waf: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>Specifies whether to enable Web Application Firewall (WAF) for the distribution. WAF inspects viewer requests and blocks requests that match the WAF rule groups that you enable.</p> <p>When you enable WAF without specifying the <code>wafRules</code> parameter, the distribution has no WAF rule groups enabled and doesn't block any requests.</p> <note> <p>WAF is available only for distributions that use the <code>medium_1_0</code> or <code>large_1_0</code> bundle.</p> </note>"""
    waf_rules: NotRequired["capo_lightsail.types.waf_rule_list.WafRuleList"]
    """<p>An array of objects that describe the WAF rule groups to enable for the distribution.</p> <p>The WAF rule groups that you can specify depend on the bundle of the distribution:</p> <ul> <li> <p> <code>medium_1_0</code> – Supports the <code>AWSManagedRulesCommonRuleSet</code>, <code>AWSManagedRulesKnownBadInputsRuleSet</code>, and <code>AWSManagedRulesAnonymousIpList</code> rule groups.</p> </li> <li> <p> <code>large_1_0</code> – Supports the rule groups for <code>medium_1_0</code>, plus <code>AWSManagedRulesAdminProtectionRuleSet</code>, <code>AWSManagedRulesSQLiRuleSet</code>, <code>AWSManagedRulesLinuxRuleSet</code>, <code>AWSManagedRulesUnixRuleSet</code>, <code>AWSManagedRulesWindowsRuleSet</code>, <code>AWSManagedRulesPHPRuleSet</code>, <code>AWSManagedRulesWordPressRuleSet</code>, <code>AWSManagedRulesAmazonIpReputationList</code>, <code>AWSManagedRulesATPRuleSet</code>, <code>AWSManagedRulesACFPRuleSet</code>, and <code>AWSManagedRulesBotControlRuleSet</code> rule groups.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDistributionRequest) -> dict:
    out: dict = {}
    out["distributionName"] = value["distribution_name"]
    import capo_lightsail.types.input_origin

    out["origin"] = capo_lightsail.types.input_origin.serialize_aws_json_1_1(
        value["origin"]
    )
    import capo_lightsail.types.cache_behavior

    out["defaultCacheBehavior"] = (
        capo_lightsail.types.cache_behavior.serialize_aws_json_1_1(
            value["default_cache_behavior"]
        )
    )
    if "cache_behavior_settings" in value:
        import capo_lightsail.types.cache_settings

        out["cacheBehaviorSettings"] = (
            capo_lightsail.types.cache_settings.serialize_aws_json_1_1(
                value["cache_behavior_settings"]
            )
        )
    if "cache_behaviors" in value:
        import capo_lightsail.types.cache_behavior_list

        out["cacheBehaviors"] = (
            capo_lightsail.types.cache_behavior_list.serialize_aws_json_1_1(
                value["cache_behaviors"]
            )
        )
    out["bundleId"] = value["bundle_id"]
    if "ip_address_type" in value:
        import capo_lightsail.types.ip_address_type

        out["ipAddressType"] = (
            capo_lightsail.types.ip_address_type.serialize_aws_json_1_1(
                value["ip_address_type"]
            )
        )
    if "tags" in value:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "certificate_name" in value:
        out["certificateName"] = value["certificate_name"]
    if "viewer_minimum_tls_protocol_version" in value:
        import capo_lightsail.types.viewer_minimum_tls_protocol_version_enum

        out["viewerMinimumTlsProtocolVersion"] = (
            capo_lightsail.types.viewer_minimum_tls_protocol_version_enum.serialize_aws_json_1_1(
                value["viewer_minimum_tls_protocol_version"]
            )
        )
    if "enable_private_origin_access" in value:
        out["enablePrivateOriginAccess"] = value["enable_private_origin_access"]
    if "default_root_object" in value:
        out["defaultRootObject"] = value["default_root_object"]
    if "custom_error_responses" in value:
        import capo_lightsail.types.distribution_custom_error_response_list

        out["customErrorResponses"] = (
            capo_lightsail.types.distribution_custom_error_response_list.serialize_aws_json_1_1(
                value["custom_error_responses"]
            )
        )
    if "enable_waf" in value:
        out["enableWaf"] = value["enable_waf"]
    if "waf_rules" in value:
        import capo_lightsail.types.waf_rule_list

        out["wafRules"] = capo_lightsail.types.waf_rule_list.serialize_aws_json_1_1(
            value["waf_rules"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDistributionRequest:
    out: CreateDistributionRequest = {}  # type: ignore[typeddict-item]
    if data.get("distributionName") is not None:
        out["distribution_name"] = data["distributionName"]
    else:
        out["distribution_name"] = ""
    if data.get("origin") is not None:
        import capo_lightsail.types.input_origin

        out["origin"] = capo_lightsail.types.input_origin.deserialize_aws_json_1_1(
            data["origin"]
        )
    else:
        raise DeserializationError("CreateDistributionRequest.origin required")
    if data.get("defaultCacheBehavior") is not None:
        import capo_lightsail.types.cache_behavior

        out["default_cache_behavior"] = (
            capo_lightsail.types.cache_behavior.deserialize_aws_json_1_1(
                data["defaultCacheBehavior"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDistributionRequest.default_cache_behavior required"
        )
    if data.get("cacheBehaviorSettings") is not None:
        import capo_lightsail.types.cache_settings

        out["cache_behavior_settings"] = (
            capo_lightsail.types.cache_settings.deserialize_aws_json_1_1(
                data["cacheBehaviorSettings"]
            )
        )
    if data.get("cacheBehaviors") is not None:
        import capo_lightsail.types.cache_behavior_list

        out["cache_behaviors"] = (
            capo_lightsail.types.cache_behavior_list.deserialize_aws_json_1_1(
                data["cacheBehaviors"]
            )
        )
    if data.get("bundleId") is not None:
        out["bundle_id"] = data["bundleId"]
    else:
        out["bundle_id"] = ""
    if data.get("ipAddressType") is not None:
        import capo_lightsail.types.ip_address_type

        out["ip_address_type"] = (
            capo_lightsail.types.ip_address_type.deserialize_aws_json_1_1(
                data["ipAddressType"]
            )
        )
    if data.get("tags") is not None:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if data.get("certificateName") is not None:
        out["certificate_name"] = data["certificateName"]
    if data.get("viewerMinimumTlsProtocolVersion") is not None:
        import capo_lightsail.types.viewer_minimum_tls_protocol_version_enum

        out["viewer_minimum_tls_protocol_version"] = (
            capo_lightsail.types.viewer_minimum_tls_protocol_version_enum.deserialize_aws_json_1_1(
                data["viewerMinimumTlsProtocolVersion"]
            )
        )
    if data.get("enablePrivateOriginAccess") is not None:
        out["enable_private_origin_access"] = data["enablePrivateOriginAccess"]
    if data.get("defaultRootObject") is not None:
        out["default_root_object"] = data["defaultRootObject"]
    if data.get("customErrorResponses") is not None:
        import capo_lightsail.types.distribution_custom_error_response_list

        out["custom_error_responses"] = (
            capo_lightsail.types.distribution_custom_error_response_list.deserialize_aws_json_1_1(
                data["customErrorResponses"]
            )
        )
    if data.get("enableWaf") is not None:
        out["enable_waf"] = data["enableWaf"]
    if data.get("wafRules") is not None:
        import capo_lightsail.types.waf_rule_list

        out["waf_rules"] = capo_lightsail.types.waf_rule_list.deserialize_aws_json_1_1(
            data["wafRules"]
        )
    return out
