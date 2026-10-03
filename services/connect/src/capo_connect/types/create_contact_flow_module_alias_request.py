"""Generated from Smithy shape ``com.amazonaws.connect#CreateContactFlowModuleAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.contact_flow_description
    import capo_connect.types.contact_flow_module_alias
    import capo_connect.types.contact_flow_module_id
    import capo_connect.types.instance_id_or_arn
    import capo_connect.types.resource_version


class CreateContactFlowModuleAliasRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id_or_arn.InstanceIdOrArn"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    description: NotRequired[
        "capo_connect.types.contact_flow_description.ContactFlowDescription"
    ]
    """<p>The description of the alias.</p>"""
    contact_flow_module_id: (
        "capo_connect.types.contact_flow_module_id.ContactFlowModuleId"
    )
    """<p>The identifier of the flow module.</p>"""
    contact_flow_module_version: "capo_connect.types.resource_version.ResourceVersion"
    """<p>The version of the flow module.</p>"""
    alias_name: "capo_connect.types.contact_flow_module_alias.ContactFlowModuleAlias"
    """<p>The name of the alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateContactFlowModuleAliasRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    out["ContactFlowModuleVersion"] = value["contact_flow_module_version"]
    out["AliasName"] = value["alias_name"]
    return out


def deserialize_json(data: dict) -> CreateContactFlowModuleAliasRequest:
    out: CreateContactFlowModuleAliasRequest = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ContactFlowModuleVersion") is not None:
        out["contact_flow_module_version"] = data["ContactFlowModuleVersion"]
    else:
        raise DeserializationError(
            "CreateContactFlowModuleAliasRequest.contact_flow_module_version required"
        )
    if data.get("AliasName") is not None:
        out["alias_name"] = data["AliasName"]
    else:
        raise DeserializationError(
            "CreateContactFlowModuleAliasRequest.alias_name required"
        )
    return out
