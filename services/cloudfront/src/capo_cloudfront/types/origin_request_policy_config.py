"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginRequestPolicyConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.origin_request_policy_cookies_config
    import capo_cloudfront.types.origin_request_policy_headers_config
    import capo_cloudfront.types.origin_request_policy_query_strings_config
    import capo_cloudfront.types.string


class OriginRequestPolicyConfig(TypedDict, closed=True):
    comment: NotRequired["capo_cloudfront.types.string.string"]
    """<p>A comment to describe the origin request policy. The comment cannot be longer than 128 characters.</p>"""
    name: "capo_cloudfront.types.string.string"
    """<p>A unique name to identify the origin request policy.</p>"""
    headers_config: "capo_cloudfront.types.origin_request_policy_headers_config.OriginRequestPolicyHeadersConfig"
    """<p>The HTTP headers to include in origin requests. These can include headers from viewer requests and additional headers added by CloudFront.</p>"""
    cookies_config: "capo_cloudfront.types.origin_request_policy_cookies_config.OriginRequestPolicyCookiesConfig"
    """<p>The cookies from viewer requests to include in origin requests.</p>"""
    query_strings_config: "capo_cloudfront.types.origin_request_policy_query_strings_config.OriginRequestPolicyQueryStringsConfig"
    """<p>The URL query strings from viewer requests to include in origin requests.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: OriginRequestPolicyConfig, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "comment" in value:
        SubElement(el, "Comment").text = str(value["comment"])
    SubElement(el, "Name").text = str(value["name"])
    import capo_cloudfront.types.origin_request_policy_headers_config

    capo_cloudfront.types.origin_request_policy_headers_config.serialize_xml(
        value["headers_config"], el, "HeadersConfig"
    )
    import capo_cloudfront.types.origin_request_policy_cookies_config

    capo_cloudfront.types.origin_request_policy_cookies_config.serialize_xml(
        value["cookies_config"], el, "CookiesConfig"
    )
    import capo_cloudfront.types.origin_request_policy_query_strings_config

    capo_cloudfront.types.origin_request_policy_query_strings_config.serialize_xml(
        value["query_strings_config"], el, "QueryStringsConfig"
    )


def deserialize_xml(el: Element) -> OriginRequestPolicyConfig:
    out: OriginRequestPolicyConfig = {}  # type: ignore[typeddict-item]
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        out["name"] = ""
    child_headers_config = el.find("HeadersConfig")
    if child_headers_config is not None:
        import capo_cloudfront.types.origin_request_policy_headers_config

        out["headers_config"] = (
            capo_cloudfront.types.origin_request_policy_headers_config.deserialize_xml(
                child_headers_config
            )
        )
    else:
        raise DeserializationError("OriginRequestPolicyConfig.headers_config required")
    child_cookies_config = el.find("CookiesConfig")
    if child_cookies_config is not None:
        import capo_cloudfront.types.origin_request_policy_cookies_config

        out["cookies_config"] = (
            capo_cloudfront.types.origin_request_policy_cookies_config.deserialize_xml(
                child_cookies_config
            )
        )
    else:
        raise DeserializationError("OriginRequestPolicyConfig.cookies_config required")
    child_query_strings_config = el.find("QueryStringsConfig")
    if child_query_strings_config is not None:
        import capo_cloudfront.types.origin_request_policy_query_strings_config

        out["query_strings_config"] = (
            capo_cloudfront.types.origin_request_policy_query_strings_config.deserialize_xml(
                child_query_strings_config
            )
        )
    else:
        raise DeserializationError(
            "OriginRequestPolicyConfig.query_strings_config required"
        )
    return out
