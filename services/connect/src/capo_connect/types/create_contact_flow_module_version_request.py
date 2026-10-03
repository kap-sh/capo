"""Generated from Smithy shape ``com.amazonaws.connect#CreateContactFlowModuleVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.contact_flow_module_description
    import capo_connect.types.flow_module_content_sha256
    import capo_connect.types.instance_id


class CreateContactFlowModuleVersionRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    description: NotRequired[
        "capo_connect.types.contact_flow_module_description.ContactFlowModuleDescription"
    ]
    """<p>The description of the flow module version.</p>"""
    contact_flow_module_id: "capo_connect.types.arn.ARN"
    """<p>The identifier of the flow module.</p>"""
    flow_module_content_sha256: NotRequired[
        "capo_connect.types.flow_module_content_sha256.FlowModuleContentSha256"
    ]
    """<p>Indicates the checksum value of the flow module content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateContactFlowModuleVersionRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "flow_module_content_sha256" in value:
        out["FlowModuleContentSha256"] = value["flow_module_content_sha256"]
    return out


def deserialize_json(data: dict) -> CreateContactFlowModuleVersionRequest:
    out: CreateContactFlowModuleVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("FlowModuleContentSha256") is not None:
        out["flow_module_content_sha256"] = data["FlowModuleContentSha256"]
    return out
