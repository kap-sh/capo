"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#CreateConfigurationManagerInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ssm_quicksetup.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_quicksetup.types.configuration_definitions_input_list
    import capo_ssm_quicksetup.types.tags_map


class CreateConfigurationManagerInput(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>A name for the configuration manager.</p>"""
    description: NotRequired["str"]
    """<p>A description of the configuration manager.</p>"""
    configuration_definitions: "capo_ssm_quicksetup.types.configuration_definitions_input_list.ConfigurationDefinitionsInputList"
    """<p>The definition of the Quick Setup configuration that the configuration manager deploys.</p>"""
    tags: NotRequired["capo_ssm_quicksetup.types.tags_map.TagsMap"]
    """<p>Key-value pairs of metadata to assign to the configuration manager.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfigurationManagerInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_ssm_quicksetup.types.configuration_definitions_input_list

    out["ConfigurationDefinitions"] = (
        capo_ssm_quicksetup.types.configuration_definitions_input_list.serialize_json(
            value["configuration_definitions"]
        )
    )
    if "tags" in value:
        import capo_ssm_quicksetup.types.tags_map

        out["Tags"] = capo_ssm_quicksetup.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateConfigurationManagerInput:
    out: CreateConfigurationManagerInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ConfigurationDefinitions") is not None:
        import capo_ssm_quicksetup.types.configuration_definitions_input_list

        out["configuration_definitions"] = (
            capo_ssm_quicksetup.types.configuration_definitions_input_list.deserialize_json(
                data["ConfigurationDefinitions"]
            )
        )
    else:
        raise DeserializationError(
            "CreateConfigurationManagerInput.configuration_definitions required"
        )
    if data.get("Tags") is not None:
        import capo_ssm_quicksetup.types.tags_map

        out["tags"] = capo_ssm_quicksetup.types.tags_map.deserialize_json(data["Tags"])
    return out


def redact_sensitive(value: CreateConfigurationManagerInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
