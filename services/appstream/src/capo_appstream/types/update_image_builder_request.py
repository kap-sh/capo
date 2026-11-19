"""Generated from Smithy shape ``com.amazonaws.appstream#UpdateImageBuilderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.description
    import capo_appstream.types.display_name
    import capo_appstream.types.image_builder_agent_access_config_for_update
    import capo_appstream.types.image_builder_attributes
    import capo_appstream.types.name


class UpdateImageBuilderRequest(TypedDict, closed=True):
    name: NotRequired["capo_appstream.types.name.Name"]
    """<p>The name of the image builder.</p>"""
    description: NotRequired["capo_appstream.types.description.Description"]
    """<p>The description to display.</p>"""
    display_name: NotRequired["capo_appstream.types.display_name.DisplayName"]
    """<p>The image builder name to display.</p>"""
    agent_access_config: NotRequired[
        "capo_appstream.types.image_builder_agent_access_config_for_update.ImageBuilderAgentAccessConfigForUpdate"
    ]
    """<p>The configuration for agent access on the image builder. Specify this to update agent access settings. To remove agent access, use AttributesToDelete with the AGENT_ACCESS_CONFIG value.</p>"""
    attributes_to_delete: NotRequired[
        "capo_appstream.types.image_builder_attributes.ImageBuilderAttributes"
    ]
    """<p>The image builder attributes to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateImageBuilderRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "agent_access_config" in value:
        import capo_appstream.types.image_builder_agent_access_config_for_update

        out["AgentAccessConfig"] = (
            capo_appstream.types.image_builder_agent_access_config_for_update.serialize_aws_json_1_1(
                value["agent_access_config"]
            )
        )
    if "attributes_to_delete" in value:
        import capo_appstream.types.image_builder_attributes

        out["AttributesToDelete"] = (
            capo_appstream.types.image_builder_attributes.serialize_aws_json_1_1(
                value["attributes_to_delete"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateImageBuilderRequest:
    out: UpdateImageBuilderRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("AgentAccessConfig") is not None:
        import capo_appstream.types.image_builder_agent_access_config_for_update

        out["agent_access_config"] = (
            capo_appstream.types.image_builder_agent_access_config_for_update.deserialize_aws_json_1_1(
                data["AgentAccessConfig"]
            )
        )
    if data.get("AttributesToDelete") is not None:
        import capo_appstream.types.image_builder_attributes

        out["attributes_to_delete"] = (
            capo_appstream.types.image_builder_attributes.deserialize_aws_json_1_1(
                data["AttributesToDelete"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateImageBuilderRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "agent_access_config" in value:
        import capo_appstream.types.image_builder_agent_access_config_for_update

        out["AgentAccessConfig"] = (
            capo_appstream.types.image_builder_agent_access_config_for_update.serialize_cbor(
                value["agent_access_config"]
            )
        )
    if "attributes_to_delete" in value:
        import capo_appstream.types.image_builder_attributes

        out["AttributesToDelete"] = (
            capo_appstream.types.image_builder_attributes.serialize_cbor(
                value["attributes_to_delete"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> UpdateImageBuilderRequest:
    out: UpdateImageBuilderRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("AgentAccessConfig") is not None:
        import capo_appstream.types.image_builder_agent_access_config_for_update

        out["agent_access_config"] = (
            capo_appstream.types.image_builder_agent_access_config_for_update.deserialize_cbor(
                data["AgentAccessConfig"]
            )
        )
    if data.get("AttributesToDelete") is not None:
        import capo_appstream.types.image_builder_attributes

        out["attributes_to_delete"] = (
            capo_appstream.types.image_builder_attributes.deserialize_cbor(
                data["AttributesToDelete"]
            )
        )
    return out
