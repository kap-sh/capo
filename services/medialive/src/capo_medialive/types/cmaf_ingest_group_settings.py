"""Generated from Smithy shape ``com.amazonaws.medialive#CmafIngestGroupSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min0_max2000
    import capo_medialive.types.__integer_min0_max10000
    import capo_medialive.types.__integer_min1
    import capo_medialive.types.__list_of_additional_destinations
    import capo_medialive.types.__list_of_cmaf_ingest_caption_language_mapping
    import capo_medialive.types.__string_max100
    import capo_medialive.types.cmaf_id3_behavior
    import capo_medialive.types.cmaf_ingest_segment_length_units
    import capo_medialive.types.cmaf_ingest_watermarking_settings
    import capo_medialive.types.cmaf_klv_behavior
    import capo_medialive.types.cmaf_nielsen_id3_behavior
    import capo_medialive.types.cmaf_timed_metadata_id3_frame
    import capo_medialive.types.cmaf_timed_metadata_passthrough
    import capo_medialive.types.output_location_ref
    import capo_medialive.types.scte35_type


class CmafIngestGroupSettings(TypedDict, closed=True):
    destination: NotRequired[
        "capo_medialive.types.output_location_ref.OutputLocationRef"
    ]
    """A HTTP destination for the tracks"""
    nielsen_id3_behavior: NotRequired[
        "capo_medialive.types.cmaf_nielsen_id3_behavior.CmafNielsenId3Behavior"
    ]
    """If set to passthrough, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output."""
    scte35_type: NotRequired["capo_medialive.types.scte35_type.Scte35Type"]
    """SCTE-35 insertion type. Option "none" indicates that a SCTE-35 marker will not be inserted, nor will an IDR be inserted at the SCTE-35 cue point, nor will the segment be segmented. Option "scte35WithoutIdr" indicates that a SCTE-35 marker will be inserted to indicate the cue point, but MediaLive will not insert an IDR on that frame nor will it introduce a new segment boundary there if it wasn't already going to be one (this option is required for use with downstream multiview bitstream stitching workflows). Option "scte35WithoutSegmentation" indicates that a SCTE-35 marker will be inserted to indicate the cue point, and an IDR will be inserted on that frame so that a downstream re-packager might split the segment there, but MediaLive itself will not introduce a new segment boundary there."""
    segment_length: NotRequired["capo_medialive.types.__integer_min1.__integerMin1"]
    """The nominal duration of segments. The units are specified in SegmentLengthUnits. The segments will end on the next keyframe after the specified duration, so the actual segment length might be longer, and it might be a fraction of the units."""
    segment_length_units: NotRequired[
        "capo_medialive.types.cmaf_ingest_segment_length_units.CmafIngestSegmentLengthUnits"
    ]
    """Time unit for segment length parameter."""
    send_delay_ms: NotRequired[
        "capo_medialive.types.__integer_min0_max2000.__integerMin0Max2000"
    ]
    """Number of milliseconds to delay the output from the second pipeline."""
    klv_behavior: NotRequired["capo_medialive.types.cmaf_klv_behavior.CmafKLVBehavior"]
    """If set to passthrough, passes any KLV data from the input source to this output."""
    klv_name_modifier: NotRequired[
        "capo_medialive.types.__string_max100.__stringMax100"
    ]
    r"""Change the modifier that MediaLive automatically adds to the Streams() name that identifies a KLV track. The default is "klv", which means the default name will be Streams(klv.cmfm). Any string you enter here will replace the "klv" string.\nThe modifier can only contain: numbers, letters, plus (+), minus (-), underscore (_) and period (.) and has a maximum length of 100 characters."""
    nielsen_id3_name_modifier: NotRequired[
        "capo_medialive.types.__string_max100.__stringMax100"
    ]
    r"""Change the modifier that MediaLive automatically adds to the Streams() name that identifies a Nielsen ID3 track. The default is "nid3", which means the default name will be Streams(nid3.cmfm). Any string you enter here will replace the "nid3" string.\nThe modifier can only contain: numbers, letters, plus (+), minus (-), underscore (_) and period (.) and has a maximum length of 100 characters."""
    scte35_name_modifier: NotRequired[
        "capo_medialive.types.__string_max100.__stringMax100"
    ]
    r"""Change the modifier that MediaLive automatically adds to the Streams() name for a SCTE 35 track. The default is "scte", which means the default name will be Streams(scte.cmfm). Any string you enter here will replace the "scte" string.\nThe modifier can only contain: numbers, letters, plus (+), minus (-), underscore (_) and period (.) and has a maximum length of 100 characters."""
    id3_behavior: NotRequired["capo_medialive.types.cmaf_id3_behavior.CmafId3Behavior"]
    """Set to ENABLED to enable ID3 metadata insertion. To include metadata, you configure other parameters in the output group, or you add an ID3 action to the channel schedule."""
    id3_name_modifier: NotRequired[
        "capo_medialive.types.__string_max100.__stringMax100"
    ]
    r"""Change the modifier that MediaLive automatically adds to the Streams() name that identifies an ID3 track. The default is "id3", which means the default name will be Streams(id3.cmfm). Any string you enter here will replace the "id3" string.\nThe modifier can only contain: numbers, letters, plus (+), minus (-), underscore (_) and period (.) and has a maximum length of 100 characters."""
    caption_language_mappings: NotRequired[
        "capo_medialive.types.__list_of_cmaf_ingest_caption_language_mapping.__listOfCmafIngestCaptionLanguageMapping"
    ]
    """An array that identifies the languages in the four caption channels in the embedded captions."""
    timed_metadata_id3_frame: NotRequired[
        "capo_medialive.types.cmaf_timed_metadata_id3_frame.CmafTimedMetadataId3Frame"
    ]
    """Set to none if you don't want to insert a timecode in the output. Otherwise choose the frame type for the timecode."""
    timed_metadata_id3_period: NotRequired[
        "capo_medialive.types.__integer_min0_max10000.__integerMin0Max10000"
    ]
    """If you set up to insert a timecode in the output, specify the frequency for the frame, in seconds."""
    timed_metadata_passthrough: NotRequired[
        "capo_medialive.types.cmaf_timed_metadata_passthrough.CmafTimedMetadataPassthrough"
    ]
    """Set to enabled to pass through ID3 metadata from the input sources."""
    additional_destinations: NotRequired[
        "capo_medialive.types.__list_of_additional_destinations.__listOfAdditionalDestinations"
    ]
    """Optional an array of additional destinational HTTP destinations for the OutputGroup outputs"""
    watermarking_settings: NotRequired[
        "capo_medialive.types.cmaf_ingest_watermarking_settings.CmafIngestWatermarkingSettings"
    ]
    """Specifies the type of watermarking technology to use."""


# --- restJson1 ser/de ---
def serialize_json(value: CmafIngestGroupSettings) -> dict:
    out: dict = {}
    if "destination" in value:
        import capo_medialive.types.output_location_ref

        out["destination"] = capo_medialive.types.output_location_ref.serialize_json(
            value["destination"]
        )
    if "nielsen_id3_behavior" in value:
        import capo_medialive.types.cmaf_nielsen_id3_behavior

        out["nielsenId3Behavior"] = (
            capo_medialive.types.cmaf_nielsen_id3_behavior.serialize_json(
                value["nielsen_id3_behavior"]
            )
        )
    if "scte35_type" in value:
        import capo_medialive.types.scte35_type

        out["scte35Type"] = capo_medialive.types.scte35_type.serialize_json(
            value["scte35_type"]
        )
    if "segment_length" in value:
        out["segmentLength"] = value["segment_length"]
    if "segment_length_units" in value:
        import capo_medialive.types.cmaf_ingest_segment_length_units

        out["segmentLengthUnits"] = (
            capo_medialive.types.cmaf_ingest_segment_length_units.serialize_json(
                value["segment_length_units"]
            )
        )
    if "send_delay_ms" in value:
        out["sendDelayMs"] = value["send_delay_ms"]
    if "klv_behavior" in value:
        import capo_medialive.types.cmaf_klv_behavior

        out["klvBehavior"] = capo_medialive.types.cmaf_klv_behavior.serialize_json(
            value["klv_behavior"]
        )
    if "klv_name_modifier" in value:
        out["klvNameModifier"] = value["klv_name_modifier"]
    if "nielsen_id3_name_modifier" in value:
        out["nielsenId3NameModifier"] = value["nielsen_id3_name_modifier"]
    if "scte35_name_modifier" in value:
        out["scte35NameModifier"] = value["scte35_name_modifier"]
    if "id3_behavior" in value:
        import capo_medialive.types.cmaf_id3_behavior

        out["id3Behavior"] = capo_medialive.types.cmaf_id3_behavior.serialize_json(
            value["id3_behavior"]
        )
    if "id3_name_modifier" in value:
        out["id3NameModifier"] = value["id3_name_modifier"]
    if "caption_language_mappings" in value:
        import capo_medialive.types.__list_of_cmaf_ingest_caption_language_mapping

        out["captionLanguageMappings"] = (
            capo_medialive.types.__list_of_cmaf_ingest_caption_language_mapping.serialize_json(
                value["caption_language_mappings"]
            )
        )
    if "timed_metadata_id3_frame" in value:
        import capo_medialive.types.cmaf_timed_metadata_id3_frame

        out["timedMetadataId3Frame"] = (
            capo_medialive.types.cmaf_timed_metadata_id3_frame.serialize_json(
                value["timed_metadata_id3_frame"]
            )
        )
    if "timed_metadata_id3_period" in value:
        out["timedMetadataId3Period"] = value["timed_metadata_id3_period"]
    if "timed_metadata_passthrough" in value:
        import capo_medialive.types.cmaf_timed_metadata_passthrough

        out["timedMetadataPassthrough"] = (
            capo_medialive.types.cmaf_timed_metadata_passthrough.serialize_json(
                value["timed_metadata_passthrough"]
            )
        )
    if "additional_destinations" in value:
        import capo_medialive.types.__list_of_additional_destinations

        out["additionalDestinations"] = (
            capo_medialive.types.__list_of_additional_destinations.serialize_json(
                value["additional_destinations"]
            )
        )
    if "watermarking_settings" in value:
        import capo_medialive.types.cmaf_ingest_watermarking_settings

        out["watermarkingSettings"] = (
            capo_medialive.types.cmaf_ingest_watermarking_settings.serialize_json(
                value["watermarking_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> CmafIngestGroupSettings:
    out: CmafIngestGroupSettings = {}  # type: ignore[typeddict-item]
    if data.get("destination") is not None:
        import capo_medialive.types.output_location_ref

        out["destination"] = capo_medialive.types.output_location_ref.deserialize_json(
            data["destination"]
        )
    if data.get("nielsenId3Behavior") is not None:
        import capo_medialive.types.cmaf_nielsen_id3_behavior

        out["nielsen_id3_behavior"] = (
            capo_medialive.types.cmaf_nielsen_id3_behavior.deserialize_json(
                data["nielsenId3Behavior"]
            )
        )
    if data.get("scte35Type") is not None:
        import capo_medialive.types.scte35_type

        out["scte35_type"] = capo_medialive.types.scte35_type.deserialize_json(
            data["scte35Type"]
        )
    if data.get("segmentLength") is not None:
        out["segment_length"] = data["segmentLength"]
    if data.get("segmentLengthUnits") is not None:
        import capo_medialive.types.cmaf_ingest_segment_length_units

        out["segment_length_units"] = (
            capo_medialive.types.cmaf_ingest_segment_length_units.deserialize_json(
                data["segmentLengthUnits"]
            )
        )
    if data.get("sendDelayMs") is not None:
        out["send_delay_ms"] = data["sendDelayMs"]
    if data.get("klvBehavior") is not None:
        import capo_medialive.types.cmaf_klv_behavior

        out["klv_behavior"] = capo_medialive.types.cmaf_klv_behavior.deserialize_json(
            data["klvBehavior"]
        )
    if data.get("klvNameModifier") is not None:
        out["klv_name_modifier"] = data["klvNameModifier"]
    if data.get("nielsenId3NameModifier") is not None:
        out["nielsen_id3_name_modifier"] = data["nielsenId3NameModifier"]
    if data.get("scte35NameModifier") is not None:
        out["scte35_name_modifier"] = data["scte35NameModifier"]
    if data.get("id3Behavior") is not None:
        import capo_medialive.types.cmaf_id3_behavior

        out["id3_behavior"] = capo_medialive.types.cmaf_id3_behavior.deserialize_json(
            data["id3Behavior"]
        )
    if data.get("id3NameModifier") is not None:
        out["id3_name_modifier"] = data["id3NameModifier"]
    if data.get("captionLanguageMappings") is not None:
        import capo_medialive.types.__list_of_cmaf_ingest_caption_language_mapping

        out["caption_language_mappings"] = (
            capo_medialive.types.__list_of_cmaf_ingest_caption_language_mapping.deserialize_json(
                data["captionLanguageMappings"]
            )
        )
    if data.get("timedMetadataId3Frame") is not None:
        import capo_medialive.types.cmaf_timed_metadata_id3_frame

        out["timed_metadata_id3_frame"] = (
            capo_medialive.types.cmaf_timed_metadata_id3_frame.deserialize_json(
                data["timedMetadataId3Frame"]
            )
        )
    if data.get("timedMetadataId3Period") is not None:
        out["timed_metadata_id3_period"] = data["timedMetadataId3Period"]
    if data.get("timedMetadataPassthrough") is not None:
        import capo_medialive.types.cmaf_timed_metadata_passthrough

        out["timed_metadata_passthrough"] = (
            capo_medialive.types.cmaf_timed_metadata_passthrough.deserialize_json(
                data["timedMetadataPassthrough"]
            )
        )
    if data.get("additionalDestinations") is not None:
        import capo_medialive.types.__list_of_additional_destinations

        out["additional_destinations"] = (
            capo_medialive.types.__list_of_additional_destinations.deserialize_json(
                data["additionalDestinations"]
            )
        )
    if data.get("watermarkingSettings") is not None:
        import capo_medialive.types.cmaf_ingest_watermarking_settings

        out["watermarking_settings"] = (
            capo_medialive.types.cmaf_ingest_watermarking_settings.deserialize_json(
                data["watermarkingSettings"]
            )
        )
    return out
