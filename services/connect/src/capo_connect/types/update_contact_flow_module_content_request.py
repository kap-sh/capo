"""Generated from Smithy shape ``com.amazonaws.connect#UpdateContactFlowModuleContentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_flow_module_content
    import capo_connect.types.contact_flow_module_id
    import capo_connect.types.flow_module_settings
    import capo_connect.types.instance_id


class UpdateContactFlowModuleContentRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_flow_module_id: (
        "capo_connect.types.contact_flow_module_id.ContactFlowModuleId"
    )
    """<p>The identifier of the flow module.</p>"""
    content: NotRequired[
        "capo_connect.types.contact_flow_module_content.ContactFlowModuleContent"
    ]
    """<p>The JSON string that represents the content of the flow. For an example, see <a href="https://docs.aws.amazon.com/connect/latest/APIReference/flow-language-example.html">Example flow in Connect Customer Flow language</a>. </p>"""
    settings: NotRequired["capo_connect.types.flow_module_settings.FlowModuleSettings"]
    """<p>Serialized JSON string of the flow module Settings schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateContactFlowModuleContentRequest) -> dict:
    out: dict = {}
    if "content" in value:
        out["Content"] = value["content"]
    if "settings" in value:
        out["Settings"] = value["settings"]
    return out


def deserialize_json(data: dict) -> UpdateContactFlowModuleContentRequest:
    out: UpdateContactFlowModuleContentRequest = {}  # type: ignore[typeddict-item]
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    if data.get("Settings") is not None:
        out["settings"] = data["Settings"]
    return out
