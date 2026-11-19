"""Generated from Smithy shape ``com.amazonaws.scheduler#EventBridgePutRawEventsParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_scheduler.types.event_bridge_metadata_map


class EventBridgePutRawEventsParameters(TypedDict, closed=True):
    metadata: NotRequired[
        "capo_scheduler.types.event_bridge_metadata_map.EventBridgeMetadataMap"
    ]
    """<p>Optional metadata key-value pairs you define. Keys must be 1-128 characters and must not contain "/".</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventBridgePutRawEventsParameters) -> dict:
    out: dict = {}
    if "metadata" in value:
        import capo_scheduler.types.event_bridge_metadata_map

        out["Metadata"] = capo_scheduler.types.event_bridge_metadata_map.serialize_json(
            value["metadata"]
        )
    return out


def deserialize_json(data: dict) -> EventBridgePutRawEventsParameters:
    out: EventBridgePutRawEventsParameters = {}  # type: ignore[typeddict-item]
    if data.get("Metadata") is not None:
        import capo_scheduler.types.event_bridge_metadata_map

        out["metadata"] = (
            capo_scheduler.types.event_bridge_metadata_map.deserialize_json(
                data["Metadata"]
            )
        )
    return out
