"""Generated from Smithy shape ``com.amazonaws.cloudfront#EndPoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.kinesis_stream_config
    import capo_cloudfront.types.string


class EndPoint(TypedDict, closed=True):
    stream_type: "capo_cloudfront.types.string.string"
    """<p>The type of data stream where you are sending real-time log data. The only valid value is <code>Kinesis</code>.</p>"""
    kinesis_stream_config: NotRequired[
        "capo_cloudfront.types.kinesis_stream_config.KinesisStreamConfig"
    ]
    """<p>Contains information about the Amazon Kinesis data stream where you are sending real-time log data in a real-time log configuration.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: EndPoint, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "StreamType").text = str(value["stream_type"])
    if "kinesis_stream_config" in value:
        import capo_cloudfront.types.kinesis_stream_config

        capo_cloudfront.types.kinesis_stream_config.serialize_xml(
            value["kinesis_stream_config"], el, "KinesisStreamConfig"
        )


def deserialize_xml(el: Element) -> EndPoint:
    out: EndPoint = {}  # type: ignore[typeddict-item]
    child_stream_type = el.find("StreamType")
    if child_stream_type is not None:
        out["stream_type"] = str(child_stream_type.text or "")
    else:
        out["stream_type"] = ""
    child_kinesis_stream_config = el.find("KinesisStreamConfig")
    if child_kinesis_stream_config is not None:
        import capo_cloudfront.types.kinesis_stream_config

        out["kinesis_stream_config"] = (
            capo_cloudfront.types.kinesis_stream_config.deserialize_xml(
                child_kinesis_stream_config
            )
        )
    return out
