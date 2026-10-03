"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateFunctionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.function_blob
    import capo_cloudfront.types.function_config
    import capo_cloudfront.types.function_name
    import capo_cloudfront.types.tags


class CreateFunctionRequest(TypedDict, closed=True):
    name: "capo_cloudfront.types.function_name.FunctionName"
    """<p>A name to identify the function.</p>"""
    function_config: "capo_cloudfront.types.function_config.FunctionConfig"
    """<p>Configuration information about the function, including an optional comment and the function's runtime.</p>"""
    function_code: "capo_cloudfront.types.function_blob.FunctionBlob"
    """<p>The function code. For more information about writing a CloudFront function, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/writing-function-code.html">Writing function code for CloudFront Functions</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    tags: NotRequired["capo_cloudfront.types.tags.Tags"]


# --- restXml ser/de ---
def serialize_xml(value: CreateFunctionRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Name").text = str(value["name"])
    import capo_cloudfront.types.function_config

    capo_cloudfront.types.function_config.serialize_xml(
        value["function_config"], el, "FunctionConfig"
    )
    import capo_cloudfront.types.function_blob

    capo_cloudfront.types.function_blob.serialize_xml(
        value["function_code"], el, "FunctionCode"
    )
    if "tags" in value:
        import capo_cloudfront.types.tags

        capo_cloudfront.types.tags.serialize_xml(value["tags"], el, "Tags")


def deserialize_xml(el: Element) -> CreateFunctionRequest:
    out: CreateFunctionRequest = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("CreateFunctionRequest.name required")
    child_function_config = el.find("FunctionConfig")
    if child_function_config is not None:
        import capo_cloudfront.types.function_config

        out["function_config"] = capo_cloudfront.types.function_config.deserialize_xml(
            child_function_config
        )
    else:
        raise DeserializationError("CreateFunctionRequest.function_config required")
    child_function_code = el.find("FunctionCode")
    if child_function_code is not None:
        import capo_cloudfront.types.function_blob

        out["function_code"] = capo_cloudfront.types.function_blob.deserialize_xml(
            child_function_code
        )
    else:
        raise DeserializationError("CreateFunctionRequest.function_code required")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_cloudfront.types.tags

        out["tags"] = capo_cloudfront.types.tags.deserialize_xml(child_tags)
    return out
