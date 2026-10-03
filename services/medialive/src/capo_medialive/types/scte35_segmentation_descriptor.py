"""Generated from Smithy shape ``com.amazonaws.medialive#Scte35SegmentationDescriptor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min0_max255
    import capo_medialive.types.__long_min0_max4294967295
    import capo_medialive.types.__long_min0_max1099511627775
    import capo_medialive.types.__string
    import capo_medialive.types.scte35_delivery_restrictions
    import capo_medialive.types.scte35_segmentation_cancel_indicator


class Scte35SegmentationDescriptor(TypedDict, closed=True):
    delivery_restrictions: NotRequired[
        "capo_medialive.types.scte35_delivery_restrictions.Scte35DeliveryRestrictions"
    ]
    """Holds the four SCTE-35 delivery restriction parameters."""
    segment_num: NotRequired[
        "capo_medialive.types.__integer_min0_max255.__integerMin0Max255"
    ]
    """Corresponds to SCTE-35 segment_num. A value that is valid for the specified segmentation_type_id."""
    segmentation_cancel_indicator: NotRequired[
        "capo_medialive.types.scte35_segmentation_cancel_indicator.Scte35SegmentationCancelIndicator"
    ]
    """Corresponds to SCTE-35 segmentation_event_cancel_indicator."""
    segmentation_duration: NotRequired[
        "capo_medialive.types.__long_min0_max1099511627775.__longMin0Max1099511627775"
    ]
    """Corresponds to SCTE-35 segmentation_duration. Optional. The duration for the time_signal, in 90 KHz ticks. To convert seconds to ticks, multiple the seconds by 90,000. Enter time in 90 KHz clock ticks. If you do not enter a duration, the time_signal will continue until you insert a cancellation message."""
    segmentation_event_id: NotRequired[
        "capo_medialive.types.__long_min0_max4294967295.__longMin0Max4294967295"
    ]
    """Corresponds to SCTE-35 segmentation_event_id."""
    segmentation_type_id: NotRequired[
        "capo_medialive.types.__integer_min0_max255.__integerMin0Max255"
    ]
    """Corresponds to SCTE-35 segmentation_type_id. One of the segmentation_type_id values listed in the SCTE-35 specification. On the console, enter the ID in decimal (for example, "52"). In the CLI, API, or an SDK, enter the ID in hex (for example, "0x34") or decimal (for example, "52")."""
    segmentation_upid: NotRequired["capo_medialive.types.__string.__string"]
    """Corresponds to SCTE-35 segmentation_upid. Enter a string containing the hexadecimal representation of the characters that make up the SCTE-35 segmentation_upid value. Must contain an even number of hex characters. Do not include spaces between each hex pair. For example, the ASCII "ADS Information" becomes hex "41445320496e666f726d6174696f6e."""
    segmentation_upid_type: NotRequired[
        "capo_medialive.types.__integer_min0_max255.__integerMin0Max255"
    ]
    """Corresponds to SCTE-35 segmentation_upid_type. On the console, enter one of the types listed in the SCTE-35 specification, converted to a decimal. For example, "0x0C" hex from the specification is "12" in decimal. In the CLI, API, or an SDK, enter one of the types listed in the SCTE-35 specification, in either hex (for example, "0x0C" ) or in decimal (for example, "12")."""
    segments_expected: NotRequired[
        "capo_medialive.types.__integer_min0_max255.__integerMin0Max255"
    ]
    """Corresponds to SCTE-35 segments_expected. A value that is valid for the specified segmentation_type_id."""
    sub_segment_num: NotRequired[
        "capo_medialive.types.__integer_min0_max255.__integerMin0Max255"
    ]
    """Corresponds to SCTE-35 sub_segment_num. A value that is valid for the specified segmentation_type_id."""
    sub_segments_expected: NotRequired[
        "capo_medialive.types.__integer_min0_max255.__integerMin0Max255"
    ]
    """Corresponds to SCTE-35 sub_segments_expected. A value that is valid for the specified segmentation_type_id."""


# --- restJson1 ser/de ---
def serialize_json(value: Scte35SegmentationDescriptor) -> dict:
    out: dict = {}
    if "delivery_restrictions" in value:
        import capo_medialive.types.scte35_delivery_restrictions

        out["deliveryRestrictions"] = (
            capo_medialive.types.scte35_delivery_restrictions.serialize_json(
                value["delivery_restrictions"]
            )
        )
    if "segment_num" in value:
        out["segmentNum"] = value["segment_num"]
    if "segmentation_cancel_indicator" in value:
        import capo_medialive.types.scte35_segmentation_cancel_indicator

        out["segmentationCancelIndicator"] = (
            capo_medialive.types.scte35_segmentation_cancel_indicator.serialize_json(
                value["segmentation_cancel_indicator"]
            )
        )
    if "segmentation_duration" in value:
        out["segmentationDuration"] = value["segmentation_duration"]
    if "segmentation_event_id" in value:
        out["segmentationEventId"] = value["segmentation_event_id"]
    if "segmentation_type_id" in value:
        out["segmentationTypeId"] = value["segmentation_type_id"]
    if "segmentation_upid" in value:
        out["segmentationUpid"] = value["segmentation_upid"]
    if "segmentation_upid_type" in value:
        out["segmentationUpidType"] = value["segmentation_upid_type"]
    if "segments_expected" in value:
        out["segmentsExpected"] = value["segments_expected"]
    if "sub_segment_num" in value:
        out["subSegmentNum"] = value["sub_segment_num"]
    if "sub_segments_expected" in value:
        out["subSegmentsExpected"] = value["sub_segments_expected"]
    return out


def deserialize_json(data: dict) -> Scte35SegmentationDescriptor:
    out: Scte35SegmentationDescriptor = {}  # type: ignore[typeddict-item]
    if data.get("deliveryRestrictions") is not None:
        import capo_medialive.types.scte35_delivery_restrictions

        out["delivery_restrictions"] = (
            capo_medialive.types.scte35_delivery_restrictions.deserialize_json(
                data["deliveryRestrictions"]
            )
        )
    if data.get("segmentNum") is not None:
        out["segment_num"] = data["segmentNum"]
    if data.get("segmentationCancelIndicator") is not None:
        import capo_medialive.types.scte35_segmentation_cancel_indicator

        out["segmentation_cancel_indicator"] = (
            capo_medialive.types.scte35_segmentation_cancel_indicator.deserialize_json(
                data["segmentationCancelIndicator"]
            )
        )
    if data.get("segmentationDuration") is not None:
        out["segmentation_duration"] = data["segmentationDuration"]
    if data.get("segmentationEventId") is not None:
        out["segmentation_event_id"] = data["segmentationEventId"]
    if data.get("segmentationTypeId") is not None:
        out["segmentation_type_id"] = data["segmentationTypeId"]
    if data.get("segmentationUpid") is not None:
        out["segmentation_upid"] = data["segmentationUpid"]
    if data.get("segmentationUpidType") is not None:
        out["segmentation_upid_type"] = data["segmentationUpidType"]
    if data.get("segmentsExpected") is not None:
        out["segments_expected"] = data["segmentsExpected"]
    if data.get("subSegmentNum") is not None:
        out["sub_segment_num"] = data["subSegmentNum"]
    if data.get("subSegmentsExpected") is not None:
        out["sub_segments_expected"] = data["subSegmentsExpected"]
    return out
