"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#CreateOriginEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediapackagev2.types.container_type
    import capo_mediapackagev2.types.create_dash_manifests
    import capo_mediapackagev2.types.create_hls_manifests
    import capo_mediapackagev2.types.create_low_latency_hls_manifests
    import capo_mediapackagev2.types.create_mss_manifests
    import capo_mediapackagev2.types.force_endpoint_error_configuration
    import capo_mediapackagev2.types.idempotency_token
    import capo_mediapackagev2.types.resource_description
    import capo_mediapackagev2.types.resource_name
    import capo_mediapackagev2.types.segment
    import capo_mediapackagev2.types.stream_name_output_mode
    import capo_mediapackagev2.types.tag_map
    import capo_mediapackagev2.types.uri_separator


class CreateOriginEndpointRequest(TypedDict, closed=True):
    channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>"""
    channel_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. </p>"""
    origin_endpoint_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and must be unique for your account in the AWS Region and channel. You can't use spaces in the name. You can't change the name after you create the endpoint.</p>"""
    container_type: "capo_mediapackagev2.types.container_type.ContainerType"
    """<p>The type of container to attach to this origin endpoint. A container type is a file format that encapsulates one or more media streams, such as audio and video, into a single file. You can't change the container type after you create the endpoint.</p>"""
    segment: NotRequired["capo_mediapackagev2.types.segment.Segment"]
    """<p>The segment configuration, including the segment name, duration, and other configuration values.</p>"""
    client_token: NotRequired[
        "capo_mediapackagev2.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive token that you provide to ensure the idempotency of the request.</p>"""
    description: NotRequired[
        "capo_mediapackagev2.types.resource_description.ResourceDescription"
    ]
    """<p>Enter any descriptive text that helps you to identify the origin endpoint.</p>"""
    startover_window_seconds: NotRequired["int"]
    """<p>The size of the window (in seconds) to create a window of the live stream that's available for on-demand viewing. Viewers can start-over or catch-up on content that falls within the window. The maximum startover window is 1,209,600 seconds (14 days).</p>"""
    hls_manifests: NotRequired[
        "capo_mediapackagev2.types.create_hls_manifests.CreateHlsManifests"
    ]
    """<p>An HTTP live streaming (HLS) manifest configuration.</p>"""
    low_latency_hls_manifests: NotRequired[
        "capo_mediapackagev2.types.create_low_latency_hls_manifests.CreateLowLatencyHlsManifests"
    ]
    """<p>A low-latency HLS manifest configuration.</p>"""
    dash_manifests: NotRequired[
        "capo_mediapackagev2.types.create_dash_manifests.CreateDashManifests"
    ]
    """<p>A DASH manifest configuration.</p>"""
    mss_manifests: NotRequired[
        "capo_mediapackagev2.types.create_mss_manifests.CreateMssManifests"
    ]
    """<p>A list of Microsoft Smooth Streaming (MSS) manifest configurations for the origin endpoint. You can configure multiple MSS manifests to provide different streaming experiences or to support different client requirements.</p>"""
    force_endpoint_error_configuration: NotRequired[
        "capo_mediapackagev2.types.force_endpoint_error_configuration.ForceEndpointErrorConfiguration"
    ]
    """<p>The failover settings for the endpoint.</p>"""
    uri_separator: NotRequired["capo_mediapackagev2.types.uri_separator.UriSeparator"]
    """<p>The separator character to use in generated URIs for this origin endpoint. This setting applies to all manifest types on the endpoint. If you don't specify a value, the default is <code>UNDERSCORE</code>.</p>"""
    stream_name_output_mode: NotRequired[
        "capo_mediapackagev2.types.stream_name_output_mode.StreamNameOutputMode"
    ]
    """<p>The output mode for stream names in egress manifests. This setting is valid only when the associated channel's <code>InputType</code> is <code>HLS</code>. You can't change the stream name output mode after you create the endpoint.</p> <p> <code>INDEX</code> uses numeric indices for stream names (for example, 1, 2, 3). <code>PASSTHROUGH_NAME</code> uses the stream names from the input manifest. If you don't specify a value, the default is <code>INDEX</code>.</p>"""
    tags: NotRequired["capo_mediapackagev2.types.tag_map.TagMap"]
    """<p>A comma-separated list of tag key:value pairs that you define. For example:</p> <p> <code>"Key1": "Value1",</code> </p> <p> <code>"Key2": "Value2"</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOriginEndpointRequest) -> dict:
    out: dict = {}
    out["OriginEndpointName"] = value["origin_endpoint_name"]
    import capo_mediapackagev2.types.container_type

    out["ContainerType"] = capo_mediapackagev2.types.container_type.serialize_json(
        value["container_type"]
    )
    if "segment" in value:
        import capo_mediapackagev2.types.segment

        out["Segment"] = capo_mediapackagev2.types.segment.serialize_json(
            value["segment"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "startover_window_seconds" in value:
        out["StartoverWindowSeconds"] = value["startover_window_seconds"]
    if "hls_manifests" in value:
        import capo_mediapackagev2.types.create_hls_manifests

        out["HlsManifests"] = (
            capo_mediapackagev2.types.create_hls_manifests.serialize_json(
                value["hls_manifests"]
            )
        )
    if "low_latency_hls_manifests" in value:
        import capo_mediapackagev2.types.create_low_latency_hls_manifests

        out["LowLatencyHlsManifests"] = (
            capo_mediapackagev2.types.create_low_latency_hls_manifests.serialize_json(
                value["low_latency_hls_manifests"]
            )
        )
    if "dash_manifests" in value:
        import capo_mediapackagev2.types.create_dash_manifests

        out["DashManifests"] = (
            capo_mediapackagev2.types.create_dash_manifests.serialize_json(
                value["dash_manifests"]
            )
        )
    if "mss_manifests" in value:
        import capo_mediapackagev2.types.create_mss_manifests

        out["MssManifests"] = (
            capo_mediapackagev2.types.create_mss_manifests.serialize_json(
                value["mss_manifests"]
            )
        )
    if "force_endpoint_error_configuration" in value:
        import capo_mediapackagev2.types.force_endpoint_error_configuration

        out["ForceEndpointErrorConfiguration"] = (
            capo_mediapackagev2.types.force_endpoint_error_configuration.serialize_json(
                value["force_endpoint_error_configuration"]
            )
        )
    if "uri_separator" in value:
        import capo_mediapackagev2.types.uri_separator

        out["UriSeparator"] = capo_mediapackagev2.types.uri_separator.serialize_json(
            value["uri_separator"]
        )
    if "stream_name_output_mode" in value:
        import capo_mediapackagev2.types.stream_name_output_mode

        out["StreamNameOutputMode"] = (
            capo_mediapackagev2.types.stream_name_output_mode.serialize_json(
                value["stream_name_output_mode"]
            )
        )
    if "tags" in value:
        import capo_mediapackagev2.types.tag_map

        out["Tags"] = capo_mediapackagev2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateOriginEndpointRequest:
    out: CreateOriginEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("OriginEndpointName") is not None:
        out["origin_endpoint_name"] = data["OriginEndpointName"]
    else:
        raise DeserializationError(
            "CreateOriginEndpointRequest.origin_endpoint_name required"
        )
    if data.get("ContainerType") is not None:
        import capo_mediapackagev2.types.container_type

        out["container_type"] = (
            capo_mediapackagev2.types.container_type.deserialize_json(
                data["ContainerType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateOriginEndpointRequest.container_type required"
        )
    if data.get("Segment") is not None:
        import capo_mediapackagev2.types.segment

        out["segment"] = capo_mediapackagev2.types.segment.deserialize_json(
            data["Segment"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("StartoverWindowSeconds") is not None:
        out["startover_window_seconds"] = data["StartoverWindowSeconds"]
    if data.get("HlsManifests") is not None:
        import capo_mediapackagev2.types.create_hls_manifests

        out["hls_manifests"] = (
            capo_mediapackagev2.types.create_hls_manifests.deserialize_json(
                data["HlsManifests"]
            )
        )
    if data.get("LowLatencyHlsManifests") is not None:
        import capo_mediapackagev2.types.create_low_latency_hls_manifests

        out["low_latency_hls_manifests"] = (
            capo_mediapackagev2.types.create_low_latency_hls_manifests.deserialize_json(
                data["LowLatencyHlsManifests"]
            )
        )
    if data.get("DashManifests") is not None:
        import capo_mediapackagev2.types.create_dash_manifests

        out["dash_manifests"] = (
            capo_mediapackagev2.types.create_dash_manifests.deserialize_json(
                data["DashManifests"]
            )
        )
    if data.get("MssManifests") is not None:
        import capo_mediapackagev2.types.create_mss_manifests

        out["mss_manifests"] = (
            capo_mediapackagev2.types.create_mss_manifests.deserialize_json(
                data["MssManifests"]
            )
        )
    if data.get("ForceEndpointErrorConfiguration") is not None:
        import capo_mediapackagev2.types.force_endpoint_error_configuration

        out["force_endpoint_error_configuration"] = (
            capo_mediapackagev2.types.force_endpoint_error_configuration.deserialize_json(
                data["ForceEndpointErrorConfiguration"]
            )
        )
    if data.get("UriSeparator") is not None:
        import capo_mediapackagev2.types.uri_separator

        out["uri_separator"] = capo_mediapackagev2.types.uri_separator.deserialize_json(
            data["UriSeparator"]
        )
    if data.get("StreamNameOutputMode") is not None:
        import capo_mediapackagev2.types.stream_name_output_mode

        out["stream_name_output_mode"] = (
            capo_mediapackagev2.types.stream_name_output_mode.deserialize_json(
                data["StreamNameOutputMode"]
            )
        )
    if data.get("Tags") is not None:
        import capo_mediapackagev2.types.tag_map

        out["tags"] = capo_mediapackagev2.types.tag_map.deserialize_json(data["Tags"])
    return out
