"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateRealtimeLogConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.end_point_list
    import capo_cloudfront.types.field_list
    import capo_cloudfront.types.long
    import capo_cloudfront.types.string


class UpdateRealtimeLogConfigRequest(TypedDict, closed=True):
    end_points: NotRequired["capo_cloudfront.types.end_point_list.EndPointList"]
    """<p>Contains information about the Amazon Kinesis data stream where you are sending real-time log data.</p>"""
    fields: NotRequired["capo_cloudfront.types.field_list.FieldList"]
    """<p>A list of fields to include in each real-time log record.</p> <p>For more information about fields, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html#understand-real-time-log-config-fields">Real-time log configuration fields</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""
    name: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The name for this real-time log configuration.</p>"""
    arn: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The Amazon Resource Name (ARN) for this real-time log configuration.</p>"""
    sampling_rate: NotRequired["capo_cloudfront.types.long.long"]
    """<p>The sampling rate for this real-time log configuration. The sampling rate determines the percentage of viewer requests that are represented in the real-time log data. You must provide an integer between 1 and 100, inclusive.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateRealtimeLogConfigRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "end_points" in value:
        import capo_cloudfront.types.end_point_list

        capo_cloudfront.types.end_point_list.serialize_xml(
            value["end_points"], el, "EndPoints"
        )
    if "fields" in value:
        import capo_cloudfront.types.field_list

        capo_cloudfront.types.field_list.serialize_xml(value["fields"], el, "Fields")
    if "name" in value:
        SubElement(el, "Name").text = str(value["name"])
    if "arn" in value:
        SubElement(el, "ARN").text = str(value["arn"])
    if "sampling_rate" in value:
        SubElement(el, "SamplingRate").text = str(value["sampling_rate"])


def deserialize_xml(el: Element) -> UpdateRealtimeLogConfigRequest:
    out: UpdateRealtimeLogConfigRequest = {}  # type: ignore[typeddict-item]
    child_end_points = el.find("EndPoints")
    if child_end_points is not None:
        import capo_cloudfront.types.end_point_list

        out["end_points"] = capo_cloudfront.types.end_point_list.deserialize_xml(
            child_end_points
        )
    child_fields = el.find("Fields")
    if child_fields is not None:
        import capo_cloudfront.types.field_list

        out["fields"] = capo_cloudfront.types.field_list.deserialize_xml(child_fields)
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_arn = el.find("ARN")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    child_sampling_rate = el.find("SamplingRate")
    if child_sampling_rate is not None:
        out["sampling_rate"] = int(child_sampling_rate.text or "")
    return out
