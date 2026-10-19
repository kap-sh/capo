"""Generated from Smithy shape ``com.amazonaws.appconfig#CreateExtensionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.actions_map
    import capo_appconfig.types.description
    import capo_appconfig.types.extension_or_parameter_name
    import capo_appconfig.types.integer
    import capo_appconfig.types.parameter_map
    import capo_appconfig.types.tag_map


class CreateExtensionRequest(TypedDict, closed=True):
    name: "capo_appconfig.types.extension_or_parameter_name.ExtensionOrParameterName"
    """<p>A name for the extension. Each extension name in your account must be unique. Extension versions use the same name.</p>"""
    description: NotRequired["capo_appconfig.types.description.Description"]
    """<p>Information about the extension.</p>"""
    actions: "capo_appconfig.types.actions_map.ActionsMap"
    """<p>The actions defined in the extension.</p>"""
    parameters: NotRequired["capo_appconfig.types.parameter_map.ParameterMap"]
    """<p>The parameters accepted by the extension. You specify parameter values when you associate the extension to an AppConfig resource by using the <code>CreateExtensionAssociation</code> API action. For Lambda extension actions, these parameters are included in the Lambda request object.</p>"""
    tags: NotRequired["capo_appconfig.types.tag_map.TagMap"]
    """<p>Adds one or more tags for the specified extension. Tags are metadata that help you categorize resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define. </p>"""
    latest_version_number: NotRequired["capo_appconfig.types.integer.Integer"]
    """<p>You can omit this field when you create an extension. When you create a new version, specify the most recent current version number. For example, you create version 3, enter 2 for this field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateExtensionRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_appconfig.types.actions_map

    out["Actions"] = capo_appconfig.types.actions_map.serialize_json(value["actions"])
    if "parameters" in value:
        import capo_appconfig.types.parameter_map

        out["Parameters"] = capo_appconfig.types.parameter_map.serialize_json(
            value["parameters"]
        )
    if "tags" in value:
        import capo_appconfig.types.tag_map

        out["Tags"] = capo_appconfig.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateExtensionRequest:
    out: CreateExtensionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Actions") is not None:
        import capo_appconfig.types.actions_map

        out["actions"] = capo_appconfig.types.actions_map.deserialize_json(
            data["Actions"]
        )
    else:
        out["actions"] = {}
    if data.get("Parameters") is not None:
        import capo_appconfig.types.parameter_map

        out["parameters"] = capo_appconfig.types.parameter_map.deserialize_json(
            data["Parameters"]
        )
    if data.get("Tags") is not None:
        import capo_appconfig.types.tag_map

        out["tags"] = capo_appconfig.types.tag_map.deserialize_json(data["Tags"])
    return out
