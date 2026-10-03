"""Generated from Smithy shape ``com.amazonaws.lightsail#UpdateDistributionRequest``."""

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
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.string
    import capo_lightsail.types.viewer_minimum_tls_protocol_version_enum


class UpdateDistributionRequest(TypedDict, closed=True):
    distribution_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the distribution to update.</p> <p>Use the <code>GetDistributions</code> action to get a list of distribution names that you can specify.</p>"""
    origin: NotRequired["capo_lightsail.types.input_origin.InputOrigin"]
    """<p>An object that describes the origin resource for the distribution, such as a Lightsail instance, bucket, or load balancer.</p> <p>The distribution pulls, caches, and serves content from the origin.</p>"""
    default_cache_behavior: NotRequired[
        "capo_lightsail.types.cache_behavior.CacheBehavior"
    ]
    """<p>An object that describes the default cache behavior for the distribution.</p>"""
    cache_behavior_settings: NotRequired[
        "capo_lightsail.types.cache_settings.CacheSettings"
    ]
    """<p>An object that describes the cache behavior settings for the distribution.</p> <note> <p>The <code>cacheBehaviorSettings</code> specified in your <code>UpdateDistributionRequest</code> will replace your distribution's existing settings.</p> </note>"""
    cache_behaviors: NotRequired[
        "capo_lightsail.types.cache_behavior_list.CacheBehaviorList"
    ]
    """<p>An array of objects that describe the per-path cache behavior for the distribution.</p>"""
    is_enabled: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>Indicates whether to enable the distribution.</p>"""
    viewer_minimum_tls_protocol_version: NotRequired[
        "capo_lightsail.types.viewer_minimum_tls_protocol_version_enum.ViewerMinimumTlsProtocolVersionEnum"
    ]
    """<p>Use this parameter to update the minimum TLS protocol version for the SSL/TLS certificate that's attached to the distribution.</p>"""
    certificate_name: NotRequired["capo_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the SSL/TLS certificate that you want to attach to the distribution.</p> <p>Only certificates with a status of <code>ISSUED</code> can be attached to a distribution.</p> <p>Use the <a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetCertificates.html">GetCertificates</a> action to get a list of certificate names that you can specify.</p>"""
    use_default_certificate: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>Indicates whether the default SSL/TLS certificate is attached to the distribution. The default value is <code>true</code>. When <code>true</code>, the distribution uses the default domain name such as <code>d111111abcdef8.cloudfront.net</code>.</p> <p> Set this value to <code>false</code> to attach a new certificate to the distribution.</p>"""
    enable_private_origin_access: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>Specifies whether to enable private origin access for the distribution. With private origin access, the distribution can serve objects that aren't publicly accessible from a Lightsail bucket.</p> <p>Lightsail grants the distribution permission to read the bucket's objects. Enabling private origin access doesn't change the bucket's access settings, and you can still retrieve publicly accessible objects directly from the bucket's endpoint.</p> <note> <p>When you include this parameter, you must also include the <code>origin</code> parameter with the resource name, even if the origin is not changing.</p> <p>You can enable private origin access only when the distribution's origin is a Lightsail bucket. If the origin is another resource type, the request fails.</p> </note>"""
    default_root_object: NotRequired["capo_lightsail.types.string.string"]
    """<p>The object (for example, <code>index.html</code>) that the distribution returns when a viewer requests the root URL of the distribution (<code>/</code>) instead of a specific object. The object that you specify must be available from the origin.</p>"""
    custom_error_responses: NotRequired[
        "capo_lightsail.types.distribution_custom_error_response_list.DistributionCustomErrorResponseList"
    ]
    """<p>An array of objects that describe the custom error responses for the distribution. With a custom error response, you can specify the page to return when the origin responds with a given HTTP error code. You can also specify the HTTP status code to send to the viewer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDistributionRequest) -> dict:
    out: dict = {}
    out["distributionName"] = value["distribution_name"]
    if "origin" in value:
        import capo_lightsail.types.input_origin

        out["origin"] = capo_lightsail.types.input_origin.serialize_aws_json_1_1(
            value["origin"]
        )
    if "default_cache_behavior" in value:
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
    if "is_enabled" in value:
        out["isEnabled"] = value["is_enabled"]
    if "viewer_minimum_tls_protocol_version" in value:
        import capo_lightsail.types.viewer_minimum_tls_protocol_version_enum

        out["viewerMinimumTlsProtocolVersion"] = (
            capo_lightsail.types.viewer_minimum_tls_protocol_version_enum.serialize_aws_json_1_1(
                value["viewer_minimum_tls_protocol_version"]
            )
        )
    if "certificate_name" in value:
        out["certificateName"] = value["certificate_name"]
    if "use_default_certificate" in value:
        out["useDefaultCertificate"] = value["use_default_certificate"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDistributionRequest:
    out: UpdateDistributionRequest = {}  # type: ignore[typeddict-item]
    if data.get("distributionName") is not None:
        out["distribution_name"] = data["distributionName"]
    else:
        raise DeserializationError(
            "UpdateDistributionRequest.distribution_name required"
        )
    if data.get("origin") is not None:
        import capo_lightsail.types.input_origin

        out["origin"] = capo_lightsail.types.input_origin.deserialize_aws_json_1_1(
            data["origin"]
        )
    if data.get("defaultCacheBehavior") is not None:
        import capo_lightsail.types.cache_behavior

        out["default_cache_behavior"] = (
            capo_lightsail.types.cache_behavior.deserialize_aws_json_1_1(
                data["defaultCacheBehavior"]
            )
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
    if data.get("isEnabled") is not None:
        out["is_enabled"] = data["isEnabled"]
    if data.get("viewerMinimumTlsProtocolVersion") is not None:
        import capo_lightsail.types.viewer_minimum_tls_protocol_version_enum

        out["viewer_minimum_tls_protocol_version"] = (
            capo_lightsail.types.viewer_minimum_tls_protocol_version_enum.deserialize_aws_json_1_1(
                data["viewerMinimumTlsProtocolVersion"]
            )
        )
    if data.get("certificateName") is not None:
        out["certificate_name"] = data["certificateName"]
    if data.get("useDefaultCertificate") is not None:
        out["use_default_certificate"] = data["useDefaultCertificate"]
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
    return out
