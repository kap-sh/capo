"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetConnectionFunctionResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.function_blob
    import capo_cloudfront.types.string


class GetConnectionFunctionResult(TypedDict, closed=True):
    connection_function_code: NotRequired[
        "capo_cloudfront.types.function_blob.FunctionBlob"
    ]
    """<p>The connection function's code.</p>"""
    e_tag: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The version identifier for the current version of the connection function.</p>"""
    content_type: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The connection function's content type.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetConnectionFunctionResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "connection_function_code" in value:
        import capo_cloudfront.types.function_blob

        capo_cloudfront.types.function_blob.serialize_xml(
            value["connection_function_code"], el, "ConnectionFunctionCode"
        )


def deserialize_xml(el: Element) -> GetConnectionFunctionResult:
    out: GetConnectionFunctionResult = {}  # type: ignore[typeddict-item]
    child_connection_function_code = el.find("ConnectionFunctionCode")
    if child_connection_function_code is not None:
        import capo_cloudfront.types.function_blob

        out["connection_function_code"] = (
            capo_cloudfront.types.function_blob.deserialize_xml(
                child_connection_function_code
            )
        )
    return out


def redact_sensitive(value: GetConnectionFunctionResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "connection_function_code" in value:
        out["connection_function_code"] = "*** Sensitive Data Redacted ***"
    return out
