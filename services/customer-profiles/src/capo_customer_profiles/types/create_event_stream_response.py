"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CreateEventStreamResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.string1_to255
    import capo_customer_profiles.types.tag_map


class CreateEventStreamResponse(TypedDict, closed=True):
    event_stream_arn: "capo_customer_profiles.types.string1_to255.string1To255"
    """<p>A unique identifier for the event stream.</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEventStreamResponse) -> dict:
    out: dict = {}
    out["EventStreamArn"] = value["event_stream_arn"]
    if "tags" in value:
        import capo_customer_profiles.types.tag_map

        out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateEventStreamResponse:
    out: CreateEventStreamResponse = {}  # type: ignore[typeddict-item]
    if data.get("EventStreamArn") is not None:
        out["event_stream_arn"] = data["EventStreamArn"]
    else:
        out["event_stream_arn"] = ""
    if data.get("Tags") is not None:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
