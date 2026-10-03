"""Generated from Smithy shape ``com.amazonaws.medialive#MultiplexM2tsSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__double_min0_max5000
    import capo_medialive.types.__integer_min0
    import capo_medialive.types.__integer_min0_max500
    import capo_medialive.types.m2ts_absent_input_audio_behavior
    import capo_medialive.types.m2ts_arib
    import capo_medialive.types.m2ts_audio_buffer_model
    import capo_medialive.types.m2ts_audio_stream_type
    import capo_medialive.types.m2ts_cc_descriptor
    import capo_medialive.types.m2ts_ebif_control
    import capo_medialive.types.m2ts_es_rate_in_pes
    import capo_medialive.types.m2ts_klv
    import capo_medialive.types.m2ts_nielsen_id3_behavior
    import capo_medialive.types.m2ts_pcr_control
    import capo_medialive.types.m2ts_scte35_control


class MultiplexM2tsSettings(TypedDict, closed=True):
    absent_input_audio_behavior: NotRequired[
        "capo_medialive.types.m2ts_absent_input_audio_behavior.M2tsAbsentInputAudioBehavior"
    ]
    """When set to drop, output audio streams will be removed from the program if the selected input audio stream is removed from the input. This allows the output audio configuration to dynamically change based on input configuration. If this is set to encodeSilence, all output audio streams will output encoded silence when not connected to an active input stream."""
    arib: NotRequired["capo_medialive.types.m2ts_arib.M2tsArib"]
    """When set to enabled, uses ARIB-compliant field muxing and removes video descriptor."""
    audio_buffer_model: NotRequired[
        "capo_medialive.types.m2ts_audio_buffer_model.M2tsAudioBufferModel"
    ]
    """When set to dvb, uses DVB buffer model for Dolby Digital audio. When set to atsc, the ATSC model is used."""
    audio_frames_per_pes: NotRequired[
        "capo_medialive.types.__integer_min0.__integerMin0"
    ]
    """The number of audio frames to insert for each PES packet."""
    audio_stream_type: NotRequired[
        "capo_medialive.types.m2ts_audio_stream_type.M2tsAudioStreamType"
    ]
    """When set to atsc, uses stream type = 0x81 for AC3 and stream type = 0x87 for EAC3. When set to dvb, uses stream type = 0x06."""
    cc_descriptor: NotRequired[
        "capo_medialive.types.m2ts_cc_descriptor.M2tsCcDescriptor"
    ]
    """When set to enabled, generates captionServiceDescriptor in PMT."""
    ebif: NotRequired["capo_medialive.types.m2ts_ebif_control.M2tsEbifControl"]
    """If set to passthrough, passes any EBIF data from the input source to this output."""
    es_rate_in_pes: NotRequired[
        "capo_medialive.types.m2ts_es_rate_in_pes.M2tsEsRateInPes"
    ]
    """Include or exclude the ES Rate field in the PES header."""
    klv: NotRequired["capo_medialive.types.m2ts_klv.M2tsKlv"]
    """If set to passthrough, passes any KLV data from the input source to this output."""
    nielsen_id3_behavior: NotRequired[
        "capo_medialive.types.m2ts_nielsen_id3_behavior.M2tsNielsenId3Behavior"
    ]
    """If set to passthrough, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output."""
    pcr_control: NotRequired["capo_medialive.types.m2ts_pcr_control.M2tsPcrControl"]
    """When set to pcrEveryPesPacket, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream."""
    pcr_period: NotRequired[
        "capo_medialive.types.__integer_min0_max500.__integerMin0Max500"
    ]
    """Maximum time in milliseconds between Program Clock Reference (PCRs) inserted into the transport stream."""
    scte35_control: NotRequired[
        "capo_medialive.types.m2ts_scte35_control.M2tsScte35Control"
    ]
    """SCTE-35 control. Option "none" indicates that a SCTE-35 marker will not be inserted, nor will an IDR be inserted at the SCTE-35 cue point, nor will the segment be segmented. Option "scte35WithoutIdr" indicates that a SCTE-35 marker will be inserted to indicate the cue point, but MediaLive will not insert an IDR on that frame nor will it introduce a new segment boundary there if it wasn't already going to be one (this option is required for use with downstream multiview bitstream stitching workflows). Option "passthrough" indicates that a SCTE-35 marker will be inserted to indicate the cue point, and an IDR will be inserted on that frame, and MediaLive itself will introduce a new segment boundary there."""
    scte35_preroll_pullup_milliseconds: NotRequired[
        "capo_medialive.types.__double_min0_max5000.__doubleMin0Max5000"
    ]
    """Defines the amount SCTE-35 preroll will be increased (in milliseconds) on the output. Preroll is the amount of time between the presence of a SCTE-35 indication in a transport stream and the PTS of the video frame it references. Zero means don't add pullup (it doesn't mean set the preroll to zero). Negative pullup is not supported, which means that you can't make the preroll shorter. Be aware that latency in the output will increase by the pullup amount."""


# --- restJson1 ser/de ---
def serialize_json(value: MultiplexM2tsSettings) -> dict:
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
    if "audio_buffer_model" in value:
        import capo_medialive.types.m2ts_audio_buffer_model

        out["audioBufferModel"] = (
            capo_medialive.types.m2ts_audio_buffer_model.serialize_json(
                value["audio_buffer_model"]
            )
        )
    if "audio_frames_per_pes" in value:
        out["audioFramesPerPes"] = value["audio_frames_per_pes"]
    if "audio_stream_type" in value:
        import capo_medialive.types.m2ts_audio_stream_type

        out["audioStreamType"] = (
            capo_medialive.types.m2ts_audio_stream_type.serialize_json(
                value["audio_stream_type"]
            )
        )
    if "cc_descriptor" in value:
        import capo_medialive.types.m2ts_cc_descriptor

        out["ccDescriptor"] = capo_medialive.types.m2ts_cc_descriptor.serialize_json(
            value["cc_descriptor"]
        )
    if "ebif" in value:
        import capo_medialive.types.m2ts_ebif_control

        out["ebif"] = capo_medialive.types.m2ts_ebif_control.serialize_json(
            value["ebif"]
        )
    if "es_rate_in_pes" in value:
        import capo_medialive.types.m2ts_es_rate_in_pes

        out["esRateInPes"] = capo_medialive.types.m2ts_es_rate_in_pes.serialize_json(
            value["es_rate_in_pes"]
        )
    if "klv" in value:
        import capo_medialive.types.m2ts_klv

        out["klv"] = capo_medialive.types.m2ts_klv.serialize_json(value["klv"])
    if "nielsen_id3_behavior" in value:
        import capo_medialive.types.m2ts_nielsen_id3_behavior

        out["nielsenId3Behavior"] = (
            capo_medialive.types.m2ts_nielsen_id3_behavior.serialize_json(
                value["nielsen_id3_behavior"]
            )
        )
    if "pcr_control" in value:
        import capo_medialive.types.m2ts_pcr_control

        out["pcrControl"] = capo_medialive.types.m2ts_pcr_control.serialize_json(
            value["pcr_control"]
        )
    if "pcr_period" in value:
        out["pcrPeriod"] = value["pcr_period"]
    if "scte35_control" in value:
        import capo_medialive.types.m2ts_scte35_control

        out["scte35Control"] = capo_medialive.types.m2ts_scte35_control.serialize_json(
            value["scte35_control"]
        )
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


def deserialize_json(data: dict) -> MultiplexM2tsSettings:
    out: MultiplexM2tsSettings = {}  # type: ignore[typeddict-item]
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
    if data.get("audioBufferModel") is not None:
        import capo_medialive.types.m2ts_audio_buffer_model

        out["audio_buffer_model"] = (
            capo_medialive.types.m2ts_audio_buffer_model.deserialize_json(
                data["audioBufferModel"]
            )
        )
    if data.get("audioFramesPerPes") is not None:
        out["audio_frames_per_pes"] = data["audioFramesPerPes"]
    if data.get("audioStreamType") is not None:
        import capo_medialive.types.m2ts_audio_stream_type

        out["audio_stream_type"] = (
            capo_medialive.types.m2ts_audio_stream_type.deserialize_json(
                data["audioStreamType"]
            )
        )
    if data.get("ccDescriptor") is not None:
        import capo_medialive.types.m2ts_cc_descriptor

        out["cc_descriptor"] = capo_medialive.types.m2ts_cc_descriptor.deserialize_json(
            data["ccDescriptor"]
        )
    if data.get("ebif") is not None:
        import capo_medialive.types.m2ts_ebif_control

        out["ebif"] = capo_medialive.types.m2ts_ebif_control.deserialize_json(
            data["ebif"]
        )
    if data.get("esRateInPes") is not None:
        import capo_medialive.types.m2ts_es_rate_in_pes

        out["es_rate_in_pes"] = (
            capo_medialive.types.m2ts_es_rate_in_pes.deserialize_json(
                data["esRateInPes"]
            )
        )
    if data.get("klv") is not None:
        import capo_medialive.types.m2ts_klv

        out["klv"] = capo_medialive.types.m2ts_klv.deserialize_json(data["klv"])
    if data.get("nielsenId3Behavior") is not None:
        import capo_medialive.types.m2ts_nielsen_id3_behavior

        out["nielsen_id3_behavior"] = (
            capo_medialive.types.m2ts_nielsen_id3_behavior.deserialize_json(
                data["nielsenId3Behavior"]
            )
        )
    if data.get("pcrControl") is not None:
        import capo_medialive.types.m2ts_pcr_control

        out["pcr_control"] = capo_medialive.types.m2ts_pcr_control.deserialize_json(
            data["pcrControl"]
        )
    if data.get("pcrPeriod") is not None:
        out["pcr_period"] = data["pcrPeriod"]
    if data.get("scte35Control") is not None:
        import capo_medialive.types.m2ts_scte35_control

        out["scte35_control"] = (
            capo_medialive.types.m2ts_scte35_control.deserialize_json(
                data["scte35Control"]
            )
        )
    if data.get("scte35PrerollPullupMilliseconds") is not None:
        out["scte35_preroll_pullup_milliseconds"] = float(
            data["scte35PrerollPullupMilliseconds"]
        )
    return out
