"""Generated from Smithy shape ``com.amazonaws.connect#DeleteEmailAddressRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.email_address_id
    import capo_connect.types.instance_id


class DeleteEmailAddressRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    email_address_id: "capo_connect.types.email_address_id.EmailAddressId"
    """<p>The identifier of the email address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEmailAddressRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEmailAddressRequest:
    out: DeleteEmailAddressRequest = {}  # type: ignore[typeddict-item]
    return out
