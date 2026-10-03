"""Generated from Smithy shape ``com.amazonaws.s3#Redirect``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.host_name
    import capo_s3.types.http_redirect_code
    import capo_s3.types.protocol
    import capo_s3.types.replace_key_prefix_with
    import capo_s3.types.replace_key_with


class Redirect(TypedDict, closed=True):
    host_name: NotRequired["capo_s3.types.host_name.HostName"]
    """<p>The host name to use in the redirect request.</p>"""
    http_redirect_code: NotRequired["capo_s3.types.http_redirect_code.HttpRedirectCode"]
    """<p>The HTTP redirect code to use on the response. Not required if one of the siblings is present.</p>"""
    protocol: NotRequired["capo_s3.types.protocol.Protocol"]
    """<p>Protocol to use when redirecting requests. The default is the protocol that is used in the original request.</p>"""
    replace_key_prefix_with: NotRequired[
        "capo_s3.types.replace_key_prefix_with.ReplaceKeyPrefixWith"
    ]
    """<p>The object key prefix to use in the redirect request. For example, to redirect requests for all pages with prefix <code>docs/</code> (objects in the <code>docs/</code> folder) to <code>documents/</code>, you can set a condition block with <code>KeyPrefixEquals</code> set to <code>docs/</code> and in the Redirect set <code>ReplaceKeyPrefixWith</code> to <code>/documents</code>. Not required if one of the siblings is present. Can be present only if <code>ReplaceKeyWith</code> is not provided.</p> <important> <p>Replacement must be made for object keys containing special characters (such as carriage returns) when using XML requests. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints"> XML related object key constraints</a>.</p> </important>"""
    replace_key_with: NotRequired["capo_s3.types.replace_key_with.ReplaceKeyWith"]
    """<p>The specific object key to use in the redirect request. For example, redirect request to <code>error.html</code>. Not required if one of the siblings is present. Can be present only if <code>ReplaceKeyPrefixWith</code> is not provided.</p> <important> <p>Replacement must be made for object keys containing special characters (such as carriage returns) when using XML requests. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints"> XML related object key constraints</a>.</p> </important>"""


# --- restXml ser/de ---
def serialize_xml(value: Redirect, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "host_name" in value:
        SubElement(el, "HostName").text = str(value["host_name"])
    if "http_redirect_code" in value:
        SubElement(el, "HttpRedirectCode").text = str(value["http_redirect_code"])
    if "protocol" in value:
        import capo_s3.types.protocol

        capo_s3.types.protocol.serialize_xml(value["protocol"], el, "Protocol")
    if "replace_key_prefix_with" in value:
        SubElement(el, "ReplaceKeyPrefixWith").text = str(
            value["replace_key_prefix_with"]
        )
    if "replace_key_with" in value:
        SubElement(el, "ReplaceKeyWith").text = str(value["replace_key_with"])


def deserialize_xml(el: Element) -> Redirect:
    out: Redirect = {}  # type: ignore[typeddict-item]
    child_host_name = el.find("HostName")
    if child_host_name is not None:
        out["host_name"] = str(child_host_name.text or "")
    child_http_redirect_code = el.find("HttpRedirectCode")
    if child_http_redirect_code is not None:
        out["http_redirect_code"] = str(child_http_redirect_code.text or "")
    child_protocol = el.find("Protocol")
    if child_protocol is not None:
        import capo_s3.types.protocol

        out["protocol"] = capo_s3.types.protocol.deserialize_xml(child_protocol)
    child_replace_key_prefix_with = el.find("ReplaceKeyPrefixWith")
    if child_replace_key_prefix_with is not None:
        out["replace_key_prefix_with"] = str(child_replace_key_prefix_with.text or "")
    child_replace_key_with = el.find("ReplaceKeyWith")
    if child_replace_key_with is not None:
        out["replace_key_with"] = str(child_replace_key_with.text or "")
    return out
