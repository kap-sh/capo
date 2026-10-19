"""Generated from Smithy shape ``com.amazonaws.appsync#UpdateApiRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appsync.types.api_name
    import capo_appsync.types.event_config
    import capo_appsync.types.string


class UpdateApiRequest(TypedDict, closed=True):
    api_id: "capo_appsync.types.string.String"
    """<p>The <code>Api</code> ID.</p>"""
    name: "capo_appsync.types.api_name.ApiName"
    """<p>The name of the Api.</p>"""
    owner_contact: NotRequired["capo_appsync.types.string.String"]
    """<p>The owner contact information for the <code>Api</code>.</p>"""
    event_config: "capo_appsync.types.event_config.EventConfig"
    """<p>The new event configuration. This includes the default authorization configuration for connecting, publishing, and subscribing to an Event API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApiRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "owner_contact" in value:
        out["ownerContact"] = value["owner_contact"]
    import capo_appsync.types.event_config

    out["eventConfig"] = capo_appsync.types.event_config.serialize_json(
        value["event_config"]
    )
    return out


def deserialize_json(data: dict) -> UpdateApiRequest:
    out: UpdateApiRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("ownerContact") is not None:
        out["owner_contact"] = data["ownerContact"]
    if data.get("eventConfig") is not None:
        import capo_appsync.types.event_config

        out["event_config"] = capo_appsync.types.event_config.deserialize_json(
            data["eventConfig"]
        )
    else:
        raise DeserializationError("UpdateApiRequest.event_config required")
    return out
