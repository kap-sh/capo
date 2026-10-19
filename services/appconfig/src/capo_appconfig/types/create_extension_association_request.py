"""Generated from Smithy shape ``com.amazonaws.appconfig#CreateExtensionAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.identifier
    import capo_appconfig.types.integer
    import capo_appconfig.types.parameter_value_map
    import capo_appconfig.types.tag_map


class CreateExtensionAssociationRequest(TypedDict, closed=True):
    extension_identifier: "capo_appconfig.types.identifier.Identifier"
    """<p>The name, the ID, or the Amazon Resource Name (ARN) of the extension.</p>"""
    extension_version_number: NotRequired["capo_appconfig.types.integer.Integer"]
    """<p>The version number of the extension. If not specified, AppConfig uses the maximum version of the extension.</p>"""
    resource_identifier: "capo_appconfig.types.identifier.Identifier"
    """<p>The ARN of an application, configuration profile, or environment.</p>"""
    parameters: NotRequired[
        "capo_appconfig.types.parameter_value_map.ParameterValueMap"
    ]
    """<p>The parameter names and values defined in the extensions. Extension parameters marked <code>Required</code> must be entered for this field.</p>"""
    tags: NotRequired["capo_appconfig.types.tag_map.TagMap"]
    """<p>Adds one or more tags for the specified extension association. Tags are metadata that help you categorize resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateExtensionAssociationRequest) -> dict:
    out: dict = {}
    out["ExtensionIdentifier"] = value["extension_identifier"]
    if "extension_version_number" in value:
        out["ExtensionVersionNumber"] = value["extension_version_number"]
    out["ResourceIdentifier"] = value["resource_identifier"]
    if "parameters" in value:
        import capo_appconfig.types.parameter_value_map

        out["Parameters"] = capo_appconfig.types.parameter_value_map.serialize_json(
            value["parameters"]
        )
    if "tags" in value:
        import capo_appconfig.types.tag_map

        out["Tags"] = capo_appconfig.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateExtensionAssociationRequest:
    out: CreateExtensionAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ExtensionIdentifier") is not None:
        out["extension_identifier"] = data["ExtensionIdentifier"]
    else:
        out["extension_identifier"] = ""
    if data.get("ExtensionVersionNumber") is not None:
        out["extension_version_number"] = data["ExtensionVersionNumber"]
    if data.get("ResourceIdentifier") is not None:
        out["resource_identifier"] = data["ResourceIdentifier"]
    else:
        out["resource_identifier"] = ""
    if data.get("Parameters") is not None:
        import capo_appconfig.types.parameter_value_map

        out["parameters"] = capo_appconfig.types.parameter_value_map.deserialize_json(
            data["Parameters"]
        )
    if data.get("Tags") is not None:
        import capo_appconfig.types.tag_map

        out["tags"] = capo_appconfig.types.tag_map.deserialize_json(data["Tags"])
    return out
