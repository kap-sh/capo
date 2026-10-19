"""Generated from Smithy shape ``com.amazonaws.s3#CORSRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.allowed_headers
    import capo_s3.types.allowed_methods
    import capo_s3.types.allowed_origins
    import capo_s3.types.expose_headers
    import capo_s3.types.id
    import capo_s3.types.max_age_seconds


class CORSRule(TypedDict, closed=True):
    id: NotRequired["capo_s3.types.id.ID"]
    """<p>Unique identifier for the rule. The value cannot be longer than 255 characters.</p>"""
    allowed_headers: NotRequired["capo_s3.types.allowed_headers.AllowedHeaders"]
    """<p>Headers that are specified in the <code>Access-Control-Request-Headers</code> header. These headers are allowed in a preflight OPTIONS request. In response to any preflight OPTIONS request, Amazon S3 returns any requested headers that are allowed.</p>"""
    allowed_methods: "capo_s3.types.allowed_methods.AllowedMethods"
    """<p>An HTTP method that you allow the origin to execute. Valid values are <code>GET</code>, <code>PUT</code>, <code>HEAD</code>, <code>POST</code>, and <code>DELETE</code>.</p>"""
    allowed_origins: "capo_s3.types.allowed_origins.AllowedOrigins"
    """<p>One or more origins you want customers to be able to access the bucket from.</p>"""
    expose_headers: NotRequired["capo_s3.types.expose_headers.ExposeHeaders"]
    """<p>One or more headers in the response that you want customers to be able to access from their applications (for example, from a JavaScript <code>XMLHttpRequest</code> object).</p>"""
    max_age_seconds: NotRequired["capo_s3.types.max_age_seconds.MaxAgeSeconds"]
    """<p>The time in seconds that your browser is to cache the preflight response for the specified resource.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CORSRule, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "id" in value:
        SubElement(el, "ID").text = str(value["id"])
    if "allowed_headers" in value:
        import capo_s3.types.allowed_headers

        capo_s3.types.allowed_headers.serialize_xml_flat(
            value["allowed_headers"], el, "AllowedHeader"
        )
    import capo_s3.types.allowed_methods

    capo_s3.types.allowed_methods.serialize_xml_flat(
        value["allowed_methods"], el, "AllowedMethod"
    )
    import capo_s3.types.allowed_origins

    capo_s3.types.allowed_origins.serialize_xml_flat(
        value["allowed_origins"], el, "AllowedOrigin"
    )
    if "expose_headers" in value:
        import capo_s3.types.expose_headers

        capo_s3.types.expose_headers.serialize_xml_flat(
            value["expose_headers"], el, "ExposeHeader"
        )
    if "max_age_seconds" in value:
        SubElement(el, "MaxAgeSeconds").text = str(value["max_age_seconds"])


def deserialize_xml(el: Element) -> CORSRule:
    out: CORSRule = {}  # type: ignore[typeddict-item]
    child_id = el.find("ID")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    if el.find("AllowedHeader") is not None:
        import capo_s3.types.allowed_headers

        out["allowed_headers"] = capo_s3.types.allowed_headers.deserialize_xml_flat(
            el, "AllowedHeader"
        )
    if el.find("AllowedMethod") is not None:
        import capo_s3.types.allowed_methods

        out["allowed_methods"] = capo_s3.types.allowed_methods.deserialize_xml_flat(
            el, "AllowedMethod"
        )
    else:
        out["allowed_methods"] = []
    if el.find("AllowedOrigin") is not None:
        import capo_s3.types.allowed_origins

        out["allowed_origins"] = capo_s3.types.allowed_origins.deserialize_xml_flat(
            el, "AllowedOrigin"
        )
    else:
        out["allowed_origins"] = []
    if el.find("ExposeHeader") is not None:
        import capo_s3.types.expose_headers

        out["expose_headers"] = capo_s3.types.expose_headers.deserialize_xml_flat(
            el, "ExposeHeader"
        )
    child_max_age_seconds = el.find("MaxAgeSeconds")
    if child_max_age_seconds is not None:
        out["max_age_seconds"] = int(child_max_age_seconds.text or "")
    return out
