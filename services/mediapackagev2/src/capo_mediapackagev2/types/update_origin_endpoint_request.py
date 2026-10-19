"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#UpdateOriginEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackagev2.types.container_type
    import capo_mediapackagev2.types.create_dash_manifests
    import capo_mediapackagev2.types.create_hls_manifests
    import capo_mediapackagev2.types.create_low_latency_hls_manifests
    import capo_mediapackagev2.types.create_mss_manifests
    import capo_mediapackagev2.types.entity_tag
    import capo_mediapackagev2.types.force_endpoint_error_configuration
    import capo_mediapackagev2.types.resource_description
    import capo_mediapackagev2.types.resource_name
    import capo_mediapackagev2.types.segment
    import capo_mediapackagev2.types.stream_name_output_mode
    import capo_mediapackagev2.types.uri_separator


class UpdateOriginEndpointRequest(TypedDict, closed=True):
    channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>"""
    channel_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. </p>"""
    origin_endpoint_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel. </p>"""
    container_type: "capo_mediapackagev2.types.container_type.ContainerType"
    """<p>The type of container attached to this origin endpoint. A container type is a file format that encapsulates one or more media streams, such as audio and video, into a single file. </p>"""
    segment: NotRequired["capo_mediapackagev2.types.segment.Segment"]
    """<p>The segment configuration, including the segment name, duration, and other configuration values.</p>"""
    description: NotRequired[
        "capo_mediapackagev2.types.resource_description.ResourceDescription"
    ]
    """<p>Any descriptive information that you want to add to the origin endpoint for future identification purposes.</p>"""
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
    """<p>A list of Microsoft Smooth Streaming (MSS) manifest configurations to update for the origin endpoint. This replaces the existing MSS manifest configurations.</p>"""
    force_endpoint_error_configuration: NotRequired[
        "capo_mediapackagev2.types.force_endpoint_error_configuration.ForceEndpointErrorConfiguration"
    ]
    """<p>The failover settings for the endpoint.</p>"""
    uri_separator: NotRequired["capo_mediapackagev2.types.uri_separator.UriSeparator"]
    """<p>The separator character to use in generated URIs for this origin endpoint. This setting applies to all manifest types on the endpoint. If you don't specify a value in the update request, the current value is preserved.</p>"""
    stream_name_output_mode: NotRequired[
        "capo_mediapackagev2.types.stream_name_output_mode.StreamNameOutputMode"
    ]
    """<p>The output mode for stream names in egress manifests. If you provide a value, it must match the current value. You can't change the stream name output mode after you create the endpoint.</p>"""
    e_tag: NotRequired["capo_mediapackagev2.types.entity_tag.EntityTag"]
    """<p>The expected current Entity Tag (ETag) for the resource. If the specified ETag does not match the resource's current entity tag, the update request will be rejected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOriginEndpointRequest) -> dict:
    out: dict = {}
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
    return out


def deserialize_json(data: dict) -> UpdateOriginEndpointRequest:
    out: UpdateOriginEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("ContainerType") is not None:
        import capo_mediapackagev2.types.container_type

        out["container_type"] = (
            capo_mediapackagev2.types.container_type.deserialize_json(
                data["ContainerType"]
            )
        )
    else:
        import typing

        out["container_type"] = typing.cast(
            "capo_mediapackagev2.types.container_type.ContainerType", ""
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
    return out
