"""Generated from Smithy shape ``com.amazonaws.cloudfront#DefaultCacheBehavior``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.allowed_methods
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.forwarded_values
    import capo_cloudfront.types.function_associations
    import capo_cloudfront.types.grpc_config
    import capo_cloudfront.types.lambda_function_associations
    import capo_cloudfront.types.long
    import capo_cloudfront.types.string
    import capo_cloudfront.types.trusted_key_groups
    import capo_cloudfront.types.trusted_signers
    import capo_cloudfront.types.viewer_protocol_policy


class DefaultCacheBehavior(TypedDict, closed=True):
    target_origin_id: "capo_cloudfront.types.string.string"
    """<p>The value of <code>ID</code> for the origin that you want CloudFront to route requests to when they use the default cache behavior.</p>"""
    trusted_signers: NotRequired["capo_cloudfront.types.trusted_signers.TrustedSigners"]
    """<important> <p>We recommend using <code>TrustedKeyGroups</code> instead of <code>TrustedSigners</code>.</p> </important> <note> <p>This field only supports standard distributions. You can't specify this field for multi-tenant distributions. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html#unsupported-saas">Unsupported features for SaaS Manager for Amazon CloudFront</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> </note> <p>A list of Amazon Web Services account IDs whose public keys CloudFront can use to validate signed URLs or signed cookies.</p> <p>When a cache behavior contains trusted signers, CloudFront requires signed URLs or signed cookies for all requests that match the cache behavior. The URLs or cookies must be signed with the private key of a CloudFront key pair in a trusted signer's Amazon Web Services account. The signed URL or cookie contains information about which public key CloudFront should use to verify the signature. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html">Serving private content</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    trusted_key_groups: NotRequired[
        "capo_cloudfront.types.trusted_key_groups.TrustedKeyGroups"
    ]
    """<p>A list of key groups that CloudFront can use to validate signed URLs or signed cookies.</p> <p>When a cache behavior contains trusted key groups, CloudFront requires signed URLs or signed cookies for all requests that match the cache behavior. The URLs or cookies must be signed with a private key whose corresponding public key is in the key group. The signed URL or cookie contains information about which public key CloudFront should use to verify the signature. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html">Serving private content</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    viewer_protocol_policy: (
        "capo_cloudfront.types.viewer_protocol_policy.ViewerProtocolPolicy"
    )
    """<p>The protocol that viewers can use to access the files in the origin specified by <code>TargetOriginId</code> when a request matches the path pattern in <code>PathPattern</code>. You can specify the following options:</p> <ul> <li> <p> <code>allow-all</code>: Viewers can use HTTP or HTTPS.</p> </li> <li> <p> <code>redirect-to-https</code>: If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.</p> </li> <li> <p> <code>https-only</code>: If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).</p> </li> </ul> <p>For more information about requiring the HTTPS protocol, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-viewers-to-cloudfront.html">Requiring HTTPS Between Viewers and CloudFront</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <note> <p>The only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objects' cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html">Managing Cache Expiration</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> </note>"""
    allowed_methods: NotRequired["capo_cloudfront.types.allowed_methods.AllowedMethods"]
    smooth_streaming: NotRequired["capo_cloudfront.types.boolean.boolean"]
    """<note> <p>This field only supports standard distributions. You can't specify this field for multi-tenant distributions. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html#unsupported-saas">Unsupported features for SaaS Manager for Amazon CloudFront</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> </note> <p>Indicates whether you want to distribute media files in the Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify <code>true</code>; if not, specify <code>false</code>. If you specify <code>true</code> for <code>SmoothStreaming</code>, you can still distribute other content using this cache behavior if the content matches the value of <code>PathPattern</code>.</p>"""
    compress: NotRequired["capo_cloudfront.types.boolean.boolean"]
    """<p>Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify <code>true</code>; if not, specify <code>false</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.html">Serving Compressed Files</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    lambda_function_associations: NotRequired[
        "capo_cloudfront.types.lambda_function_associations.LambdaFunctionAssociations"
    ]
    """<p>A complex type that contains zero or more Lambda@Edge function associations for a cache behavior.</p>"""
    function_associations: NotRequired[
        "capo_cloudfront.types.function_associations.FunctionAssociations"
    ]
    """<p>A list of CloudFront functions that are associated with this cache behavior. Your functions must be published to the <code>LIVE</code> stage to associate them with a cache behavior.</p>"""
    field_level_encryption_id: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The value of <code>ID</code> for the field-level encryption configuration that you want CloudFront to use for encrypting specific fields of data for the default cache behavior.</p>"""
    realtime_log_config_arn: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The Amazon Resource Name (ARN) of the real-time log configuration that is attached to this cache behavior. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html">Real-time logs</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    cache_policy_id: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The unique identifier of the cache policy that is attached to the default cache behavior. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy">Creating cache policies</a> or <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-cache-policies.html">Using the managed cache policies</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <p>A <code>DefaultCacheBehavior</code> must include either a <code>CachePolicyId</code> or <code>ForwardedValues</code>. We recommend that you use a <code>CachePolicyId</code>.</p>"""
    origin_request_policy_id: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The unique identifier of the origin request policy that is attached to the default cache behavior. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html#origin-request-create-origin-request-policy">Creating origin request policies</a> or <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-origin-request-policies.html">Using the managed origin request policies</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    response_headers_policy_id: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The identifier for a response headers policy.</p>"""
    grpc_config: NotRequired["capo_cloudfront.types.grpc_config.GrpcConfig"]
    """<p>The gRPC configuration for your cache behavior.</p>"""
    forwarded_values: NotRequired[
        "capo_cloudfront.types.forwarded_values.ForwardedValues"
    ]
    """<p>This field is deprecated. We recommend that you use a cache policy or an origin request policy instead of this field. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/working-with-policies.html">Working with policies</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <p>If you want to include values in the cache key, use a cache policy. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy">Creating cache policies</a> or <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-cache-policies.html">Using the managed cache policies</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <p>If you want to send values to the origin but not include them in the cache key, use an origin request policy. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html#origin-request-create-origin-request-policy">Creating origin request policies</a> or <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-origin-request-policies.html">Using the managed origin request policies</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <p>A <code>DefaultCacheBehavior</code> must include either a <code>CachePolicyId</code> or <code>ForwardedValues</code>. We recommend that you use a <code>CachePolicyId</code>.</p> <p>A complex type that specifies how CloudFront handles query strings, cookies, and HTTP headers.</p>"""
    min_ttl: NotRequired["capo_cloudfront.types.long.long"]
    """<note> <p>This field only supports standard distributions. You can't specify this field for multi-tenant distributions. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html#unsupported-saas">Unsupported features for SaaS Manager for Amazon CloudFront</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> </note> <p>This field is deprecated. We recommend that you use the <code>MinTTL</code> field in a cache policy instead of this field. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy">Creating cache policies</a> or <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-cache-policies.html">Using the managed cache policies</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <p>The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html">Managing How Long Content Stays in an Edge Cache (Expiration)</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <p>You must specify <code>0</code> for <code>MinTTL</code> if you configure CloudFront to forward all headers to your origin (under <code>Headers</code>, if you specify <code>1</code> for <code>Quantity</code> and <code>*</code> for <code>Name</code>).</p>"""
    default_ttl: NotRequired["capo_cloudfront.types.long.long"]
    """<note> <p>This field only supports standard distributions. You can't specify this field for multi-tenant distributions. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html#unsupported-saas">Unsupported features for SaaS Manager for Amazon CloudFront</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> </note> <p>This field is deprecated. We recommend that you use the <code>DefaultTTL</code> field in a cache policy instead of this field. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy">Creating cache policies</a> or <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-cache-policies.html">Using the managed cache policies</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <p>The default amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as <code>Cache-Control max-age</code>, <code>Cache-Control s-maxage</code>, and <code>Expires</code> to objects. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html">Managing How Long Content Stays in an Edge Cache (Expiration)</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    max_ttl: NotRequired["capo_cloudfront.types.long.long"]
    """<note> <p>This field only supports standard distributions. You can't specify this field for multi-tenant distributions. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html#unsupported-saas">Unsupported features for SaaS Manager for Amazon CloudFront</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> </note> <p>This field is deprecated. We recommend that you use the <code>MaxTTL</code> field in a cache policy instead of this field. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy">Creating cache policies</a> or <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-cache-policies.html">Using the managed cache policies</a> in the <i>Amazon CloudFront Developer Guide</i>.</p> <p>The maximum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as <code>Cache-Control max-age</code>, <code>Cache-Control s-maxage</code>, and <code>Expires</code> to objects. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html">Managing How Long Content Stays in an Edge Cache (Expiration)</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DefaultCacheBehavior, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "TargetOriginId").text = str(value["target_origin_id"])
    if "trusted_signers" in value:
        import capo_cloudfront.types.trusted_signers

        capo_cloudfront.types.trusted_signers.serialize_xml(
            value["trusted_signers"], el, "TrustedSigners"
        )
    if "trusted_key_groups" in value:
        import capo_cloudfront.types.trusted_key_groups

        capo_cloudfront.types.trusted_key_groups.serialize_xml(
            value["trusted_key_groups"], el, "TrustedKeyGroups"
        )
    import capo_cloudfront.types.viewer_protocol_policy

    capo_cloudfront.types.viewer_protocol_policy.serialize_xml(
        value["viewer_protocol_policy"], el, "ViewerProtocolPolicy"
    )
    if "allowed_methods" in value:
        import capo_cloudfront.types.allowed_methods

        capo_cloudfront.types.allowed_methods.serialize_xml(
            value["allowed_methods"], el, "AllowedMethods"
        )
    if "smooth_streaming" in value:
        SubElement(el, "SmoothStreaming").text = (
            "true" if value["smooth_streaming"] else "false"
        )
    if "compress" in value:
        SubElement(el, "Compress").text = "true" if value["compress"] else "false"
    if "lambda_function_associations" in value:
        import capo_cloudfront.types.lambda_function_associations

        capo_cloudfront.types.lambda_function_associations.serialize_xml(
            value["lambda_function_associations"], el, "LambdaFunctionAssociations"
        )
    if "function_associations" in value:
        import capo_cloudfront.types.function_associations

        capo_cloudfront.types.function_associations.serialize_xml(
            value["function_associations"], el, "FunctionAssociations"
        )
    if "field_level_encryption_id" in value:
        SubElement(el, "FieldLevelEncryptionId").text = str(
            value["field_level_encryption_id"]
        )
    if "realtime_log_config_arn" in value:
        SubElement(el, "RealtimeLogConfigArn").text = str(
            value["realtime_log_config_arn"]
        )
    if "cache_policy_id" in value:
        SubElement(el, "CachePolicyId").text = str(value["cache_policy_id"])
    if "origin_request_policy_id" in value:
        SubElement(el, "OriginRequestPolicyId").text = str(
            value["origin_request_policy_id"]
        )
    if "response_headers_policy_id" in value:
        SubElement(el, "ResponseHeadersPolicyId").text = str(
            value["response_headers_policy_id"]
        )
    if "grpc_config" in value:
        import capo_cloudfront.types.grpc_config

        capo_cloudfront.types.grpc_config.serialize_xml(
            value["grpc_config"], el, "GrpcConfig"
        )
    if "forwarded_values" in value:
        import capo_cloudfront.types.forwarded_values

        capo_cloudfront.types.forwarded_values.serialize_xml(
            value["forwarded_values"], el, "ForwardedValues"
        )
    if "min_ttl" in value:
        SubElement(el, "MinTTL").text = str(value["min_ttl"])
    if "default_ttl" in value:
        SubElement(el, "DefaultTTL").text = str(value["default_ttl"])
    if "max_ttl" in value:
        SubElement(el, "MaxTTL").text = str(value["max_ttl"])


def deserialize_xml(el: Element) -> DefaultCacheBehavior:
    out: DefaultCacheBehavior = {}  # type: ignore[typeddict-item]
    child_target_origin_id = el.find("TargetOriginId")
    if child_target_origin_id is not None:
        out["target_origin_id"] = str(child_target_origin_id.text or "")
    else:
        raise DeserializationError("DefaultCacheBehavior.target_origin_id required")
    child_trusted_signers = el.find("TrustedSigners")
    if child_trusted_signers is not None:
        import capo_cloudfront.types.trusted_signers

        out["trusted_signers"] = capo_cloudfront.types.trusted_signers.deserialize_xml(
            child_trusted_signers
        )
    child_trusted_key_groups = el.find("TrustedKeyGroups")
    if child_trusted_key_groups is not None:
        import capo_cloudfront.types.trusted_key_groups

        out["trusted_key_groups"] = (
            capo_cloudfront.types.trusted_key_groups.deserialize_xml(
                child_trusted_key_groups
            )
        )
    child_viewer_protocol_policy = el.find("ViewerProtocolPolicy")
    if child_viewer_protocol_policy is not None:
        import capo_cloudfront.types.viewer_protocol_policy

        out["viewer_protocol_policy"] = (
            capo_cloudfront.types.viewer_protocol_policy.deserialize_xml(
                child_viewer_protocol_policy
            )
        )
    else:
        raise DeserializationError(
            "DefaultCacheBehavior.viewer_protocol_policy required"
        )
    child_allowed_methods = el.find("AllowedMethods")
    if child_allowed_methods is not None:
        import capo_cloudfront.types.allowed_methods

        out["allowed_methods"] = capo_cloudfront.types.allowed_methods.deserialize_xml(
            child_allowed_methods
        )
    child_smooth_streaming = el.find("SmoothStreaming")
    if child_smooth_streaming is not None:
        out["smooth_streaming"] = (child_smooth_streaming.text or "").lower() == "true"
    child_compress = el.find("Compress")
    if child_compress is not None:
        out["compress"] = (child_compress.text or "").lower() == "true"
    child_lambda_function_associations = el.find("LambdaFunctionAssociations")
    if child_lambda_function_associations is not None:
        import capo_cloudfront.types.lambda_function_associations

        out["lambda_function_associations"] = (
            capo_cloudfront.types.lambda_function_associations.deserialize_xml(
                child_lambda_function_associations
            )
        )
    child_function_associations = el.find("FunctionAssociations")
    if child_function_associations is not None:
        import capo_cloudfront.types.function_associations

        out["function_associations"] = (
            capo_cloudfront.types.function_associations.deserialize_xml(
                child_function_associations
            )
        )
    child_field_level_encryption_id = el.find("FieldLevelEncryptionId")
    if child_field_level_encryption_id is not None:
        out["field_level_encryption_id"] = str(
            child_field_level_encryption_id.text or ""
        )
    child_realtime_log_config_arn = el.find("RealtimeLogConfigArn")
    if child_realtime_log_config_arn is not None:
        out["realtime_log_config_arn"] = str(child_realtime_log_config_arn.text or "")
    child_cache_policy_id = el.find("CachePolicyId")
    if child_cache_policy_id is not None:
        out["cache_policy_id"] = str(child_cache_policy_id.text or "")
    child_origin_request_policy_id = el.find("OriginRequestPolicyId")
    if child_origin_request_policy_id is not None:
        out["origin_request_policy_id"] = str(child_origin_request_policy_id.text or "")
    child_response_headers_policy_id = el.find("ResponseHeadersPolicyId")
    if child_response_headers_policy_id is not None:
        out["response_headers_policy_id"] = str(
            child_response_headers_policy_id.text or ""
        )
    child_grpc_config = el.find("GrpcConfig")
    if child_grpc_config is not None:
        import capo_cloudfront.types.grpc_config

        out["grpc_config"] = capo_cloudfront.types.grpc_config.deserialize_xml(
            child_grpc_config
        )
    child_forwarded_values = el.find("ForwardedValues")
    if child_forwarded_values is not None:
        import capo_cloudfront.types.forwarded_values

        out["forwarded_values"] = (
            capo_cloudfront.types.forwarded_values.deserialize_xml(
                child_forwarded_values
            )
        )
    child_min_ttl = el.find("MinTTL")
    if child_min_ttl is not None:
        out["min_ttl"] = int(child_min_ttl.text or "")
    child_default_ttl = el.find("DefaultTTL")
    if child_default_ttl is not None:
        out["default_ttl"] = int(child_default_ttl.text or "")
    child_max_ttl = el.find("MaxTTL")
    if child_max_ttl is not None:
        out["max_ttl"] = int(child_max_ttl.text or "")
    return out
