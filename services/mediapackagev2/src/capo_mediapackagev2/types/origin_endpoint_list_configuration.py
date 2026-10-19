"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#OriginEndpointListConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mediapackagev2.types.container_type
    import capo_mediapackagev2.types.force_endpoint_error_configuration
    import capo_mediapackagev2.types.list_dash_manifests
    import capo_mediapackagev2.types.list_hls_manifests
    import capo_mediapackagev2.types.list_low_latency_hls_manifests
    import capo_mediapackagev2.types.list_mss_manifests
    import capo_mediapackagev2.types.resource_description
    import capo_mediapackagev2.types.resource_name
    import capo_mediapackagev2.types.stream_name_output_mode
    import capo_mediapackagev2.types.uri_separator


class OriginEndpointListConfiguration(TypedDict, closed=True):
    arn: "str"
    """<p>The Amazon Resource Name (ARN) associated with the resource.</p>"""
    channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>"""
    channel_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. </p>"""
    origin_endpoint_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel. </p>"""
    container_type: "capo_mediapackagev2.types.container_type.ContainerType"
    """<p>The type of container attached to this origin endpoint. A container type is a file format that encapsulates one or more media streams, such as audio and video, into a single file. </p>"""
    description: NotRequired[
        "capo_mediapackagev2.types.resource_description.ResourceDescription"
    ]
    """<p>Any descriptive information that you want to add to the origin endpoint for future identification purposes.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time the origin endpoint was created.</p>"""
    modified_at: NotRequired["datetime.datetime"]
    """<p>The date and time the origin endpoint was modified.</p>"""
    hls_manifests: NotRequired[
        "capo_mediapackagev2.types.list_hls_manifests.ListHlsManifests"
    ]
    """<p>An HTTP live streaming (HLS) manifest configuration.</p>"""
    low_latency_hls_manifests: NotRequired[
        "capo_mediapackagev2.types.list_low_latency_hls_manifests.ListLowLatencyHlsManifests"
    ]
    """<p>A low-latency HLS manifest configuration.</p>"""
    dash_manifests: NotRequired[
        "capo_mediapackagev2.types.list_dash_manifests.ListDashManifests"
    ]
    """<p>A DASH manifest configuration.</p>"""
    mss_manifests: NotRequired[
        "capo_mediapackagev2.types.list_mss_manifests.ListMssManifests"
    ]
    """<p>A list of Microsoft Smooth Streaming (MSS) manifest configurations associated with the origin endpoint. Each configuration represents a different MSS streaming option available from this endpoint.</p>"""
    force_endpoint_error_configuration: NotRequired[
        "capo_mediapackagev2.types.force_endpoint_error_configuration.ForceEndpointErrorConfiguration"
    ]
    """<p>The failover settings for the endpoint.</p>"""
    uri_separator: NotRequired["capo_mediapackagev2.types.uri_separator.UriSeparator"]
    """<p>The separator character used in generated URIs for this origin endpoint.</p>"""
    stream_name_output_mode: NotRequired[
        "capo_mediapackagev2.types.stream_name_output_mode.StreamNameOutputMode"
    ]
    """<p>The output mode for stream names in egress manifests for this origin endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OriginEndpointListConfiguration) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["ChannelGroupName"] = value["channel_group_name"]
    out["ChannelName"] = value["channel_name"]
    out["OriginEndpointName"] = value["origin_endpoint_name"]
    import capo_mediapackagev2.types.container_type

    out["ContainerType"] = capo_mediapackagev2.types.container_type.serialize_json(
        value["container_type"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "created_at" in value:
        import capo_mediapackagev2.types._prelude.timestamp

        out["CreatedAt"] = capo_mediapackagev2.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "modified_at" in value:
        import capo_mediapackagev2.types._prelude.timestamp

        out["ModifiedAt"] = capo_mediapackagev2.types._prelude.timestamp.serialize_json(
            value["modified_at"]
        )
    if "hls_manifests" in value:
        import capo_mediapackagev2.types.list_hls_manifests

        out["HlsManifests"] = (
            capo_mediapackagev2.types.list_hls_manifests.serialize_json(
                value["hls_manifests"]
            )
        )
    if "low_latency_hls_manifests" in value:
        import capo_mediapackagev2.types.list_low_latency_hls_manifests

        out["LowLatencyHlsManifests"] = (
            capo_mediapackagev2.types.list_low_latency_hls_manifests.serialize_json(
                value["low_latency_hls_manifests"]
            )
        )
    if "dash_manifests" in value:
        import capo_mediapackagev2.types.list_dash_manifests

        out["DashManifests"] = (
            capo_mediapackagev2.types.list_dash_manifests.serialize_json(
                value["dash_manifests"]
            )
        )
    if "mss_manifests" in value:
        import capo_mediapackagev2.types.list_mss_manifests

        out["MssManifests"] = (
            capo_mediapackagev2.types.list_mss_manifests.serialize_json(
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


def deserialize_json(data: dict) -> OriginEndpointListConfiguration:
    out: OriginEndpointListConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("ChannelGroupName") is not None:
        out["channel_group_name"] = data["ChannelGroupName"]
    else:
        out["channel_group_name"] = ""
    if data.get("ChannelName") is not None:
        out["channel_name"] = data["ChannelName"]
    else:
        out["channel_name"] = ""
    if data.get("OriginEndpointName") is not None:
        out["origin_endpoint_name"] = data["OriginEndpointName"]
    else:
        out["origin_endpoint_name"] = ""
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
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("CreatedAt") is not None:
        import capo_mediapackagev2.types._prelude.timestamp

        out["created_at"] = (
            capo_mediapackagev2.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    if data.get("ModifiedAt") is not None:
        import capo_mediapackagev2.types._prelude.timestamp

        out["modified_at"] = (
            capo_mediapackagev2.types._prelude.timestamp.deserialize_json(
                data["ModifiedAt"]
            )
        )
    if data.get("HlsManifests") is not None:
        import capo_mediapackagev2.types.list_hls_manifests

        out["hls_manifests"] = (
            capo_mediapackagev2.types.list_hls_manifests.deserialize_json(
                data["HlsManifests"]
            )
        )
    if data.get("LowLatencyHlsManifests") is not None:
        import capo_mediapackagev2.types.list_low_latency_hls_manifests

        out["low_latency_hls_manifests"] = (
            capo_mediapackagev2.types.list_low_latency_hls_manifests.deserialize_json(
                data["LowLatencyHlsManifests"]
            )
        )
    if data.get("DashManifests") is not None:
        import capo_mediapackagev2.types.list_dash_manifests

        out["dash_manifests"] = (
            capo_mediapackagev2.types.list_dash_manifests.deserialize_json(
                data["DashManifests"]
            )
        )
    if data.get("MssManifests") is not None:
        import capo_mediapackagev2.types.list_mss_manifests

        out["mss_manifests"] = (
            capo_mediapackagev2.types.list_mss_manifests.deserialize_json(
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
