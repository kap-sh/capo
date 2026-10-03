"""Generated from Smithy shape ``com.amazonaws.cloudfront#RealtimeLogConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.end_point_list
    import capo_cloudfront.types.field_list
    import capo_cloudfront.types.long
    import capo_cloudfront.types.string


class RealtimeLogConfig(TypedDict, closed=True):
    arn: "capo_cloudfront.types.string.string"
    """<p>The Amazon Resource Name (ARN) of this real-time log configuration.</p>"""
    name: "capo_cloudfront.types.string.string"
    """<p>The unique name of this real-time log configuration.</p>"""
    sampling_rate: "capo_cloudfront.types.long.long"
    """<p>The sampling rate for this real-time log configuration. The sampling rate determines the percentage of viewer requests that are represented in the real-time log data. The sampling rate is an integer between 1 and 100, inclusive.</p>"""
    end_points: "capo_cloudfront.types.end_point_list.EndPointList"
    """<p>Contains information about the Amazon Kinesis data stream where you are sending real-time log data for this real-time log configuration.</p>"""
    fields: "capo_cloudfront.types.field_list.FieldList"
    """<p>A list of fields that are included in each real-time log record. In an API response, the fields are provided in the same order in which they are sent to the Amazon Kinesis data stream.</p> <p>For more information about fields, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html#understand-real-time-log-config-fields">Real-time log configuration fields</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: RealtimeLogConfig, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "ARN").text = str(value["arn"])
    SubElement(el, "Name").text = str(value["name"])
    SubElement(el, "SamplingRate").text = str(value["sampling_rate"])
    import capo_cloudfront.types.end_point_list

    capo_cloudfront.types.end_point_list.serialize_xml(
        value["end_points"], el, "EndPoints"
    )
    import capo_cloudfront.types.field_list

    capo_cloudfront.types.field_list.serialize_xml(value["fields"], el, "Fields")


def deserialize_xml(el: Element) -> RealtimeLogConfig:
    out: RealtimeLogConfig = {}  # type: ignore[typeddict-item]
    child_arn = el.find("ARN")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    else:
        raise DeserializationError("RealtimeLogConfig.arn required")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("RealtimeLogConfig.name required")
    child_sampling_rate = el.find("SamplingRate")
    if child_sampling_rate is not None:
        out["sampling_rate"] = int(child_sampling_rate.text or "")
    else:
        raise DeserializationError("RealtimeLogConfig.sampling_rate required")
    child_end_points = el.find("EndPoints")
    if child_end_points is not None:
        import capo_cloudfront.types.end_point_list

        out["end_points"] = capo_cloudfront.types.end_point_list.deserialize_xml(
            child_end_points
        )
    else:
        raise DeserializationError("RealtimeLogConfig.end_points required")
    child_fields = el.find("Fields")
    if child_fields is not None:
        import capo_cloudfront.types.field_list

        out["fields"] = capo_cloudfront.types.field_list.deserialize_xml(child_fields)
    else:
        raise DeserializationError("RealtimeLogConfig.fields required")
    return out
