"""Generated from Smithy shape ``com.amazonaws.mediastore#CorsRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediastore.types.allowed_headers
    import capo_mediastore.types.allowed_methods
    import capo_mediastore.types.allowed_origins
    import capo_mediastore.types.expose_headers
    import capo_mediastore.types.max_age_seconds


class CorsRule(TypedDict, closed=True):
    allowed_origins: "capo_mediastore.types.allowed_origins.AllowedOrigins"
    """<p>One or more response headers that you want users to be able to access from their applications (for example, from a JavaScript <code>XMLHttpRequest</code> object).</p> <p>Each CORS rule must have at least one <code>AllowedOrigins</code> element. The string value can include only one wildcard character (*), for example, http://*.example.com. Additionally, you can specify only one wildcard character to allow cross-origin access for all origins.</p>"""
    allowed_methods: NotRequired["capo_mediastore.types.allowed_methods.AllowedMethods"]
    """<p>Identifies an HTTP method that the origin that is specified in the rule is allowed to execute.</p> <p>Each CORS rule must contain at least one <code>AllowedMethods</code> and one <code>AllowedOrigins</code> element.</p>"""
    allowed_headers: "capo_mediastore.types.allowed_headers.AllowedHeaders"
    """<p>Specifies which headers are allowed in a preflight <code>OPTIONS</code> request through the <code>Access-Control-Request-Headers</code> header. Each header name that is specified in <code>Access-Control-Request-Headers</code> must have a corresponding entry in the rule. Only the headers that were requested are sent back. </p> <p>This element can contain only one wildcard character (*).</p>"""
    max_age_seconds: "capo_mediastore.types.max_age_seconds.MaxAgeSeconds"
    """<p>The time in seconds that your browser caches the preflight response for the specified resource.</p> <p>A CORS rule can have only one <code>MaxAgeSeconds</code> element.</p>"""
    expose_headers: NotRequired["capo_mediastore.types.expose_headers.ExposeHeaders"]
    """<p>One or more headers in the response that you want users to be able to access from their applications (for example, from a JavaScript <code>XMLHttpRequest</code> object).</p> <p>This element is optional for each rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CorsRule) -> dict:
    out: dict = {}
    import capo_mediastore.types.allowed_origins

    out["AllowedOrigins"] = (
        capo_mediastore.types.allowed_origins.serialize_aws_json_1_1(
            value["allowed_origins"]
        )
    )
    if "allowed_methods" in value:
        import capo_mediastore.types.allowed_methods

        out["AllowedMethods"] = (
            capo_mediastore.types.allowed_methods.serialize_aws_json_1_1(
                value["allowed_methods"]
            )
        )
    import capo_mediastore.types.allowed_headers

    out["AllowedHeaders"] = (
        capo_mediastore.types.allowed_headers.serialize_aws_json_1_1(
            value["allowed_headers"]
        )
    )
    out["MaxAgeSeconds"] = value.get("max_age_seconds", 0)
    if "expose_headers" in value:
        import capo_mediastore.types.expose_headers

        out["ExposeHeaders"] = (
            capo_mediastore.types.expose_headers.serialize_aws_json_1_1(
                value["expose_headers"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CorsRule:
    out: CorsRule = {}  # type: ignore[typeddict-item]
    if data.get("AllowedOrigins") is not None:
        import capo_mediastore.types.allowed_origins

        out["allowed_origins"] = (
            capo_mediastore.types.allowed_origins.deserialize_aws_json_1_1(
                data["AllowedOrigins"]
            )
        )
    else:
        out["allowed_origins"] = []
    if data.get("AllowedMethods") is not None:
        import capo_mediastore.types.allowed_methods

        out["allowed_methods"] = (
            capo_mediastore.types.allowed_methods.deserialize_aws_json_1_1(
                data["AllowedMethods"]
            )
        )
    if data.get("AllowedHeaders") is not None:
        import capo_mediastore.types.allowed_headers

        out["allowed_headers"] = (
            capo_mediastore.types.allowed_headers.deserialize_aws_json_1_1(
                data["AllowedHeaders"]
            )
        )
    else:
        out["allowed_headers"] = []
    if data.get("MaxAgeSeconds") is not None:
        out["max_age_seconds"] = data["MaxAgeSeconds"]
    else:
        out["max_age_seconds"] = 0
    if data.get("ExposeHeaders") is not None:
        import capo_mediastore.types.expose_headers

        out["expose_headers"] = (
            capo_mediastore.types.expose_headers.deserialize_aws_json_1_1(
                data["ExposeHeaders"]
            )
        )
    return out
