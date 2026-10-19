"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#CreateEventBusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.event_bus_name
    import capo_cloudwatch_events.types.event_source_name
    import capo_cloudwatch_events.types.tag_list


class CreateEventBusRequest(TypedDict, closed=True):
    name: "capo_cloudwatch_events.types.event_bus_name.EventBusName"
    """<p>The name of the new event bus. </p> <p>Event bus names cannot contain the / character. You can't use the name <code>default</code> for a custom event bus, as this name is already used for your account's default event bus.</p> <p>If this is a partner event bus, the name must exactly match the name of the partner event source that this event bus is matched to.</p>"""
    event_source_name: NotRequired[
        "capo_cloudwatch_events.types.event_source_name.EventSourceName"
    ]
    """<p>If you are creating a partner event bus, this specifies the partner event source that the new event bus will be matched with.</p>"""
    tags: NotRequired["capo_cloudwatch_events.types.tag_list.TagList"]
    """<p>Tags to associate with the event bus.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEventBusRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "event_source_name" in value:
        out["EventSourceName"] = value["event_source_name"]
    if "tags" in value:
        import capo_cloudwatch_events.types.tag_list

        out["Tags"] = capo_cloudwatch_events.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEventBusRequest:
    out: CreateEventBusRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("EventSourceName") is not None:
        out["event_source_name"] = data["EventSourceName"]
    if data.get("Tags") is not None:
        import capo_cloudwatch_events.types.tag_list

        out["tags"] = capo_cloudwatch_events.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
