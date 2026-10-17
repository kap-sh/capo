"""Generated from Smithy shape ``com.amazonaws.mediaconnect#Transport``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.__list_of_string
    import capo_mediaconnect.types.ndi_output_timecode_source
    import capo_mediaconnect.types.ndi_source_settings
    import capo_mediaconnect.types.protocol


class Transport(TypedDict, closed=True):
    cidr_allow_list: NotRequired[
        "capo_mediaconnect.types.__list_of_string.__listOfString"
    ]
    """<p> The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16</p>"""
    max_bitrate: NotRequired["int"]
    """<p> The smoothing max bitrate (in bps) for RIST, RTP, and RTP-FEC streams.</p>"""
    max_latency: NotRequired["int"]
    """<p> The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.</p>"""
    max_sync_buffer: NotRequired["int"]
    """<p> The size of the buffer (in milliseconds) to use to sync incoming source data.</p>"""
    min_latency: NotRequired["int"]
    """<p> The minimum latency in milliseconds for SRT-based streams. In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the sender’s minimum latency and the receiver’s minimum latency.</p>"""
    protocol: NotRequired["capo_mediaconnect.types.protocol.Protocol"]
    """<p> The protocol that is used by the source or output.</p> <note> <p>Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.</p> </note>"""
    remote_id: NotRequired["str"]
    """<p> The remote ID for the Zixi-pull stream.</p>"""
    sender_control_port: NotRequired["int"]
    """<p> The port that the flow uses to send outbound requests to initiate connection with the sender.</p>"""
    sender_ip_address: NotRequired["str"]
    """<p> The IP address that the flow communicates with to initiate connection with the sender.</p>"""
    smoothing_latency: NotRequired["int"]
    """<p> The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.</p>"""
    source_listener_address: NotRequired["str"]
    """<p> Source IP or domain name for SRT-caller protocol.</p>"""
    source_listener_port: NotRequired["int"]
    """<p> Source port for SRT-caller protocol.</p>"""
    stream_id: NotRequired["str"]
    """<p> The stream ID that you want to use for this transport. This parameter applies only to Zixi and SRT caller-based streams.</p>"""
    ndi_speed_hq_quality: NotRequired["int"]
    """<p>A quality setting for the NDI Speed HQ encoder. </p>"""
    ndi_program_name: NotRequired["str"]
    """<p>A suffix for the name of the NDI® sender that the flow creates. If a custom name isn't specified, MediaConnect uses the output name. </p>"""
    ndi_source_settings: NotRequired[
        "capo_mediaconnect.types.ndi_source_settings.NdiSourceSettings"
    ]
    """<p> The settings for the NDI source. This includes the exact name of the upstream NDI sender that you want to connect to your source. </p>"""
    ndi_output_timecode_source: NotRequired[
        "capo_mediaconnect.types.ndi_output_timecode_source.NdiOutputTimecodeSource"
    ]
    """<p>The timecode source for NDI output frames. For NDI outputs, this field is always present and defaults to <code>EMBEDDED_TIMECODE</code>.</p> <ul> <li> <p> <code>EMBEDDED_TIMECODE</code> - Preserves timecodes from the input transport stream. The timecodes must be embedded in the video stream as SEI timing messages. If no embedded timecode is detected, MediaConnect uses the UTC system time instead.</p> </li> <li> <p> <code>UTC_SYSTEM_TIME</code> - Generates timecodes based on the system clock time when each frame is sent.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: Transport) -> dict:
    out: dict = {}
    if "cidr_allow_list" in value:
        import capo_mediaconnect.types.__list_of_string

        out["cidrAllowList"] = capo_mediaconnect.types.__list_of_string.serialize_json(
            value["cidr_allow_list"]
        )
    if "max_bitrate" in value:
        out["maxBitrate"] = value["max_bitrate"]
    if "max_latency" in value:
        out["maxLatency"] = value["max_latency"]
    if "max_sync_buffer" in value:
        out["maxSyncBuffer"] = value["max_sync_buffer"]
    if "min_latency" in value:
        out["minLatency"] = value["min_latency"]
    if "protocol" in value:
        import capo_mediaconnect.types.protocol

        out["protocol"] = capo_mediaconnect.types.protocol.serialize_json(
            value["protocol"]
        )
    if "remote_id" in value:
        out["remoteId"] = value["remote_id"]
    if "sender_control_port" in value:
        out["senderControlPort"] = value["sender_control_port"]
    if "sender_ip_address" in value:
        out["senderIpAddress"] = value["sender_ip_address"]
    if "smoothing_latency" in value:
        out["smoothingLatency"] = value["smoothing_latency"]
    if "source_listener_address" in value:
        out["sourceListenerAddress"] = value["source_listener_address"]
    if "source_listener_port" in value:
        out["sourceListenerPort"] = value["source_listener_port"]
    if "stream_id" in value:
        out["streamId"] = value["stream_id"]
    if "ndi_speed_hq_quality" in value:
        out["ndiSpeedHqQuality"] = value["ndi_speed_hq_quality"]
    if "ndi_program_name" in value:
        out["ndiProgramName"] = value["ndi_program_name"]
    if "ndi_source_settings" in value:
        import capo_mediaconnect.types.ndi_source_settings

        out["ndiSourceSettings"] = (
            capo_mediaconnect.types.ndi_source_settings.serialize_json(
                value["ndi_source_settings"]
            )
        )
    if "ndi_output_timecode_source" in value:
        import capo_mediaconnect.types.ndi_output_timecode_source

        out["ndiOutputTimecodeSource"] = (
            capo_mediaconnect.types.ndi_output_timecode_source.serialize_json(
                value["ndi_output_timecode_source"]
            )
        )
    return out


def deserialize_json(data: dict) -> Transport:
    out: Transport = {}  # type: ignore[typeddict-item]
    if data.get("cidrAllowList") is not None:
        import capo_mediaconnect.types.__list_of_string

        out["cidr_allow_list"] = (
            capo_mediaconnect.types.__list_of_string.deserialize_json(
                data["cidrAllowList"]
            )
        )
    if data.get("maxBitrate") is not None:
        out["max_bitrate"] = data["maxBitrate"]
    if data.get("maxLatency") is not None:
        out["max_latency"] = data["maxLatency"]
    if data.get("maxSyncBuffer") is not None:
        out["max_sync_buffer"] = data["maxSyncBuffer"]
    if data.get("minLatency") is not None:
        out["min_latency"] = data["minLatency"]
    if data.get("protocol") is not None:
        import capo_mediaconnect.types.protocol

        out["protocol"] = capo_mediaconnect.types.protocol.deserialize_json(
            data["protocol"]
        )
    if data.get("remoteId") is not None:
        out["remote_id"] = data["remoteId"]
    if data.get("senderControlPort") is not None:
        out["sender_control_port"] = data["senderControlPort"]
    if data.get("senderIpAddress") is not None:
        out["sender_ip_address"] = data["senderIpAddress"]
    if data.get("smoothingLatency") is not None:
        out["smoothing_latency"] = data["smoothingLatency"]
    if data.get("sourceListenerAddress") is not None:
        out["source_listener_address"] = data["sourceListenerAddress"]
    if data.get("sourceListenerPort") is not None:
        out["source_listener_port"] = data["sourceListenerPort"]
    if data.get("streamId") is not None:
        out["stream_id"] = data["streamId"]
    if data.get("ndiSpeedHqQuality") is not None:
        out["ndi_speed_hq_quality"] = data["ndiSpeedHqQuality"]
    if data.get("ndiProgramName") is not None:
        out["ndi_program_name"] = data["ndiProgramName"]
    if data.get("ndiSourceSettings") is not None:
        import capo_mediaconnect.types.ndi_source_settings

        out["ndi_source_settings"] = (
            capo_mediaconnect.types.ndi_source_settings.deserialize_json(
                data["ndiSourceSettings"]
            )
        )
    if data.get("ndiOutputTimecodeSource") is not None:
        import capo_mediaconnect.types.ndi_output_timecode_source

        out["ndi_output_timecode_source"] = (
            capo_mediaconnect.types.ndi_output_timecode_source.deserialize_json(
                data["ndiOutputTimecodeSource"]
            )
        )
    return out
