"""Generated from Smithy shape ``com.amazonaws.qapps#UpdateQAppInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.app_definition_input
    import capo_qapps.types.description
    import capo_qapps.types.instance_id
    import capo_qapps.types.title
    import capo_qapps.types.uuid


class UpdateQAppInput(TypedDict, closed=True):
    instance_id: "capo_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    app_id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the Q App to update.</p>"""
    title: NotRequired["capo_qapps.types.title.Title"]
    """<p>The new title for the Q App.</p>"""
    description: NotRequired["capo_qapps.types.description.Description"]
    """<p>The new description for the Q App.</p>"""
    app_definition: NotRequired[
        "capo_qapps.types.app_definition_input.AppDefinitionInput"
    ]
    """<p>The new definition specifying the cards and flow for the Q App.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQAppInput) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    if "title" in value:
        out["title"] = value["title"]
    if "description" in value:
        out["description"] = value["description"]
    if "app_definition" in value:
        import capo_qapps.types.app_definition_input

        out["appDefinition"] = capo_qapps.types.app_definition_input.serialize_json(
            value["app_definition"]
        )
    return out


def deserialize_json(data: dict) -> UpdateQAppInput:
    out: UpdateQAppInput = {}  # type: ignore[typeddict-item]
    if data.get("appId") is not None:
        out["app_id"] = data["appId"]
    else:
        out["app_id"] = ""
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("appDefinition") is not None:
        import capo_qapps.types.app_definition_input

        out["app_definition"] = capo_qapps.types.app_definition_input.deserialize_json(
            data["appDefinition"]
        )
    return out
