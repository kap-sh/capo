"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateConnectionFunctionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.function_blob
    import capo_cloudfront.types.function_config
    import capo_cloudfront.types.resource_id
    import capo_cloudfront.types.string


class UpdateConnectionFunctionRequest(TypedDict, closed=True):
    id: "capo_cloudfront.types.resource_id.ResourceId"
    """<p>The connection function ID.</p>"""
    if_match: "capo_cloudfront.types.string.string"
    """<p>The current version (<code>ETag</code> value) of the connection function you are updating.</p>"""
    connection_function_config: "capo_cloudfront.types.function_config.FunctionConfig"
    connection_function_code: "capo_cloudfront.types.function_blob.FunctionBlob"
    """<p>The connection function code.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateConnectionFunctionRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.function_config

    capo_cloudfront.types.function_config.serialize_xml(
        value["connection_function_config"], el, "ConnectionFunctionConfig"
    )
    import capo_cloudfront.types.function_blob

    capo_cloudfront.types.function_blob.serialize_xml(
        value["connection_function_code"], el, "ConnectionFunctionCode"
    )


def deserialize_xml(el: Element) -> UpdateConnectionFunctionRequest:
    out: UpdateConnectionFunctionRequest = {}  # type: ignore[typeddict-item]
    child_connection_function_config = el.find("ConnectionFunctionConfig")
    if child_connection_function_config is not None:
        import capo_cloudfront.types.function_config

        out["connection_function_config"] = (
            capo_cloudfront.types.function_config.deserialize_xml(
                child_connection_function_config
            )
        )
    else:
        raise DeserializationError(
            "UpdateConnectionFunctionRequest.connection_function_config required"
        )
    child_connection_function_code = el.find("ConnectionFunctionCode")
    if child_connection_function_code is not None:
        import capo_cloudfront.types.function_blob

        out["connection_function_code"] = (
            capo_cloudfront.types.function_blob.deserialize_xml(
                child_connection_function_code
            )
        )
    else:
        raise DeserializationError(
            "UpdateConnectionFunctionRequest.connection_function_code required"
        )
    return out


def redact_sensitive(value: UpdateConnectionFunctionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "connection_function_code" in value:
        out["connection_function_code"] = "*** Sensitive Data Redacted ***"
    return out
