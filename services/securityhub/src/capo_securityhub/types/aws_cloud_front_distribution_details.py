"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCloudFrontDistributionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_cloud_front_distribution_cache_behaviors
    import capo_securityhub.types.aws_cloud_front_distribution_default_cache_behavior
    import capo_securityhub.types.aws_cloud_front_distribution_logging
    import capo_securityhub.types.aws_cloud_front_distribution_origin_groups
    import capo_securityhub.types.aws_cloud_front_distribution_origins
    import capo_securityhub.types.aws_cloud_front_distribution_viewer_certificate
    import capo_securityhub.types.non_empty_string


class AwsCloudFrontDistributionDetails(TypedDict, closed=True):
    cache_behaviors: NotRequired[
        "capo_securityhub.types.aws_cloud_front_distribution_cache_behaviors.AwsCloudFrontDistributionCacheBehaviors"
    ]
    """<p>Provides information about the cache configuration for the distribution.</p>"""
    default_cache_behavior: NotRequired[
        "capo_securityhub.types.aws_cloud_front_distribution_default_cache_behavior.AwsCloudFrontDistributionDefaultCacheBehavior"
    ]
    """<p>The default cache behavior for the configuration.</p>"""
    default_root_object: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The object that CloudFront sends in response to requests from the origin (for example, index.html) when a viewer requests the root URL for the distribution (http://www.example.com) instead of an object in your distribution (http://www.example.com/product-description.html). </p>"""
    domain_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The domain name corresponding to the distribution.</p>"""
    e_tag: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The entity tag is a hash of the object.</p>"""
    last_modified_time: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates when that the distribution was last modified.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    logging: NotRequired[
        "capo_securityhub.types.aws_cloud_front_distribution_logging.AwsCloudFrontDistributionLogging"
    ]
    """<p>A complex type that controls whether access logs are written for the distribution.</p>"""
    origins: NotRequired[
        "capo_securityhub.types.aws_cloud_front_distribution_origins.AwsCloudFrontDistributionOrigins"
    ]
    """<p>A complex type that contains information about origins for this distribution.</p>"""
    origin_groups: NotRequired[
        "capo_securityhub.types.aws_cloud_front_distribution_origin_groups.AwsCloudFrontDistributionOriginGroups"
    ]
    """<p>Provides information about the origin groups in the distribution.</p>"""
    viewer_certificate: NotRequired[
        "capo_securityhub.types.aws_cloud_front_distribution_viewer_certificate.AwsCloudFrontDistributionViewerCertificate"
    ]
    """<p>Provides information about the TLS/SSL configuration that the distribution uses to communicate with viewers.</p>"""
    status: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Indicates the current status of the distribution.</p>"""
    web_acl_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A unique identifier that specifies the WAF web ACL, if any, to associate with this distribution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCloudFrontDistributionDetails) -> dict:
    out: dict = {}
    if "cache_behaviors" in value:
        import capo_securityhub.types.aws_cloud_front_distribution_cache_behaviors

        out["CacheBehaviors"] = (
            capo_securityhub.types.aws_cloud_front_distribution_cache_behaviors.serialize_json(
                value["cache_behaviors"]
            )
        )
    if "default_cache_behavior" in value:
        import capo_securityhub.types.aws_cloud_front_distribution_default_cache_behavior

        out["DefaultCacheBehavior"] = (
            capo_securityhub.types.aws_cloud_front_distribution_default_cache_behavior.serialize_json(
                value["default_cache_behavior"]
            )
        )
    if "default_root_object" in value:
        out["DefaultRootObject"] = value["default_root_object"]
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "e_tag" in value:
        out["ETag"] = value["e_tag"]
    if "last_modified_time" in value:
        out["LastModifiedTime"] = value["last_modified_time"]
    if "logging" in value:
        import capo_securityhub.types.aws_cloud_front_distribution_logging

        out["Logging"] = (
            capo_securityhub.types.aws_cloud_front_distribution_logging.serialize_json(
                value["logging"]
            )
        )
    if "origins" in value:
        import capo_securityhub.types.aws_cloud_front_distribution_origins

        out["Origins"] = (
            capo_securityhub.types.aws_cloud_front_distribution_origins.serialize_json(
                value["origins"]
            )
        )
    if "origin_groups" in value:
        import capo_securityhub.types.aws_cloud_front_distribution_origin_groups

        out["OriginGroups"] = (
            capo_securityhub.types.aws_cloud_front_distribution_origin_groups.serialize_json(
                value["origin_groups"]
            )
        )
    if "viewer_certificate" in value:
        import capo_securityhub.types.aws_cloud_front_distribution_viewer_certificate

        out["ViewerCertificate"] = (
            capo_securityhub.types.aws_cloud_front_distribution_viewer_certificate.serialize_json(
                value["viewer_certificate"]
            )
        )
    if "status" in value:
        out["Status"] = value["status"]
    if "web_acl_id" in value:
        out["WebAclId"] = value["web_acl_id"]
    return out


def deserialize_json(data: dict) -> AwsCloudFrontDistributionDetails:
    out: AwsCloudFrontDistributionDetails = {}  # type: ignore[typeddict-item]
    if data.get("CacheBehaviors") is not None:
        import capo_securityhub.types.aws_cloud_front_distribution_cache_behaviors

        out["cache_behaviors"] = (
            capo_securityhub.types.aws_cloud_front_distribution_cache_behaviors.deserialize_json(
                data["CacheBehaviors"]
            )
        )
    if data.get("DefaultCacheBehavior") is not None:
        import capo_securityhub.types.aws_cloud_front_distribution_default_cache_behavior

        out["default_cache_behavior"] = (
            capo_securityhub.types.aws_cloud_front_distribution_default_cache_behavior.deserialize_json(
                data["DefaultCacheBehavior"]
            )
        )
    if data.get("DefaultRootObject") is not None:
        out["default_root_object"] = data["DefaultRootObject"]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    if data.get("ETag") is not None:
        out["e_tag"] = data["ETag"]
    if data.get("LastModifiedTime") is not None:
        out["last_modified_time"] = data["LastModifiedTime"]
    if data.get("Logging") is not None:
        import capo_securityhub.types.aws_cloud_front_distribution_logging

        out["logging"] = (
            capo_securityhub.types.aws_cloud_front_distribution_logging.deserialize_json(
                data["Logging"]
            )
        )
    if data.get("Origins") is not None:
        import capo_securityhub.types.aws_cloud_front_distribution_origins

        out["origins"] = (
            capo_securityhub.types.aws_cloud_front_distribution_origins.deserialize_json(
                data["Origins"]
            )
        )
    if data.get("OriginGroups") is not None:
        import capo_securityhub.types.aws_cloud_front_distribution_origin_groups

        out["origin_groups"] = (
            capo_securityhub.types.aws_cloud_front_distribution_origin_groups.deserialize_json(
                data["OriginGroups"]
            )
        )
    if data.get("ViewerCertificate") is not None:
        import capo_securityhub.types.aws_cloud_front_distribution_viewer_certificate

        out["viewer_certificate"] = (
            capo_securityhub.types.aws_cloud_front_distribution_viewer_certificate.deserialize_json(
                data["ViewerCertificate"]
            )
        )
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("WebAclId") is not None:
        out["web_acl_id"] = data["WebAclId"]
    return out
