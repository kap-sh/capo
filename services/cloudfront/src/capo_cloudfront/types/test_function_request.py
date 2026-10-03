"""Generated from Smithy shape ``com.amazonaws.cloudfront#TestFunctionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.function_event_object
    import capo_cloudfront.types.function_name
    import capo_cloudfront.types.function_stage
    import capo_cloudfront.types.string


class TestFunctionRequest(TypedDict, closed=True):
    name: "capo_cloudfront.types.function_name.FunctionName"
    """<p>The name of the function that you are testing.</p>"""
    if_match: "capo_cloudfront.types.string.string"
    """<p>The current version (<code>ETag</code> value) of the function that you are testing, which you can get using <code>DescribeFunction</code>.</p>"""
    stage: NotRequired["capo_cloudfront.types.function_stage.FunctionStage"]
    """<p>The stage of the function that you are testing, either <code>DEVELOPMENT</code> or <code>LIVE</code>.</p>"""
    event_object: "capo_cloudfront.types.function_event_object.FunctionEventObject"
    """<p>The event object to test the function with. For more information about the structure of the event object, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/managing-functions.html#test-function">Testing functions</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: TestFunctionRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "stage" in value:
        import capo_cloudfront.types.function_stage

        capo_cloudfront.types.function_stage.serialize_xml(value["stage"], el, "Stage")
    import capo_cloudfront.types.function_event_object

    capo_cloudfront.types.function_event_object.serialize_xml(
        value["event_object"], el, "EventObject"
    )


def deserialize_xml(el: Element) -> TestFunctionRequest:
    out: TestFunctionRequest = {}  # type: ignore[typeddict-item]
    child_stage = el.find("Stage")
    if child_stage is not None:
        import capo_cloudfront.types.function_stage

        out["stage"] = capo_cloudfront.types.function_stage.deserialize_xml(child_stage)
    child_event_object = el.find("EventObject")
    if child_event_object is not None:
        import capo_cloudfront.types.function_event_object

        out["event_object"] = (
            capo_cloudfront.types.function_event_object.deserialize_xml(
                child_event_object
            )
        )
    else:
        raise DeserializationError("TestFunctionRequest.event_object required")
    return out
