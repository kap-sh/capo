"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__double_min0
    import capo_medialive.types.__double_min0_max5000
    import capo_medialive.types.__double_min1
    import capo_medialive.types.__integer_min0
    import capo_medialive.types.__integer_min0_max500
    import capo_medialive.types.__integer_min0_max1000
    import capo_medialive.types.__integer_min0_max10000
    import capo_medialive.types.__integer_min0_max65535
    import capo_medialive.types.__string
    import capo_medialive.types.dvb_nit_settings
    import capo_medialive.types.dvb_sdt_settings
    import capo_medialive.types.dvb_tdt_settings
    import capo_medialive.types.m2ts_absent_input_audio_behavior
    import capo_medialive.types.m2ts_arib
    import capo_medialive.types.m2ts_arib_captions_pid_control
    import capo_medialive.types.m2ts_audio_buffer_model
    import capo_medialive.types.m2ts_audio_interval
    import capo_medialive.types.m2ts_audio_stream_type
    import capo_medialive.types.m2ts_buffer_model
    import capo_medialive.types.m2ts_cc_descriptor
    import capo_medialive.types.m2ts_ebif_control
    import capo_medialive.types.m2ts_ebp_placement
    import capo_medialive.types.m2ts_es_rate_in_pes
    import capo_medialive.types.m2ts_klv
    import capo_medialive.types.m2ts_nielsen_id3_behavior
    import capo_medialive.types.m2ts_pcr_control
    import capo_medialive.types.m2ts_rate_mode
    import capo_medialive.types.m2ts_scte35_control
    import capo_medialive.types.m2ts_segmentation_markers
    import capo_medialive.types.m2ts_segmentation_style
    import capo_medialive.types.m2ts_timed_metadata_behavior


class M2tsSettings(TypedDict, closed=True):
    absent_input_audio_behavior: NotRequired[
        "capo_medialive.types.m2ts_absent_input_audio_behavior.M2tsAbsentInputAudioBehavior"
    ]
    """When set to drop, output audio streams will be removed from the program if the selected input audio stream is removed from the input. This allows the output audio configuration to dynamically change based on input configuration. If this is set to encodeSilence, all output audio streams will output encoded silence when not connected to an active input stream."""
    arib: NotRequired["capo_medialive.types.m2ts_arib.M2tsArib"]
    """When set to enabled, uses ARIB-compliant field muxing and removes video descriptor."""
    arib_captions_pid: NotRequired["capo_medialive.types.__string.__string"]
    """Packet Identifier (PID) for ARIB Captions in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6)."""
    arib_captions_pid_control: NotRequired[
        "capo_medialive.types.m2ts_arib_captions_pid_control.M2tsAribCaptionsPidControl"
    ]
    """If set to auto, pid number used for ARIB Captions will be auto-selected from unused pids. If set to useConfigured, ARIB Captions will be on the configured pid number."""
    audio_buffer_model: NotRequired[
        "capo_medialive.types.m2ts_audio_buffer_model.M2tsAudioBufferModel"
    ]
    """When set to dvb, uses DVB buffer model for Dolby Digital audio. When set to atsc, the ATSC model is used."""
    audio_frames_per_pes: NotRequired[
        "capo_medialive.types.__integer_min0.__integerMin0"
    ]
    """The number of audio frames to insert for each PES packet."""
    audio_pids: NotRequired["capo_medialive.types.__string.__string"]
    """Packet Identifier (PID) of the elementary audio stream(s) in the transport stream. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6)."""
    audio_stream_type: NotRequired[
        "capo_medialive.types.m2ts_audio_stream_type.M2tsAudioStreamType"
    ]
    """When set to atsc, uses stream type = 0x81 for AC3 and stream type = 0x87 for EAC3. When set to dvb, uses stream type = 0x06."""
    bitrate: NotRequired["capo_medialive.types.__integer_min0.__integerMin0"]
    """The output bitrate of the transport stream in bits per second. Setting to 0 lets the muxer automatically determine the appropriate bitrate."""
    buffer_model: NotRequired["capo_medialive.types.m2ts_buffer_model.M2tsBufferModel"]
    """Controls the timing accuracy for output network traffic. Leave as MULTIPLEX to ensure accurate network packet timing. Or set to NONE, which might result in lower latency but will result in more variability in output network packet timing. This variability might cause interruptions, jitter, or bursty behavior in your playback or receiving devices."""
    cc_descriptor: NotRequired[
        "capo_medialive.types.m2ts_cc_descriptor.M2tsCcDescriptor"
    ]
    """When set to enabled, generates captionServiceDescriptor in PMT."""
    dvb_nit_settings: NotRequired[
        "capo_medialive.types.dvb_nit_settings.DvbNitSettings"
    ]
    """Inserts DVB Network Information Table (NIT) at the specified table repetition interval."""
    dvb_sdt_settings: NotRequired[
        "capo_medialive.types.dvb_sdt_settings.DvbSdtSettings"
    ]
    """Inserts DVB Service Description Table (SDT) at the specified table repetition interval."""
    dvb_sub_pids: NotRequired["capo_medialive.types.__string.__string"]
    """Packet Identifier (PID) for input source DVB Subtitle data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6)."""
    dvb_tdt_settings: NotRequired[
        "capo_medialive.types.dvb_tdt_settings.DvbTdtSettings"
    ]
    """Inserts DVB Time and Date Table (TDT) at the specified table repetition interval."""
    dvb_teletext_pid: NotRequired["capo_medialive.types.__string.__string"]
    """Packet Identifier (PID) for input source DVB Teletext data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6)."""
    ebif: NotRequired["capo_medialive.types.m2ts_ebif_control.M2tsEbifControl"]
    """If set to passthrough, passes any EBIF data from the input source to this output."""
    ebp_audio_interval: NotRequired[
        "capo_medialive.types.m2ts_audio_interval.M2tsAudioInterval"
    ]
    """When videoAndFixedIntervals is selected, audio EBP markers will be added to partitions 3 and 4. The interval between these additional markers will be fixed, and will be slightly shorter than the video EBP marker interval. Only available when EBP Cablelabs segmentation markers are selected. Partitions 1 and 2 will always follow the video interval."""
    ebp_lookahead_ms: NotRequired[
        "capo_medialive.types.__integer_min0_max10000.__integerMin0Max10000"
    ]
    """When set, enforces that Encoder Boundary Points do not come within the specified time interval of each other by looking ahead at input video. If another EBP is going to come in within the specified time interval, the current EBP is not emitted, and the segment is "stretched" to the next marker. The lookahead value does not add latency to the system. The Live Event must be configured elsewhere to create sufficient latency to make the lookahead accurate."""
    ebp_placement: NotRequired[
        "capo_medialive.types.m2ts_ebp_placement.M2tsEbpPlacement"
    ]
    """Controls placement of EBP on Audio PIDs. If set to videoAndAudioPids, EBP markers will be placed on the video PID and all audio PIDs. If set to videoPid, EBP markers will be placed on only the video PID."""
    ecm_pid: NotRequired["capo_medialive.types.__string.__string"]
    """This field is unused and deprecated."""
    es_rate_in_pes: NotRequired[
        "capo_medialive.types.m2ts_es_rate_in_pes.M2tsEsRateInPes"
    ]
    """Include or exclude the ES Rate field in the PES header."""
    etv_platform_pid: NotRequired["capo_medialive.types.__string.__string"]
    """Packet Identifier (PID) for input source ETV Platform data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6)."""
    etv_signal_pid: NotRequired["capo_medialive.types.__string.__string"]
    """Packet Identifier (PID) for input source ETV Signal data to this output. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6)."""
    fragment_time: NotRequired["capo_medialive.types.__double_min0.__doubleMin0"]
    """The length in seconds of each fragment. Only used with EBP markers."""
    klv: NotRequired["capo_medialive.types.m2ts_klv.M2tsKlv"]
    """If set to passthrough, passes any KLV data from the input source to this output."""
    klv_data_pids: NotRequired["capo_medialive.types.__string.__string"]
    """Packet Identifier (PID) for input source KLV data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6)."""
    nielsen_id3_behavior: NotRequired[
        "capo_medialive.types.m2ts_nielsen_id3_behavior.M2tsNielsenId3Behavior"
    ]
    """If set to passthrough, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output."""
    null_packet_bitrate: NotRequired["capo_medialive.types.__double_min0.__doubleMin0"]
    """Value in bits per second of extra null packets to insert into the transport stream. This can be used if a downstream encryption system requires periodic null packets."""
    pat_interval: NotRequired[
        "capo_medialive.types.__integer_min0_max1000.__integerMin0Max1000"
    ]
    """The number of milliseconds between instances of this table in the output transport stream. Valid values are 0, 10..1000."""
    pcr_control: NotRequired["capo_medialive.types.m2ts_pcr_control.M2tsPcrControl"]
    """When set to pcrEveryPesPacket, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream."""
    pcr_period: NotRequired[
        "capo_medialive.types.__integer_min0_max500.__integerMin0Max500"
    ]
    """Maximum time in milliseconds between Program Clock Reference (PCRs) inserted into the transport stream."""
    pcr_pid: NotRequired["capo_medialive.types.__string.__string"]
    """Packet Identifier (PID) of the Program Clock Reference (PCR) in the transport stream. When no value is given, the encoder will assign the same value as the Video PID. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6)."""
    pmt_interval: NotRequired[
        "capo_medialive.types.__integer_min0_max1000.__integerMin0Max1000"
    ]
    """The number of milliseconds between instances of this table in the output transport stream. Valid values are 0, 10..1000."""
    pmt_pid: NotRequired["capo_medialive.types.__string.__string"]
    """Packet Identifier (PID) for the Program Map Table (PMT) in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6)."""
    program_num: NotRequired[
        "capo_medialive.types.__integer_min0_max65535.__integerMin0Max65535"
    ]
    """The value of the program number field in the Program Map Table."""
    rate_mode: NotRequired["capo_medialive.types.m2ts_rate_mode.M2tsRateMode"]
    """When vbr, does not insert null packets into transport stream to fill specified bitrate. The bitrate setting acts as the maximum bitrate when vbr is set."""
    scte27_pids: NotRequired["capo_medialive.types.__string.__string"]
    """Packet Identifier (PID) for input source SCTE-27 data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6)."""
    scte35_control: NotRequired[
        "capo_medialive.types.m2ts_scte35_control.M2tsScte35Control"
    ]
    """SCTE-35 control. Option "none" indicates that a SCTE-35 marker will not be inserted, nor will an IDR be inserted at the SCTE-35 cue point, nor will the segment be segmented. Option "scte35WithoutIdr" indicates that a SCTE-35 marker will be inserted to indicate the cue point, but MediaLive will not insert an IDR on that frame nor will it introduce a new segment boundary there if it wasn't already going to be one (this option is required for use with downstream multiview bitstream stitching workflows). Option "passthrough" indicates that a SCTE-35 marker will be inserted to indicate the cue point, and an IDR will be inserted on that frame, and MediaLive itself will introduce a new segment boundary there."""
    scte35_pid: NotRequired["capo_medialive.types.__string.__string"]
    """Packet Identifier (PID) of the SCTE-35 stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6)."""
    segmentation_markers: NotRequired[
        "capo_medialive.types.m2ts_segmentation_markers.M2tsSegmentationMarkers"
    ]
    """Inserts segmentation markers at each segmentationTime period. raiSegstart sets the Random Access Indicator bit in the adaptation field. raiAdapt sets the RAI bit and adds the current timecode in the private data bytes. psiSegstart inserts PAT and PMT tables at the start of segments. ebp adds Encoder Boundary Point information to the adaptation field as per OpenCable specification OC-SP-EBP-I01-130118. ebpLegacy adds Encoder Boundary Point information to the adaptation field using a legacy proprietary format."""
    segmentation_style: NotRequired[
        "capo_medialive.types.m2ts_segmentation_style.M2tsSegmentationStyle"
    ]
    """The segmentation style parameter controls how segmentation markers are inserted into the transport stream. With avails, it is possible that segments may be truncated, which can influence where future segmentation markers are inserted. When a segmentation style of "resetCadence" is selected and a segment is truncated due to an avail, we will reset the segmentation cadence. This means the subsequent segment will have a duration of $segmentationTime seconds. When a segmentation style of "maintainCadence" is selected and a segment is truncated due to an avail, we will not reset the segmentation cadence. This means the subsequent segment will likely be truncated as well. However, all segments after that will have a duration of $segmentationTime seconds. Note that EBP lookahead is a slight exception to this rule."""
    segmentation_time: NotRequired["capo_medialive.types.__double_min1.__doubleMin1"]
    """The length in seconds of each segment. Required unless markers is set to _none_."""
    timed_metadata_behavior: NotRequired[
        "capo_medialive.types.m2ts_timed_metadata_behavior.M2tsTimedMetadataBehavior"
    ]
    """When set to passthrough, timed metadata will be passed through from input to output."""
    timed_metadata_pid: NotRequired["capo_medialive.types.__string.__string"]
    """Packet Identifier (PID) of the timed metadata stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6)."""
    transport_stream_id: NotRequired[
        "capo_medialive.types.__integer_min0_max65535.__integerMin0Max65535"
    ]
    """The value of the transport stream ID field in the Program Map Table."""
    video_pid: NotRequired["capo_medialive.types.__string.__string"]
    """Packet Identifier (PID) of the elementary video stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6)."""
    scte35_preroll_pullup_milliseconds: NotRequired[
        "capo_medialive.types.__double_min0_max5000.__doubleMin0Max5000"
    ]
    """Defines the amount SCTE-35 preroll will be increased (in milliseconds) on the output. Preroll is the amount of time between the presence of a SCTE-35 indication in a transport stream and the PTS of the video frame it references. Zero means don't add pullup (it doesn't mean set the preroll to zero). Negative pullup is not supported, which means that you can't make the preroll shorter. Be aware that latency in the output will increase by the pullup amount."""


# --- restJson1 ser/de ---
def serialize_json(value: M2tsSettings) -> dict:
    out: dict = {}
    if "absent_input_audio_behavior" in value:
        import capo_medialive.types.m2ts_absent_input_audio_behavior

        out["absentInputAudioBehavior"] = (
            capo_medialive.types.m2ts_absent_input_audio_behavior.serialize_json(
                value["absent_input_audio_behavior"]
            )
        )
    if "arib" in value:
        import capo_medialive.types.m2ts_arib

        out["arib"] = capo_medialive.types.m2ts_arib.serialize_json(value["arib"])
    if "arib_captions_pid" in value:
        out["aribCaptionsPid"] = value["arib_captions_pid"]
    if "arib_captions_pid_control" in value:
        import capo_medialive.types.m2ts_arib_captions_pid_control

        out["aribCaptionsPidControl"] = (
            capo_medialive.types.m2ts_arib_captions_pid_control.serialize_json(
                value["arib_captions_pid_control"]
            )
        )
    if "audio_buffer_model" in value:
        import capo_medialive.types.m2ts_audio_buffer_model

        out["audioBufferModel"] = (
            capo_medialive.types.m2ts_audio_buffer_model.serialize_json(
                value["audio_buffer_model"]
            )
        )
    if "audio_frames_per_pes" in value:
        out["audioFramesPerPes"] = value["audio_frames_per_pes"]
    if "audio_pids" in value:
        out["audioPids"] = value["audio_pids"]
    if "audio_stream_type" in value:
        import capo_medialive.types.m2ts_audio_stream_type

        out["audioStreamType"] = (
            capo_medialive.types.m2ts_audio_stream_type.serialize_json(
                value["audio_stream_type"]
            )
        )
    if "bitrate" in value:
        out["bitrate"] = value["bitrate"]
    if "buffer_model" in value:
        import capo_medialive.types.m2ts_buffer_model

        out["bufferModel"] = capo_medialive.types.m2ts_buffer_model.serialize_json(
            value["buffer_model"]
        )
    if "cc_descriptor" in value:
        import capo_medialive.types.m2ts_cc_descriptor

        out["ccDescriptor"] = capo_medialive.types.m2ts_cc_descriptor.serialize_json(
            value["cc_descriptor"]
        )
    if "dvb_nit_settings" in value:
        import capo_medialive.types.dvb_nit_settings

        out["dvbNitSettings"] = capo_medialive.types.dvb_nit_settings.serialize_json(
            value["dvb_nit_settings"]
        )
    if "dvb_sdt_settings" in value:
        import capo_medialive.types.dvb_sdt_settings

        out["dvbSdtSettings"] = capo_medialive.types.dvb_sdt_settings.serialize_json(
            value["dvb_sdt_settings"]
        )
    if "dvb_sub_pids" in value:
        out["dvbSubPids"] = value["dvb_sub_pids"]
    if "dvb_tdt_settings" in value:
        import capo_medialive.types.dvb_tdt_settings

        out["dvbTdtSettings"] = capo_medialive.types.dvb_tdt_settings.serialize_json(
            value["dvb_tdt_settings"]
        )
    if "dvb_teletext_pid" in value:
        out["dvbTeletextPid"] = value["dvb_teletext_pid"]
    if "ebif" in value:
        import capo_medialive.types.m2ts_ebif_control

        out["ebif"] = capo_medialive.types.m2ts_ebif_control.serialize_json(
            value["ebif"]
        )
    if "ebp_audio_interval" in value:
        import capo_medialive.types.m2ts_audio_interval

        out["ebpAudioInterval"] = (
            capo_medialive.types.m2ts_audio_interval.serialize_json(
                value["ebp_audio_interval"]
            )
        )
    if "ebp_lookahead_ms" in value:
        out["ebpLookaheadMs"] = value["ebp_lookahead_ms"]
    if "ebp_placement" in value:
        import capo_medialive.types.m2ts_ebp_placement

        out["ebpPlacement"] = capo_medialive.types.m2ts_ebp_placement.serialize_json(
            value["ebp_placement"]
        )
    if "ecm_pid" in value:
        out["ecmPid"] = value["ecm_pid"]
    if "es_rate_in_pes" in value:
        import capo_medialive.types.m2ts_es_rate_in_pes

        out["esRateInPes"] = capo_medialive.types.m2ts_es_rate_in_pes.serialize_json(
            value["es_rate_in_pes"]
        )
    if "etv_platform_pid" in value:
        out["etvPlatformPid"] = value["etv_platform_pid"]
    if "etv_signal_pid" in value:
        out["etvSignalPid"] = value["etv_signal_pid"]
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
    if "klv" in value:
        import capo_medialive.types.m2ts_klv

        out["klv"] = capo_medialive.types.m2ts_klv.serialize_json(value["klv"])
    if "klv_data_pids" in value:
        out["klvDataPids"] = value["klv_data_pids"]
    if "nielsen_id3_behavior" in value:
        import capo_medialive.types.m2ts_nielsen_id3_behavior

        out["nielsenId3Behavior"] = (
            capo_medialive.types.m2ts_nielsen_id3_behavior.serialize_json(
                value["nielsen_id3_behavior"]
            )
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
        import capo_medialive.types.m2ts_pcr_control

        out["pcrControl"] = capo_medialive.types.m2ts_pcr_control.serialize_json(
            value["pcr_control"]
        )
    if "pcr_period" in value:
        out["pcrPeriod"] = value["pcr_period"]
    if "pcr_pid" in value:
        out["pcrPid"] = value["pcr_pid"]
    if "pmt_interval" in value:
        out["pmtInterval"] = value["pmt_interval"]
    if "pmt_pid" in value:
        out["pmtPid"] = value["pmt_pid"]
    if "program_num" in value:
        out["programNum"] = value["program_num"]
    if "rate_mode" in value:
        import capo_medialive.types.m2ts_rate_mode

        out["rateMode"] = capo_medialive.types.m2ts_rate_mode.serialize_json(
            value["rate_mode"]
        )
    if "scte27_pids" in value:
        out["scte27Pids"] = value["scte27_pids"]
    if "scte35_control" in value:
        import capo_medialive.types.m2ts_scte35_control

        out["scte35Control"] = capo_medialive.types.m2ts_scte35_control.serialize_json(
            value["scte35_control"]
        )
    if "scte35_pid" in value:
        out["scte35Pid"] = value["scte35_pid"]
    if "segmentation_markers" in value:
        import capo_medialive.types.m2ts_segmentation_markers

        out["segmentationMarkers"] = (
            capo_medialive.types.m2ts_segmentation_markers.serialize_json(
                value["segmentation_markers"]
            )
        )
    if "segmentation_style" in value:
        import capo_medialive.types.m2ts_segmentation_style

        out["segmentationStyle"] = (
            capo_medialive.types.m2ts_segmentation_style.serialize_json(
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
    if "timed_metadata_behavior" in value:
        import capo_medialive.types.m2ts_timed_metadata_behavior

        out["timedMetadataBehavior"] = (
            capo_medialive.types.m2ts_timed_metadata_behavior.serialize_json(
                value["timed_metadata_behavior"]
            )
        )
    if "timed_metadata_pid" in value:
        out["timedMetadataPid"] = value["timed_metadata_pid"]
    if "transport_stream_id" in value:
        out["transportStreamId"] = value["transport_stream_id"]
    if "video_pid" in value:
        out["videoPid"] = value["video_pid"]
    if "scte35_preroll_pullup_milliseconds" in value:
        out["scte35PrerollPullupMilliseconds"] = (
            "NaN"
            if value["scte35_preroll_pullup_milliseconds"]
            != value["scte35_preroll_pullup_milliseconds"]
            else "Infinity"
            if value["scte35_preroll_pullup_milliseconds"] == float("inf")
            else "-Infinity"
            if value["scte35_preroll_pullup_milliseconds"] == float("-inf")
            else value["scte35_preroll_pullup_milliseconds"]
        )
    return out


def deserialize_json(data: dict) -> M2tsSettings:
    out: M2tsSettings = {}  # type: ignore[typeddict-item]
    if data.get("absentInputAudioBehavior") is not None:
        import capo_medialive.types.m2ts_absent_input_audio_behavior

        out["absent_input_audio_behavior"] = (
            capo_medialive.types.m2ts_absent_input_audio_behavior.deserialize_json(
                data["absentInputAudioBehavior"]
            )
        )
    if data.get("arib") is not None:
        import capo_medialive.types.m2ts_arib

        out["arib"] = capo_medialive.types.m2ts_arib.deserialize_json(data["arib"])
    if data.get("aribCaptionsPid") is not None:
        out["arib_captions_pid"] = data["aribCaptionsPid"]
    if data.get("aribCaptionsPidControl") is not None:
        import capo_medialive.types.m2ts_arib_captions_pid_control

        out["arib_captions_pid_control"] = (
            capo_medialive.types.m2ts_arib_captions_pid_control.deserialize_json(
                data["aribCaptionsPidControl"]
            )
        )
    if data.get("audioBufferModel") is not None:
        import capo_medialive.types.m2ts_audio_buffer_model

        out["audio_buffer_model"] = (
            capo_medialive.types.m2ts_audio_buffer_model.deserialize_json(
                data["audioBufferModel"]
            )
        )
    if data.get("audioFramesPerPes") is not None:
        out["audio_frames_per_pes"] = data["audioFramesPerPes"]
    if data.get("audioPids") is not None:
        out["audio_pids"] = data["audioPids"]
    if data.get("audioStreamType") is not None:
        import capo_medialive.types.m2ts_audio_stream_type

        out["audio_stream_type"] = (
            capo_medialive.types.m2ts_audio_stream_type.deserialize_json(
                data["audioStreamType"]
            )
        )
    if data.get("bitrate") is not None:
        out["bitrate"] = data["bitrate"]
    if data.get("bufferModel") is not None:
        import capo_medialive.types.m2ts_buffer_model

        out["buffer_model"] = capo_medialive.types.m2ts_buffer_model.deserialize_json(
            data["bufferModel"]
        )
    if data.get("ccDescriptor") is not None:
        import capo_medialive.types.m2ts_cc_descriptor

        out["cc_descriptor"] = capo_medialive.types.m2ts_cc_descriptor.deserialize_json(
            data["ccDescriptor"]
        )
    if data.get("dvbNitSettings") is not None:
        import capo_medialive.types.dvb_nit_settings

        out["dvb_nit_settings"] = (
            capo_medialive.types.dvb_nit_settings.deserialize_json(
                data["dvbNitSettings"]
            )
        )
    if data.get("dvbSdtSettings") is not None:
        import capo_medialive.types.dvb_sdt_settings

        out["dvb_sdt_settings"] = (
            capo_medialive.types.dvb_sdt_settings.deserialize_json(
                data["dvbSdtSettings"]
            )
        )
    if data.get("dvbSubPids") is not None:
        out["dvb_sub_pids"] = data["dvbSubPids"]
    if data.get("dvbTdtSettings") is not None:
        import capo_medialive.types.dvb_tdt_settings

        out["dvb_tdt_settings"] = (
            capo_medialive.types.dvb_tdt_settings.deserialize_json(
                data["dvbTdtSettings"]
            )
        )
    if data.get("dvbTeletextPid") is not None:
        out["dvb_teletext_pid"] = data["dvbTeletextPid"]
    if data.get("ebif") is not None:
        import capo_medialive.types.m2ts_ebif_control

        out["ebif"] = capo_medialive.types.m2ts_ebif_control.deserialize_json(
            data["ebif"]
        )
    if data.get("ebpAudioInterval") is not None:
        import capo_medialive.types.m2ts_audio_interval

        out["ebp_audio_interval"] = (
            capo_medialive.types.m2ts_audio_interval.deserialize_json(
                data["ebpAudioInterval"]
            )
        )
    if data.get("ebpLookaheadMs") is not None:
        out["ebp_lookahead_ms"] = data["ebpLookaheadMs"]
    if data.get("ebpPlacement") is not None:
        import capo_medialive.types.m2ts_ebp_placement

        out["ebp_placement"] = capo_medialive.types.m2ts_ebp_placement.deserialize_json(
            data["ebpPlacement"]
        )
    if data.get("ecmPid") is not None:
        out["ecm_pid"] = data["ecmPid"]
    if data.get("esRateInPes") is not None:
        import capo_medialive.types.m2ts_es_rate_in_pes

        out["es_rate_in_pes"] = (
            capo_medialive.types.m2ts_es_rate_in_pes.deserialize_json(
                data["esRateInPes"]
            )
        )
    if data.get("etvPlatformPid") is not None:
        out["etv_platform_pid"] = data["etvPlatformPid"]
    if data.get("etvSignalPid") is not None:
        out["etv_signal_pid"] = data["etvSignalPid"]
    if data.get("fragmentTime") is not None:
        out["fragment_time"] = float(data["fragmentTime"])
    if data.get("klv") is not None:
        import capo_medialive.types.m2ts_klv

        out["klv"] = capo_medialive.types.m2ts_klv.deserialize_json(data["klv"])
    if data.get("klvDataPids") is not None:
        out["klv_data_pids"] = data["klvDataPids"]
    if data.get("nielsenId3Behavior") is not None:
        import capo_medialive.types.m2ts_nielsen_id3_behavior

        out["nielsen_id3_behavior"] = (
            capo_medialive.types.m2ts_nielsen_id3_behavior.deserialize_json(
                data["nielsenId3Behavior"]
            )
        )
    if data.get("nullPacketBitrate") is not None:
        out["null_packet_bitrate"] = float(data["nullPacketBitrate"])
    if data.get("patInterval") is not None:
        out["pat_interval"] = data["patInterval"]
    if data.get("pcrControl") is not None:
        import capo_medialive.types.m2ts_pcr_control

        out["pcr_control"] = capo_medialive.types.m2ts_pcr_control.deserialize_json(
            data["pcrControl"]
        )
    if data.get("pcrPeriod") is not None:
        out["pcr_period"] = data["pcrPeriod"]
    if data.get("pcrPid") is not None:
        out["pcr_pid"] = data["pcrPid"]
    if data.get("pmtInterval") is not None:
        out["pmt_interval"] = data["pmtInterval"]
    if data.get("pmtPid") is not None:
        out["pmt_pid"] = data["pmtPid"]
    if data.get("programNum") is not None:
        out["program_num"] = data["programNum"]
    if data.get("rateMode") is not None:
        import capo_medialive.types.m2ts_rate_mode

        out["rate_mode"] = capo_medialive.types.m2ts_rate_mode.deserialize_json(
            data["rateMode"]
        )
    if data.get("scte27Pids") is not None:
        out["scte27_pids"] = data["scte27Pids"]
    if data.get("scte35Control") is not None:
        import capo_medialive.types.m2ts_scte35_control

        out["scte35_control"] = (
            capo_medialive.types.m2ts_scte35_control.deserialize_json(
                data["scte35Control"]
            )
        )
    if data.get("scte35Pid") is not None:
        out["scte35_pid"] = data["scte35Pid"]
    if data.get("segmentationMarkers") is not None:
        import capo_medialive.types.m2ts_segmentation_markers

        out["segmentation_markers"] = (
            capo_medialive.types.m2ts_segmentation_markers.deserialize_json(
                data["segmentationMarkers"]
            )
        )
    if data.get("segmentationStyle") is not None:
        import capo_medialive.types.m2ts_segmentation_style

        out["segmentation_style"] = (
            capo_medialive.types.m2ts_segmentation_style.deserialize_json(
                data["segmentationStyle"]
            )
        )
    if data.get("segmentationTime") is not None:
        out["segmentation_time"] = float(data["segmentationTime"])
    if data.get("timedMetadataBehavior") is not None:
        import capo_medialive.types.m2ts_timed_metadata_behavior

        out["timed_metadata_behavior"] = (
            capo_medialive.types.m2ts_timed_metadata_behavior.deserialize_json(
                data["timedMetadataBehavior"]
            )
        )
    if data.get("timedMetadataPid") is not None:
        out["timed_metadata_pid"] = data["timedMetadataPid"]
    if data.get("transportStreamId") is not None:
        out["transport_stream_id"] = data["transportStreamId"]
    if data.get("videoPid") is not None:
        out["video_pid"] = data["videoPid"]
    if data.get("scte35PrerollPullupMilliseconds") is not None:
        out["scte35_preroll_pullup_milliseconds"] = float(
            data["scte35PrerollPullupMilliseconds"]
        )
    return out
