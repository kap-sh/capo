"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#Channel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.channel_id
    import capo_codeguruprofiler.types.channel_uri
    import capo_codeguruprofiler.types.event_publishers


class Channel(TypedDict, closed=True):
    id: NotRequired["capo_codeguruprofiler.types.channel_id.ChannelId"]
    """<p>Unique identifier for each <code>Channel</code> in the notification configuration of a Profiling Group. A random UUID for channelId is used when adding a channel to the notification configuration if not specified in the request.</p>"""
    uri: "capo_codeguruprofiler.types.channel_uri.ChannelUri"
    """<p>Unique arn of the resource to be used for notifications. We support a valid SNS topic arn as a channel uri.</p>"""
    event_publishers: "capo_codeguruprofiler.types.event_publishers.EventPublishers"
    """<p>List of publishers for different type of events that may be detected in an application from the profile. Anomaly detection is the only event publisher in Profiler.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Channel) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    out["uri"] = value["uri"]
    import capo_codeguruprofiler.types.event_publishers

    out["eventPublishers"] = (
        capo_codeguruprofiler.types.event_publishers.serialize_json(
            value["event_publishers"]
        )
    )
    return out


def deserialize_json(data: dict) -> Channel:
    out: Channel = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("uri") is not None:
        out["uri"] = data["uri"]
    else:
        out["uri"] = ""
    if data.get("eventPublishers") is not None:
        import capo_codeguruprofiler.types.event_publishers

        out["event_publishers"] = (
            capo_codeguruprofiler.types.event_publishers.deserialize_json(
                data["eventPublishers"]
            )
        )
    else:
        out["event_publishers"] = []
    return out
