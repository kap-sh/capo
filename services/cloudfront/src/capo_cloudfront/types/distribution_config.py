"""Generated from Smithy shape ``com.amazonaws.cloudfront#DistributionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.aliases
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.cache_behaviors
    import capo_cloudfront.types.cache_tag_config
    import capo_cloudfront.types.comment_type
    import capo_cloudfront.types.connection_function_association
    import capo_cloudfront.types.connection_mode
    import capo_cloudfront.types.custom_error_responses
    import capo_cloudfront.types.default_cache_behavior
    import capo_cloudfront.types.http_version
    import capo_cloudfront.types.logging_config
    import capo_cloudfront.types.origin_groups
    import capo_cloudfront.types.origins
    import capo_cloudfront.types.price_class
    import capo_cloudfront.types.restrictions
    import capo_cloudfront.types.string
    import capo_cloudfront.types.tenant_config
    import capo_cloudfront.types.viewer_certificate
    import capo_cloudfront.types.viewer_mtls_config


class DistributionConfig(TypedDict, closed=True):
    caller_reference: "capo_cloudfront.types.string.string"
    """<p>A unique value (for example, a date-time stamp) that ensures that the request can't be replayed.</p> <p>If the value of <code>CallerReference</code> is new (regardless of the content of the <code>DistributionConfig</code> object), CloudFront creates a new distribution.</p> <p>If <code>CallerReference</code> is a value that you already sent in a previous request to create a distribution, CloudFront returns a <code>DistributionAlreadyExists</code> error.</p>"""
    aliases: NotRequired["capo_cloudfront.types.aliases.Aliases"]
    """<note> <p>This field only supports standard distributions. You can't specify this field for multi-tenant distributions. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html#unsupported-saas">Unsupported features for SaaS Manager for Amazon CloudFront</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> </note> <p>A complex type that contains information about CNAMEs (alternate domain names), if any, for this distribution.</p>"""
    default_root_object: NotRequired["capo_cloudfront.types.string.string"]
    """<p>When a viewer requests the root URL for your distribution, the default root object is the object that you want CloudFront to request from your origin. For example, if your root URL is <code>https://www.example.com</code>, you can specify CloudFront to return the <code>index.html</code> file as the default root object. You can specify a default root object so that viewers see a specific file or object, instead of another object in your distribution (for example, <code>https://www.example.com/product-description.html</code>). A default root object avoids exposing the contents of your distribution.</p> <p>You can specify the object name or a path to the object name (for example, <code>index.html</code> or <code>exampleFolderName/index.html</code>). Your string can't begin with a forward slash (<code>/</code>). Only specify the object name or the path to the object.</p> <p>If you don't want to specify a default root object when you create a distribution, include an empty <code>DefaultRootObject</code> element.</p> <p>To delete the default root object from an existing distribution, update the distribution configuration and include an empty <code>DefaultRootObject</code> element.</p> <p>To replace the default root object, update the distribution configuration and specify the new object.</p> <p>For more information about the default root object, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DefaultRootObject.html">Specify a default root object</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    origins: "capo_cloudfront.types.origins.Origins"
    """<p>A complex type that contains information about origins for this distribution.</p>"""
    origin_groups: NotRequired["capo_cloudfront.types.origin_groups.OriginGroups"]
    """<p>A complex type that contains information about origin groups for this distribution.</p>"""
    default_cache_behavior: (
        "capo_cloudfront.types.default_cache_behavior.DefaultCacheBehavior"
    )
    """<p>A complex type that describes the default cache behavior if you don't specify a <code>CacheBehavior</code> element or if files don't match any of the values of <code>PathPattern</code> in <code>CacheBehavior</code> elements. You must create exactly one default cache behavior.</p>"""
    cache_behaviors: NotRequired["capo_cloudfront.types.cache_behaviors.CacheBehaviors"]
    """<p>A complex type that contains zero or more <code>CacheBehavior</code> elements.</p>"""
    custom_error_responses: NotRequired[
        "capo_cloudfront.types.custom_error_responses.CustomErrorResponses"
    ]
    """<p>A complex type that controls the following:</p> <ul> <li> <p>Whether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer.</p> </li> <li> <p>How long CloudFront caches HTTP status codes in the 4xx and 5xx range.</p> </li> </ul> <p>For more information about custom error pages, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/custom-error-pages.html">Customizing Error Responses</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    comment: "capo_cloudfront.types.comment_type.CommentType"
    """<p>A comment to describe the distribution. The comment cannot be longer than 128 characters.</p>"""
    logging: NotRequired["capo_cloudfront.types.logging_config.LoggingConfig"]
    """<p>A complex type that controls whether access logs are written for the distribution.</p> <p>For more information about logging, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html">Access Logs</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    price_class: NotRequired["capo_cloudfront.types.price_class.PriceClass"]
    """<note> <p>This field only supports standard distributions. You can't specify this field for multi-tenant distributions. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html#unsupported-saas">Unsupported features for SaaS Manager for Amazon CloudFront</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> </note> <p>The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify <code>PriceClass_All</code>, CloudFront responds to requests for your objects from all CloudFront edge locations.</p> <p>If you specify a price class other than <code>PriceClass_All</code>, CloudFront serves your objects from the CloudFront edge location that has the lowest latency among the edge locations in your price class. Viewers who are in or near regions that are excluded from your specified price class may encounter slower performance.</p> <p>For more information about price classes, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PriceClass.html">Choosing the Price Class for a CloudFront Distribution</a> in the <i>Amazon CloudFront Developer Guide</i>. For information about CloudFront pricing, including how price classes (such as Price Class 100) map to CloudFront regions, see <a href="http://aws.amazon.com/cloudfront/pricing/">Amazon CloudFront Pricing</a>.</p>"""
    enabled: "capo_cloudfront.types.boolean.boolean"
    """<p>From this field, you can enable or disable the selected distribution.</p>"""
    viewer_certificate: NotRequired[
        "capo_cloudfront.types.viewer_certificate.ViewerCertificate"
    ]
    """<p>A complex type that determines the distribution's SSL/TLS configuration for communicating with viewers.</p>"""
    restrictions: NotRequired["capo_cloudfront.types.restrictions.Restrictions"]
    """<p>A complex type that identifies ways in which you want to restrict distribution of your content.</p>"""
    web_acl_id: NotRequired["capo_cloudfront.types.string.string"]
    """<note> <p>Multi-tenant distributions only support WAF V2 web ACLs.</p> </note> <p>A unique identifier that specifies the WAF web ACL, if any, to associate with this distribution. To specify a web ACL created using the latest version of WAF, use the ACL ARN, for example <code>arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111</code>. To specify a web ACL created using WAF Classic, use the ACL ID, for example <code>a1b2c3d4-5678-90ab-cdef-EXAMPLE11111</code>.</p> <p>WAF is a web application firewall that lets you monitor the HTTP and HTTPS requests that are forwarded to CloudFront, and lets you control access to your content. Based on conditions that you specify, such as the IP addresses that requests originate from or the values of query strings, CloudFront responds to requests either with the requested content or with an HTTP 403 status code (Forbidden). You can also configure CloudFront to return a custom error page when a request is blocked. For more information about WAF, see the <a href="https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html">WAF Developer Guide</a>.</p>"""
    http_version: NotRequired["capo_cloudfront.types.http_version.HttpVersion"]
    """<p>(Optional) Specify the HTTP version(s) that you want viewers to use to communicate with CloudFront. The default value for new web distributions is <code>http2</code>. Viewers that don't support HTTP/2 automatically use an earlier HTTP version.</p> <p>For viewers and CloudFront to use HTTP/2, viewers must support TLSv1.2 or later, and must support Server Name Indication (SNI).</p> <p>For viewers and CloudFront to use HTTP/3, viewers must support TLSv1.3 and Server Name Indication (SNI). CloudFront supports HTTP/3 connection migration to allow the viewer to switch networks without losing connection. For more information about connection migration, see <a href="https://www.rfc-editor.org/rfc/rfc9000.html#name-connection-migration">Connection Migration</a> at RFC 9000. For more information about supported TLSv1.3 ciphers, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html">Supported protocols and ciphers between viewers and CloudFront</a>.</p>"""
    is_ipv6_enabled: NotRequired["capo_cloudfront.types.boolean.boolean"]
    """<note> <p>To use this field for a multi-tenant distribution, use a connection group instead. For more information, see <a href="https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ConnectionGroup.html">ConnectionGroup</a>.</p> </note> <p>If you want CloudFront to respond to IPv6 DNS requests with an IPv6 address for your distribution, specify <code>true</code>. If you specify <code>false</code>, CloudFront responds to IPv6 DNS requests with the DNS response code <code>NOERROR</code> and with no IP addresses. This allows viewers to submit a second request, for an IPv4 address for your distribution.</p> <p>In general, you should enable IPv6 if you have users on IPv6 networks who want to access your content. However, if you're using signed URLs or signed cookies to restrict access to your content, and if you're using a custom policy that includes the <code>IpAddress</code> parameter to restrict the IP addresses that can access your content, don't enable IPv6. If you want to restrict access to some content by IP address and not restrict access to other content (or restrict access but not by IP address), you can create two distributions. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-creating-signed-url-custom-policy.html">Creating a Signed URL Using a Custom Policy</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <p>If you're using an Route 53 Amazon Web Services Integration alias resource record set to route traffic to your CloudFront distribution, you need to create a second alias resource record set when both of the following are true:</p> <ul> <li> <p>You enable IPv6 for the distribution</p> </li> <li> <p>You're using alternate domain names in the URLs for your objects</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-cloudfront-distribution.html">Routing Traffic to an Amazon CloudFront Web Distribution by Using Your Domain Name</a> in the <i>Route 53 Amazon Web Services Integration Developer Guide</i>.</p> <p>If you created a CNAME resource record set, either with Route 53 Amazon Web Services Integration or with another DNS service, you don't need to make any changes. A CNAME record will route traffic to your distribution regardless of the IP address format of the viewer request.</p>"""
    continuous_deployment_policy_id: NotRequired["capo_cloudfront.types.string.string"]
    """<note> <p>This field only supports standard distributions. You can't specify this field for multi-tenant distributions. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html#unsupported-saas">Unsupported features for SaaS Manager for Amazon CloudFront</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> </note> <p>The identifier of a continuous deployment policy. For more information, see <code>CreateContinuousDeploymentPolicy</code>.</p>"""
    staging: NotRequired["capo_cloudfront.types.boolean.boolean"]
    """<note> <p>This field only supports standard distributions. You can't specify this field for multi-tenant distributions. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html#unsupported-saas">Unsupported features for SaaS Manager for Amazon CloudFront</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> </note> <p>A Boolean that indicates whether this is a staging distribution. When this value is <code>true</code>, this is a staging distribution. When this value is <code>false</code>, this is not a staging distribution.</p>"""
    anycast_ip_list_id: NotRequired["capo_cloudfront.types.string.string"]
    """<note> <p>To use this field for a multi-tenant distribution, use a connection group instead. For more information, see <a href="https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ConnectionGroup.html">ConnectionGroup</a>.</p> </note> <p>ID of the Anycast static IP list that is associated with the distribution.</p>"""
    tenant_config: NotRequired["capo_cloudfront.types.tenant_config.TenantConfig"]
    """<note> <p>This field only supports multi-tenant distributions. You can't specify this field for standard distributions. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html#unsupported-saas">Unsupported features for SaaS Manager for Amazon CloudFront</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> </note> <p>A distribution tenant configuration.</p>"""
    connection_mode: NotRequired["capo_cloudfront.types.connection_mode.ConnectionMode"]
    """<p>This field specifies whether the connection mode is through a standard distribution (direct) or a multi-tenant distribution with distribution tenants (tenant-only).</p>"""
    viewer_mtls_config: NotRequired[
        "capo_cloudfront.types.viewer_mtls_config.ViewerMtlsConfig"
    ]
    """<p>The distribution's viewer mTLS configuration.</p>"""
    connection_function_association: NotRequired[
        "capo_cloudfront.types.connection_function_association.ConnectionFunctionAssociation"
    ]
    """<p>The distribution's connection function association.</p>"""
    cache_tag_config: NotRequired[
        "capo_cloudfront.types.cache_tag_config.CacheTagConfig"
    ]
    """<p>Configuration for cache tag extraction from origin responses. When specified, CloudFront reads the header named in <code>HeaderName</code> from origin responses and stores the comma-separated values as cache tags on the object.</p> <p>Distributions without <code>CacheTagConfig</code> do not extract tags. When <code>CacheTagConfig</code> is removed from a distribution via <code>UpdateDistribution</code>, CloudFront stops extracting tags from origin responses.</p> <note> <p>Changing the <code>HeaderName</code> on an existing distribution does not retroactively affect previously cached objects. Tag-based invalidations will not apply to objects already cached using a previous header. To ensure tag invalidations function after updating the header name, use path-based invalidations to recache all objects that use cache tags.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: DistributionConfig, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "CallerReference").text = str(value["caller_reference"])
    if "aliases" in value:
        import capo_cloudfront.types.aliases

        capo_cloudfront.types.aliases.serialize_xml(value["aliases"], el, "Aliases")
    if "default_root_object" in value:
        SubElement(el, "DefaultRootObject").text = str(value["default_root_object"])
    import capo_cloudfront.types.origins

    capo_cloudfront.types.origins.serialize_xml(value["origins"], el, "Origins")
    if "origin_groups" in value:
        import capo_cloudfront.types.origin_groups

        capo_cloudfront.types.origin_groups.serialize_xml(
            value["origin_groups"], el, "OriginGroups"
        )
    import capo_cloudfront.types.default_cache_behavior

    capo_cloudfront.types.default_cache_behavior.serialize_xml(
        value["default_cache_behavior"], el, "DefaultCacheBehavior"
    )
    if "cache_behaviors" in value:
        import capo_cloudfront.types.cache_behaviors

        capo_cloudfront.types.cache_behaviors.serialize_xml(
            value["cache_behaviors"], el, "CacheBehaviors"
        )
    if "custom_error_responses" in value:
        import capo_cloudfront.types.custom_error_responses

        capo_cloudfront.types.custom_error_responses.serialize_xml(
            value["custom_error_responses"], el, "CustomErrorResponses"
        )
    SubElement(el, "Comment").text = str(value["comment"])
    if "logging" in value:
        import capo_cloudfront.types.logging_config

        capo_cloudfront.types.logging_config.serialize_xml(
            value["logging"], el, "Logging"
        )
    if "price_class" in value:
        import capo_cloudfront.types.price_class

        capo_cloudfront.types.price_class.serialize_xml(
            value["price_class"], el, "PriceClass"
        )
    SubElement(el, "Enabled").text = "true" if value["enabled"] else "false"
    if "viewer_certificate" in value:
        import capo_cloudfront.types.viewer_certificate

        capo_cloudfront.types.viewer_certificate.serialize_xml(
            value["viewer_certificate"], el, "ViewerCertificate"
        )
    if "restrictions" in value:
        import capo_cloudfront.types.restrictions

        capo_cloudfront.types.restrictions.serialize_xml(
            value["restrictions"], el, "Restrictions"
        )
    if "web_acl_id" in value:
        SubElement(el, "WebACLId").text = str(value["web_acl_id"])
    if "http_version" in value:
        import capo_cloudfront.types.http_version

        capo_cloudfront.types.http_version.serialize_xml(
            value["http_version"], el, "HttpVersion"
        )
    if "is_ipv6_enabled" in value:
        SubElement(el, "IsIPV6Enabled").text = (
            "true" if value["is_ipv6_enabled"] else "false"
        )
    if "continuous_deployment_policy_id" in value:
        SubElement(el, "ContinuousDeploymentPolicyId").text = str(
            value["continuous_deployment_policy_id"]
        )
    if "staging" in value:
        SubElement(el, "Staging").text = "true" if value["staging"] else "false"
    if "anycast_ip_list_id" in value:
        SubElement(el, "AnycastIpListId").text = str(value["anycast_ip_list_id"])
    if "tenant_config" in value:
        import capo_cloudfront.types.tenant_config

        capo_cloudfront.types.tenant_config.serialize_xml(
            value["tenant_config"], el, "TenantConfig"
        )
    if "connection_mode" in value:
        import capo_cloudfront.types.connection_mode

        capo_cloudfront.types.connection_mode.serialize_xml(
            value["connection_mode"], el, "ConnectionMode"
        )
    if "viewer_mtls_config" in value:
        import capo_cloudfront.types.viewer_mtls_config

        capo_cloudfront.types.viewer_mtls_config.serialize_xml(
            value["viewer_mtls_config"], el, "ViewerMtlsConfig"
        )
    if "connection_function_association" in value:
        import capo_cloudfront.types.connection_function_association

        capo_cloudfront.types.connection_function_association.serialize_xml(
            value["connection_function_association"],
            el,
            "ConnectionFunctionAssociation",
        )
    if "cache_tag_config" in value:
        import capo_cloudfront.types.cache_tag_config

        capo_cloudfront.types.cache_tag_config.serialize_xml(
            value["cache_tag_config"], el, "CacheTagConfig"
        )


def deserialize_xml(el: Element) -> DistributionConfig:
    out: DistributionConfig = {}  # type: ignore[typeddict-item]
    child_caller_reference = el.find("CallerReference")
    if child_caller_reference is not None:
        out["caller_reference"] = str(child_caller_reference.text or "")
    else:
        raise DeserializationError("DistributionConfig.caller_reference required")
    child_aliases = el.find("Aliases")
    if child_aliases is not None:
        import capo_cloudfront.types.aliases

        out["aliases"] = capo_cloudfront.types.aliases.deserialize_xml(child_aliases)
    child_default_root_object = el.find("DefaultRootObject")
    if child_default_root_object is not None:
        out["default_root_object"] = str(child_default_root_object.text or "")
    child_origins = el.find("Origins")
    if child_origins is not None:
        import capo_cloudfront.types.origins

        out["origins"] = capo_cloudfront.types.origins.deserialize_xml(child_origins)
    else:
        raise DeserializationError("DistributionConfig.origins required")
    child_origin_groups = el.find("OriginGroups")
    if child_origin_groups is not None:
        import capo_cloudfront.types.origin_groups

        out["origin_groups"] = capo_cloudfront.types.origin_groups.deserialize_xml(
            child_origin_groups
        )
    child_default_cache_behavior = el.find("DefaultCacheBehavior")
    if child_default_cache_behavior is not None:
        import capo_cloudfront.types.default_cache_behavior

        out["default_cache_behavior"] = (
            capo_cloudfront.types.default_cache_behavior.deserialize_xml(
                child_default_cache_behavior
            )
        )
    else:
        raise DeserializationError("DistributionConfig.default_cache_behavior required")
    child_cache_behaviors = el.find("CacheBehaviors")
    if child_cache_behaviors is not None:
        import capo_cloudfront.types.cache_behaviors

        out["cache_behaviors"] = capo_cloudfront.types.cache_behaviors.deserialize_xml(
            child_cache_behaviors
        )
    child_custom_error_responses = el.find("CustomErrorResponses")
    if child_custom_error_responses is not None:
        import capo_cloudfront.types.custom_error_responses

        out["custom_error_responses"] = (
            capo_cloudfront.types.custom_error_responses.deserialize_xml(
                child_custom_error_responses
            )
        )
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    else:
        raise DeserializationError("DistributionConfig.comment required")
    child_logging = el.find("Logging")
    if child_logging is not None:
        import capo_cloudfront.types.logging_config

        out["logging"] = capo_cloudfront.types.logging_config.deserialize_xml(
            child_logging
        )
    child_price_class = el.find("PriceClass")
    if child_price_class is not None:
        import capo_cloudfront.types.price_class

        out["price_class"] = capo_cloudfront.types.price_class.deserialize_xml(
            child_price_class
        )
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    else:
        raise DeserializationError("DistributionConfig.enabled required")
    child_viewer_certificate = el.find("ViewerCertificate")
    if child_viewer_certificate is not None:
        import capo_cloudfront.types.viewer_certificate

        out["viewer_certificate"] = (
            capo_cloudfront.types.viewer_certificate.deserialize_xml(
                child_viewer_certificate
            )
        )
    child_restrictions = el.find("Restrictions")
    if child_restrictions is not None:
        import capo_cloudfront.types.restrictions

        out["restrictions"] = capo_cloudfront.types.restrictions.deserialize_xml(
            child_restrictions
        )
    child_web_acl_id = el.find("WebACLId")
    if child_web_acl_id is not None:
        out["web_acl_id"] = str(child_web_acl_id.text or "")
    child_http_version = el.find("HttpVersion")
    if child_http_version is not None:
        import capo_cloudfront.types.http_version

        out["http_version"] = capo_cloudfront.types.http_version.deserialize_xml(
            child_http_version
        )
    child_is_ipv6_enabled = el.find("IsIPV6Enabled")
    if child_is_ipv6_enabled is not None:
        out["is_ipv6_enabled"] = (child_is_ipv6_enabled.text or "").lower() == "true"
    child_continuous_deployment_policy_id = el.find("ContinuousDeploymentPolicyId")
    if child_continuous_deployment_policy_id is not None:
        out["continuous_deployment_policy_id"] = str(
            child_continuous_deployment_policy_id.text or ""
        )
    child_staging = el.find("Staging")
    if child_staging is not None:
        out["staging"] = (child_staging.text or "").lower() == "true"
    child_anycast_ip_list_id = el.find("AnycastIpListId")
    if child_anycast_ip_list_id is not None:
        out["anycast_ip_list_id"] = str(child_anycast_ip_list_id.text or "")
    child_tenant_config = el.find("TenantConfig")
    if child_tenant_config is not None:
        import capo_cloudfront.types.tenant_config

        out["tenant_config"] = capo_cloudfront.types.tenant_config.deserialize_xml(
            child_tenant_config
        )
    child_connection_mode = el.find("ConnectionMode")
    if child_connection_mode is not None:
        import capo_cloudfront.types.connection_mode

        out["connection_mode"] = capo_cloudfront.types.connection_mode.deserialize_xml(
            child_connection_mode
        )
    child_viewer_mtls_config = el.find("ViewerMtlsConfig")
    if child_viewer_mtls_config is not None:
        import capo_cloudfront.types.viewer_mtls_config

        out["viewer_mtls_config"] = (
            capo_cloudfront.types.viewer_mtls_config.deserialize_xml(
                child_viewer_mtls_config
            )
        )
    child_connection_function_association = el.find("ConnectionFunctionAssociation")
    if child_connection_function_association is not None:
        import capo_cloudfront.types.connection_function_association

        out["connection_function_association"] = (
            capo_cloudfront.types.connection_function_association.deserialize_xml(
                child_connection_function_association
            )
        )
    child_cache_tag_config = el.find("CacheTagConfig")
    if child_cache_tag_config is not None:
        import capo_cloudfront.types.cache_tag_config

        out["cache_tag_config"] = (
            capo_cloudfront.types.cache_tag_config.deserialize_xml(
                child_cache_tag_config
            )
        )
    return out
