"""Generated from Smithy shape ``com.amazonaws.lightsail#BucketCorsRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.bucket_cors_allowed_headers
    import capo_lightsail.types.bucket_cors_allowed_methods
    import capo_lightsail.types.bucket_cors_allowed_origins
    import capo_lightsail.types.bucket_cors_expose_headers
    import capo_lightsail.types.bucket_cors_rule_id
    import capo_lightsail.types.integer


class BucketCorsRule(TypedDict, closed=True):
    id: NotRequired["capo_lightsail.types.bucket_cors_rule_id.BucketCorsRuleId"]
    """<p>A unique identifier for the CORS rule. The ID value can be up to 255 characters long. The IDs help you find a rule in the configuration.</p>"""
    allowed_methods: (
        "capo_lightsail.types.bucket_cors_allowed_methods.BucketCorsAllowedMethods"
    )
    """<p>The HTTP methods that are allowed when accessing the bucket from the specified origin. Each CORS rule must identify at least one origin and one method.</p> <p>You can use the following HTTP methods:</p> <ul> <li> <p> <code>GET</code> - Retrieves data from the server, such as downloading files or viewing content.</p> </li> <li> <p> <code>PUT</code> - Uploads or replaces data on the server, such as uploading new files.</p> </li> <li> <p> <code>POST</code> - Sends data to the server for processing, such as submitting forms or creating new resources.</p> </li> <li> <p> <code>DELETE</code> - Removes data from the server, such as deleting files or resources.</p> </li> <li> <p> <code>HEAD</code> - Retrieves only the headers from the server without the actual content, useful for checking if a resource exists.</p> </li> </ul>"""
    allowed_origins: (
        "capo_lightsail.types.bucket_cors_allowed_origins.BucketCorsAllowedOrigins"
    )
    """<p>One or more origins you want customers to be able to access the bucket from. Each CORS rule must identify at least one origin and one method.</p>"""
    allowed_headers: NotRequired[
        "capo_lightsail.types.bucket_cors_allowed_headers.BucketCorsAllowedHeaders"
    ]
    """<p>Headers that are specified in the <code>Access-Control-Request-Headers</code> header. These headers are allowed in a preflight <code>OPTIONS</code> request. In response to any preflight <code>OPTIONS</code> request, Amazon S3 returns any requested headers that are allowed.</p>"""
    expose_headers: NotRequired[
        "capo_lightsail.types.bucket_cors_expose_headers.BucketCorsExposeHeaders"
    ]
    """<p>One or more headers in the response that you want customers to be able to access from their applications (for example, from a JavaScript <code>XMLHttpRequest</code> object).</p>"""
    max_age_seconds: NotRequired["capo_lightsail.types.integer.integer"]
    """<p>The time in seconds that your browser is to cache the preflight response for the specified resource. A CORS rule can have only one <code>maxAgeSeconds</code> element.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BucketCorsRule) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    import capo_lightsail.types.bucket_cors_allowed_methods

    out["allowedMethods"] = (
        capo_lightsail.types.bucket_cors_allowed_methods.serialize_aws_json_1_1(
            value["allowed_methods"]
        )
    )
    import capo_lightsail.types.bucket_cors_allowed_origins

    out["allowedOrigins"] = (
        capo_lightsail.types.bucket_cors_allowed_origins.serialize_aws_json_1_1(
            value["allowed_origins"]
        )
    )
    if "allowed_headers" in value:
        import capo_lightsail.types.bucket_cors_allowed_headers

        out["allowedHeaders"] = (
            capo_lightsail.types.bucket_cors_allowed_headers.serialize_aws_json_1_1(
                value["allowed_headers"]
            )
        )
    if "expose_headers" in value:
        import capo_lightsail.types.bucket_cors_expose_headers

        out["exposeHeaders"] = (
            capo_lightsail.types.bucket_cors_expose_headers.serialize_aws_json_1_1(
                value["expose_headers"]
            )
        )
    if "max_age_seconds" in value:
        out["maxAgeSeconds"] = value["max_age_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BucketCorsRule:
    out: BucketCorsRule = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("allowedMethods") is not None:
        import capo_lightsail.types.bucket_cors_allowed_methods

        out["allowed_methods"] = (
            capo_lightsail.types.bucket_cors_allowed_methods.deserialize_aws_json_1_1(
                data["allowedMethods"]
            )
        )
    else:
        out["allowed_methods"] = []
    if data.get("allowedOrigins") is not None:
        import capo_lightsail.types.bucket_cors_allowed_origins

        out["allowed_origins"] = (
            capo_lightsail.types.bucket_cors_allowed_origins.deserialize_aws_json_1_1(
                data["allowedOrigins"]
            )
        )
    else:
        out["allowed_origins"] = []
    if data.get("allowedHeaders") is not None:
        import capo_lightsail.types.bucket_cors_allowed_headers

        out["allowed_headers"] = (
            capo_lightsail.types.bucket_cors_allowed_headers.deserialize_aws_json_1_1(
                data["allowedHeaders"]
            )
        )
    if data.get("exposeHeaders") is not None:
        import capo_lightsail.types.bucket_cors_expose_headers

        out["expose_headers"] = (
            capo_lightsail.types.bucket_cors_expose_headers.deserialize_aws_json_1_1(
                data["exposeHeaders"]
            )
        )
    if data.get("maxAgeSeconds") is not None:
        out["max_age_seconds"] = data["maxAgeSeconds"]
    return out
