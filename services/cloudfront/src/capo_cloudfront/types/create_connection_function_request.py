"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateConnectionFunctionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.function_blob
    import capo_cloudfront.types.function_config
    import capo_cloudfront.types.function_name
    import capo_cloudfront.types.tags


class CreateConnectionFunctionRequest(TypedDict, closed=True):
    name: "capo_cloudfront.types.function_name.FunctionName"
    """<p>A name for the connection function.</p>"""
    connection_function_config: "capo_cloudfront.types.function_config.FunctionConfig"
    connection_function_code: "capo_cloudfront.types.function_blob.FunctionBlob"
    """<p>The code for the connection function.</p>"""
    tags: NotRequired["capo_cloudfront.types.tags.Tags"]


# --- restXml ser/de ---
def serialize_xml(
    value: CreateConnectionFunctionRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Name").text = str(value["name"])
    import capo_cloudfront.types.function_config

    capo_cloudfront.types.function_config.serialize_xml(
        value["connection_function_config"], el, "ConnectionFunctionConfig"
    )
    import capo_cloudfront.types.function_blob

    capo_cloudfront.types.function_blob.serialize_xml(
        value["connection_function_code"], el, "ConnectionFunctionCode"
    )
    if "tags" in value:
        import capo_cloudfront.types.tags

        capo_cloudfront.types.tags.serialize_xml(value["tags"], el, "Tags")


def deserialize_xml(el: Element) -> CreateConnectionFunctionRequest:
    out: CreateConnectionFunctionRequest = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        out["name"] = ""
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
            "CreateConnectionFunctionRequest.connection_function_config required"
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
        out["connection_function_code"] = b""
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_cloudfront.types.tags

        out["tags"] = capo_cloudfront.types.tags.deserialize_xml(child_tags)
    return out


def redact_sensitive(value: CreateConnectionFunctionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "connection_function_code" in value:
        out["connection_function_code"] = "*** Sensitive Data Redacted ***"
    return out
