"""Generated from Smithy shape ``com.amazonaws.cloudfront#TestConnectionFunctionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.function_event_object
    import capo_cloudfront.types.function_stage
    import capo_cloudfront.types.resource_id
    import capo_cloudfront.types.string


class TestConnectionFunctionRequest(TypedDict, closed=True):
    id: "capo_cloudfront.types.resource_id.ResourceId"
    """<p>The connection function ID.</p>"""
    if_match: "capo_cloudfront.types.string.string"
    """<p>The current version (<code>ETag</code> value) of the connection function.</p>"""
    stage: NotRequired["capo_cloudfront.types.function_stage.FunctionStage"]
    """<p>The connection function stage.</p>"""
    connection_object: "capo_cloudfront.types.function_event_object.FunctionEventObject"
    """<p>The connection object.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: TestConnectionFunctionRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "stage" in value:
        import capo_cloudfront.types.function_stage

        capo_cloudfront.types.function_stage.serialize_xml(value["stage"], el, "Stage")
    import capo_cloudfront.types.function_event_object

    capo_cloudfront.types.function_event_object.serialize_xml(
        value["connection_object"], el, "ConnectionObject"
    )


def deserialize_xml(el: Element) -> TestConnectionFunctionRequest:
    out: TestConnectionFunctionRequest = {}  # type: ignore[typeddict-item]
    child_stage = el.find("Stage")
    if child_stage is not None:
        import capo_cloudfront.types.function_stage

        out["stage"] = capo_cloudfront.types.function_stage.deserialize_xml(child_stage)
    child_connection_object = el.find("ConnectionObject")
    if child_connection_object is not None:
        import capo_cloudfront.types.function_event_object

        out["connection_object"] = (
            capo_cloudfront.types.function_event_object.deserialize_xml(
                child_connection_object
            )
        )
    else:
        raise DeserializationError(
            "TestConnectionFunctionRequest.connection_object required"
        )
    return out


def redact_sensitive(value: TestConnectionFunctionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "connection_object" in value:
        out["connection_object"] = "*** Sensitive Data Redacted ***"
    return out
