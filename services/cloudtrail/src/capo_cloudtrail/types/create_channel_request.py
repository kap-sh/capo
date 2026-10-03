"""Generated from Smithy shape ``com.amazonaws.cloudtrail#CreateChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudtrail.types.channel_name
    import capo_cloudtrail.types.destinations
    import capo_cloudtrail.types.source
    import capo_cloudtrail.types.tags_list


class CreateChannelRequest(TypedDict, closed=True):
    name: "capo_cloudtrail.types.channel_name.ChannelName"
    """<p>The name of the channel.</p>"""
    source: "capo_cloudtrail.types.source.Source"
    """<p>The name of the partner or external event source. You cannot change this name after you create the channel. A maximum of one channel is allowed per source.</p> <p> A source can be either <code>Custom</code> for all valid non-Amazon Web Services events, or the name of a partner event source. For information about the source names for available partners, see <a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-event-data-store-integration.html#cloudtrail-lake-partner-information">Additional information about integration partners</a> in the CloudTrail User Guide. </p>"""
    destinations: "capo_cloudtrail.types.destinations.Destinations"
    """<p>One or more event data stores to which events arriving through a channel will be logged.</p>"""
    tags: NotRequired["capo_cloudtrail.types.tags_list.TagsList"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateChannelRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Source"] = value["source"]
    import capo_cloudtrail.types.destinations

    out["Destinations"] = capo_cloudtrail.types.destinations.serialize_aws_json_1_1(
        value["destinations"]
    )
    if "tags" in value:
        import capo_cloudtrail.types.tags_list

        out["Tags"] = capo_cloudtrail.types.tags_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateChannelRequest:
    out: CreateChannelRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateChannelRequest.name required")
    if data.get("Source") is not None:
        out["source"] = data["Source"]
    else:
        raise DeserializationError("CreateChannelRequest.source required")
    if data.get("Destinations") is not None:
        import capo_cloudtrail.types.destinations

        out["destinations"] = (
            capo_cloudtrail.types.destinations.deserialize_aws_json_1_1(
                data["Destinations"]
            )
        )
    else:
        raise DeserializationError("CreateChannelRequest.destinations required")
    if data.get("Tags") is not None:
        import capo_cloudtrail.types.tags_list

        out["tags"] = capo_cloudtrail.types.tags_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
