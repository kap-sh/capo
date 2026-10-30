"""Generated from Smithy shape ``com.amazonaws.connect#TaskTemplateContactHooks``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_flow_module_id


class TaskTemplateContactHooks(TypedDict, closed=True):
    wrap_up_flow_id: NotRequired[
        "capo_connect.types.contact_flow_module_id.ContactFlowModuleId"
    ]
    """<p>The identifier of the flow module that runs when an agent attempts to disconnect from a task created by referencing this template. If no agent ever connects to the task, the flow module runs when the task is terminated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaskTemplateContactHooks) -> dict:
    out: dict = {}
    if "wrap_up_flow_id" in value:
        out["WrapUpFlowId"] = value["wrap_up_flow_id"]
    return out


def deserialize_json(data: dict) -> TaskTemplateContactHooks:
    out: TaskTemplateContactHooks = {}  # type: ignore[typeddict-item]
    if data.get("WrapUpFlowId") is not None:
        out["wrap_up_flow_id"] = data["WrapUpFlowId"]
    return out
