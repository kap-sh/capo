"""Generated from Smithy shape ``com.amazonaws.appintegrations#GetEventIntegrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appintegrations.types.arn
    import capo_appintegrations.types.description
    import capo_appintegrations.types.event_bridge_bus
    import capo_appintegrations.types.event_filter
    import capo_appintegrations.types.name
    import capo_appintegrations.types.tag_map


class GetEventIntegrationResponse(TypedDict, closed=True):
    name: NotRequired["capo_appintegrations.types.name.Name"]
    """<p>The name of the event integration. </p>"""
    description: NotRequired["capo_appintegrations.types.description.Description"]
    """<p>The description of the event integration.</p>"""
    event_integration_arn: NotRequired["capo_appintegrations.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the event integration.</p>"""
    event_bridge_bus: NotRequired[
        "capo_appintegrations.types.event_bridge_bus.EventBridgeBus"
    ]
    """<p>The EventBridge bus.</p>"""
    event_filter: NotRequired["capo_appintegrations.types.event_filter.EventFilter"]
    """<p>The event filter.</p>"""
    tags: NotRequired["capo_appintegrations.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEventIntegrationResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "event_integration_arn" in value:
        out["EventIntegrationArn"] = value["event_integration_arn"]
    if "event_bridge_bus" in value:
        out["EventBridgeBus"] = value["event_bridge_bus"]
    if "event_filter" in value:
        import capo_appintegrations.types.event_filter

        out["EventFilter"] = capo_appintegrations.types.event_filter.serialize_json(
            value["event_filter"]
        )
    if "tags" in value:
        import capo_appintegrations.types.tag_map

        out["Tags"] = capo_appintegrations.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetEventIntegrationResponse:
    out: GetEventIntegrationResponse = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("EventIntegrationArn") is not None:
        out["event_integration_arn"] = data["EventIntegrationArn"]
    if data.get("EventBridgeBus") is not None:
        out["event_bridge_bus"] = data["EventBridgeBus"]
    if data.get("EventFilter") is not None:
        import capo_appintegrations.types.event_filter

        out["event_filter"] = capo_appintegrations.types.event_filter.deserialize_json(
            data["EventFilter"]
        )
    if data.get("Tags") is not None:
        import capo_appintegrations.types.tag_map

        out["tags"] = capo_appintegrations.types.tag_map.deserialize_json(data["Tags"])
    return out
