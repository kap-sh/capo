"""Generated from Smithy shape ``com.amazonaws.cloudfront#FunctionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.function_config
    import capo_cloudfront.types.function_metadata
    import capo_cloudfront.types.function_name
    import capo_cloudfront.types.string


class FunctionSummary(TypedDict, closed=True):
    name: "capo_cloudfront.types.function_name.FunctionName"
    """<p>The name of the CloudFront function.</p>"""
    status: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The status of the CloudFront function.</p>"""
    function_config: "capo_cloudfront.types.function_config.FunctionConfig"
    """<p>Contains configuration information about a CloudFront function.</p>"""
    function_metadata: "capo_cloudfront.types.function_metadata.FunctionMetadata"
    """<p>Contains metadata about a CloudFront function.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: FunctionSummary, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Name").text = str(value["name"])
    if "status" in value:
        SubElement(el, "Status").text = str(value["status"])
    import capo_cloudfront.types.function_config

    capo_cloudfront.types.function_config.serialize_xml(
        value["function_config"], el, "FunctionConfig"
    )
    import capo_cloudfront.types.function_metadata

    capo_cloudfront.types.function_metadata.serialize_xml(
        value["function_metadata"], el, "FunctionMetadata"
    )


def deserialize_xml(el: Element) -> FunctionSummary:
    out: FunctionSummary = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        out["name"] = ""
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_function_config = el.find("FunctionConfig")
    if child_function_config is not None:
        import capo_cloudfront.types.function_config

        out["function_config"] = capo_cloudfront.types.function_config.deserialize_xml(
            child_function_config
        )
    else:
        raise DeserializationError("FunctionSummary.function_config required")
    child_function_metadata = el.find("FunctionMetadata")
    if child_function_metadata is not None:
        import capo_cloudfront.types.function_metadata

        out["function_metadata"] = (
            capo_cloudfront.types.function_metadata.deserialize_xml(
                child_function_metadata
            )
        )
    else:
        raise DeserializationError("FunctionSummary.function_metadata required")
    return out
