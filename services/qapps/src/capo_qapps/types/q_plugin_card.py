"""Generated from Smithy shape ``com.amazonaws.qapps#QPluginCard``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.action_identifier
    import capo_qapps.types.card_type
    import capo_qapps.types.dependency_list
    import capo_qapps.types.plugin_type
    import capo_qapps.types.prompt
    import capo_qapps.types.title
    import capo_qapps.types.uuid


class QPluginCard(TypedDict, closed=True):
    id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the plugin card.</p>"""
    title: "capo_qapps.types.title.Title"
    """<p>The title or label of the plugin card.</p>"""
    dependencies: "capo_qapps.types.dependency_list.DependencyList"
    """<p>Any dependencies or requirements for the plugin card.</p>"""
    type: "capo_qapps.types.card_type.CardType"
    """<p>The type of the card.</p>"""
    prompt: "capo_qapps.types.prompt.Prompt"
    """<p>The prompt or instructions displayed for the plugin card.</p>"""
    plugin_type: "capo_qapps.types.plugin_type.PluginType"
    """<p>The type or category of the plugin used by the card.</p>"""
    plugin_id: "str"
    """<p>The unique identifier of the plugin used by the card.</p>"""
    action_identifier: NotRequired[
        "capo_qapps.types.action_identifier.ActionIdentifier"
    ]
    """<p>The action identifier of the action to be performed by the plugin card.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QPluginCard) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["title"] = value["title"]
    import capo_qapps.types.dependency_list

    out["dependencies"] = capo_qapps.types.dependency_list.serialize_json(
        value["dependencies"]
    )
    import capo_qapps.types.card_type

    out["type"] = capo_qapps.types.card_type.serialize_json(value["type"])
    out["prompt"] = value["prompt"]
    import capo_qapps.types.plugin_type

    out["pluginType"] = capo_qapps.types.plugin_type.serialize_json(
        value["plugin_type"]
    )
    out["pluginId"] = value["plugin_id"]
    if "action_identifier" in value:
        out["actionIdentifier"] = value["action_identifier"]
    return out


def deserialize_json(data: dict) -> QPluginCard:
    out: QPluginCard = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    if data.get("dependencies") is not None:
        import capo_qapps.types.dependency_list

        out["dependencies"] = capo_qapps.types.dependency_list.deserialize_json(
            data["dependencies"]
        )
    else:
        out["dependencies"] = []
    if data.get("type") is not None:
        import capo_qapps.types.card_type

        out["type"] = capo_qapps.types.card_type.deserialize_json(data["type"])
    else:
        import typing

        out["type"] = typing.cast("capo_qapps.types.card_type.CardType", "")
    if data.get("prompt") is not None:
        out["prompt"] = data["prompt"]
    else:
        out["prompt"] = ""
    if data.get("pluginType") is not None:
        import capo_qapps.types.plugin_type

        out["plugin_type"] = capo_qapps.types.plugin_type.deserialize_json(
            data["pluginType"]
        )
    else:
        import typing

        out["plugin_type"] = typing.cast("capo_qapps.types.plugin_type.PluginType", "")
    if data.get("pluginId") is not None:
        out["plugin_id"] = data["pluginId"]
    else:
        out["plugin_id"] = ""
    if data.get("actionIdentifier") is not None:
        out["action_identifier"] = data["actionIdentifier"]
    return out
