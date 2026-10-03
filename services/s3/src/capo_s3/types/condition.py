"""Generated from Smithy shape ``com.amazonaws.s3#Condition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.http_error_code_returned_equals
    import capo_s3.types.key_prefix_equals


class Condition(TypedDict, closed=True):
    http_error_code_returned_equals: NotRequired[
        "capo_s3.types.http_error_code_returned_equals.HttpErrorCodeReturnedEquals"
    ]
    """<p>The HTTP error code when the redirect is applied. In the event of an error, if the error code equals this value, then the specified redirect is applied. Required when parent element <code>Condition</code> is specified and sibling <code>KeyPrefixEquals</code> is not specified. If both are specified, then both must be true for the redirect to be applied.</p>"""
    key_prefix_equals: NotRequired["capo_s3.types.key_prefix_equals.KeyPrefixEquals"]
    """<p>The object key name prefix when the redirect is applied. For example, to redirect requests for <code>ExamplePage.html</code>, the key prefix will be <code>ExamplePage.html</code>. To redirect request for all pages with the prefix <code>docs/</code>, the key prefix will be <code>/docs</code>, which identifies all objects in the <code>docs/</code> folder. Required when the parent element <code>Condition</code> is specified and sibling <code>HttpErrorCodeReturnedEquals</code> is not specified. If both conditions are specified, both must be true for the redirect to be applied.</p> <important> <p>Replacement must be made for object keys containing special characters (such as carriage returns) when using XML requests. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints"> XML related object key constraints</a>.</p> </important>"""


# --- restXml ser/de ---
def serialize_xml(value: Condition, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "http_error_code_returned_equals" in value:
        SubElement(el, "HttpErrorCodeReturnedEquals").text = str(
            value["http_error_code_returned_equals"]
        )
    if "key_prefix_equals" in value:
        SubElement(el, "KeyPrefixEquals").text = str(value["key_prefix_equals"])


def deserialize_xml(el: Element) -> Condition:
    out: Condition = {}  # type: ignore[typeddict-item]
    child_http_error_code_returned_equals = el.find("HttpErrorCodeReturnedEquals")
    if child_http_error_code_returned_equals is not None:
        out["http_error_code_returned_equals"] = str(
            child_http_error_code_returned_equals.text or ""
        )
    child_key_prefix_equals = el.find("KeyPrefixEquals")
    if child_key_prefix_equals is not None:
        out["key_prefix_equals"] = str(child_key_prefix_equals.text or "")
    return out
