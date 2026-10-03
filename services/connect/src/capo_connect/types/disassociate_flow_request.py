"""Generated from Smithy shape ``com.amazonaws.connect#DisassociateFlowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.flow_association_resource_type
    import capo_connect.types.instance_id


class DisassociateFlowRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    resource_id: "capo_connect.types.arn.ARN"
    """<p>The identifier of the resource.</p> <ul> <li> <p>Amazon Web Services End User Messaging SMS phone number ARN when using <code>SMS_PHONE_NUMBER</code> </p> </li> <li> <p>Amazon Web Services End User Messaging Social phone number ARN when using <code>WHATSAPP_MESSAGING_PHONE_NUMBER</code> </p> </li> </ul>"""
    resource_type: (
        "capo_connect.types.flow_association_resource_type.FlowAssociationResourceType"
    )
    """<p>A valid resource type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateFlowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateFlowRequest:
    out: DisassociateFlowRequest = {}  # type: ignore[typeddict-item]
    return out
