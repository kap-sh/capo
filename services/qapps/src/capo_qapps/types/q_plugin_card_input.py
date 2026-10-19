"""Generated from Smithy shape ``com.amazonaws.qapps#QPluginCardInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.action_identifier
    import capo_qapps.types.card_type
    import capo_qapps.types.plugin_id
    import capo_qapps.types.prompt
    import capo_qapps.types.title
    import capo_qapps.types.uuid


class QPluginCardInput(TypedDict, closed=True):
    title: "capo_qapps.types.title.Title"
    """<p>The title or label of the plugin card.</p>"""
    id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the plugin card.</p>"""
    type: "capo_qapps.types.card_type.CardType"
    """<p>The type of the card.</p>"""
    prompt: "capo_qapps.types.prompt.Prompt"
    """<p>The prompt or instructions displayed for the plugin card.</p>"""
    plugin_id: "capo_qapps.types.plugin_id.PluginId"
    """<p>The unique identifier of the plugin used by the card.</p>"""
    action_identifier: NotRequired[
        "capo_qapps.types.action_identifier.ActionIdentifier"
    ]
    """<p>The action identifier of the action to be performed by the plugin card.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QPluginCardInput) -> dict:
    out: dict = {}
    out["title"] = value["title"]
    out["id"] = value["id"]
    import capo_qapps.types.card_type

    out["type"] = capo_qapps.types.card_type.serialize_json(
        value.get("type", "q-plugin")
    )
    out["prompt"] = value["prompt"]
    out["pluginId"] = value["plugin_id"]
    if "action_identifier" in value:
        out["actionIdentifier"] = value["action_identifier"]
    return out


def deserialize_json(data: dict) -> QPluginCardInput:
    out: QPluginCardInput = {}  # type: ignore[typeddict-item]
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("type") is not None:
        import capo_qapps.types.card_type

        out["type"] = capo_qapps.types.card_type.deserialize_json(data["type"])
    else:
        out["type"] = "q-plugin"
    if data.get("prompt") is not None:
        out["prompt"] = data["prompt"]
    else:
        out["prompt"] = ""
    if data.get("pluginId") is not None:
        out["plugin_id"] = data["pluginId"]
    else:
        out["plugin_id"] = ""
    if data.get("actionIdentifier") is not None:
        out["action_identifier"] = data["actionIdentifier"]
    return out
