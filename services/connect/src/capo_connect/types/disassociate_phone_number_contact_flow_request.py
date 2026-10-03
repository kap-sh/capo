"""Generated from Smithy shape ``com.amazonaws.connect#DisassociatePhoneNumberContactFlowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.phone_number_id


class DisassociatePhoneNumberContactFlowRequest(TypedDict, closed=True):
    phone_number_id: "capo_connect.types.phone_number_id.PhoneNumberId"
    """<p>A unique identifier for the phone number.</p>"""
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociatePhoneNumberContactFlowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociatePhoneNumberContactFlowRequest:
    out: DisassociatePhoneNumberContactFlowRequest = {}  # type: ignore[typeddict-item]
    return out
