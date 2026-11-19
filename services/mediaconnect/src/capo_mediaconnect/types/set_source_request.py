"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SetSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.__list_of_media_stream_source_configuration_request
    import capo_mediaconnect.types.__map_of_string
    import capo_mediaconnect.types.encryption
    import capo_mediaconnect.types.flow_transit_encryption
    import capo_mediaconnect.types.ndi_source_settings
    import capo_mediaconnect.types.protocol
    import capo_mediaconnect.types.set_gateway_bridge_source_request
    import capo_mediaconnect.types.set_rtmp_push_source_settings
    import capo_mediaconnect.types.state


class SetSourceRequest(TypedDict, closed=True):
    decryption: NotRequired["capo_mediaconnect.types.encryption.Encryption"]
    """<p> The type of encryption that is used on the content ingested from this source. Allowable encryption types: static-key.</p>"""
    description: NotRequired["str"]
    """<p> A description for the source. This value is not used or seen outside of the current MediaConnect account.</p>"""
    entitlement_arn: NotRequired["str"]
    """<p> The ARN of the entitlement that allows you to subscribe to this flow. The entitlement is set by the flow originator, and the ARN is generated as part of the originator's flow.</p>"""
    ingest_port: NotRequired["int"]
    """<p> The port that the flow will be listening on for incoming content.</p>"""
    max_bitrate: NotRequired["int"]
    """<p> The smoothing max bitrate (in bps) for RIST, RTP, and RTP-FEC streams.</p>"""
    max_latency: NotRequired["int"]
    """<p> The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.</p>"""
    max_sync_buffer: NotRequired["int"]
    """<p> The size of the buffer (in milliseconds) to use to sync incoming source data.</p>"""
    media_stream_source_configurations: NotRequired[
        "capo_mediaconnect.types.__list_of_media_stream_source_configuration_request.__listOfMediaStreamSourceConfigurationRequest"
    ]
    """<p> The media streams that are associated with the source, and the parameters for those associations.</p>"""
    min_latency: NotRequired["int"]
    """<p> The minimum latency in milliseconds for SRT-based streams. In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the sender’s minimum latency and the receiver’s minimum latency.</p>"""
    name: NotRequired["str"]
    """<p> The name of the source.</p>"""
    protocol: NotRequired["capo_mediaconnect.types.protocol.Protocol"]
    """<p> The protocol that is used by the source.</p> <note> <p>Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.</p> </note>"""
    sender_control_port: NotRequired["int"]
    """<p> The port that the flow uses to send outbound requests to initiate connection with the sender.</p>"""
    sender_ip_address: NotRequired["str"]
    """<p> The IP address that the flow communicates with to initiate connection with the sender.</p>"""
    source_listener_address: NotRequired["str"]
    """<p> Source IP or domain name for SRT-caller protocol.</p>"""
    source_listener_port: NotRequired["int"]
    """<p> Source port for SRT-caller protocol.</p>"""
    stream_id: NotRequired["str"]
    """<p> The stream ID that you want to use for this transport. This parameter applies only to Zixi and SRT caller-based streams.</p>"""
    vpc_interface_name: NotRequired["str"]
    """<p> The name of the VPC interface to use for this source.</p>"""
    whitelist_cidr: NotRequired["str"]
    """<p> The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.</p>"""
    gateway_bridge_source: NotRequired[
        "capo_mediaconnect.types.set_gateway_bridge_source_request.SetGatewayBridgeSourceRequest"
    ]
    """<p> The source configuration for cloud flows receiving a stream from a bridge.</p>"""
    ndi_source_settings: NotRequired[
        "capo_mediaconnect.types.ndi_source_settings.NdiSourceSettings"
    ]
    """<p> The settings for the NDI® source. This includes the exact name of the upstream NDI sender that you want to connect to your source. </p>"""
    source_tags: NotRequired["capo_mediaconnect.types.__map_of_string.__mapOfString"]
    """<p> The key-value pairs that can be used to tag and organize the source. </p>"""
    router_integration_state: NotRequired["capo_mediaconnect.types.state.State"]
    """<p>Indicates whether to enable or disable router integration when setting a flow source.</p>"""
    router_integration_transit_decryption: NotRequired[
        "capo_mediaconnect.types.flow_transit_encryption.FlowTransitEncryption"
    ]
    """<p>The decryption configuration for the flow source when router integration is enabled. Specifies how the source content should be decrypted when router integration is used.</p>"""
    rtmp_push_settings: NotRequired[
        "capo_mediaconnect.types.set_rtmp_push_source_settings.SetRtmpPushSourceSettings"
    ]
    """<p>The settings for the RTMP (Real-Time Messaging Protocol) source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SetSourceRequest) -> dict:
    out: dict = {}
    if "decryption" in value:
        import capo_mediaconnect.types.encryption

        out["decryption"] = capo_mediaconnect.types.encryption.serialize_json(
            value["decryption"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "entitlement_arn" in value:
        out["entitlementArn"] = value["entitlement_arn"]
    if "ingest_port" in value:
        out["ingestPort"] = value["ingest_port"]
    if "max_bitrate" in value:
        out["maxBitrate"] = value["max_bitrate"]
    if "max_latency" in value:
        out["maxLatency"] = value["max_latency"]
    if "max_sync_buffer" in value:
        out["maxSyncBuffer"] = value["max_sync_buffer"]
    if "media_stream_source_configurations" in value:
        import capo_mediaconnect.types.__list_of_media_stream_source_configuration_request

        out["mediaStreamSourceConfigurations"] = (
            capo_mediaconnect.types.__list_of_media_stream_source_configuration_request.serialize_json(
                value["media_stream_source_configurations"]
            )
        )
    if "min_latency" in value:
        out["minLatency"] = value["min_latency"]
    if "name" in value:
        out["name"] = value["name"]
    if "protocol" in value:
        import capo_mediaconnect.types.protocol

        out["protocol"] = capo_mediaconnect.types.protocol.serialize_json(
            value["protocol"]
        )
    if "sender_control_port" in value:
        out["senderControlPort"] = value["sender_control_port"]
    if "sender_ip_address" in value:
        out["senderIpAddress"] = value["sender_ip_address"]
    if "source_listener_address" in value:
        out["sourceListenerAddress"] = value["source_listener_address"]
    if "source_listener_port" in value:
        out["sourceListenerPort"] = value["source_listener_port"]
    if "stream_id" in value:
        out["streamId"] = value["stream_id"]
    if "vpc_interface_name" in value:
        out["vpcInterfaceName"] = value["vpc_interface_name"]
    if "whitelist_cidr" in value:
        out["whitelistCidr"] = value["whitelist_cidr"]
    if "gateway_bridge_source" in value:
        import capo_mediaconnect.types.set_gateway_bridge_source_request

        out["gatewayBridgeSource"] = (
            capo_mediaconnect.types.set_gateway_bridge_source_request.serialize_json(
                value["gateway_bridge_source"]
            )
        )
    if "ndi_source_settings" in value:
        import capo_mediaconnect.types.ndi_source_settings

        out["ndiSourceSettings"] = (
            capo_mediaconnect.types.ndi_source_settings.serialize_json(
                value["ndi_source_settings"]
            )
        )
    if "source_tags" in value:
        import capo_mediaconnect.types.__map_of_string

        out["sourceTags"] = capo_mediaconnect.types.__map_of_string.serialize_json(
            value["source_tags"]
        )
    if "router_integration_state" in value:
        import capo_mediaconnect.types.state

        out["routerIntegrationState"] = capo_mediaconnect.types.state.serialize_json(
            value["router_integration_state"]
        )
    if "router_integration_transit_decryption" in value:
        import capo_mediaconnect.types.flow_transit_encryption

        out["routerIntegrationTransitDecryption"] = (
            capo_mediaconnect.types.flow_transit_encryption.serialize_json(
                value["router_integration_transit_decryption"]
            )
        )
    if "rtmp_push_settings" in value:
        import capo_mediaconnect.types.set_rtmp_push_source_settings

        out["rtmpPushSettings"] = (
            capo_mediaconnect.types.set_rtmp_push_source_settings.serialize_json(
                value["rtmp_push_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> SetSourceRequest:
    out: SetSourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("decryption") is not None:
        import capo_mediaconnect.types.encryption

        out["decryption"] = capo_mediaconnect.types.encryption.deserialize_json(
            data["decryption"]
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("entitlementArn") is not None:
        out["entitlement_arn"] = data["entitlementArn"]
    if data.get("ingestPort") is not None:
        out["ingest_port"] = data["ingestPort"]
    if data.get("maxBitrate") is not None:
        out["max_bitrate"] = data["maxBitrate"]
    if data.get("maxLatency") is not None:
        out["max_latency"] = data["maxLatency"]
    if data.get("maxSyncBuffer") is not None:
        out["max_sync_buffer"] = data["maxSyncBuffer"]
    if data.get("mediaStreamSourceConfigurations") is not None:
        import capo_mediaconnect.types.__list_of_media_stream_source_configuration_request

        out["media_stream_source_configurations"] = (
            capo_mediaconnect.types.__list_of_media_stream_source_configuration_request.deserialize_json(
                data["mediaStreamSourceConfigurations"]
            )
        )
    if data.get("minLatency") is not None:
        out["min_latency"] = data["minLatency"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("protocol") is not None:
        import capo_mediaconnect.types.protocol

        out["protocol"] = capo_mediaconnect.types.protocol.deserialize_json(
            data["protocol"]
        )
    if data.get("senderControlPort") is not None:
        out["sender_control_port"] = data["senderControlPort"]
    if data.get("senderIpAddress") is not None:
        out["sender_ip_address"] = data["senderIpAddress"]
    if data.get("sourceListenerAddress") is not None:
        out["source_listener_address"] = data["sourceListenerAddress"]
    if data.get("sourceListenerPort") is not None:
        out["source_listener_port"] = data["sourceListenerPort"]
    if data.get("streamId") is not None:
        out["stream_id"] = data["streamId"]
    if data.get("vpcInterfaceName") is not None:
        out["vpc_interface_name"] = data["vpcInterfaceName"]
    if data.get("whitelistCidr") is not None:
        out["whitelist_cidr"] = data["whitelistCidr"]
    if data.get("gatewayBridgeSource") is not None:
        import capo_mediaconnect.types.set_gateway_bridge_source_request

        out["gateway_bridge_source"] = (
            capo_mediaconnect.types.set_gateway_bridge_source_request.deserialize_json(
                data["gatewayBridgeSource"]
            )
        )
    if data.get("ndiSourceSettings") is not None:
        import capo_mediaconnect.types.ndi_source_settings

        out["ndi_source_settings"] = (
            capo_mediaconnect.types.ndi_source_settings.deserialize_json(
                data["ndiSourceSettings"]
            )
        )
    if data.get("sourceTags") is not None:
        import capo_mediaconnect.types.__map_of_string

        out["source_tags"] = capo_mediaconnect.types.__map_of_string.deserialize_json(
            data["sourceTags"]
        )
    if data.get("routerIntegrationState") is not None:
        import capo_mediaconnect.types.state

        out["router_integration_state"] = (
            capo_mediaconnect.types.state.deserialize_json(
                data["routerIntegrationState"]
            )
        )
    if data.get("routerIntegrationTransitDecryption") is not None:
        import capo_mediaconnect.types.flow_transit_encryption

        out["router_integration_transit_decryption"] = (
            capo_mediaconnect.types.flow_transit_encryption.deserialize_json(
                data["routerIntegrationTransitDecryption"]
            )
        )
    if data.get("rtmpPushSettings") is not None:
        import capo_mediaconnect.types.set_rtmp_push_source_settings

        out["rtmp_push_settings"] = (
            capo_mediaconnect.types.set_rtmp_push_source_settings.deserialize_json(
                data["rtmpPushSettings"]
            )
        )
    return out
