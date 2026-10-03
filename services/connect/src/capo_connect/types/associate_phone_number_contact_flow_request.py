"""Generated from Smithy shape ``com.amazonaws.connect#AssociatePhoneNumberContactFlowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.contact_flow_id
    import capo_connect.types.instance_id
    import capo_connect.types.phone_number_id


class AssociatePhoneNumberContactFlowRequest(TypedDict, closed=True):
    phone_number_id: "capo_connect.types.phone_number_id.PhoneNumberId"
    """<p>A unique identifier for the phone number.</p>"""
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_flow_id: "capo_connect.types.contact_flow_id.ContactFlowId"
    """<p>The identifier of the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatePhoneNumberContactFlowRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    out["ContactFlowId"] = value["contact_flow_id"]
    return out


def deserialize_json(data: dict) -> AssociatePhoneNumberContactFlowRequest:
    out: AssociatePhoneNumberContactFlowRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError(
            "AssociatePhoneNumberContactFlowRequest.instance_id required"
        )
    if data.get("ContactFlowId") is not None:
        out["contact_flow_id"] = data["ContactFlowId"]
    else:
        raise DeserializationError(
            "AssociatePhoneNumberContactFlowRequest.contact_flow_id required"
        )
    return out
