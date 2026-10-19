"""Generated from Smithy shape ``com.amazonaws.appsync#CreateApiRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appsync.types.api_name
    import capo_appsync.types.event_config
    import capo_appsync.types.string
    import capo_appsync.types.tag_map


class CreateApiRequest(TypedDict, closed=True):
    name: "capo_appsync.types.api_name.ApiName"
    """<p>The name for the <code>Api</code>.</p>"""
    owner_contact: NotRequired["capo_appsync.types.string.String"]
    """<p>The owner contact information for the <code>Api</code>.</p>"""
    tags: NotRequired["capo_appsync.types.tag_map.TagMap"]
    event_config: "capo_appsync.types.event_config.EventConfig"
    """<p>The Event API configuration. This includes the default authorization configuration for connecting, publishing, and subscribing to an Event API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApiRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "owner_contact" in value:
        out["ownerContact"] = value["owner_contact"]
    if "tags" in value:
        import capo_appsync.types.tag_map

        out["tags"] = capo_appsync.types.tag_map.serialize_json(value["tags"])
    import capo_appsync.types.event_config

    out["eventConfig"] = capo_appsync.types.event_config.serialize_json(
        value["event_config"]
    )
    return out


def deserialize_json(data: dict) -> CreateApiRequest:
    out: CreateApiRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("ownerContact") is not None:
        out["owner_contact"] = data["ownerContact"]
    if data.get("tags") is not None:
        import capo_appsync.types.tag_map

        out["tags"] = capo_appsync.types.tag_map.deserialize_json(data["tags"])
    if data.get("eventConfig") is not None:
        import capo_appsync.types.event_config

        out["event_config"] = capo_appsync.types.event_config.deserialize_json(
            data["eventConfig"]
        )
    else:
        raise DeserializationError("CreateApiRequest.event_config required")
    return out
