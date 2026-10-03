"""Generated from Smithy shape ``com.amazonaws.connect#UpdateContactFlowModuleMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_flow_module_description
    import capo_connect.types.contact_flow_module_id
    import capo_connect.types.contact_flow_module_name
    import capo_connect.types.contact_flow_module_state
    import capo_connect.types.instance_id


class UpdateContactFlowModuleMetadataRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_flow_module_id: (
        "capo_connect.types.contact_flow_module_id.ContactFlowModuleId"
    )
    """<p>The identifier of the flow module.</p>"""
    name: NotRequired[
        "capo_connect.types.contact_flow_module_name.ContactFlowModuleName"
    ]
    """<p>The name of the flow module.</p>"""
    description: NotRequired[
        "capo_connect.types.contact_flow_module_description.ContactFlowModuleDescription"
    ]
    """<p>The description of the flow module.</p>"""
    state: NotRequired[
        "capo_connect.types.contact_flow_module_state.ContactFlowModuleState"
    ]
    """<p>The state of flow module.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateContactFlowModuleMetadataRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "state" in value:
        import capo_connect.types.contact_flow_module_state

        out["State"] = capo_connect.types.contact_flow_module_state.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> UpdateContactFlowModuleMetadataRequest:
    out: UpdateContactFlowModuleMetadataRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("State") is not None:
        import capo_connect.types.contact_flow_module_state

        out["state"] = capo_connect.types.contact_flow_module_state.deserialize_json(
            data["State"]
        )
    return out
