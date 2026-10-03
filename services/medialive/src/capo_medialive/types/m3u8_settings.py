"""Generated from Smithy shape ``com.amazonaws.medialive#M3u8Settings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min0
    import capo_medialive.types.__integer_min0_max500
    import capo_medialive.types.__integer_min0_max1000
    import capo_medialive.types.__integer_min0_max65535
    import capo_medialive.types.__string
    import capo_medialive.types.m3u8_klv_behavior
    import capo_medialive.types.m3u8_nielsen_id3_behavior
    import capo_medialive.types.m3u8_pcr_control
    import capo_medialive.types.m3u8_scte35_behavior
    import capo_medialive.types.m3u8_timed_metadata_behavior


class M3u8Settings(TypedDict, closed=True):
    audio_frames_per_pes: NotRequired[
        "capo_medialive.types.__integer_min0.__integerMin0"
    ]
    """The number of audio frames to insert for each PES packet."""
    audio_pids: NotRequired["capo_medialive.types.__string.__string"]
    """Packet Identifier (PID) of the elementary audio stream(s) in the transport stream. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values."""
    ecm_pid: NotRequired["capo_medialive.types.__string.__string"]
    """This parameter is unused and deprecated."""
    nielsen_id3_behavior: NotRequired[
        "capo_medialive.types.m3u8_nielsen_id3_behavior.M3u8NielsenId3Behavior"
    ]
    """If set to passthrough, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output."""
    pat_interval: NotRequired[
        "capo_medialive.types.__integer_min0_max1000.__integerMin0Max1000"
    ]
    r"""The number of milliseconds between instances of this table in the output transport stream. A value of \"0\" writes out the PMT once per segment file."""
    pcr_control: NotRequired["capo_medialive.types.m3u8_pcr_control.M3u8PcrControl"]
    """When set to pcrEveryPesPacket, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream."""
    pcr_period: NotRequired[
        "capo_medialive.types.__integer_min0_max500.__integerMin0Max500"
    ]
    """Maximum time in milliseconds between Program Clock References (PCRs) inserted into the transport stream."""
    pcr_pid: NotRequired["capo_medialive.types.__string.__string"]
    """Packet Identifier (PID) of the Program Clock Reference (PCR) in the transport stream. When no value is given, the encoder will assign the same value as the Video PID. Can be entered as a decimal or hexadecimal value."""
    pmt_interval: NotRequired[
        "capo_medialive.types.__integer_min0_max1000.__integerMin0Max1000"
    ]
    r"""The number of milliseconds between instances of this table in the output transport stream. A value of \"0\" writes out the PMT once per segment file."""
    pmt_pid: NotRequired["capo_medialive.types.__string.__string"]
    """Packet Identifier (PID) for the Program Map Table (PMT) in the transport stream. Can be entered as a decimal or hexadecimal value."""
    program_num: NotRequired[
        "capo_medialive.types.__integer_min0_max65535.__integerMin0Max65535"
    ]
    """The value of the program number field in the Program Map Table."""
    scte35_behavior: NotRequired[
        "capo_medialive.types.m3u8_scte35_behavior.M3u8Scte35Behavior"
    ]
    """If set to passthrough, passes any SCTE-35 signals from the input source to this output."""
    scte35_pid: NotRequired["capo_medialive.types.__string.__string"]
    """Packet Identifier (PID) of the SCTE-35 stream in the transport stream. Can be entered as a decimal or hexadecimal value."""
    timed_metadata_behavior: NotRequired[
        "capo_medialive.types.m3u8_timed_metadata_behavior.M3u8TimedMetadataBehavior"
    ]
    """Set to PASSTHROUGH to enable ID3 metadata insertion. To include metadata, you configure other parameters in the output group or individual outputs, or you add an ID3 action to the channel schedule."""
    timed_metadata_pid: NotRequired["capo_medialive.types.__string.__string"]
    """Packet Identifier (PID) of the timed metadata stream in the transport stream. Can be entered as a decimal or hexadecimal value. Valid values are 32 (or 0x20)..8182 (or 0x1ff6)."""
    transport_stream_id: NotRequired[
        "capo_medialive.types.__integer_min0_max65535.__integerMin0Max65535"
    ]
    """The value of the transport stream ID field in the Program Map Table."""
    video_pid: NotRequired["capo_medialive.types.__string.__string"]
    """Packet Identifier (PID) of the elementary video stream in the transport stream. Can be entered as a decimal or hexadecimal value."""
    klv_behavior: NotRequired["capo_medialive.types.m3u8_klv_behavior.M3u8KlvBehavior"]
    """If set to passthrough, passes any KLV data from the input source to this output."""
    klv_data_pids: NotRequired["capo_medialive.types.__string.__string"]
    """Packet Identifier (PID) for input source KLV data to this output. Multiple values are accepted, and can be entered in ranges and/or by comma separation. Can be entered as decimal or hexadecimal values. Each PID specified must be in the range of 32 (or 0x20)..8182 (or 0x1ff6)."""


# --- restJson1 ser/de ---
def serialize_json(value: M3u8Settings) -> dict:
    out: dict = {}
    if "audio_frames_per_pes" in value:
        out["audioFramesPerPes"] = value["audio_frames_per_pes"]
    if "audio_pids" in value:
        out["audioPids"] = value["audio_pids"]
    if "ecm_pid" in value:
        out["ecmPid"] = value["ecm_pid"]
    if "nielsen_id3_behavior" in value:
        import capo_medialive.types.m3u8_nielsen_id3_behavior

        out["nielsenId3Behavior"] = (
            capo_medialive.types.m3u8_nielsen_id3_behavior.serialize_json(
                value["nielsen_id3_behavior"]
            )
        )
    if "pat_interval" in value:
        out["patInterval"] = value["pat_interval"]
    if "pcr_control" in value:
        import capo_medialive.types.m3u8_pcr_control

        out["pcrControl"] = capo_medialive.types.m3u8_pcr_control.serialize_json(
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
    if "scte35_behavior" in value:
        import capo_medialive.types.m3u8_scte35_behavior

        out["scte35Behavior"] = (
            capo_medialive.types.m3u8_scte35_behavior.serialize_json(
                value["scte35_behavior"]
            )
        )
    if "scte35_pid" in value:
        out["scte35Pid"] = value["scte35_pid"]
    if "timed_metadata_behavior" in value:
        import capo_medialive.types.m3u8_timed_metadata_behavior

        out["timedMetadataBehavior"] = (
            capo_medialive.types.m3u8_timed_metadata_behavior.serialize_json(
                value["timed_metadata_behavior"]
            )
        )
    if "timed_metadata_pid" in value:
        out["timedMetadataPid"] = value["timed_metadata_pid"]
    if "transport_stream_id" in value:
        out["transportStreamId"] = value["transport_stream_id"]
    if "video_pid" in value:
        out["videoPid"] = value["video_pid"]
    if "klv_behavior" in value:
        import capo_medialive.types.m3u8_klv_behavior

        out["klvBehavior"] = capo_medialive.types.m3u8_klv_behavior.serialize_json(
            value["klv_behavior"]
        )
    if "klv_data_pids" in value:
        out["klvDataPids"] = value["klv_data_pids"]
    return out


def deserialize_json(data: dict) -> M3u8Settings:
    out: M3u8Settings = {}  # type: ignore[typeddict-item]
    if data.get("audioFramesPerPes") is not None:
        out["audio_frames_per_pes"] = data["audioFramesPerPes"]
    if data.get("audioPids") is not None:
        out["audio_pids"] = data["audioPids"]
    if data.get("ecmPid") is not None:
        out["ecm_pid"] = data["ecmPid"]
    if data.get("nielsenId3Behavior") is not None:
        import capo_medialive.types.m3u8_nielsen_id3_behavior

        out["nielsen_id3_behavior"] = (
            capo_medialive.types.m3u8_nielsen_id3_behavior.deserialize_json(
                data["nielsenId3Behavior"]
            )
        )
    if data.get("patInterval") is not None:
        out["pat_interval"] = data["patInterval"]
    if data.get("pcrControl") is not None:
        import capo_medialive.types.m3u8_pcr_control

        out["pcr_control"] = capo_medialive.types.m3u8_pcr_control.deserialize_json(
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
    if data.get("scte35Behavior") is not None:
        import capo_medialive.types.m3u8_scte35_behavior

        out["scte35_behavior"] = (
            capo_medialive.types.m3u8_scte35_behavior.deserialize_json(
                data["scte35Behavior"]
            )
        )
    if data.get("scte35Pid") is not None:
        out["scte35_pid"] = data["scte35Pid"]
    if data.get("timedMetadataBehavior") is not None:
        import capo_medialive.types.m3u8_timed_metadata_behavior

        out["timed_metadata_behavior"] = (
            capo_medialive.types.m3u8_timed_metadata_behavior.deserialize_json(
                data["timedMetadataBehavior"]
            )
        )
    if data.get("timedMetadataPid") is not None:
        out["timed_metadata_pid"] = data["timedMetadataPid"]
    if data.get("transportStreamId") is not None:
        out["transport_stream_id"] = data["transportStreamId"]
    if data.get("videoPid") is not None:
        out["video_pid"] = data["videoPid"]
    if data.get("klvBehavior") is not None:
        import capo_medialive.types.m3u8_klv_behavior

        out["klv_behavior"] = capo_medialive.types.m3u8_klv_behavior.deserialize_json(
            data["klvBehavior"]
        )
    if data.get("klvDataPids") is not None:
        out["klv_data_pids"] = data["klvDataPids"]
    return out
