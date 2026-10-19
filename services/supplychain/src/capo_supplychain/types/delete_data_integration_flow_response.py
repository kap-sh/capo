"""Generated from Smithy shape ``com.amazonaws.supplychain#DeleteDataIntegrationFlowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.data_integration_flow_name
    import capo_supplychain.types.uuid


class DeleteDataIntegrationFlowResponse(TypedDict, closed=True):
    instance_id: "capo_supplychain.types.uuid.UUID"
    """<p>The Amazon Web Services Supply Chain instance identifier.</p>"""
    name: "capo_supplychain.types.data_integration_flow_name.DataIntegrationFlowName"
    """<p>The name of the DataIntegrationFlow deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataIntegrationFlowResponse) -> dict:
    out: dict = {}
    out["instanceId"] = value["instance_id"]
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> DeleteDataIntegrationFlowResponse:
    out: DeleteDataIntegrationFlowResponse = {}  # type: ignore[typeddict-item]
    if data.get("instanceId") is not None:
        out["instance_id"] = data["instanceId"]
    else:
        out["instance_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
