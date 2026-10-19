"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#UpdateChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mediapackagev2.types.attached_multiview_channel_list
    import capo_mediapackagev2.types.entity_tag
    import capo_mediapackagev2.types.ingest_endpoint_list
    import capo_mediapackagev2.types.input_switch_configuration
    import capo_mediapackagev2.types.input_type
    import capo_mediapackagev2.types.multiview_configuration
    import capo_mediapackagev2.types.output_header_configuration
    import capo_mediapackagev2.types.output_locking_mode
    import capo_mediapackagev2.types.resource_description
    import capo_mediapackagev2.types.tag_map


class UpdateChannelResponse(TypedDict, closed=True):
    multiview_configuration: NotRequired[
        "capo_mediapackagev2.types.multiview_configuration.MultiviewConfiguration"
    ]
    """<p>The multiview configuration for the channel. This is present only when <code>InputType</code> is <code>MULTIVIEW</code>.</p>"""
    attached_multiview_channels: NotRequired[
        "capo_mediapackagev2.types.attached_multiview_channel_list.AttachedMultiviewChannelList"
    ]
    """<p>The multiview channels, in the same channel group, that list this channel as an available source. This is a read-only field. You can't delete a channel while any multiview channel still lists it as a source. Use this field to find the multiview channels that you need to update first.</p>"""
    arn: "str"
    """<p>The Amazon Resource Name (ARN) associated with the resource.</p>"""
    channel_name: "str"
    """<p>The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.</p>"""
    channel_group_name: "str"
    """<p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time the channel was created.</p>"""
    modified_at: "datetime.datetime"
    """<p>The date and time the channel was modified.</p>"""
    description: NotRequired[
        "capo_mediapackagev2.types.resource_description.ResourceDescription"
    ]
    """<p>The description for your channel.</p>"""
    ingest_endpoints: NotRequired[
        "capo_mediapackagev2.types.ingest_endpoint_list.IngestEndpointList"
    ]
    input_type: NotRequired["capo_mediapackagev2.types.input_type.InputType"]
    """<p>The input type is an immutable field. It defines whether the channel allows CMAF ingest, HLS ingest, or server-side multiview output. Multiview channels receive no ingest of their own. If unprovided, the value defaults to HLS.</p> <p>The allowed values are:</p> <ul> <li> <p> <code>HLS</code> - The HLS streaming specification (which defines M3U8 manifests and TS segments).</p> </li> <li> <p> <code>CMAF</code> - The DASH-IF CMAF Ingest specification (which defines CMAF segments with optional DASH manifests).</p> </li> <li> <p> <code>MULTIVIEW</code> – Server-side multiview. The channel receives no ingest of its own. Instead, it composites video from the source channels in its <code>MultiviewConfiguration</code> into a single tiled output stream.</p> </li> </ul>"""
    e_tag: NotRequired["capo_mediapackagev2.types.entity_tag.EntityTag"]
    """<p>The current Entity Tag (ETag) associated with this resource. The entity tag can be used to safely make concurrent updates to the resource.</p>"""
    tags: NotRequired["capo_mediapackagev2.types.tag_map.TagMap"]
    """<p>The comma-separated list of tag key:value pairs assigned to the channel.</p>"""
    input_switch_configuration: NotRequired[
        "capo_mediapackagev2.types.input_switch_configuration.InputSwitchConfiguration"
    ]
    """<p>The configuration for input switching based on the media quality confidence score (MQCS) as provided from AWS Elemental MediaLive. This setting is valid only when <code>InputType</code> is <code>CMAF</code>.</p>"""
    output_header_configuration: NotRequired[
        "capo_mediapackagev2.types.output_header_configuration.OutputHeaderConfiguration"
    ]
    """<p>The settings for what common media server data (CMSD) headers AWS Elemental MediaPackage includes in responses to the CDN. This setting is valid only when <code>InputType</code> is <code>CMAF</code>.</p>"""
    output_locking_mode: NotRequired[
        "capo_mediapackagev2.types.output_locking_mode.OutputLockingMode"
    ]
    """<p>The output locking mode configured for the channel. This value is immutable after channel creation.</p> <p>The allowed values are:</p> <ul> <li> <p> <code>EPOCH_LOCKED</code> - The channel uses epoch-locked behavior with deterministic sequence numbering and fixed segment boundaries aligned to epoch time.</p> </li> <li> <p> <code>NON_EPOCH_LOCKED</code> - The channel uses non-epoch-locked behavior with duration-based segment combining and monotonically increasing sequence numbers starting from 0.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChannelResponse) -> dict:
    out: dict = {}
    if "multiview_configuration" in value:
        import capo_mediapackagev2.types.multiview_configuration

        out["MultiviewConfiguration"] = (
            capo_mediapackagev2.types.multiview_configuration.serialize_json(
                value["multiview_configuration"]
            )
        )
    if "attached_multiview_channels" in value:
        import capo_mediapackagev2.types.attached_multiview_channel_list

        out["AttachedMultiviewChannels"] = (
            capo_mediapackagev2.types.attached_multiview_channel_list.serialize_json(
                value["attached_multiview_channels"]
            )
        )
    out["Arn"] = value["arn"]
    out["ChannelName"] = value["channel_name"]
    out["ChannelGroupName"] = value["channel_group_name"]
    import capo_mediapackagev2.types._prelude.timestamp

    out["CreatedAt"] = capo_mediapackagev2.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_mediapackagev2.types._prelude.timestamp

    out["ModifiedAt"] = capo_mediapackagev2.types._prelude.timestamp.serialize_json(
        value["modified_at"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "ingest_endpoints" in value:
        import capo_mediapackagev2.types.ingest_endpoint_list

        out["IngestEndpoints"] = (
            capo_mediapackagev2.types.ingest_endpoint_list.serialize_json(
                value["ingest_endpoints"]
            )
        )
    if "input_type" in value:
        import capo_mediapackagev2.types.input_type

        out["InputType"] = capo_mediapackagev2.types.input_type.serialize_json(
            value["input_type"]
        )
    if "e_tag" in value:
        out["ETag"] = value["e_tag"]
    if "tags" in value:
        import capo_mediapackagev2.types.tag_map

        out["tags"] = capo_mediapackagev2.types.tag_map.serialize_json(value["tags"])
    if "input_switch_configuration" in value:
        import capo_mediapackagev2.types.input_switch_configuration

        out["InputSwitchConfiguration"] = (
            capo_mediapackagev2.types.input_switch_configuration.serialize_json(
                value["input_switch_configuration"]
            )
        )
    if "output_header_configuration" in value:
        import capo_mediapackagev2.types.output_header_configuration

        out["OutputHeaderConfiguration"] = (
            capo_mediapackagev2.types.output_header_configuration.serialize_json(
                value["output_header_configuration"]
            )
        )
    if "output_locking_mode" in value:
        import capo_mediapackagev2.types.output_locking_mode

        out["OutputLockingMode"] = (
            capo_mediapackagev2.types.output_locking_mode.serialize_json(
                value["output_locking_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateChannelResponse:
    out: UpdateChannelResponse = {}  # type: ignore[typeddict-item]
    if data.get("MultiviewConfiguration") is not None:
        import capo_mediapackagev2.types.multiview_configuration

        out["multiview_configuration"] = (
            capo_mediapackagev2.types.multiview_configuration.deserialize_json(
                data["MultiviewConfiguration"]
            )
        )
    if data.get("AttachedMultiviewChannels") is not None:
        import capo_mediapackagev2.types.attached_multiview_channel_list

        out["attached_multiview_channels"] = (
            capo_mediapackagev2.types.attached_multiview_channel_list.deserialize_json(
                data["AttachedMultiviewChannels"]
            )
        )
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("ChannelName") is not None:
        out["channel_name"] = data["ChannelName"]
    else:
        out["channel_name"] = ""
    if data.get("ChannelGroupName") is not None:
        out["channel_group_name"] = data["ChannelGroupName"]
    else:
        out["channel_group_name"] = ""
    if data.get("CreatedAt") is not None:
        import capo_mediapackagev2.types._prelude.timestamp

        out["created_at"] = (
            capo_mediapackagev2.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("ModifiedAt") is not None:
        import capo_mediapackagev2.types._prelude.timestamp

        out["modified_at"] = (
            capo_mediapackagev2.types._prelude.timestamp.deserialize_json(
                data["ModifiedAt"]
            )
        )
    else:
        import datetime

        out["modified_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("IngestEndpoints") is not None:
        import capo_mediapackagev2.types.ingest_endpoint_list

        out["ingest_endpoints"] = (
            capo_mediapackagev2.types.ingest_endpoint_list.deserialize_json(
                data["IngestEndpoints"]
            )
        )
    if data.get("InputType") is not None:
        import capo_mediapackagev2.types.input_type

        out["input_type"] = capo_mediapackagev2.types.input_type.deserialize_json(
            data["InputType"]
        )
    if data.get("ETag") is not None:
        out["e_tag"] = data["ETag"]
    if data.get("tags") is not None:
        import capo_mediapackagev2.types.tag_map

        out["tags"] = capo_mediapackagev2.types.tag_map.deserialize_json(data["tags"])
    if data.get("InputSwitchConfiguration") is not None:
        import capo_mediapackagev2.types.input_switch_configuration

        out["input_switch_configuration"] = (
            capo_mediapackagev2.types.input_switch_configuration.deserialize_json(
                data["InputSwitchConfiguration"]
            )
        )
    if data.get("OutputHeaderConfiguration") is not None:
        import capo_mediapackagev2.types.output_header_configuration

        out["output_header_configuration"] = (
            capo_mediapackagev2.types.output_header_configuration.deserialize_json(
                data["OutputHeaderConfiguration"]
            )
        )
    if data.get("OutputLockingMode") is not None:
        import capo_mediapackagev2.types.output_locking_mode

        out["output_locking_mode"] = (
            capo_mediapackagev2.types.output_locking_mode.deserialize_json(
                data["OutputLockingMode"]
            )
        )
    return out
