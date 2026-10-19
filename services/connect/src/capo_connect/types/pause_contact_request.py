"""Generated from Smithy shape ``com.amazonaws.connect#PauseContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_flow_id
    import capo_connect.types.contact_id
    import capo_connect.types.instance_id


class PauseContactRequest(TypedDict, closed=True):
    contact_id: "capo_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact.</p>"""
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can find the <code>instanceId</code> in the ARN of the instance.</p>"""
    contact_flow_id: NotRequired["capo_connect.types.contact_flow_id.ContactFlowId"]
    """<p>The identifier of the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PauseContactRequest) -> dict:
    out: dict = {}
    out["ContactId"] = value["contact_id"]
    out["InstanceId"] = value["instance_id"]
    if "contact_flow_id" in value:
        out["ContactFlowId"] = value["contact_flow_id"]
    return out


def deserialize_json(data: dict) -> PauseContactRequest:
    out: PauseContactRequest = {}  # type: ignore[typeddict-item]
    if data.get("ContactId") is not None:
        out["contact_id"] = data["ContactId"]
    else:
        out["contact_id"] = ""
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        out["instance_id"] = ""
    if data.get("ContactFlowId") is not None:
        out["contact_flow_id"] = data["ContactFlowId"]
    return out
