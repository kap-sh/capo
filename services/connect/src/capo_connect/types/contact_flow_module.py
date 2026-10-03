"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowModule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.contact_flow_module_content
    import capo_connect.types.contact_flow_module_description
    import capo_connect.types.contact_flow_module_id
    import capo_connect.types.contact_flow_module_name
    import capo_connect.types.contact_flow_module_state
    import capo_connect.types.contact_flow_module_status
    import capo_connect.types.external_invocation_configuration
    import capo_connect.types.flow_module_content_sha256
    import capo_connect.types.flow_module_settings
    import capo_connect.types.resource_version
    import capo_connect.types.tag_map


class ContactFlowModule(TypedDict, closed=True):
    arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN).</p>"""
    id: NotRequired["capo_connect.types.contact_flow_module_id.ContactFlowModuleId"]
    """<p>The identifier of the flow module.</p>"""
    name: NotRequired[
        "capo_connect.types.contact_flow_module_name.ContactFlowModuleName"
    ]
    """<p>The name of the flow module.</p>"""
    content: NotRequired[
        "capo_connect.types.contact_flow_module_content.ContactFlowModuleContent"
    ]
    """<p>The JSON string that represents the content of the flow. For an example, see <a href="https://docs.aws.amazon.com/connect/latest/APIReference/flow-language-example.html">Example flow in Connect Customer Flow language</a>. </p>"""
    description: NotRequired[
        "capo_connect.types.contact_flow_module_description.ContactFlowModuleDescription"
    ]
    """<p>The description of the flow module.</p>"""
    state: NotRequired[
        "capo_connect.types.contact_flow_module_state.ContactFlowModuleState"
    ]
    """<p>The type of flow module.</p>"""
    status: NotRequired[
        "capo_connect.types.contact_flow_module_status.ContactFlowModuleStatus"
    ]
    """<p>The status of the flow module.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.</p>"""
    flow_module_content_sha256: NotRequired[
        "capo_connect.types.flow_module_content_sha256.FlowModuleContentSha256"
    ]
    """<p>Hash of the module content for integrity verification.</p>"""
    version: NotRequired["capo_connect.types.resource_version.ResourceVersion"]
    """<p>The version of the flow module.</p>"""
    version_description: NotRequired[
        "capo_connect.types.contact_flow_module_description.ContactFlowModuleDescription"
    ]
    """<p>Description of the version.</p>"""
    settings: NotRequired["capo_connect.types.flow_module_settings.FlowModuleSettings"]
    """<p>The configuration settings for the flow module.</p>"""
    external_invocation_configuration: NotRequired[
        "capo_connect.types.external_invocation_configuration.ExternalInvocationConfiguration"
    ]
    """<p>The external invocation configuration for the flow module</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowModule) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "content" in value:
        out["Content"] = value["content"]
    if "description" in value:
        out["Description"] = value["description"]
    if "state" in value:
        import capo_connect.types.contact_flow_module_state

        out["State"] = capo_connect.types.contact_flow_module_state.serialize_json(
            value["state"]
        )
    if "status" in value:
        import capo_connect.types.contact_flow_module_status

        out["Status"] = capo_connect.types.contact_flow_module_status.serialize_json(
            value["status"]
        )
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    if "flow_module_content_sha256" in value:
        out["FlowModuleContentSha256"] = value["flow_module_content_sha256"]
    if "version" in value:
        out["Version"] = value["version"]
    if "version_description" in value:
        out["VersionDescription"] = value["version_description"]
    if "settings" in value:
        out["Settings"] = value["settings"]
    if "external_invocation_configuration" in value:
        import capo_connect.types.external_invocation_configuration

        out["ExternalInvocationConfiguration"] = (
            capo_connect.types.external_invocation_configuration.serialize_json(
                value["external_invocation_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContactFlowModule:
    out: ContactFlowModule = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("State") is not None:
        import capo_connect.types.contact_flow_module_state

        out["state"] = capo_connect.types.contact_flow_module_state.deserialize_json(
            data["State"]
        )
    if data.get("Status") is not None:
        import capo_connect.types.contact_flow_module_status

        out["status"] = capo_connect.types.contact_flow_module_status.deserialize_json(
            data["Status"]
        )
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    if data.get("FlowModuleContentSha256") is not None:
        out["flow_module_content_sha256"] = data["FlowModuleContentSha256"]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    if data.get("VersionDescription") is not None:
        out["version_description"] = data["VersionDescription"]
    if data.get("Settings") is not None:
        out["settings"] = data["Settings"]
    if data.get("ExternalInvocationConfiguration") is not None:
        import capo_connect.types.external_invocation_configuration

        out["external_invocation_configuration"] = (
            capo_connect.types.external_invocation_configuration.deserialize_json(
                data["ExternalInvocationConfiguration"]
            )
        )
    return out
