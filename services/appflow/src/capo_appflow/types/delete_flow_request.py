"""Generated from Smithy shape ``com.amazonaws.appflow#DeleteFlowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.boolean
    import capo_appflow.types.flow_name


class DeleteFlowRequest(TypedDict, closed=True):
    flow_name: "capo_appflow.types.flow_name.FlowName"
    """<p> The specified name of the flow. Spaces are not allowed. Use underscores (_) or hyphens (-) only. </p>"""
    force_delete: NotRequired["capo_appflow.types.boolean.Boolean"]
    """<p> Indicates whether Amazon AppFlow should delete the flow, even if it is currently in use. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFlowRequest) -> dict:
    out: dict = {}
    out["flowName"] = value["flow_name"]
    if "force_delete" in value:
        out["forceDelete"] = value["force_delete"]
    return out


def deserialize_json(data: dict) -> DeleteFlowRequest:
    out: DeleteFlowRequest = {}  # type: ignore[typeddict-item]
    if data.get("flowName") is not None:
        out["flow_name"] = data["flowName"]
    else:
        out["flow_name"] = ""
    if data.get("forceDelete") is not None:
        out["force_delete"] = data["forceDelete"]
    return out
