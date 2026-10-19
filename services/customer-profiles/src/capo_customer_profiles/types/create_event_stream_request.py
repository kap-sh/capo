"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CreateEventStreamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.string1_to255
    import capo_customer_profiles.types.tag_map


class CreateEventStreamRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    uri: "capo_customer_profiles.types.string1_to255.string1To255"
    """<p>The StreamARN of the destination to deliver profile events to. For example, arn:aws:kinesis:region:account-id:stream/stream-name</p>"""
    event_stream_name: "capo_customer_profiles.types.name.name"
    """<p>The name of the event stream.</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEventStreamRequest) -> dict:
    out: dict = {}
    out["Uri"] = value["uri"]
    if "tags" in value:
        import capo_customer_profiles.types.tag_map

        out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateEventStreamRequest:
    out: CreateEventStreamRequest = {}  # type: ignore[typeddict-item]
    if data.get("Uri") is not None:
        out["uri"] = data["Uri"]
    else:
        out["uri"] = ""
    if data.get("Tags") is not None:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
