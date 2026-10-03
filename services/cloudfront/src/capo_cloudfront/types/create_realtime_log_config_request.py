"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateRealtimeLogConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.end_point_list
    import capo_cloudfront.types.field_list
    import capo_cloudfront.types.long
    import capo_cloudfront.types.string


class CreateRealtimeLogConfigRequest(TypedDict, closed=True):
    end_points: "capo_cloudfront.types.end_point_list.EndPointList"
    """<p>Contains information about the Amazon Kinesis data stream where you are sending real-time log data.</p>"""
    fields: "capo_cloudfront.types.field_list.FieldList"
    """<p>A list of fields to include in each real-time log record.</p> <p>For more information about fields, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html#understand-real-time-log-config-fields">Real-time log configuration fields</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    name: "capo_cloudfront.types.string.string"
    """<p>A unique name to identify this real-time log configuration.</p>"""
    sampling_rate: "capo_cloudfront.types.long.long"
    """<p>The sampling rate for this real-time log configuration. You can specify a whole number between 1 and 100 (inclusive) to determine the percentage of viewer requests that are represented in the real-time log data.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateRealtimeLogConfigRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.end_point_list

    capo_cloudfront.types.end_point_list.serialize_xml(
        value["end_points"], el, "EndPoints"
    )
    import capo_cloudfront.types.field_list

    capo_cloudfront.types.field_list.serialize_xml(value["fields"], el, "Fields")
    SubElement(el, "Name").text = str(value["name"])
    SubElement(el, "SamplingRate").text = str(value["sampling_rate"])


def deserialize_xml(el: Element) -> CreateRealtimeLogConfigRequest:
    out: CreateRealtimeLogConfigRequest = {}  # type: ignore[typeddict-item]
    child_end_points = el.find("EndPoints")
    if child_end_points is not None:
        import capo_cloudfront.types.end_point_list

        out["end_points"] = capo_cloudfront.types.end_point_list.deserialize_xml(
            child_end_points
        )
    else:
        raise DeserializationError("CreateRealtimeLogConfigRequest.end_points required")
    child_fields = el.find("Fields")
    if child_fields is not None:
        import capo_cloudfront.types.field_list

        out["fields"] = capo_cloudfront.types.field_list.deserialize_xml(child_fields)
    else:
        raise DeserializationError("CreateRealtimeLogConfigRequest.fields required")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("CreateRealtimeLogConfigRequest.name required")
    child_sampling_rate = el.find("SamplingRate")
    if child_sampling_rate is not None:
        out["sampling_rate"] = int(child_sampling_rate.text or "")
    else:
        raise DeserializationError(
            "CreateRealtimeLogConfigRequest.sampling_rate required"
        )
    return out
