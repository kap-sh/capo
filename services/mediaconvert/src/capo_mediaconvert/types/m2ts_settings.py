"""Generated from Smithy shape ``com.amazonaws.mediaconvert#M2tsSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__double_min0
    import capo_mediaconvert.types.__integer_min0_max500
    import capo_mediaconvert.types.__integer_min0_max1000
    import capo_mediaconvert.types.__integer_min0_max3600
    import capo_mediaconvert.types.__integer_min0_max10000
    import capo_mediaconvert.types.__integer_min0_max65535
    import capo_mediaconvert.types.__integer_min0_max2147483647
    import capo_mediaconvert.types.__integer_min32_max8182
    import capo_mediaconvert.types.__integer_min_negative10000_max10000
    import capo_mediaconvert.types.__list_of__integer_min32_max8182
    import capo_mediaconvert.types.dvb_nit_settings
    import capo_mediaconvert.types.dvb_sdt_settings
    import capo_mediaconvert.types.dvb_tdt_settings
    import capo_mediaconvert.types.m2ts_audio_buffer_model
    import capo_mediaconvert.types.m2ts_audio_duration
    import capo_mediaconvert.types.m2ts_buffer_model
    import capo_mediaconvert.types.m2ts_data_pts_control
    import capo_mediaconvert.types.m2ts_ebp_audio_interval
    import capo_mediaconvert.types.m2ts_ebp_placement
    import capo_mediaconvert.types.m2ts_es_rate_in_pes
    import capo_mediaconvert.types.m2ts_force_ts_video_ebp_order
    import capo_mediaconvert.types.m2ts_klv_metadata
    import capo_mediaconvert.types.m2ts_nielsen_id3
    import capo_mediaconvert.types.m2ts_pcr_control
    import capo_mediaconvert.types.m2ts_prevent_buffer_underflow
    import capo_mediaconvert.types.m2ts_rate_mode
    import capo_mediaconvert.types.m2ts_scte35_esam
    import capo_mediaconvert.types.m2ts_scte35_source
    import capo_mediaconvert.types.m2ts_segmentation_markers
    import capo_mediaconvert.types.m2ts_segmentation_style
    import capo_mediaconvert.types.ts_pts_offset


class M2tsSettings(TypedDict, closed=True):
    audio_buffer_model: NotRequired[
        "capo_mediaconvert.types.m2ts_audio_buffer_model.M2tsAudioBufferModel"
    ]
    """Selects between the DVB and ATSC buffer models for Dolby Digital audio."""
    audio_duration: NotRequired[
        "capo_mediaconvert.types.m2ts_audio_duration.M2tsAudioDuration"
    ]
    """Specify this setting only when your output will be consumed by a downstream repackaging workflow that is sensitive to very small duration differences between video and audio. For this situation, choose Match video duration. In all other cases, keep the default value, Default codec duration. When you choose Match video duration, MediaConvert pads the output audio streams with silence or trims them to ensure that the total duration of each audio stream is at least as long as the total duration of the video stream. After padding or trimming, the audio stream duration is no more than one frame longer than the video stream. MediaConvert applies audio padding or trimming only to the end of the last segment of the output. For unsegmented outputs, MediaConvert adds padding only to the end of the file. When you keep the default value, any minor discrepancies between audio and video duration will depend on your output audio codec."""
    audio_frames_per_pes: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """The number of audio frames to insert for each PES packet."""
    audio_pids: NotRequired[
        "capo_mediaconvert.types.__list_of__integer_min32_max8182.__listOf__integerMin32Max8182"
    ]
    """Specify the packet identifiers (PIDs) for any elementary audio streams you include in this output. Specify multiple PIDs as a JSON array. Default is the range 482-492."""
    audio_pts_offset_delta: NotRequired[
        "capo_mediaconvert.types.__integer_min_negative10000_max10000.__integerMinNegative10000Max10000"
    ]
    """Manually specify the difference in PTS offset that will be applied to the audio track, in seconds or milliseconds, when you set PTS offset to Seconds or Milliseconds. Enter an integer from -10000 to 10000. Leave blank to keep the default value 0."""
    bitrate: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max2147483647.__integerMin0Max2147483647"
    ]
    """Specify the output bitrate of the transport stream in bits per second. Setting to 0 lets the muxer automatically determine the appropriate bitrate. Other common values are 3750000, 7500000, and 15000000."""
    buffer_model: NotRequired[
        "capo_mediaconvert.types.m2ts_buffer_model.M2tsBufferModel"
    ]
    """Controls what buffer model to use for accurate interleaving. If set to MULTIPLEX, use multiplex buffer model. If set to NONE, this can lead to lower latency, but low-memory devices may not be able to play back the stream without interruptions."""
    data_pts_control: NotRequired[
        "capo_mediaconvert.types.m2ts_data_pts_control.M2tsDataPtsControl"
    ]
    """If you select ALIGN_TO_VIDEO, MediaConvert writes captions and data packets with Presentation Timestamp (PTS) values greater than or equal to the first video packet PTS (MediaConvert drops captions and data packets with lesser PTS values). Keep the default value to allow all PTS values."""
    dvb_nit_settings: NotRequired[
        "capo_mediaconvert.types.dvb_nit_settings.DvbNitSettings"
    ]
    """Use these settings to insert a DVB Network Information Table (NIT) in the transport stream of this output."""
    dvb_sdt_settings: NotRequired[
        "capo_mediaconvert.types.dvb_sdt_settings.DvbSdtSettings"
    ]
    """Use these settings to insert a DVB Service Description Table (SDT) in the transport stream of this output."""
    dvb_sub_pids: NotRequired[
        "capo_mediaconvert.types.__list_of__integer_min32_max8182.__listOf__integerMin32Max8182"
    ]
    """Specify the packet identifiers (PIDs) for DVB subtitle data included in this output. Specify multiple PIDs as a JSON array. Default is the range 460-479."""
    dvb_tdt_settings: NotRequired[
        "capo_mediaconvert.types.dvb_tdt_settings.DvbTdtSettings"
    ]
    """Use these settings to insert a DVB Time and Date Table (TDT) in the transport stream of this output."""
    dvb_teletext_pid: NotRequired[
        "capo_mediaconvert.types.__integer_min32_max8182.__integerMin32Max8182"
    ]
    """Specify the packet identifier (PID) for DVB teletext data you include in this output. Default is 499."""
    ebp_audio_interval: NotRequired[
        "capo_mediaconvert.types.m2ts_ebp_audio_interval.M2tsEbpAudioInterval"
    ]
    """When set to VIDEO_AND_FIXED_INTERVALS, audio EBP markers will be added to partitions 3 and 4. The interval between these additional markers will be fixed, and will be slightly shorter than the video EBP marker interval. When set to VIDEO_INTERVAL, these additional markers will not be inserted. Only applicable when EBP segmentation markers are is selected (segmentationMarkers is EBP or EBP_LEGACY)."""
    ebp_placement: NotRequired[
        "capo_mediaconvert.types.m2ts_ebp_placement.M2tsEbpPlacement"
    ]
    """Selects which PIDs to place EBP markers on. They can either be placed only on the video PID, or on both the video PID and all audio PIDs. Only applicable when EBP segmentation markers are is selected (segmentationMarkers is EBP or EBP_LEGACY)."""
    es_rate_in_pes: NotRequired[
        "capo_mediaconvert.types.m2ts_es_rate_in_pes.M2tsEsRateInPes"
    ]
    """Controls whether to include the ES Rate field in the PES header."""
    force_ts_video_ebp_order: NotRequired[
        "capo_mediaconvert.types.m2ts_force_ts_video_ebp_order.M2tsForceTsVideoEbpOrder"
    ]
    """Keep the default value unless you know that your audio EBP markers are incorrectly appearing before your video EBP markers. To correct this problem, set this value to Force."""
    fragment_time: NotRequired["capo_mediaconvert.types.__double_min0.__doubleMin0"]
    """The length, in seconds, of each fragment. Only used with EBP markers."""
    klv_metadata: NotRequired[
        "capo_mediaconvert.types.m2ts_klv_metadata.M2tsKlvMetadata"
    ]
    """To include key-length-value metadata in this output: Set KLV metadata insertion to Passthrough. MediaConvert reads KLV metadata present in your input and passes it through to the output transport stream. To exclude this KLV metadata: Set KLV metadata insertion to None or leave blank."""
    max_pcr_interval: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max500.__integerMin0Max500"
    ]
    """Specify the maximum time, in milliseconds, between Program Clock References (PCRs) inserted into the transport stream."""
    min_ebp_interval: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max10000.__integerMin0Max10000"
    ]
    """When set, enforces that Encoder Boundary Points do not come within the specified time interval of each other by looking ahead at input video. If another EBP is going to come in within the specified time interval, the current EBP is not emitted, and the segment is "stretched" to the next marker. The lookahead value does not add latency to the system. The Live Event must be configured elsewhere to create sufficient latency to make the lookahead accurate."""
    nielsen_id3: NotRequired["capo_mediaconvert.types.m2ts_nielsen_id3.M2tsNielsenId3"]
    """If INSERT, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output."""
    null_packet_bitrate: NotRequired[
        "capo_mediaconvert.types.__double_min0.__doubleMin0"
    ]
    """Value in bits per second of extra null packets to insert into the transport stream. This can be used if a downstream encryption system requires periodic null packets."""
    pat_interval: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max1000.__integerMin0Max1000"
    ]
    """The number of milliseconds between instances of this table in the output transport stream."""
    pcr_control: NotRequired["capo_mediaconvert.types.m2ts_pcr_control.M2tsPcrControl"]
    """When set to PCR_EVERY_PES_PACKET, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This is effective only when the PCR PID is the same as the video or audio elementary stream."""
    pcr_pid: NotRequired[
        "capo_mediaconvert.types.__integer_min32_max8182.__integerMin32Max8182"
    ]
    """Specify the packet identifier (PID) for the program clock reference (PCR) in this output. If you do not specify a value, the service will use the value for Video PID."""
    pmt_interval: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max1000.__integerMin0Max1000"
    ]
    """Specify the number of milliseconds between instances of the program map table (PMT) in the output transport stream."""
    pmt_pid: NotRequired[
        "capo_mediaconvert.types.__integer_min32_max8182.__integerMin32Max8182"
    ]
    """Specify the packet identifier (PID) for the program map table (PMT) itself. Default is 480."""
    prevent_buffer_underflow: NotRequired[
        "capo_mediaconvert.types.m2ts_prevent_buffer_underflow.M2tsPreventBufferUnderflow"
    ]
    """Specify whether MediaConvert automatically attempts to prevent decoder buffer underflows in your transport stream output. Use if you are seeing decoder buffer underflows in your output and are unable to increase your transport stream's bitrate. For most workflows: We recommend that you keep the default value, Disabled. To prevent decoder buffer underflows in your output, when possible: Choose Enabled. Note that if MediaConvert prevents a decoder buffer underflow in your output, output video quality is reduced and your job will take longer to complete."""
    private_metadata_pid: NotRequired[
        "capo_mediaconvert.types.__integer_min32_max8182.__integerMin32Max8182"
    ]
    """Specify the packet identifier (PID) of the private metadata stream. Default is 503."""
    program_number: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max65535.__integerMin0Max65535"
    ]
    """Use Program number to specify the program number used in the program map table (PMT) for this output. Default is 1. Program numbers and program map tables are parts of MPEG-2 transport stream containers, used for organizing data."""
    pts_offset: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max3600.__integerMin0Max3600"
    ]
    """Manually specify the initial PTS offset, in seconds, when you set PTS offset to Seconds. Enter an integer from 0 to 3600. Leave blank to keep the default value 2."""
    pts_offset_mode: NotRequired["capo_mediaconvert.types.ts_pts_offset.TsPtsOffset"]
    """Specify the initial presentation timestamp (PTS) offset for your transport stream output. To let MediaConvert automatically determine the initial PTS offset: Keep the default value, Auto. We recommend that you choose Auto for the widest player compatibility. The initial PTS will be at least two seconds and vary depending on your output's bitrate, HRD buffer size and HRD buffer initial fill percentage. To manually specify an initial PTS offset: Choose Seconds or Milliseconds. Then specify the number of seconds or milliseconds with PTS offset."""
    rate_mode: NotRequired["capo_mediaconvert.types.m2ts_rate_mode.M2tsRateMode"]
    """When set to CBR, inserts null packets into transport stream to fill specified bitrate. When set to VBR, the bitrate setting acts as the maximum bitrate, but the output will not be padded up to that bitrate."""
    scte35_esam: NotRequired["capo_mediaconvert.types.m2ts_scte35_esam.M2tsScte35Esam"]
    """Include this in your job settings to put SCTE-35 markers in your HLS and transport stream outputs at the insertion points that you specify in an ESAM XML document. Provide the document in the setting SCC XML."""
    scte35_pid: NotRequired[
        "capo_mediaconvert.types.__integer_min32_max8182.__integerMin32Max8182"
    ]
    """Specify the packet identifier (PID) of the SCTE-35 stream in the transport stream."""
    scte35_source: NotRequired[
        "capo_mediaconvert.types.m2ts_scte35_source.M2tsScte35Source"
    ]
    """For SCTE-35 markers from your input-- Choose Passthrough if you want SCTE-35 markers that appear in your input to also appear in this output. Choose None if you don't want SCTE-35 markers in this output. When your input is an HLS manifest, choose Manifest cues to pass through CUE markers in your HLS manifest as segment boundaries and SCTE-35 markers in this output at each EXT-X-CUE-OUT splice point in the input manifest. For SCTE-35 markers from an ESAM XML document-- Choose None. Also provide the ESAM XML as a string in the setting Signal processing notification XML. Also enable ESAM SCTE-35 (include the property scte35Esam)."""
    segmentation_markers: NotRequired[
        "capo_mediaconvert.types.m2ts_segmentation_markers.M2tsSegmentationMarkers"
    ]
    """Inserts segmentation markers at each segmentation_time period. rai_segstart sets the Random Access Indicator bit in the adaptation field. rai_adapt sets the RAI bit and adds the current timecode in the private data bytes. psi_segstart inserts PAT and PMT tables at the start of segments. ebp adds Encoder Boundary Point information to the adaptation field as per OpenCable specification OC-SP-EBP-I01-130118. ebp_legacy adds Encoder Boundary Point information to the adaptation field using a legacy proprietary format."""
    segmentation_style: NotRequired[
        "capo_mediaconvert.types.m2ts_segmentation_style.M2tsSegmentationStyle"
    ]
    """The segmentation style parameter controls how segmentation markers are inserted into the transport stream. With avails, it is possible that segments may be truncated, which can influence where future segmentation markers are inserted. When a segmentation style of "reset_cadence" is selected and a segment is truncated due to an avail, we will reset the segmentation cadence. This means the subsequent segment will have a duration of of $segmentation_time seconds. When a segmentation style of "maintain_cadence" is selected and a segment is truncated due to an avail, we will not reset the segmentation cadence. This means the subsequent segment will likely be truncated as well. However, all segments after that will have a duration of $segmentation_time seconds. Note that EBP lookahead is a slight exception to this rule."""
    segmentation_time: NotRequired["capo_mediaconvert.types.__double_min0.__doubleMin0"]
    """Specify the length, in seconds, of each segment. Required unless markers is set to _none_."""
    timed_metadata_pid: NotRequired[
        "capo_mediaconvert.types.__integer_min32_max8182.__integerMin32Max8182"
    ]
    """Packet Identifier (PID) of the ID3 metadata stream in the transport stream."""
    transport_stream_id: NotRequired[
        "capo_mediaconvert.types.__integer_min0_max65535.__integerMin0Max65535"
    ]
    """Specify the ID for the transport stream itself in the program map table for this output. Transport stream IDs and program map tables are parts of MPEG-2 transport stream containers, used for organizing data."""
    video_pid: NotRequired[
        "capo_mediaconvert.types.__integer_min32_max8182.__integerMin32Max8182"
    ]
    """Specify the packet identifier (PID) of the elementary video stream in the transport stream."""


# --- restJson1 ser/de ---
def serialize_json(value: M2tsSettings) -> dict:
    out: dict = {}
    if "audio_buffer_model" in value:
        import capo_mediaconvert.types.m2ts_audio_buffer_model

        out["audioBufferModel"] = (
            capo_mediaconvert.types.m2ts_audio_buffer_model.serialize_json(
                value["audio_buffer_model"]
            )
        )
    if "audio_duration" in value:
        import capo_mediaconvert.types.m2ts_audio_duration

        out["audioDuration"] = (
            capo_mediaconvert.types.m2ts_audio_duration.serialize_json(
                value["audio_duration"]
            )
        )
    if "audio_frames_per_pes" in value:
        out["audioFramesPerPes"] = value["audio_frames_per_pes"]
    if "audio_pids" in value:
        import capo_mediaconvert.types.__list_of__integer_min32_max8182

        out["audioPids"] = (
            capo_mediaconvert.types.__list_of__integer_min32_max8182.serialize_json(
                value["audio_pids"]
            )
        )
    if "audio_pts_offset_delta" in value:
        out["audioPtsOffsetDelta"] = value["audio_pts_offset_delta"]
    if "bitrate" in value:
        out["bitrate"] = value["bitrate"]
    if "buffer_model" in value:
        import capo_mediaconvert.types.m2ts_buffer_model

        out["bufferModel"] = capo_mediaconvert.types.m2ts_buffer_model.serialize_json(
            value["buffer_model"]
        )
    if "data_pts_control" in value:
        import capo_mediaconvert.types.m2ts_data_pts_control

        out["dataPTSControl"] = (
            capo_mediaconvert.types.m2ts_data_pts_control.serialize_json(
                value["data_pts_control"]
            )
        )
    if "dvb_nit_settings" in value:
        import capo_mediaconvert.types.dvb_nit_settings

        out["dvbNitSettings"] = capo_mediaconvert.types.dvb_nit_settings.serialize_json(
            value["dvb_nit_settings"]
        )
    if "dvb_sdt_settings" in value:
        import capo_mediaconvert.types.dvb_sdt_settings

        out["dvbSdtSettings"] = capo_mediaconvert.types.dvb_sdt_settings.serialize_json(
            value["dvb_sdt_settings"]
        )
    if "dvb_sub_pids" in value:
        import capo_mediaconvert.types.__list_of__integer_min32_max8182

        out["dvbSubPids"] = (
            capo_mediaconvert.types.__list_of__integer_min32_max8182.serialize_json(
                value["dvb_sub_pids"]
            )
        )
    if "dvb_tdt_settings" in value:
        import capo_mediaconvert.types.dvb_tdt_settings

        out["dvbTdtSettings"] = capo_mediaconvert.types.dvb_tdt_settings.serialize_json(
            value["dvb_tdt_settings"]
        )
    if "dvb_teletext_pid" in value:
        out["dvbTeletextPid"] = value["dvb_teletext_pid"]
    if "ebp_audio_interval" in value:
        import capo_mediaconvert.types.m2ts_ebp_audio_interval

        out["ebpAudioInterval"] = (
            capo_mediaconvert.types.m2ts_ebp_audio_interval.serialize_json(
                value["ebp_audio_interval"]
            )
        )
    if "ebp_placement" in value:
        import capo_mediaconvert.types.m2ts_ebp_placement

        out["ebpPlacement"] = capo_mediaconvert.types.m2ts_ebp_placement.serialize_json(
            value["ebp_placement"]
        )
    if "es_rate_in_pes" in value:
        import capo_mediaconvert.types.m2ts_es_rate_in_pes

        out["esRateInPes"] = capo_mediaconvert.types.m2ts_es_rate_in_pes.serialize_json(
            value["es_rate_in_pes"]
        )
    if "force_ts_video_ebp_order" in value:
        import capo_mediaconvert.types.m2ts_force_ts_video_ebp_order

        out["forceTsVideoEbpOrder"] = (
            capo_mediaconvert.types.m2ts_force_ts_video_ebp_order.serialize_json(
                value["force_ts_video_ebp_order"]
            )
        )
    if "fragment_time" in value:
        out["fragmentTime"] = (
            "NaN"
            if value["fragment_time"] != value["fragment_time"]
            else "Infinity"
            if value["fragment_time"] == float("inf")
            else "-Infinity"
            if value["fragment_time"] == float("-inf")
            else value["fragment_time"]
        )
    if "klv_metadata" in value:
        import capo_mediaconvert.types.m2ts_klv_metadata

        out["klvMetadata"] = capo_mediaconvert.types.m2ts_klv_metadata.serialize_json(
            value["klv_metadata"]
        )
    if "max_pcr_interval" in value:
        out["maxPcrInterval"] = value["max_pcr_interval"]
    if "min_ebp_interval" in value:
        out["minEbpInterval"] = value["min_ebp_interval"]
    if "nielsen_id3" in value:
        import capo_mediaconvert.types.m2ts_nielsen_id3

        out["nielsenId3"] = capo_mediaconvert.types.m2ts_nielsen_id3.serialize_json(
            value["nielsen_id3"]
        )
    if "null_packet_bitrate" in value:
        out["nullPacketBitrate"] = (
            "NaN"
            if value["null_packet_bitrate"] != value["null_packet_bitrate"]
            else "Infinity"
            if value["null_packet_bitrate"] == float("inf")
            else "-Infinity"
            if value["null_packet_bitrate"] == float("-inf")
            else value["null_packet_bitrate"]
        )
    if "pat_interval" in value:
        out["patInterval"] = value["pat_interval"]
    if "pcr_control" in value:
        import capo_mediaconvert.types.m2ts_pcr_control

        out["pcrControl"] = capo_mediaconvert.types.m2ts_pcr_control.serialize_json(
            value["pcr_control"]
        )
    if "pcr_pid" in value:
        out["pcrPid"] = value["pcr_pid"]
    if "pmt_interval" in value:
        out["pmtInterval"] = value["pmt_interval"]
    if "pmt_pid" in value:
        out["pmtPid"] = value["pmt_pid"]
    if "prevent_buffer_underflow" in value:
        import capo_mediaconvert.types.m2ts_prevent_buffer_underflow

        out["preventBufferUnderflow"] = (
            capo_mediaconvert.types.m2ts_prevent_buffer_underflow.serialize_json(
                value["prevent_buffer_underflow"]
            )
        )
    if "private_metadata_pid" in value:
        out["privateMetadataPid"] = value["private_metadata_pid"]
    if "program_number" in value:
        out["programNumber"] = value["program_number"]
    if "pts_offset" in value:
        out["ptsOffset"] = value["pts_offset"]
    if "pts_offset_mode" in value:
        import capo_mediaconvert.types.ts_pts_offset

        out["ptsOffsetMode"] = capo_mediaconvert.types.ts_pts_offset.serialize_json(
            value["pts_offset_mode"]
        )
    if "rate_mode" in value:
        import capo_mediaconvert.types.m2ts_rate_mode

        out["rateMode"] = capo_mediaconvert.types.m2ts_rate_mode.serialize_json(
            value["rate_mode"]
        )
    if "scte35_esam" in value:
        import capo_mediaconvert.types.m2ts_scte35_esam

        out["scte35Esam"] = capo_mediaconvert.types.m2ts_scte35_esam.serialize_json(
            value["scte35_esam"]
        )
    if "scte35_pid" in value:
        out["scte35Pid"] = value["scte35_pid"]
    if "scte35_source" in value:
        import capo_mediaconvert.types.m2ts_scte35_source

        out["scte35Source"] = capo_mediaconvert.types.m2ts_scte35_source.serialize_json(
            value["scte35_source"]
        )
    if "segmentation_markers" in value:
        import capo_mediaconvert.types.m2ts_segmentation_markers

        out["segmentationMarkers"] = (
            capo_mediaconvert.types.m2ts_segmentation_markers.serialize_json(
                value["segmentation_markers"]
            )
        )
    if "segmentation_style" in value:
        import capo_mediaconvert.types.m2ts_segmentation_style

        out["segmentationStyle"] = (
            capo_mediaconvert.types.m2ts_segmentation_style.serialize_json(
                value["segmentation_style"]
            )
        )
    if "segmentation_time" in value:
        out["segmentationTime"] = (
            "NaN"
            if value["segmentation_time"] != value["segmentation_time"]
            else "Infinity"
            if value["segmentation_time"] == float("inf")
            else "-Infinity"
            if value["segmentation_time"] == float("-inf")
            else value["segmentation_time"]
        )
    if "timed_metadata_pid" in value:
        out["timedMetadataPid"] = value["timed_metadata_pid"]
    if "transport_stream_id" in value:
        out["transportStreamId"] = value["transport_stream_id"]
    if "video_pid" in value:
        out["videoPid"] = value["video_pid"]
    return out


def deserialize_json(data: dict) -> M2tsSettings:
    out: M2tsSettings = {}  # type: ignore[typeddict-item]
    if data.get("audioBufferModel") is not None:
        import capo_mediaconvert.types.m2ts_audio_buffer_model

        out["audio_buffer_model"] = (
            capo_mediaconvert.types.m2ts_audio_buffer_model.deserialize_json(
                data["audioBufferModel"]
            )
        )
    if data.get("audioDuration") is not None:
        import capo_mediaconvert.types.m2ts_audio_duration

        out["audio_duration"] = (
            capo_mediaconvert.types.m2ts_audio_duration.deserialize_json(
                data["audioDuration"]
            )
        )
    if data.get("audioFramesPerPes") is not None:
        out["audio_frames_per_pes"] = data["audioFramesPerPes"]
    if data.get("audioPids") is not None:
        import capo_mediaconvert.types.__list_of__integer_min32_max8182

        out["audio_pids"] = (
            capo_mediaconvert.types.__list_of__integer_min32_max8182.deserialize_json(
                data["audioPids"]
            )
        )
    if data.get("audioPtsOffsetDelta") is not None:
        out["audio_pts_offset_delta"] = data["audioPtsOffsetDelta"]
    if data.get("bitrate") is not None:
        out["bitrate"] = data["bitrate"]
    if data.get("bufferModel") is not None:
        import capo_mediaconvert.types.m2ts_buffer_model

        out["buffer_model"] = (
            capo_mediaconvert.types.m2ts_buffer_model.deserialize_json(
                data["bufferModel"]
            )
        )
    if data.get("dataPTSControl") is not None:
        import capo_mediaconvert.types.m2ts_data_pts_control

        out["data_pts_control"] = (
            capo_mediaconvert.types.m2ts_data_pts_control.deserialize_json(
                data["dataPTSControl"]
            )
        )
    if data.get("dvbNitSettings") is not None:
        import capo_mediaconvert.types.dvb_nit_settings

        out["dvb_nit_settings"] = (
            capo_mediaconvert.types.dvb_nit_settings.deserialize_json(
                data["dvbNitSettings"]
            )
        )
    if data.get("dvbSdtSettings") is not None:
        import capo_mediaconvert.types.dvb_sdt_settings

        out["dvb_sdt_settings"] = (
            capo_mediaconvert.types.dvb_sdt_settings.deserialize_json(
                data["dvbSdtSettings"]
            )
        )
    if data.get("dvbSubPids") is not None:
        import capo_mediaconvert.types.__list_of__integer_min32_max8182

        out["dvb_sub_pids"] = (
            capo_mediaconvert.types.__list_of__integer_min32_max8182.deserialize_json(
                data["dvbSubPids"]
            )
        )
    if data.get("dvbTdtSettings") is not None:
        import capo_mediaconvert.types.dvb_tdt_settings

        out["dvb_tdt_settings"] = (
            capo_mediaconvert.types.dvb_tdt_settings.deserialize_json(
                data["dvbTdtSettings"]
            )
        )
    if data.get("dvbTeletextPid") is not None:
        out["dvb_teletext_pid"] = data["dvbTeletextPid"]
    if data.get("ebpAudioInterval") is not None:
        import capo_mediaconvert.types.m2ts_ebp_audio_interval

        out["ebp_audio_interval"] = (
            capo_mediaconvert.types.m2ts_ebp_audio_interval.deserialize_json(
                data["ebpAudioInterval"]
            )
        )
    if data.get("ebpPlacement") is not None:
        import capo_mediaconvert.types.m2ts_ebp_placement

        out["ebp_placement"] = (
            capo_mediaconvert.types.m2ts_ebp_placement.deserialize_json(
                data["ebpPlacement"]
            )
        )
    if data.get("esRateInPes") is not None:
        import capo_mediaconvert.types.m2ts_es_rate_in_pes

        out["es_rate_in_pes"] = (
            capo_mediaconvert.types.m2ts_es_rate_in_pes.deserialize_json(
                data["esRateInPes"]
            )
        )
    if data.get("forceTsVideoEbpOrder") is not None:
        import capo_mediaconvert.types.m2ts_force_ts_video_ebp_order

        out["force_ts_video_ebp_order"] = (
            capo_mediaconvert.types.m2ts_force_ts_video_ebp_order.deserialize_json(
                data["forceTsVideoEbpOrder"]
            )
        )
    if data.get("fragmentTime") is not None:
        out["fragment_time"] = float(data["fragmentTime"])
    if data.get("klvMetadata") is not None:
        import capo_mediaconvert.types.m2ts_klv_metadata

        out["klv_metadata"] = (
            capo_mediaconvert.types.m2ts_klv_metadata.deserialize_json(
                data["klvMetadata"]
            )
        )
    if data.get("maxPcrInterval") is not None:
        out["max_pcr_interval"] = data["maxPcrInterval"]
    if data.get("minEbpInterval") is not None:
        out["min_ebp_interval"] = data["minEbpInterval"]
    if data.get("nielsenId3") is not None:
        import capo_mediaconvert.types.m2ts_nielsen_id3

        out["nielsen_id3"] = capo_mediaconvert.types.m2ts_nielsen_id3.deserialize_json(
            data["nielsenId3"]
        )
    if data.get("nullPacketBitrate") is not None:
        out["null_packet_bitrate"] = float(data["nullPacketBitrate"])
    if data.get("patInterval") is not None:
        out["pat_interval"] = data["patInterval"]
    if data.get("pcrControl") is not None:
        import capo_mediaconvert.types.m2ts_pcr_control

        out["pcr_control"] = capo_mediaconvert.types.m2ts_pcr_control.deserialize_json(
            data["pcrControl"]
        )
    if data.get("pcrPid") is not None:
        out["pcr_pid"] = data["pcrPid"]
    if data.get("pmtInterval") is not None:
        out["pmt_interval"] = data["pmtInterval"]
    if data.get("pmtPid") is not None:
        out["pmt_pid"] = data["pmtPid"]
    if data.get("preventBufferUnderflow") is not None:
        import capo_mediaconvert.types.m2ts_prevent_buffer_underflow

        out["prevent_buffer_underflow"] = (
            capo_mediaconvert.types.m2ts_prevent_buffer_underflow.deserialize_json(
                data["preventBufferUnderflow"]
            )
        )
    if data.get("privateMetadataPid") is not None:
        out["private_metadata_pid"] = data["privateMetadataPid"]
    if data.get("programNumber") is not None:
        out["program_number"] = data["programNumber"]
    if data.get("ptsOffset") is not None:
        out["pts_offset"] = data["ptsOffset"]
    if data.get("ptsOffsetMode") is not None:
        import capo_mediaconvert.types.ts_pts_offset

        out["pts_offset_mode"] = capo_mediaconvert.types.ts_pts_offset.deserialize_json(
            data["ptsOffsetMode"]
        )
    if data.get("rateMode") is not None:
        import capo_mediaconvert.types.m2ts_rate_mode

        out["rate_mode"] = capo_mediaconvert.types.m2ts_rate_mode.deserialize_json(
            data["rateMode"]
        )
    if data.get("scte35Esam") is not None:
        import capo_mediaconvert.types.m2ts_scte35_esam

        out["scte35_esam"] = capo_mediaconvert.types.m2ts_scte35_esam.deserialize_json(
            data["scte35Esam"]
        )
    if data.get("scte35Pid") is not None:
        out["scte35_pid"] = data["scte35Pid"]
    if data.get("scte35Source") is not None:
        import capo_mediaconvert.types.m2ts_scte35_source

        out["scte35_source"] = (
            capo_mediaconvert.types.m2ts_scte35_source.deserialize_json(
                data["scte35Source"]
            )
        )
    if data.get("segmentationMarkers") is not None:
        import capo_mediaconvert.types.m2ts_segmentation_markers

        out["segmentation_markers"] = (
            capo_mediaconvert.types.m2ts_segmentation_markers.deserialize_json(
                data["segmentationMarkers"]
            )
        )
    if data.get("segmentationStyle") is not None:
        import capo_mediaconvert.types.m2ts_segmentation_style

        out["segmentation_style"] = (
            capo_mediaconvert.types.m2ts_segmentation_style.deserialize_json(
                data["segmentationStyle"]
            )
        )
    if data.get("segmentationTime") is not None:
        out["segmentation_time"] = float(data["segmentationTime"])
    if data.get("timedMetadataPid") is not None:
        out["timed_metadata_pid"] = data["timedMetadataPid"]
    if data.get("transportStreamId") is not None:
        out["transport_stream_id"] = data["transportStreamId"]
    if data.get("videoPid") is not None:
        out["video_pid"] = data["videoPid"]
    return out
