"""Generated from Smithy shape ``com.amazonaws.connect#UpdateContactFlowModuleAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_flow_module_description
    import capo_connect.types.contact_flow_module_id
    import capo_connect.types.contact_flow_module_name
    import capo_connect.types.instance_id_or_arn
    import capo_connect.types.resource_id
    import capo_connect.types.resource_version


class UpdateContactFlowModuleAliasRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id_or_arn.InstanceIdOrArn"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_flow_module_id: (
        "capo_connect.types.contact_flow_module_id.ContactFlowModuleId"
    )
    """<p>The identifier of the flow module.</p>"""
    alias_id: "capo_connect.types.resource_id.ResourceId"
    """<p>The identifier of the alias.</p>"""
    name: NotRequired[
        "capo_connect.types.contact_flow_module_name.ContactFlowModuleName"
    ]
    """<p>The name of the alias.</p>"""
    description: NotRequired[
        "capo_connect.types.contact_flow_module_description.ContactFlowModuleDescription"
    ]
    """<p>The description of the alias.</p>"""
    contact_flow_module_version: NotRequired[
        "capo_connect.types.resource_version.ResourceVersion"
    ]
    """<p>The version of the flow module.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateContactFlowModuleAliasRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "contact_flow_module_version" in value:
        out["ContactFlowModuleVersion"] = value["contact_flow_module_version"]
    return out


def deserialize_json(data: dict) -> UpdateContactFlowModuleAliasRequest:
    out: UpdateContactFlowModuleAliasRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ContactFlowModuleVersion") is not None:
        out["contact_flow_module_version"] = data["ContactFlowModuleVersion"]
    return out
