"""Generated from Smithy shape ``com.amazonaws.cloudfront#FunctionAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.event_type
    import capo_cloudfront.types.function_arn


class FunctionAssociation(TypedDict, closed=True):
    function_arn: "capo_cloudfront.types.function_arn.FunctionARN"
    """<p>The Amazon Resource Name (ARN) of the function.</p>"""
    event_type: "capo_cloudfront.types.event_type.EventType"
    """<p>The event type of the function, either <code>viewer-request</code> or <code>viewer-response</code>. You cannot use origin-facing event types (<code>origin-request</code> and <code>origin-response</code>) with a CloudFront function.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: FunctionAssociation, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "FunctionARN").text = str(value["function_arn"])
    import capo_cloudfront.types.event_type

    capo_cloudfront.types.event_type.serialize_xml(value["event_type"], el, "EventType")


def deserialize_xml(el: Element) -> FunctionAssociation:
    out: FunctionAssociation = {}  # type: ignore[typeddict-item]
    child_function_arn = el.find("FunctionARN")
    if child_function_arn is not None:
        out["function_arn"] = str(child_function_arn.text or "")
    else:
        out["function_arn"] = ""
    child_event_type = el.find("EventType")
    if child_event_type is not None:
        import capo_cloudfront.types.event_type

        out["event_type"] = capo_cloudfront.types.event_type.deserialize_xml(
            child_event_type
        )
    else:
        import typing

        out["event_type"] = typing.cast(
            "capo_cloudfront.types.event_type.EventType", ""
        )
    return out
