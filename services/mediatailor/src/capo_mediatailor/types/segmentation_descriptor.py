"""Generated from Smithy shape ``com.amazonaws.mediatailor#SegmentationDescriptor``."""

from typing_extensions import NotRequired, TypedDict


class SegmentationDescriptor(TypedDict, closed=True):
    segmentation_event_id: NotRequired["int"]
    """<p>The Event Identifier to assign to the <code>segmentation_descriptor.segmentation_event_id</code> message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. The default value is 1.</p>"""
    segmentation_upid_type: NotRequired["int"]
    """<p>The Upid Type to assign to the <code>segmentation_descriptor.segmentation_upid_type</code> message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. Values must be between 0 and 256, inclusive. The default value is 14.</p>"""
    segmentation_upid: NotRequired["str"]
    """<p>The Upid to assign to the <code>segmentation_descriptor.segmentation_upid</code> message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. The value must be a hexadecimal string containing only the characters 0 though 9 and A through F. The default value is "" (an empty string).</p>"""
    segmentation_type_id: NotRequired["int"]
    """<p>The Type Identifier to assign to the <code>segmentation_descriptor.segmentation_type_id</code> message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. Values must be between 0 and 256, inclusive. The default value is 48.</p>"""
    segment_num: NotRequired["int"]
    """<p>The segment number to assign to the <code>segmentation_descriptor.segment_num</code> message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification Values must be between 0 and 256, inclusive. The default value is 0.</p>"""
    segments_expected: NotRequired["int"]
    """<p>The number of segments expected, which is assigned to the <code>segmentation_descriptor.segments_expectedS</code> message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification Values must be between 0 and 256, inclusive. The default value is 0.</p>"""
    sub_segment_num: NotRequired["int"]
    """<p>The sub-segment number to assign to the <code>segmentation_descriptor.sub_segment_num</code> message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. Values must be between 0 and 256, inclusive. The defualt value is null.</p>"""
    sub_segments_expected: NotRequired["int"]
    """<p>The number of sub-segments expected, which is assigned to the <code>segmentation_descriptor.sub_segments_expected</code> message, as defined in section 10.3.3.1 of the 2022 SCTE-35 specification. Values must be between 0 and 256, inclusive. The default value is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SegmentationDescriptor) -> dict:
    out: dict = {}
    if "segmentation_event_id" in value:
        out["SegmentationEventId"] = value["segmentation_event_id"]
    if "segmentation_upid_type" in value:
        out["SegmentationUpidType"] = value["segmentation_upid_type"]
    if "segmentation_upid" in value:
        out["SegmentationUpid"] = value["segmentation_upid"]
    if "segmentation_type_id" in value:
        out["SegmentationTypeId"] = value["segmentation_type_id"]
    if "segment_num" in value:
        out["SegmentNum"] = value["segment_num"]
    if "segments_expected" in value:
        out["SegmentsExpected"] = value["segments_expected"]
    if "sub_segment_num" in value:
        out["SubSegmentNum"] = value["sub_segment_num"]
    if "sub_segments_expected" in value:
        out["SubSegmentsExpected"] = value["sub_segments_expected"]
    return out


def deserialize_json(data: dict) -> SegmentationDescriptor:
    out: SegmentationDescriptor = {}  # type: ignore[typeddict-item]
    if data.get("SegmentationEventId") is not None:
        out["segmentation_event_id"] = data["SegmentationEventId"]
    if data.get("SegmentationUpidType") is not None:
        out["segmentation_upid_type"] = data["SegmentationUpidType"]
    if data.get("SegmentationUpid") is not None:
        out["segmentation_upid"] = data["SegmentationUpid"]
    if data.get("SegmentationTypeId") is not None:
        out["segmentation_type_id"] = data["SegmentationTypeId"]
    if data.get("SegmentNum") is not None:
        out["segment_num"] = data["SegmentNum"]
    if data.get("SegmentsExpected") is not None:
        out["segments_expected"] = data["SegmentsExpected"]
    if data.get("SubSegmentNum") is not None:
        out["sub_segment_num"] = data["SubSegmentNum"]
    if data.get("SubSegmentsExpected") is not None:
        out["sub_segments_expected"] = data["SubSegmentsExpected"]
    return out
