"""Generated from Smithy shape ``com.amazonaws.connect#CreateContactFlowModuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.client_token
    import capo_connect.types.contact_flow_module_content
    import capo_connect.types.contact_flow_module_description
    import capo_connect.types.contact_flow_module_name
    import capo_connect.types.external_invocation_configuration
    import capo_connect.types.flow_module_settings
    import capo_connect.types.instance_id
    import capo_connect.types.tag_map


class CreateContactFlowModuleRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    name: "capo_connect.types.contact_flow_module_name.ContactFlowModuleName"
    """<p>The name of the flow module.</p>"""
    description: NotRequired[
        "capo_connect.types.contact_flow_module_description.ContactFlowModuleDescription"
    ]
    """<p>The description of the flow module. </p>"""
    content: "capo_connect.types.contact_flow_module_content.ContactFlowModuleContent"
    """<p>The JSON string that represents the content of the flow. For an example, see <a href="https://docs.aws.amazon.com/connect/latest/APIReference/flow-language-example.html">Example flow in Connect Customer Flow language</a>. </p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.</p>"""
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""
    settings: NotRequired["capo_connect.types.flow_module_settings.FlowModuleSettings"]
    """<p>The configuration settings for the flow module.</p>"""
    external_invocation_configuration: NotRequired[
        "capo_connect.types.external_invocation_configuration.ExternalInvocationConfiguration"
    ]
    """<p>The external invocation configuration for the flow module.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateContactFlowModuleRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["Content"] = value["content"]
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
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


def deserialize_json(data: dict) -> CreateContactFlowModuleRequest:
    out: CreateContactFlowModuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateContactFlowModuleRequest.name required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    else:
        raise DeserializationError("CreateContactFlowModuleRequest.content required")
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
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
