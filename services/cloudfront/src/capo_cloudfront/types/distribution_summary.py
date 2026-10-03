"""Generated from Smithy shape ``com.amazonaws.cloudfront#DistributionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.alias_icp_recordals
    import capo_cloudfront.types.aliases
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.cache_behaviors
    import capo_cloudfront.types.connection_function_association
    import capo_cloudfront.types.connection_mode
    import capo_cloudfront.types.custom_error_responses
    import capo_cloudfront.types.default_cache_behavior
    import capo_cloudfront.types.http_version
    import capo_cloudfront.types.origin_groups
    import capo_cloudfront.types.origins
    import capo_cloudfront.types.price_class
    import capo_cloudfront.types.restrictions
    import capo_cloudfront.types.sensitive_string_type
    import capo_cloudfront.types.string
    import capo_cloudfront.types.timestamp
    import capo_cloudfront.types.viewer_certificate
    import capo_cloudfront.types.viewer_mtls_config


class DistributionSummary(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The identifier for the distribution. For example: <code>EDFDVBD632BHDS5</code>.</p>"""
    arn: "capo_cloudfront.types.string.string"
    """<p>The ARN (Amazon Resource Name) for the distribution. For example: <code>arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5</code>, where <code>123456789012</code> is your Amazon Web Services account ID.</p>"""
    e_tag: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The current version of the distribution.</p>"""
    status: "capo_cloudfront.types.string.string"
    """<p>The current status of the distribution. When the status is <code>Deployed</code>, the distribution's information is propagated to all CloudFront edge locations.</p>"""
    last_modified_time: "capo_cloudfront.types.timestamp.timestamp"
    """<p>The date and time the distribution was last modified.</p>"""
    domain_name: "capo_cloudfront.types.string.string"
    """<p>The domain name that corresponds to the distribution, for example, <code>d111111abcdef8.cloudfront.net</code>.</p>"""
    aliases: "capo_cloudfront.types.aliases.Aliases"
    """<p>A complex type that contains information about CNAMEs (alternate domain names), if any, for this distribution.</p>"""
    origins: "capo_cloudfront.types.origins.Origins"
    """<p>A complex type that contains information about origins for this distribution.</p>"""
    origin_groups: NotRequired["capo_cloudfront.types.origin_groups.OriginGroups"]
    """<p>A complex type that contains information about origin groups for this distribution.</p>"""
    default_cache_behavior: (
        "capo_cloudfront.types.default_cache_behavior.DefaultCacheBehavior"
    )
    """<p>A complex type that describes the default cache behavior if you don't specify a <code>CacheBehavior</code> element or if files don't match any of the values of <code>PathPattern</code> in <code>CacheBehavior</code> elements. You must create exactly one default cache behavior.</p>"""
    cache_behaviors: "capo_cloudfront.types.cache_behaviors.CacheBehaviors"
    """<p>A complex type that contains zero or more <code>CacheBehavior</code> elements.</p>"""
    custom_error_responses: (
        "capo_cloudfront.types.custom_error_responses.CustomErrorResponses"
    )
    """<p>A complex type that contains zero or more <code>CustomErrorResponses</code> elements.</p>"""
    comment: "capo_cloudfront.types.sensitive_string_type.sensitiveStringType"
    """<p>The comment originally specified when this distribution was created.</p>"""
    price_class: "capo_cloudfront.types.price_class.PriceClass"
    """<note> <p>This field only supports standard distributions. You can't specify this field for multi-tenant distributions. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html#unsupported-saas">Unsupported features for SaaS Manager for Amazon CloudFront</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> </note> <p>A complex type that contains information about price class for this streaming distribution.</p>"""
    enabled: "capo_cloudfront.types.boolean.boolean"
    """<p>Whether the distribution is enabled to accept user requests for content.</p>"""
    viewer_certificate: "capo_cloudfront.types.viewer_certificate.ViewerCertificate"
    """<p>A complex type that determines the distribution's SSL/TLS configuration for communicating with viewers.</p>"""
    restrictions: "capo_cloudfront.types.restrictions.Restrictions"
    """<p>A complex type that identifies ways in which you want to restrict distribution of your content.</p>"""
    web_acl_id: "capo_cloudfront.types.string.string"
    """<p>The Web ACL Id (if any) associated with the distribution.</p>"""
    http_version: "capo_cloudfront.types.http_version.HttpVersion"
    """<p>Specify the maximum HTTP version that you want viewers to use to communicate with CloudFront. The default value for new web distributions is <code>http2</code>. Viewers that don't support <code>HTTP/2</code> will automatically use an earlier version.</p>"""
    is_ipv6_enabled: "capo_cloudfront.types.boolean.boolean"
    """<p>Whether CloudFront responds to IPv6 DNS requests with an IPv6 address for your distribution.</p>"""
    alias_icp_recordals: NotRequired[
        "capo_cloudfront.types.alias_icp_recordals.AliasICPRecordals"
    ]
    """<p>Amazon Web Services services in China customers must file for an Internet Content Provider (ICP) recordal if they want to serve content publicly on an alternate domain name, also known as a CNAME, that they've added to CloudFront. AliasICPRecordal provides the ICP recordal status for CNAMEs associated with distributions.</p> <p>For more information about ICP recordals, see <a href="https://docs.amazonaws.cn/en_us/aws/latest/userguide/accounts-and-credentials.html"> Signup, Accounts, and Credentials</a> in <i>Getting Started with Amazon Web Services services in China</i>.</p>"""
    staging: "capo_cloudfront.types.boolean.boolean"
    """<p>A Boolean that indicates whether this is a staging distribution. When this value is <code>true</code>, this is a staging distribution. When this value is <code>false</code>, this is not a staging distribution.</p>"""
    connection_mode: NotRequired["capo_cloudfront.types.connection_mode.ConnectionMode"]
    """<p>This field specifies whether the connection mode is through a standard distribution (direct) or a multi-tenant distribution with distribution tenants (tenant-only).</p>"""
    anycast_ip_list_id: NotRequired["capo_cloudfront.types.string.string"]
    """<p>ID of the Anycast static IP list that is associated with the distribution.</p>"""
    viewer_mtls_config: NotRequired[
        "capo_cloudfront.types.viewer_mtls_config.ViewerMtlsConfig"
    ]
    """<p>The distribution's viewer mTLS configuration.</p>"""
    connection_function_association: NotRequired[
        "capo_cloudfront.types.connection_function_association.ConnectionFunctionAssociation"
    ]
    """<p>The distribution's connection function association.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DistributionSummary, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    SubElement(el, "ARN").text = str(value["arn"])
    if "e_tag" in value:
        SubElement(el, "ETag").text = str(value["e_tag"])
    SubElement(el, "Status").text = str(value["status"])
    import capo_cloudfront.types.timestamp

    capo_cloudfront.types.timestamp.serialize_xml(
        value["last_modified_time"], el, "LastModifiedTime"
    )
    SubElement(el, "DomainName").text = str(value["domain_name"])
    import capo_cloudfront.types.aliases

    capo_cloudfront.types.aliases.serialize_xml(value["aliases"], el, "Aliases")
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
    import capo_cloudfront.types.cache_behaviors

    capo_cloudfront.types.cache_behaviors.serialize_xml(
        value["cache_behaviors"], el, "CacheBehaviors"
    )
    import capo_cloudfront.types.custom_error_responses

    capo_cloudfront.types.custom_error_responses.serialize_xml(
        value["custom_error_responses"], el, "CustomErrorResponses"
    )
    SubElement(el, "Comment").text = str(value["comment"])
    import capo_cloudfront.types.price_class

    capo_cloudfront.types.price_class.serialize_xml(
        value["price_class"], el, "PriceClass"
    )
    SubElement(el, "Enabled").text = "true" if value["enabled"] else "false"
    import capo_cloudfront.types.viewer_certificate

    capo_cloudfront.types.viewer_certificate.serialize_xml(
        value["viewer_certificate"], el, "ViewerCertificate"
    )
    import capo_cloudfront.types.restrictions

    capo_cloudfront.types.restrictions.serialize_xml(
        value["restrictions"], el, "Restrictions"
    )
    SubElement(el, "WebACLId").text = str(value["web_acl_id"])
    import capo_cloudfront.types.http_version

    capo_cloudfront.types.http_version.serialize_xml(
        value["http_version"], el, "HttpVersion"
    )
    SubElement(el, "IsIPV6Enabled").text = (
        "true" if value["is_ipv6_enabled"] else "false"
    )
    if "alias_icp_recordals" in value:
        import capo_cloudfront.types.alias_icp_recordals

        capo_cloudfront.types.alias_icp_recordals.serialize_xml(
            value["alias_icp_recordals"], el, "AliasICPRecordals"
        )
    SubElement(el, "Staging").text = "true" if value["staging"] else "false"
    if "connection_mode" in value:
        import capo_cloudfront.types.connection_mode

        capo_cloudfront.types.connection_mode.serialize_xml(
            value["connection_mode"], el, "ConnectionMode"
        )
    if "anycast_ip_list_id" in value:
        SubElement(el, "AnycastIpListId").text = str(value["anycast_ip_list_id"])
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


def deserialize_xml(el: Element) -> DistributionSummary:
    out: DistributionSummary = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        raise DeserializationError("DistributionSummary.id required")
    child_arn = el.find("ARN")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    else:
        raise DeserializationError("DistributionSummary.arn required")
    child_e_tag = el.find("ETag")
    if child_e_tag is not None:
        out["e_tag"] = str(child_e_tag.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    else:
        raise DeserializationError("DistributionSummary.status required")
    child_last_modified_time = el.find("LastModifiedTime")
    if child_last_modified_time is not None:
        import capo_cloudfront.types.timestamp

        out["last_modified_time"] = capo_cloudfront.types.timestamp.deserialize_xml(
            child_last_modified_time
        )
    else:
        raise DeserializationError("DistributionSummary.last_modified_time required")
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        raise DeserializationError("DistributionSummary.domain_name required")
    child_aliases = el.find("Aliases")
    if child_aliases is not None:
        import capo_cloudfront.types.aliases

        out["aliases"] = capo_cloudfront.types.aliases.deserialize_xml(child_aliases)
    else:
        raise DeserializationError("DistributionSummary.aliases required")
    child_origins = el.find("Origins")
    if child_origins is not None:
        import capo_cloudfront.types.origins

        out["origins"] = capo_cloudfront.types.origins.deserialize_xml(child_origins)
    else:
        raise DeserializationError("DistributionSummary.origins required")
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
        raise DeserializationError(
            "DistributionSummary.default_cache_behavior required"
        )
    child_cache_behaviors = el.find("CacheBehaviors")
    if child_cache_behaviors is not None:
        import capo_cloudfront.types.cache_behaviors

        out["cache_behaviors"] = capo_cloudfront.types.cache_behaviors.deserialize_xml(
            child_cache_behaviors
        )
    else:
        raise DeserializationError("DistributionSummary.cache_behaviors required")
    child_custom_error_responses = el.find("CustomErrorResponses")
    if child_custom_error_responses is not None:
        import capo_cloudfront.types.custom_error_responses

        out["custom_error_responses"] = (
            capo_cloudfront.types.custom_error_responses.deserialize_xml(
                child_custom_error_responses
            )
        )
    else:
        raise DeserializationError(
            "DistributionSummary.custom_error_responses required"
        )
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    else:
        raise DeserializationError("DistributionSummary.comment required")
    child_price_class = el.find("PriceClass")
    if child_price_class is not None:
        import capo_cloudfront.types.price_class

        out["price_class"] = capo_cloudfront.types.price_class.deserialize_xml(
            child_price_class
        )
    else:
        raise DeserializationError("DistributionSummary.price_class required")
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    else:
        raise DeserializationError("DistributionSummary.enabled required")
    child_viewer_certificate = el.find("ViewerCertificate")
    if child_viewer_certificate is not None:
        import capo_cloudfront.types.viewer_certificate

        out["viewer_certificate"] = (
            capo_cloudfront.types.viewer_certificate.deserialize_xml(
                child_viewer_certificate
            )
        )
    else:
        raise DeserializationError("DistributionSummary.viewer_certificate required")
    child_restrictions = el.find("Restrictions")
    if child_restrictions is not None:
        import capo_cloudfront.types.restrictions

        out["restrictions"] = capo_cloudfront.types.restrictions.deserialize_xml(
            child_restrictions
        )
    else:
        raise DeserializationError("DistributionSummary.restrictions required")
    child_web_acl_id = el.find("WebACLId")
    if child_web_acl_id is not None:
        out["web_acl_id"] = str(child_web_acl_id.text or "")
    else:
        raise DeserializationError("DistributionSummary.web_acl_id required")
    child_http_version = el.find("HttpVersion")
    if child_http_version is not None:
        import capo_cloudfront.types.http_version

        out["http_version"] = capo_cloudfront.types.http_version.deserialize_xml(
            child_http_version
        )
    else:
        raise DeserializationError("DistributionSummary.http_version required")
    child_is_ipv6_enabled = el.find("IsIPV6Enabled")
    if child_is_ipv6_enabled is not None:
        out["is_ipv6_enabled"] = (child_is_ipv6_enabled.text or "").lower() == "true"
    else:
        raise DeserializationError("DistributionSummary.is_ipv6_enabled required")
    child_alias_icp_recordals = el.find("AliasICPRecordals")
    if child_alias_icp_recordals is not None:
        import capo_cloudfront.types.alias_icp_recordals

        out["alias_icp_recordals"] = (
            capo_cloudfront.types.alias_icp_recordals.deserialize_xml(
                child_alias_icp_recordals
            )
        )
    child_staging = el.find("Staging")
    if child_staging is not None:
        out["staging"] = (child_staging.text or "").lower() == "true"
    else:
        raise DeserializationError("DistributionSummary.staging required")
    child_connection_mode = el.find("ConnectionMode")
    if child_connection_mode is not None:
        import capo_cloudfront.types.connection_mode

        out["connection_mode"] = capo_cloudfront.types.connection_mode.deserialize_xml(
            child_connection_mode
        )
    child_anycast_ip_list_id = el.find("AnycastIpListId")
    if child_anycast_ip_list_id is not None:
        out["anycast_ip_list_id"] = str(child_anycast_ip_list_id.text or "")
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
    return out
